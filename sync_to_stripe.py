import os
import json
import re
import time
from decimal import Decimal
from io import BytesIO
from PIL import Image
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
DATA_DIR_PATH = os.path.abspath(DATA_DIR)
os.makedirs(DATA_DIR_PATH, exist_ok=True)

OUTPUT_FILE = os.path.join(DATA_DIR, "merch_products.json")
LEGACY_WHITNEY_FILE = os.path.join(DATA_DIR, "whitney_merch_links.json")

def save_clean_image(img_bytes, dest_path, overwrite=False):
    """
    Saves an image as high-quality RGB JPEG (quality=95).
    Guarantees:
    - Never overwrites an existing mockup file unless overwrite=True.
    - If the image has an alpha channel, composites onto a pure white (255, 255, 255) background.
    - If the image is a lifestyle photo without alpha, preserves the lifestyle background.
    """
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 0 and not overwrite:
        return
    im = Image.open(BytesIO(img_bytes))
    if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):
        im = im.convert('RGBA')
        bg = Image.new('RGB', im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[3])
        im = bg
    elif im.mode != 'RGB':
        im = im.convert('RGB')
    im.save(dest_path, 'JPEG', quality=95)

# Custom marketing descriptions, tags, and model mockup configurations
PRODUCT_METADATA = {
    480089207: {  # Mount Whitney
        "display_name": "Mount Whitney Ridgelines Elevation Graphic T-Shirt",
        "tag": "California Peaks · Direct Print-on-Demand",
        "description": "Stacked algorithmic ridgeline contours of California's highest summit (14,505 ft). Printed on premium cotton with soft water-based inks.",
        "model_prefix": "model_whitney",
        "model_config": {
            "option_group": "Men's 4",
            "option": "Left Front",
            "top": 300
        }
    },
    480350932: {  # North Palisade
        "display_name": "North Palisade - Glaciated AF - Tri-Blend T-Shirt",
        "tag": "High Sierra 14ers · Direct Print-on-Demand",
        "description": "Topographic elevation artwork celebrating North Palisade and the Palisade Glacier in California's High Sierra. Printed on ultra-soft tri-blend fabric.",
        "model_prefix": "model_palisade",
        "model_config": {
            "option_group": "Men's 3",
            "option": "Right Front",
            "top": 300
        }
    },
    480312304: {  # Rainbow Sunflower
        "display_name": "Rainbow Sunflower Tri-Blend T-Shirt",
        "tag": "Algorithmic Art · Direct Print-on-Demand",
        "description": "Vibrant algorithmic floral geometry blending mathematical phyllotaxis spiral patterns with a vivid chromatic gradient spectrum.",
        "model_prefix": "model_sunflower",
        "model_config": {
            "option_group": "Women's 4",
            "option": "Front",
            "top": 250
        }
    },
    479948902: {  # Bubbles!
        "display_name": "Bubbles! Procedural Graphic T-Shirt",
        "tag": "Mathematical Geometry · Direct Print-on-Demand",
        "description": "Original generative circle packing and procedural bubble membrane geometry rendered with striking modern color contrasts.",
        "model_prefix": "model_bubbles",
        "model_config": {
            "option_group": "Men's Lifestyle",
            "option": "Front",
            "top": 0
        }
    },
    479899530: {  # Violet Eye Hex Mandala
        "display_name": "Violet Eye Hexagon Mandala Graphic T-Shirt",
        "tag": "Fractal Art · Direct Print-on-Demand",
        "description": "Intricate hexagon fractal mandala spiraling into an intense geometric center. A striking statement piece for fans of fractal geometry.",
        "model_prefix": "model_violet",
        "model_config": {
            "option_group": "Women's Lifestyle 2",
            "option": "Front",
            "top": 200
        }
    },
    481559531: {  # Mount Diablo
        "display_name": "Mount Diablo Topographic Wireframe Elevation Graphic T-Shirt",
        "tag": "California Peaks · Direct Print-on-Demand",
        "description": "Intricate 3D terrain wireframe in vivid heat-map slopes on premium tri-blend tees.",
        "model_prefix": "model_diablo",
        "primary_color": "Brown Triblend",
        "model_config": {
            "option_group": "Men's 3",
            "option": "Front",
            "top": 300
        }
    },
    481791025: {  # California Shaded Elevations
        "display_name": "California Shaded Elevations Topographic Graphic T-Shirt",
        "tag": "California Topography · Direct Print-on-Demand",
        "description": "High-definition shaded relief elevation profile of California from coast to summit. Printed on ultra-soft tri-blend tees.",
        "model_prefix": "model_california",
        "primary_color": "Red Triblend",
        "model_config": {
            "option_group": "Women's Lifestyle",
            "option": "Front",
            "top": 200
        }
    },
    481939533: {  # Mount Vaca
        "display_name": "Mount Vaca Ridgelines Elevation Hooded Long-Sleeve Tee",
        "tag": "Northern California Peaks · Direct Print-on-Demand",
        "description": "Algorithmic ridgeline contours of Mount Vaca (2,819 ft), highest summit in the Vaca Mountains. Printed on ultra-lightweight hooded tees.",
        "model_prefix": "model_vaca"
    }
}

