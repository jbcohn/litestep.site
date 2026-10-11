import os
import json
import re
from decimal import Decimal
import requests
import stripe

# 1. Credentials
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")
PRINTFUL_API_KEY = os.environ.get("PRINTFUL_API_KEY")
PRINTFUL_STORE_ID = os.environ.get("PRINTFUL_STORE_ID", "18881050")

# Support loading from .env if present locally
ENV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
if os.path.exists(ENV_FILE):
    with open(ENV_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                k = k.strip()
                v = v.strip().strip('"').strip("'")
                if k == "STRIPE_SECRET_KEY" and not STRIPE_SECRET_KEY:
                    STRIPE_SECRET_KEY = v
                elif k == "PRINTFUL_API_KEY" and not PRINTFUL_API_KEY:
                    PRINTFUL_API_KEY = v
                elif k == "PRINTFUL_STORE_ID" and not os.environ.get("PRINTFUL_STORE_ID"):
                    PRINTFUL_STORE_ID = v

if not STRIPE_SECRET_KEY:
    raise ValueError("STRIPE_SECRET_KEY environment variable is required")
if not PRINTFUL_API_KEY:
    raise ValueError("PRINTFUL_API_KEY environment variable is required")

stripe.api_key = STRIPE_SECRET_KEY

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "assets", "images", "products")
DATA_DIR = os.path.join(BASE_DIR, "_data")
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

OUTPUT_FILE = os.path.join(DATA_DIR, "merch_products.json")
LEGACY_WHITNEY_FILE = os.path.join(DATA_DIR, "whitney_merch_links.json")

# Custom marketing descriptions & tags for specific products
PRODUCT_METADATA = {
    480089207: {  # Mount Whitney
        "display_name": "Mount Whitney Ridgelines Elevation Graphic T-Shirt",
        "tag": "California Peaks · Direct Print-on-Demand",
        "description": "Stacked algorithmic ridgeline contours of California's highest summit (14,505 ft). Printed on premium cotton with soft water-based inks."
    },
    480350932: {  # North Palisade
        "display_name": "North Palisade - Glaciated AF - Tri-Blend T-Shirt",
        "tag": "High Sierra 14ers · Direct Print-on-Demand",
        "description": "Topographic elevation artwork celebrating North Palisade and the Palisade Glacier in California's High Sierra. Printed on ultra-soft tri-blend fabric."
    },
    480312304: {  # Rainbow Sunflower
        "display_name": "Rainbow Sunflower Tri-Blend T-Shirt",
        "tag": "Algorithmic Art · Direct Print-on-Demand",
        "description": "Vibrant algorithmic floral geometry blending mathematical phyllotaxis spiral patterns with a vivid chromatic gradient spectrum."
    },
    479948902: {  # Bubbles!
        "display_name": "Bubbles! Procedural Graphic T-Shirt",
        "tag": "Mathematical Geometry · Direct Print-on-Demand",
        "description": "Original generative circle packing and procedural bubble membrane geometry rendered with striking modern color contrasts."
    },
    479899530: {  # Violet Eye Hex Mandala
        "display_name": "Violet Eye Hexagon Mandala Graphic T-Shirt",
        "tag": "Fractal Art · Direct Print-on-Demand",
        "description": "Intricate hexagon fractal mandala spiraling into an intense geometric center. A striking statement piece for fans of fractal geometry."
    }
}

size_order = ["XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL"]

def slugify(text):
    text = re.sub(r'[\s\-]+', '_', text.strip().lower())
    return re.sub(r'[^a-z0-9_]', '', text)

def parse_garment_name(raw_name):
    if not raw_name:
        return "Premium Unisex T-Shirt"
    # Extract string before parentheses e.g. "Bella + Canvas 3001 Unisex Short Sleeve Jersey T-Shirt"
    match = re.match(r'^([^(]+)', raw_name)
    if match:
        name = match.group(1).replace("with Tear Away Label", "").strip()
        return re.sub(r'\s+', ' ', name)
    return raw_name

# 2. Fetch existing Stripe Products & Payment Links to avoid duplicates
print("Loading existing Stripe Live catalog...")
existing_products_by_sync_id = {}
existing_links_by_sync_id = {}

has_more = True
starting_after = None
while has_more:
    res = stripe.Product.list(limit=100, starting_after=starting_after)
    for prod in res.data:
        meta = prod.metadata.to_dict()
        var_id = meta.get("printful_sync_variant_id")
        if var_id:
            existing_products_by_sync_id[str(var_id)] = prod
    has_more = res.has_more
    if has_more and res.data:
        starting_after = res.data[-1].id

