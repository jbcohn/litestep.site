/**
 * LiteStep Speed Bar - Venmo Inventory Automation
 * Runs on Google Apps Script (https://script.google.com)
 *
 * Setup:
 * 1. Open Google Apps Script (https://script.google.com) and paste this entire file.
 * 2. Set your GitHub Personal Access Token:
 *    - In the left sidebar, click Project Settings (gear icon).
 *    - Under "Script Properties", click "Add script property".
 *    - Property: GITHUB_TOKEN, Value: <your_github_token_with_repo_scope>.
 *    - Click "Save script properties".
 * 3. Select 'setupAndAuthorize' in the toolbar dropdown and click 'Run'.
 *    - Grants required Gmail and Script permissions.
 *    - Validates GitHub connection and displays current inventory.
 *    - Ensures the 'LiteStep-Synced' Gmail label exists.
 *    - Backfills historical Venmo orders on or before 2026-10-18 so they aren't double-decremented.
 *    - Automatically creates a 5-minute time-driven trigger for 'syncVenmoSalesToGitHub'.
 */

// ================= CONFIGURATION =================
const GITHUB_USERNAME = "jbcohn";
const GITHUB_REPO = "litestep.site";
const INVENTORY_FILE_PATH = "_data/inventory.yml";
const SYNC_LABEL_NAME = "LiteStep-Synced";
const BASELINE_DATE = new Date("2026-10-19T00:00:00-07:00");

// ================= 1. SETUP & AUTHORIZATION =================
// (Placed first so it appears as the default selected function in the Apps Script toolbar)
function setupAndAuthorize() {
  Logger.log("=== LiteStep Venmo Automation Setup ===");

  const token = getGitHubToken();
  if (!token) {
    Logger.log("ERROR: GITHUB_TOKEN is not configured in Script Properties.");
    Logger.log("To add your token:");
    Logger.log("1. Click Project Settings (gear icon in the left sidebar).");
    Logger.log("2. Under 'Script Properties', click 'Add script property'.");
    Logger.log("3. Set Property: GITHUB_TOKEN, Value: <your_personal_access_token> (requires 'repo' scope).");
    Logger.log("4. Click 'Save script properties' and re-run setupAndAuthorize().");
    return;
  }

  // Verify GitHub API connectivity & token scope
  const inventory = fetchGitHubInventory(token);
  if (!inventory) {
    Logger.log("ERROR: Failed to connect to GitHub or read _data/inventory.yml. Verify your token has 'repo' scope.");
    return;
  }
  Logger.log(`GitHub connection OK. Current inventory: Light=${inventory.lightStock}, Comp=${inventory.compStock}, Last Updated=${inventory.lastUpdated}`);

  // Ensure Gmail label exists
  const label = getOrCreateSyncLabel();
  Logger.log(`Gmail label '${SYNC_LABEL_NAME}' is ready.`);

  // Backfill existing Venmo payment threads from on or before 2026-10-18 so historical orders aren't double-counted
  const baselineQuery = `from:venmo@venmo.com "paid you" -label:${SYNC_LABEL_NAME}`;
  const threads = GmailApp.search(baselineQuery, 0, 100);
  let backfilledCount = 0;

  for (const thread of threads) {
    const messages = thread.getMessages();
    const isHistorical = messages.some(m => m.getDate() < BASELINE_DATE);
    if (isHistorical) {
      thread.addLabel(label);
      backfilledCount++;
    }
  }
  Logger.log(`Backfilled ${backfilledCount} historical payment thread(s) on or before 2026-10-18 with '${SYNC_LABEL_NAME}'.`);

  // Ensure 5-minute time-driven trigger is configured
  const triggers = ScriptApp.getProjectTriggers();
  const triggerExists = triggers.some(t => t.getHandlerFunction() === "syncVenmoSalesToGitHub");
  if (!triggerExists) {
    ScriptApp.newTrigger("syncVenmoSalesToGitHub")
      .timeBased()
      .everyMinutes(5)
      .create();
    Logger.log("Created 5-minute time-driven trigger for 'syncVenmoSalesToGitHub'.");
  } else {
    Logger.log("Recurring trigger for 'syncVenmoSalesToGitHub' is already active.");
  }

  Logger.log("=== Setup Complete! Automation is live. ===");
}

// ================= 2. PERIODIC SYNC FUNCTION =================
function syncVenmoSalesToGitHub() {
  const token = getGitHubToken();
  if (!token) {
    Logger.log("Error: GITHUB_TOKEN not set in Script Properties.");
    return;
  }

  const label = getOrCreateSyncLabel();
  const searchQuery = `from:venmo@venmo.com "paid you" -label:${SYNC_LABEL_NAME}`;
  const threads = GmailApp.search(searchQuery, 0, 10);

  if (threads.length === 0) {
    Logger.log("No new unsynced Venmo sales found.");
    return;
  }

  Logger.log(`Found ${threads.length} unsynced Venmo email(s).`);

  for (const thread of threads) {
    // Extra safety: ensure thread does not already have the label
    const existingLabels = thread.getLabels();
    if (existingLabels.some(l => l.getName().toLowerCase() === SYNC_LABEL_NAME.toLowerCase())) {
      continue;
    }

    const messages = thread.getMessages();
    for (const message of messages) {
      const msgDate = message.getDate();

      // Ignore and label historical messages without decrementing stock
      if (msgDate < BASELINE_DATE) {
        Logger.log(`Message dated ${msgDate.toISOString()} is prior to baseline (${BASELINE_DATE.toISOString()}). Marking synced without decrementing.`);
        thread.addLabel(label);
        continue;
      }

      const subject = message.getSubject();
      const body = message.getPlainBody();
      Logger.log(`Evaluating message: "${subject}" (${msgDate.toISOString()})`);

      const itemType = detectProduct(subject, body);
      if (itemType) {
        const success = decrementGitHubInventory(token, itemType, subject);
        if (success) {
          thread.addLabel(label);
          Logger.log(`Successfully decremented ${itemType} stock for: "${subject}".`);
        } else {
          Logger.log(`Failed to decrement GitHub inventory for: "${subject}".`);
        }
      } else {
        Logger.log(`Message "${subject}" did not match LiteStep products or prices. Skipping.`);
      }
    }
  }
}