size_order = ["XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL"]

def slugify(text):
    text = re.sub(r'[\s\-]+', '_', text.strip().lower())
    return re.sub(r'[^a-z0-9_]', '', text)

def parse_garment_name(raw_name):
    if not raw_name:
        return "Premium Unisex T-Shirt"
    match = re.match(r'^([^(]+)', raw_name)
    if match:
        name = match.group(1).replace("with Tear Away Label", "").strip()
        return re.sub(r'\s+', ' ', name)
    return raw_name

def sync_model_mockups(pid, prod_slug, variants, color_groups, custom_meta, existing_prod_data=None):
    """
    Ensures high-resolution (2000px) colorway model mockups exist for each color of the product,
    saving them with clean white or lifestyle backgrounds (no black backgrounds).
    Guarantees that previously chosen mockups for the store are never replaced or overwritten.
    Returns (product_model_image_rel, dict_of_color_to_model_image_rel).
    """
    model_prefix = custom_meta.get("model_prefix", f"model_{prod_slug}")
    model_cfg = custom_meta.get("model_config")
    existing_prod_data = existing_prod_data or {}

    # Check if existing product already has a primary model image
    prev_primary_rel = existing_prod_data.get("model_image")
    if prev_primary_rel and os.path.exists(os.path.join(BASE_DIR, prev_primary_rel.lstrip("/"))):
        primary_rel = prev_primary_rel
        primary_path = os.path.join(BASE_DIR, prev_primary_rel.lstrip("/"))
    else:
        primary_rel = f"/assets/images/products/{model_prefix}.jpg"
        primary_path = os.path.join(IMAGES_DIR, f"{model_prefix}.jpg")

    color_model_images = {}
    missing_for_task = {}  # catalog_variant_id -> color_name

    for color, var_list in color_groups.items():
        color_slug = slugify(color)

        # 1. First priority: Check if existing catalog already specifies a model mockup for this color
        prev_color_model = existing_prod_data.get("colors", {}).get(color, {}).get("model_image")
        if prev_color_model:
            prev_model_path = os.path.join(BASE_DIR, prev_color_model.lstrip("/"))
            if os.path.exists(prev_model_path) and os.path.getsize(prev_model_path) > 0:
                color_model_images[color] = prev_color_model
                print(f"  [Model Mockup Preserved] {color} -> {prev_color_model}")
                continue

        # 2. Second priority: Check if file already exists locally on disk
        model_filename = f"{model_prefix}_{color_slug}.jpg"
        model_rel = f"/assets/images/products/{model_filename}"
        model_path = os.path.join(IMAGES_DIR, model_filename)

        if os.path.exists(model_path) and os.path.getsize(model_path) > 0:
            color_model_images[color] = model_rel
            print(f"  [Model Mockup Preserved on Disk] {color} -> {model_rel}")
            continue

        # 3. Only if missing both in catalog and on disk, and model_cfg is configured, queue for generation
        if model_cfg:
            cat_vid = var_list[0].get("variant_id")
            if cat_vid:
                missing_for_task[cat_vid] = color

    # If any colors are missing mockups and we have a model_config, generate in batch
    if missing_for_task and model_cfg:
        v0 = variants[0] if variants else {}
        cat_prod_id = v0.get("product", {}).get("product_id")
        art_file = next((f for f in v0.get("files", []) if f.get("type") == "front_large"), None)
        if not art_file:
            art_file = next((f for f in v0.get("files", []) if f.get("preview_url")), None)

        if cat_prod_id and art_file and art_file.get("preview_url"):
            print(f"  Generating {len(missing_for_task)} missing 2000px model mockups for {model_prefix}...")
            area_w = 1800 if cat_prod_id == 162 else 2250
            area_h = 2400 if cat_prod_id == 162 else 2700
            w = area_w
            art_w = art_file.get("width") or 4000
            art_h = art_file.get("height") or 4000
            h = int(art_h * area_w / art_w)
            if h > area_h:
                h = area_h
                w = int(art_w * area_h / art_h)
            top = model_cfg.get("top", 200)
            left = max(0, (area_w - w) // 2)

            pos = {
                "area_width": area_w,
                "area_height": area_h,
                "width": w,
                "height": h,
                "top": top,
                "left": left
            }

            payload = {
                "variant_ids": list(missing_for_task.keys()),
                "format": "jpg",
                "width": 2000,
                "option_groups": [model_cfg["option_group"]],
                "options": [model_cfg["option"]],
                "files": [{
                    "placement": "front_large",
                    "image_url": art_file["preview_url"],
                    "position": pos
                }]
            }

            try:
                task_res = requests.post(
                    f"https://api.printful.com/mockup-generator/create-task/{cat_prod_id}",
                    headers={
                        "Authorization": f"Bearer {PRINTFUL_API_KEY}",
                        "X-PF-Store-Id": PRINTFUL_STORE_ID
                    },
                    json=payload,
                    timeout=20
                ).json()

                if task_res.get("code") == 200 and "task_key" in task_res.get("result", {}):
                    tkey = task_res["result"]["task_key"]
                    for _ in range(40):
                        time.sleep(3)
                        poll_res = requests.get(
                            f"https://api.printful.com/mockup-generator/task?task_key={tkey}",
                            headers={
                                "Authorization": f"Bearer {PRINTFUL_API_KEY}",
                                "X-PF-Store-Id": PRINTFUL_STORE_ID
                            },
                            timeout=15
                        ).json()
                        status = poll_res.get("result", {}).get("status")
                        if status == "completed":
                            for m in poll_res.get("result", {}).get("mockups", []):
                                vid = m.get("variant_ids", [None])[0]
                                c_name = missing_for_task.get(vid)
                                if c_name and m.get("mockup_url"):
                                    c_slug = slugify(c_name)
                                    target_filename = f"{model_prefix}_{c_slug}.jpg"
                                    target_path = os.path.join(IMAGES_DIR, target_filename)
                                    target_rel = f"/assets/images/products/{target_filename}"
                                    img_content = requests.get(m["mockup_url"], timeout=20).content
                                    save_clean_image(img_content, target_path)
                                    color_model_images[c_name] = target_rel
                                    print(f"    ✓ Saved 2000px model: {c_name} -> {target_rel}")
                            break
                        elif status == "failed":
                            print(f"    Warning: Mockup generation task failed for {model_prefix}: {poll_res}")
                            break
                else:
                    print(f"    Warning: Failed to queue mockup task for {model_prefix}: {task_res}")
            except Exception as e:
                print(f"    Warning: Exception generating model mockups for {model_prefix}: {e}")

    # Ensure primary model image exists
    if not os.path.exists(primary_path) and color_model_images:
        pref_color = custom_meta.get("primary_color")
        chosen_color_model = color_model_images.get(pref_color) if (pref_color and pref_color in color_model_images) else list(color_model_images.values())[0]
        chosen_path = os.path.join(BASE_DIR, chosen_color_model.lstrip("/"))
        if os.path.exists(chosen_path):
            with open(chosen_path, "rb") as fi, open(primary_path, "wb") as fo:
                fo.write(fi.read())

    has_primary = os.path.exists(primary_path) and os.path.getsize(primary_path) > 0
    return (primary_rel if has_primary else None, color_model_images)

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

# Load existing catalog to preserve custom mockups, slugs, and data
existing_catalog = {}
if os.path.exists(OUTPUT_FILE):
    try:
        with open(OUTPUT_FILE, "r") as f:
            existing_catalog = json.load(f)
        print(f"Loaded existing catalog with {len(existing_catalog)} products from {OUTPUT_FILE}")
    except Exception as e:
        print(f"Warning loading existing catalog: {e}")

existing_by_id = {prod["id"]: (slug, prod) for slug, prod in existing_catalog.items() if isinstance(prod, dict) and "id" in prod}

catalog_data = {}

# Preferred display order
preferred_order = [480089207, 480350932, 481559531, 481791025, 481939533, 480312304, 479899530, 479948902]
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

    existing_slug, existing_prod_data = existing_by_id.get(pid, (None, {}))
    prod_slug = existing_slug if existing_slug else slugify(
        product_name.replace("Unisex t-shirt", "")
        .replace("Short sleeve tri-blend t-shirt", "")
        .replace("short sleeve t-shirt", "")
        .replace("Hooded long-sleeve tee", "")
    )
    
    # Custom metadata or sensible defaults
    custom_meta = PRODUCT_METADATA.get(pid, {})
    display_title = custom_meta.get("display_name", existing_prod_data.get("name", product_name))
    tag = custom_meta.get("tag", existing_prod_data.get("tag", "Original Apparel · Direct Print-on-Demand"))
    description = custom_meta.get("description", existing_prod_data.get("description", f"Original graphic design printed on demand with high-definition inks."))

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

    # Sync colorway model mockups (clean white or lifestyle background, 2000px)
    primary_model_rel, color_model_rels = sync_model_mockups(
        pid, prod_slug, variants, color_groups, custom_meta, existing_prod_data=existing_prod_data
    )
    if primary_model_rel:
        prod_entry["model_image"] = primary_model_rel

    for color, var_list in color_groups.items():
        color_slug = slugify(color)
        
        # 1. First priority for flat mockup: check existing catalog & verify file exists
        prev_flat_img = existing_prod_data.get("colors", {}).get(color, {}).get("image")
        if prev_flat_img and os.path.exists(os.path.join(BASE_DIR, prev_flat_img.lstrip("/"))):
            local_img_rel = prev_flat_img
            local_img_path = os.path.join(BASE_DIR, prev_flat_img.lstrip("/"))
            print(f"  [Flat Mockup Preserved] {color} -> {local_img_rel}")
        else:
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
                print(f"  Downloading flat mockup: {color} -> {local_img_rel}")
                try:
                    img_res = requests.get(preview_url, timeout=15)
                    if img_res.ok:
                        save_clean_image(img_res.content, local_img_path)
                except Exception as e:
                    print(f"  Warning: Image download error for {color}: {e}")
            elif os.path.exists(local_img_path):
                print(f"  [Flat Mockup on Disk Preserved] {color} -> {local_img_rel}")

        prod_entry["colors"][color] = {
            "name": color,
            "slug": color_slug,
            "image": local_img_rel,
            "sizes": {}
        }
        color_model_img = color_model_rels.get(color, primary_model_rel)
        if color_model_img:
            prod_entry["colors"][color]["model_image"] = color_model_img

        for v in var_list:
            sync_variant_id = str(v["id"])
            active_printful_variant_ids.add(sync_variant_id)
            size = v.get("size", "M")

            raw_price = v.get("retail_price", "26.87")
            # Lower base price by $4.00 (400 cents) since shipping ($4.79 on 1 shirt, FREE on 2+) is charged separately at checkout
            price_cents = max(100, int(Decimal(raw_price) * 100) - 400)
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
                    after_completion={
                        "type": "redirect",
                        "redirect": {"url": "https://litestep.us/merch/thank-you/?session_id={CHECKOUT_SESSION_ID}"}
                    },
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

# Preserve any offline or un-synced products from existing catalog
for ex_slug, ex_prod in existing_catalog.items():
    if ex_slug not in catalog_data and isinstance(ex_prod, dict):
        ex_id = ex_prod.get("id")
        if not any(sp.get("id") == ex_id for sp in store_products):
            print(f"Preserving existing catalog product: {ex_slug} (ID: {ex_id})")
            catalog_data[ex_slug] = ex_prod

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

# Export verified variant pricing lookup for Cloudflare Worker dynamic cart checkout
WORKER_CATALOG_FILE = os.path.join(BASE_DIR, "..", "litestep-printful-webhook", "src", "catalog_prices.js")
if os.path.exists(os.path.dirname(WORKER_CATALOG_FILE)):
    worker_map = {}
    for p_slug, p_obj in catalog_data.items():
        for c_name, c_obj in p_obj.get("colors", {}).items():
            for s_name, s_obj in c_obj.get("sizes", {}).items():
                sv_id = str(s_obj.get("sync_variant_id", ""))
                if sv_id:
                    worker_map[sv_id] = {
                        "product_id": s_obj["product_id"],
                        "price_cents": s_obj["price_cents"]
                    }
    with open(WORKER_CATALOG_FILE, "w") as wf:
        wf.write("// Auto-generated by sync_to_stripe.py\n")
        wf.write(f"export const CATALOG_PRICES = {json.dumps(worker_map, indent=2)};\n")
    print(f"Updated Cloudflare Worker catalog prices: {WORKER_CATALOG_FILE}")

# Backward compatibility: save Mount Whitney colors to whitney_merch_links.json
if "mount_whitney_ridgelines" in catalog_data:
    with open(LEGACY_WHITNEY_FILE, "w") as f:
        json.dump(catalog_data["mount_whitney_ridgelines"]["colors"], f, indent=2)
    print(f"Updated legacy mapping: {LEGACY_WHITNEY_FILE}")

print("\n=======================================================")
print(f"ALL DONE! Synced {len(catalog_data)} products to Stripe.")
print("=======================================================")