has_more = True
starting_after = None
while has_more:
    res = stripe.PaymentLink.list(limit=100, starting_after=starting_after)
    for pl in res.data:
        meta = pl.metadata.to_dict()
        var_id = meta.get("printful_sync_variant_id")
        if var_id and pl.active:
            existing_links_by_sync_id[str(var_id)] = pl
    has_more = res.has_more
    if has_more and res.data:
        starting_after = res.data[-1].id

print(f"Found {len(existing_products_by_sync_id)} existing synced products and {len(existing_links_by_sync_id)} active payment links in Stripe.")

# 3. Query all products from Printful API store
print("\nFetching product list from Printful store...")
store_res = requests.get(
    "https://api.printful.com/store/products?limit=100",
    headers={
        "Authorization": f"Bearer {PRINTFUL_API_KEY}",
        "X-PF-Store-Id": PRINTFUL_STORE_ID
    }
)
store_res.raise_for_status()
store_products = store_res.json()["result"]
print(f"Found {len(store_products)} products in Printful store.")

active_printful_variant_ids = set()
catalog_data = {}

# Preferred display order
preferred_order = [480089207, 480350932, 480312304, 479899530, 479948902]
store_products.sort(key=lambda p: preferred_order.index(p["id"]) if p["id"] in preferred_order else 999)