// ================= 3. PRODUCT DETECTION =================
function detectProduct(subject, body) {
  const fullText = subject + "\n" + body;

  const hasLiteStepKeyword = /lite[\s-]*step|speed[\s-]*bar/i.test(fullText);
  const compAmountRegex = /\$\s*(?:180|195)(?:\.00|\s+00|\b)/;
  const lightAmountRegex = /\$\s*(?:155|168|145|157)(?:\.00|\s+00|\b)/;

  const hasCompAmount = compAmountRegex.test(fullText);
  const hasLightAmount = lightAmountRegex.test(fullText);

  // Must mention LiteStep / speedbar OR match a known LiteStep price
  if (!hasLiteStepKeyword && !hasCompAmount && !hasLightAmount) {
    return null;
  }

  // Explicit note patterns
  const compNoteRegex = /(?:^|[\s+])comp(?:[\s+]|$)|comp[\s+]+litestep|litestep[\s+]+comp/i;
  const lightNoteRegex = /(?:^|[\s+])light(?:[\s+]|$)|light[\s+]+litestep|litestep[\s+]+light/i;

  const hasCompNote = compNoteRegex.test(fullText);
  const hasLightNote = lightNoteRegex.test(fullText);

  if (hasCompNote && !hasLightNote) return "comp";
  if (hasLightNote && !hasCompNote) return "light";
  if (hasCompAmount && !hasLightAmount) return "comp";
  if (hasLightAmount && !hasCompAmount) return "light";

  if (hasCompNote || hasCompAmount) return "comp";
  if (hasLightNote || hasLightAmount) return "light";

  return null;
}

// ================= 4. GITHUB INVENTORY HELPERS =================
function fetchGitHubInventory(token) {
  const apiUrl = `https://api.github.com/repos/${GITHUB_USERNAME}/${GITHUB_REPO}/contents/${INVENTORY_FILE_PATH}`;
  const options = {
    method: "get",
    headers: {
      "Authorization": `Bearer ${token}`,
      "Accept": "application/vnd.github.v3+json",
      "User-Agent": "Google-Apps-Script-LiteStep"
    },
    muteHttpExceptions: true
  };

  const response = UrlFetchApp.fetch(apiUrl, options);
  if (response.getResponseCode() !== 200) {
    Logger.log(`GitHub API error (${response.getResponseCode()}): ${response.getContentText()}`);
    return null;
  }

  const fileData = JSON.parse(response.getContentText());
  const sha = fileData.sha;
  const rawContent = Utilities.newBlob(Utilities.base64Decode(fileData.content)).getDataAsString();

  let lightStock = 0;
  let compStock = 0;
  let lastUpdated = "";
  let statusMessage = "in stock.";

  const lightMatch = rawContent.match(/light_stock:\s*(\d+)/);
  if (lightMatch) lightStock = parseInt(lightMatch[1], 10);

  const compMatch = rawContent.match(/comp_stock:\s*(\d+)/);
  if (compMatch) compStock = parseInt(compMatch[1], 10);

  const dateMatch = rawContent.match(/last_updated:\s*["']?([^"'\n]+)["']?/);
  if (dateMatch) lastUpdated = dateMatch[1];

  const statusMatch = rawContent.match(/status_message:\s*["']?([^"'\n]+)["']?/);
  if (statusMatch) statusMessage = statusMatch[1];

  return { sha, rawContent, lightStock, compStock, lastUpdated, statusMessage };
}

function decrementGitHubInventory(token, itemType, orderSubject) {
  const inventory = fetchGitHubInventory(token);
  if (!inventory) {
    Logger.log("Failed to fetch inventory from GitHub for decrement.");
    return false;
  }

  let lightStock = inventory.lightStock;
  let compStock = inventory.compStock;
  const statusMessage = inventory.statusMessage || "in stock.";

  if (itemType === "light") {
    lightStock = Math.max(0, lightStock - 1);
  } else if (itemType === "comp") {
    compStock = Math.max(0, compStock - 1);
  }

  const todayStr = Utilities.formatDate(new Date(), "GMT-7", "yyyy-MM-dd");
  const updatedYaml = 
`last_updated: "${todayStr}"
light_stock: ${lightStock}
comp_stock: ${compStock}
status_message: "${statusMessage}"
`;

  const apiUrl = `https://api.github.com/repos/${GITHUB_USERNAME}/${GITHUB_REPO}/contents/${INVENTORY_FILE_PATH}`;
  const putPayload = {
    message: `Automated inventory decrement (${itemType}) via Venmo sale: ${orderSubject}`,
    content: Utilities.base64Encode(updatedYaml),
    sha: inventory.sha
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
    Logger.log(`GitHub inventory updated: Light=${lightStock}, Comp=${compStock}`);
    return true;
  } else {
    Logger.log(`Failed to update inventory on GitHub (${putResponse.getResponseCode()}): ${putResponse.getContentText()}`);
    return false;
  }
}

function getGitHubToken() {
  return PropertiesService.getScriptProperties().getProperty('GITHUB_TOKEN');
}

function getOrCreateSyncLabel() {
  let label = GmailApp.getUserLabelByName(SYNC_LABEL_NAME);
  if (!label) {
    label = GmailApp.createLabel(SYNC_LABEL_NAME);
  }
  return label;
}
