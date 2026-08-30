/**
 * LiteStep Speed Bar - Venmo Inventory Automation
 * Runs on Google Apps Script (https://script.google.com)
 * 
 * Trigger: Time-driven (runs every 5 or 10 minutes)
 * Action: Checks Gmail for Venmo payment receipts, parses LiteStep orders,
 *         decrements stock count in _data/inventory.yml on GitHub, updates date,
 *         and marks email as read.
 */

// ================= CONFIGURATION =================
const GITHUB_USERNAME = "jbcohn";
const GITHUB_REPO = "litestep.site";
const INVENTORY_FILE_PATH = "_data/inventory.yml";

// Set your GitHub Personal Access Token in Script Properties:
// PropertiesService.getScriptProperties().setProperty('GITHUB_TOKEN', 'ghp_yourTokenHere');
// Or replace directly here if keeping script private:
function getGitHubToken() {
  return PropertiesService.getScriptProperties().getProperty('GITHUB_TOKEN');
}

// ================= MAIN SYNC FUNCTION =================
function syncVenmoSalesToGitHub() {
  const token = getGitHubToken();
  if (!token) {
    Logger.log("Error: GITHUB_TOKEN not set in Script Properties.");
    return;
  }

  // Get or create custom label so we never touch read/unread status
  const LABEL_NAME = "LiteStep-Synced";
  let label = GmailApp.getUserLabelByName(LABEL_NAME);
  if (!label) {
    label = GmailApp.createLabel(LABEL_NAME);
  }

  // Search for Venmo payment confirmation emails that haven't been synced yet
  // Notice we do NOT check "is:unread" so your inbox read/unread state is left untouched
  const searchQuery = `from:venmo@venmo.com "paid you" -label:${LABEL_NAME}`;
  const threads = GmailApp.search(searchQuery, 0, 10);

  if (threads.length === 0) {
    Logger.log("No new unsynced Venmo sales found.");
    return;
  }

  Logger.log(`Found ${threads.length} unsynced Venmo email(s).`);

  for (const thread of threads) {
    const messages = thread.getMessages();
    for (const message of messages) {
      const subject = message.getSubject();
      const body = message.getPlainBody();
      const fullText = (subject + " " + body).toLowerCase();

      Logger.log(`Processing message: "${subject}"`);

      // Determine product type by price or note text
      let isLight = false;
      let isComp = false;

      if (fullText.includes("157") || fullText.includes("145") || fullText.includes("light")) {
        isLight = true;
      }
      if (fullText.includes("195") || fullText.includes("180") || fullText.includes("comp")) {
        isComp = true;
      }

      // If matched, update GitHub inventory
      if (isLight || isComp) {
        const itemType = isComp ? "comp" : "light";
        const success = decrementGitHubInventory(token, itemType, subject);
        if (success) {
          // Label the thread as synced WITHOUT changing read/unread status
          thread.addLabel(label);
          Logger.log(`Successfully decremented ${itemType} stock for: "${subject}". Email left unread.`);
        }
      } else {
        Logger.log(`Could not identify LiteStep model in email. Skipping.`);
      }
    }
  }
}

// ================= GITHUB API HELPER =================
function decrementGitHubInventory(token, itemType, orderSubject) {
  const apiUrl = `https://api.github.com/repos/${GITHUB_USERNAME}/${GITHUB_REPO}/contents/${INVENTORY_FILE_PATH}`;

  // 1. Fetch current inventory file from GitHub
  const getOptions = {
    method: "get",
    headers: {
      "Authorization": `Bearer ${token}`,
      "Accept": "application/vnd.github.v3+json",
      "User-Agent": "Google-Apps-Script-LiteStep"
    },
    muteHttpExceptions: true
  };

  const response = UrlFetchApp.fetch(apiUrl, getOptions);
  if (response.getResponseCode() !== 200) {
    Logger.log(`Failed to fetch inventory from GitHub: ${response.getContentText()}`);
    return false;
  }

  const fileData = JSON.parse(response.getContentText());
  const sha = fileData.sha;
  const rawContent = Utilities.newBlob(Utilities.base64Decode(fileData.content)).getDataAsString();

  // 2. Parse and update YAML lines
  const todayStr = Utilities.formatDate(new Date(), "GMT-7", "yyyy-MM-dd");

  let lightStock = 0;
  let compStock = 0;
  let statusMessage = "Custom built to order. Contact for current batch lead times.";

  const lightMatch = rawContent.match(/light_stock:\s*(\d+)/);
  if (lightMatch) lightStock = parseInt(lightMatch[1], 10);

  const compMatch = rawContent.match(/comp_stock:\s*(\d+)/);
  if (compMatch) compStock = parseInt(compMatch[1], 10);

  const statusMatch = rawContent.match(/status_message:\s*["']?([^"'\n]+)["']?/);
  if (statusMatch) statusMessage = statusMatch[1];

  // Decrement matching item (minimum 0)
  if (itemType === "light") {
    lightStock = Math.max(0, lightStock - 1);
  } else if (itemType === "comp") {
    compStock = Math.max(0, compStock - 1);
  }

  const updatedYaml = 
`last_updated: "${todayStr}"
light_stock: ${lightStock}
comp_stock: ${compStock}
status_message: "${statusMessage}"
`;

  // 3. Commit updated inventory back to GitHub
  const putPayload = {
    message: `Automated inventory decrement (${itemType}) via Venmo sale: ${orderSubject}`,
    content: Utilities.base64Encode(updatedYaml),
    sha: sha
  };

  const putOptions = {
    method: "put",
    headers: {
      "Authorization": `Bearer ${token}`,
      "Accept": "application/vnd.github.v3+json",
      "Content-Type": "application/json",
      "User-Agent": "Google-Apps-Script-LiteStep"
    },
    payload: JSON.stringify(putPayload),
    muteHttpExceptions: true
  };

  const putResponse = UrlFetchApp.fetch(apiUrl, putOptions);
  if (putResponse.getResponseCode() === 200 || putResponse.getResponseCode() === 201) {
    Logger.log("GitHub inventory updated successfully.");
    return true;
  } else {
    Logger.log(`Failed to update inventory on GitHub: ${putResponse.getContentText()}`);
    return false;
  }
}