for sp in store_products:
    pid = sp["id"]
    print(f"\n=======================================================")
    print(f"Syncing Product: {sp['name']} (ID: {pid})")
    print(f"=======================================================")

    p_res = requests.get(
        f"https://api.printful.com/store/products/{pid}",
        headers={
            "Authorization": f"Bearer {PRINTFUL_API_KEY}",
            "X-PF-Store-Id": PRINTFUL_STORE_ID
        }
    )
    p_res.raise_for_status()
    p_data = p_res.json()["result"]
    sync_prod = p_data["sync_product"]
    variants = p_data["sync_variants"]
    product_name = sync_prod["name"]

    prod_slug = slugify(product_name.replace("Unisex t-shirt", "").replace("Short sleeve tri-blend t-shirt", "").replace("short sleeve t-shirt", ""))
    
    # Custom metadata or sensible defaults
    custom_meta = PRODUCT_METADATA.get(pid, {})
    display_title = custom_meta.get("display_name", product_name)
    tag = custom_meta.get("tag", "Original Apparel · Direct Print-on-Demand")
    description = custom_meta.get("description", f"Original graphic design printed on demand with high-definition inks.")

    first_var = variants[0] if variants else {}
    garment_model = parse_garment_name(first_var.get("product", {}).get("name"))

    prod_entry = {
        "id": pid,
        "slug": prod_slug,
        "name": display_title,
        "tag": tag,
        "description": description,
        "garment": garment_model,
        "colors": {}
    }

    # Group variants by color
    color_groups = {}
    for v in variants:
        color = v.get("color", "Default")
        color_groups.setdefault(color, []).append(v)

    for color, var_list in color_groups.items():
        color_slug = slugify(color)
        
        # Download preview image for this color
        local_img_rel = f"/assets/images/products/{prod_slug}_{color_slug}.jpg"
        local_img_path = os.path.join(IMAGES_DIR, f"{prod_slug}_{color_slug}.jpg")

        preview_url = None
        # Look for mockup preview ('preview' type), fallback to any preview_url
        for file_info in var_list[0].get("files", []):
            if file_info.get("type") == "preview" and file_info.get("preview_url"):
                preview_url = file_info["preview_url"]
                break
        if not preview_url:
            for file_info in var_list[0].get("files", []):
                if file_info.get("preview_url"):
                    preview_url = file_info["preview_url"]
                    break

        if preview_url and not os.path.exists(local_img_path):
            print(f"  Downloading mockup: {color} -> {local_img_rel}")
            try:
                img_res = requests.get(preview_url, timeout=15)
                if img_res.ok:
                    with open(local_img_path, "wb") as f:
                        f.write(img_res.content)
            except Exception as e:
                print(f"  Warning: Image download error for {color}: {e}")

        prod_entry["colors"][color] = {
            "name": color,
            "slug": color_slug,
            "image": local_img_rel,
            "sizes": {}
        }

        for v in var_list:
            sync_variant_id = str(v["id"])
            active_printful_variant_ids.add(sync_variant_id)
            size = v.get("size", "M")

            raw_price = v.get("retail_price", "26.87")
            price_cents = int(Decimal(raw_price) * 100)
            amount_str = f"${(price_cents / 100):.2f}"
            currency = v.get("currency", "USD").lower()

            # Check if this variant already exists in Stripe
            if sync_variant_id in existing_links_by_sync_id and sync_variant_id in existing_products_by_sync_id:
                existing_plink = existing_links_by_sync_id[sync_variant_id]
                existing_prod = existing_products_by_sync_id[sync_variant_id]
                plink_url = existing_plink.url
                prod_id = existing_prod.id
                print(f"  [Cached] {color} - {size} ({amount_str}) -> {plink_url}")
            else:
                variant_title = f"{product_name} - {color} (Size {size})"
                print(f"  [Creating] {variant_title} ({amount_str})...")

                # Create Product in Stripe
                prod_images = [preview_url] if preview_url else []
                stripe_prod = stripe.Product.create(
                    name=variant_title,
                    description=f"{garment_model} in {color}, Size {size}.",
                    images=prod_images,
                    tax_code="txcd_30011000",
                    metadata={
                        "printful_sync_product_id": str(pid),
                        "printful_sync_variant_id": sync_variant_id,
                        "color": color,
                        "size": size
                    }
                )
                prod_id = stripe_prod.id

                # Create Price
                stripe_price = stripe.Price.create(
                    product=prod_id,
                    unit_amount=price_cents,
                    currency=currency,
                    nickname=f"{color} - Size {size}",
                    metadata={
                        "printful_sync_variant_id": sync_variant_id,
                        "color": color,
                        "size": size
                    }
                )

                # Create Payment Link
                plink = stripe.PaymentLink.create(
                    line_items=[{"price": stripe_price.id, "quantity": 1}],
                    shipping_address_collection={"allowed_countries": ["US"]},
                    automatic_tax={"enabled": True},
                    billing_address_collection="auto",
                    metadata={
                        "printful_sync_variant_id": sync_variant_id,
                        "color": color,
                        "size": size
                    }
                )
                plink_url = plink.url
                existing_links_by_sync_id[sync_variant_id] = plink
                existing_products_by_sync_id[sync_variant_id] = stripe_prod
                print(f"    ✓ New Link: {plink_url}")

            prod_entry["colors"][color]["sizes"][size] = {
                "price": amount_str,
                "price_cents": price_cents,
                "url": plink_url,
                "product_id": prod_id,
                "sync_variant_id": sync_variant_id
            }

        # Sort sizes
        sorted_sizes = {}
        for s in size_order:
            if s in prod_entry["colors"][color]["sizes"]:
                sorted_sizes[s] = prod_entry["colors"][color]["sizes"][s]
        for s, obj in prod_entry["colors"][color]["sizes"].items():
            if s not in sorted_sizes:
                sorted_sizes[s] = obj
        prod_entry["colors"][color]["sizes"] = sorted_sizes

    catalog_data[prod_slug] = prod_entry

# 4. Check for deleted variants in Stripe
print("\nChecking for deleted/orphaned variants in Stripe...")
orphans_archived = 0
for var_id, prod in existing_products_by_sync_id.items():
    if var_id not in active_printful_variant_ids and prod.active:
        print(f"  Archiving deleted variant in Stripe: {prod.name} (Sync ID: {var_id})")
        try:
            stripe.Product.modify(prod.id, active=False)
            orphans_archived += 1
        except Exception as e:
            print(f"  Error archiving product {prod.id}: {e}")

print(f"Archived {orphans_archived} outdated products in Stripe.")

# 5. Save unified catalog JSON
with open(OUTPUT_FILE, "w") as f:
    json.dump(catalog_data, f, indent=2)
print(f"\nSaved unified catalog to: {OUTPUT_FILE}")

# Backward compatibility: save Mount Whitney colors to whitney_merch_links.json
if "mount_whitney_ridgelines" in catalog_data:
    with open(LEGACY_WHITNEY_FILE, "w") as f:
        json.dump(catalog_data["mount_whitney_ridgelines"]["colors"], f, indent=2)
    print(f"Updated legacy mapping: {LEGACY_WHITNEY_FILE}")

print("\n=======================================================")
print(f"ALL DONE! Synced {len(catalog_data)} products to Stripe.")
print("=======================================================")