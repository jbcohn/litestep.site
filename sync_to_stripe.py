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
SIZE_GUIDES_FILE = os.path.join(DATA_DIR, "size_guides.json")
SIZE_GUIDES_IMG_DIR = os.path.join(BASE_DIR, "assets", "images", "size_guides")
os.makedirs(SIZE_GUIDES_IMG_DIR, exist_ok=True)

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
        "display_name": "Mount Whitney Ridgelines Unisex Elevation Graphic T-Shirt",
        "tag": "California Peaks · Unisex Apparel",
        "description": "Stacked algorithmic ridgeline contours of California's highest summit (14,505 ft). Printed on premium cotton with soft water-based inks.",
        "is_unisex": True,
        "male_model_prefix": "model_whitney",
        "female_model_prefix": "model_whitney_female",
        "male_model_config": {"option_group": "Men's 4", "option": "Left Front", "top": 300},
        "female_model_config": {"option_group": "Women's 4", "option": "Front", "top": 200, "placements": ["front_large"]}
    },
    480350932: {  # North Palisade
        "display_name": "North Palisade - Glaciated AF - Unisex Tri-Blend T-Shirt",
        "tag": "High Sierra 14ers · Unisex Apparel",
        "description": "Topographic elevation artwork celebrating North Palisade and the Palisade Glacier in California's High Sierra. Printed on ultra-soft tri-blend fabric.",
        "is_unisex": True,
        "male_model_prefix": "model_palisade",
        "female_model_prefix": "model_palisade_female",
        "male_model_config": {"option_group": "Men's 3", "option": "Right Front", "top": 300},
        "female_model_config": {"option_group": "Women's Lifestyle", "option": "Front", "top": 200, "placements": ["front_large"]}
    },
    480312304: {  # Rainbow Sunflower
        "display_name": "Rainbow Sunflower Unisex Tri-Blend T-Shirt",
        "tag": "Algorithmic Art · Unisex Apparel",
        "description": "Vibrant algorithmic floral geometry blending mathematical phyllotaxis spiral patterns with a vivid chromatic gradient spectrum.",
        "is_unisex": True,
        "male_model_prefix": "model_sunflower_male",
        "female_model_prefix": "model_sunflower",
        "male_model_config": {"option_group": "Men's 3", "option": "Right Front", "top": 200, "placements": ["front_large"]},
        "female_model_config": {"option_group": "Women's 4", "option": "Front", "top": 250}
    },
    479948902: {  # Bubbles!
        "display_name": "Bubbles! Unisex Procedural Graphic T-Shirt",
        "tag": "Mathematical Geometry · Unisex Apparel",
        "description": "Original generative circle packing and procedural bubble membrane geometry rendered with striking modern color contrasts.",
        "is_unisex": True,
        "male_model_prefix": "model_bubbles",
        "female_model_prefix": "model_bubbles_female",
        "male_model_config": {"option_group": "Men's Lifestyle", "option": "Front", "top": 0},
        "female_model_config": {"option_group": "Women's 4", "option": "Front", "top": 200, "placements": ["front_large"]}
    },
    479899530: {  # Violet Eye Hex Mandala
        "display_name": "Violet Eye Hexagon Mandala Unisex Graphic T-Shirt",
        "tag": "Fractal Art · Unisex Apparel",
        "description": "Intricate hexagon fractal mandala spiraling into an intense geometric center. A striking statement piece for fans of fractal geometry.",
        "is_unisex": True,
        "male_model_prefix": "model_violet_male",
        "female_model_prefix": "model_violet",
        "male_model_config": {"option_group": "Men's 4", "option": "Left Front", "top": 200, "placements": ["front_large"]},
        "female_model_config": {"option_group": "Women's Lifestyle 2", "option": "Front", "top": 200}
    },
    481559531: {  # Mount Diablo
        "display_name": "Mount Diablo Topographic Wireframe Unisex Elevation Graphic T-Shirt",
        "tag": "California Peaks · Unisex Apparel",
        "description": "Intricate 3D terrain wireframe in vivid heat-map slopes on premium tri-blend tees.",
        "is_unisex": True,
        "primary_color": "Brown Triblend",
        "male_model_prefix": "model_diablo",
        "female_model_prefix": "model_diablo_female",
        "male_model_config": {"option_group": "Men's 3", "option": "Front", "top": 300},
        "female_model_config": {"option_group": "Women's Lifestyle", "option": "Front", "top": 200, "placements": ["front_large"]}
    },
    481791025: {  # California Shaded Elevations
        "display_name": "California Shaded Elevations Topographic Unisex Graphic T-Shirt",
        "tag": "California Topography · Unisex Apparel",
        "description": "High-definition shaded relief elevation profile of California from coast to summit. Printed on ultra-soft tri-blend tees.",
        "is_unisex": True,
        "primary_color": "Charcoal-Black Triblend",
        "male_model_prefix": "model_california_male",
        "female_model_prefix": "model_california",
        "male_model_config": {"option_group": "Men's 3", "option": "Right Front", "top": 200, "placements": ["front_large"]},
        "female_model_config": {"option_group": "Women's Lifestyle", "option": "Front", "top": 200, "placements": ["front_large"]},
        "flat_config": {"option_group": "Flat", "option": "Front", "placements": ["front_large"]}
    },
    481939533: {  # Mount Vaca
        "display_name": "Mount Vaca Ridgelines Unisex Elevation Hooded Long-Sleeve Tee",
        "tag": "Northern California Peaks · Unisex Apparel",
        "description": "Algorithmic ridgeline contours of Mount Vaca (2,819 ft), highest summit in the Vaca Mountains. Printed on ultra-lightweight hooded tees.",
        "is_unisex": True,
        "male_model_prefix": "model_vaca",
        "female_model_prefix": "model_vaca_female",
        "male_model_config": {"option_group": "Men's", "option": "Front", "top": 0, "placements": ["front"]},
        "female_model_config": {"option_group": "Women's", "option": "Front", "top": 100, "placements": ["front"]}
    },
    483500528: {  # One-Piece Swimsuit
        "display_name": "Violet Eye Hexagon Mandala One-Piece Swimsuit",
        "tag": "Fractal Art · Direct Print-on-Demand",
        "description": "Vivid all-over print featuring an intricate violet and cyan hexagon fractal mandala. Smooth, chlorine-resistant fabric with UPF 50+ protection.",
        "is_unisex": False,
        "female_model_prefix": "model_one_piece_swimsuit",
        "primary_color": "White",
        "female_model_config": {"option_group": "Women's 2", "option": "Front", "placements": ["front", "back"]}
    },
    483496351: {  # Muscle Shirt
        "display_name": "Violet Eye Hexagon Mandala Unisex Muscle Tank",
        "tag": "Fractal Art · Unisex Apparel",
        "description": "Sleeveless relaxed-fit muscle tank featuring the intricate Violet Eye hexagon mandala. Premium 100% combed ring-spun cotton.",
        "is_unisex": True,
        "male_model_prefix": "model_muscle_shirt_male",
        "female_model_prefix": "model_muscle_shirt",
        "primary_color": "White",
        "male_model_config": {"option_group": "Men's", "option": "Front", "top": 0, "placements": ["front"]},
        "female_model_config": {"option_group": "Women's", "option": "Front", "placements": ["front"]},
        "flat_config": {"option_group": "Flat", "option": "Front", "placements": ["front"]}
    },
    483495525: {  # Bodycon dress
        "display_name": "Violet Eye Hexagon Mandala Bodycon Dress",
        "tag": "Fractal Art · Direct Print-on-Demand",
        "description": "Eye-catching body-hugging dress showcasing concentric hexagon fractal geometry in vivid violet and turquoise gradients.",
        "is_unisex": False,
        "female_model_prefix": "model_bodycon_dress",
        "primary_color": "White",
        "female_model_config": {"option_group": "Women's", "option": "Front", "placements": ["default"]}
    },
    483492839: {  # Blue Hex Portal
        "display_name": "Blue Hex Portal Unisex Graphic Tri-Blend T-Shirt",
        "tag": "Fractal Art · Unisex Apparel",
        "description": "Intricate concentric hexagon fractal mandala radiating through a luminous cyan and royal blue spectrum. Printed on ultra-soft tri-blend fabric.",
        "is_unisex": True,
        "male_model_prefix": "model_blue_hex_portal_male",
        "female_model_prefix": "model_blue_hex_portal",
        "primary_color": "Solid Black Triblend",
        "male_model_config": {"option_group": "Men's 3", "option": "Right Front", "top": 200, "placements": ["front_large"]},
        "female_model_config": {"option_group": "Women's Lifestyle", "option": "Front", "top": 200, "placements": ["front_large"]},
        "flat_config": {"option_group": "Flat", "option": "Front", "placements": ["front_large"]}
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

def sync_garment_size_guides(garment_to_cat_id):
    """
    Fetches and caches Printful size tables and diagram images for all garments in the store.
    Guarantees size_guides.json and local measurement illustrations are always current.
    """
    guides = {}
    if os.path.exists(SIZE_GUIDES_FILE):
        try:
            with open(SIZE_GUIDES_FILE, "r") as f:
                guides = json.load(f)
        except Exception:
            guides = {}

    headers = {"Authorization": f"Bearer {PRINTFUL_API_KEY}"}
    updated = False

    def clean_html(html_str):
        if not html_str: return ''
        s = re.sub(r'\s+(style|id|dir)=\"[^\"]*\"', '', html_str)
        s = re.sub(r'</?span[^>]*>', '', s)
        s = re.sub(r'<h6>(.*?)</h6>', r'<div style=\"font-weight:700; color:#111827; margin-top:0.5rem; font-size:0.92rem;\">\1</div>', s)
        s = re.sub(r'<p>\s*&nbsp;\s*</p>', '', s)
        return re.sub(r'\s+', ' ', s).strip()

    for gname, cid in garment_to_cat_id.items():
        if gname in guides and guides[gname].get("inches"):
            continue
        try:
            print(f"Fetching size guide for {gname} (Catalog ID: {cid})...")
            r_in = requests.get(f"https://api.printful.com/products/{cid}/sizes", headers=headers, timeout=15).json().get("result", {})
            r_cm = requests.get(f"https://api.printful.com/products/{cid}/sizes?unit=cm", headers=headers, timeout=15).json().get("result", {})

            for unit_key, table_list in [("inches", r_in.get("size_tables", [])), ("cm", r_cm.get("size_tables", []))]:
                for tbl in table_list:
                    ttype = tbl.get("type")
                    remote_url = tbl.get("image_url")
                    if remote_url:
                        fname = f"cat_{cid}_{ttype}.png"
                        fpath = os.path.join(SIZE_GUIDES_IMG_DIR, fname)
                        rel_path = f"/assets/images/size_guides/{fname}"
                        if not os.path.exists(fpath):
                            try:
                                r_img = requests.get(remote_url, timeout=15)
                                if r_img.status_code == 200:
                                    with open(fpath, "wb") as img_f:
                                        img_f.write(r_img.content)
                            except Exception as e:
                                print(f"  Warning downloading size guide image: {e}")
                        tbl["local_image_url"] = rel_path
                    if "image_description" in tbl:
                        tbl["clean_description"] = clean_html(tbl["image_description"])
                    if "description" in tbl:
                        tbl["clean_notice"] = clean_html(tbl["description"])
                    for m in tbl.get("measurements", []):
                        lbl = m.get("type_label", "")
                        if "Dress" in gname and tbl.get("type") == "product_measure":
                            m["display_label"] = {"A": "A (Chest Width)", "B": "B (Waist Width)", "C": "C (Hip Width)", "D": "D (Length)"}.get(lbl, lbl)
                        elif "Swimsuit" in gname and tbl.get("type") == "product_measure":
                            m["display_label"] = {"A": "A (Chest Width)", "B": "B (Hip Width)", "C": "C (Length)"}.get(lbl, lbl)
                        else:
                            m["display_label"] = lbl

            guides[gname] = {
                "catalog_product_id": cid,
                "available_sizes": r_in.get("available_sizes", []),
                "inches": r_in.get("size_tables", []),
                "cm": r_cm.get("size_tables", [])
            }
            updated = True
        except Exception as e:
            print(f"  Warning syncing size guide for {gname}: {e}")

    if updated or not os.path.exists(SIZE_GUIDES_FILE):
        with open(SIZE_GUIDES_FILE, "w") as f:
            json.dump(guides, f, indent=2)
        print(f"Saved size guides to: {SIZE_GUIDES_FILE}")

def generate_printful_mockups(cat_prod_id, art_file, missing_for_task, cfg, target_prefix, is_model=True):
    """
    Calls Printful Mockup Generator API to create 2000px mockups.
    missing_for_task: dict of catalog_variant_id -> color_name
    cfg: dict with 'option_group', 'option', optional 'top', 'placements'
    target_prefix: prefix for filenames (e.g. model_prefix or prod_slug)
    Returns dict of color_name -> target_rel_path
    """
    if not missing_for_task or not cfg or not art_file or not art_file.get("preview_url"):
        return {}

    placements = cfg.get("placements")
    if not placements:
        if cat_prod_id in (162, 71):
            placements = ["front_large"]
        elif cat_prod_id == 365:
            placements = ["front"]
        elif cat_prod_id == 198:
            placements = ["default"]
        elif cat_prod_id == 272:
            placements = ["front", "back"]
        else:
            placements = ["front_large"]

    if cat_prod_id in (162, 365):
        area_w, area_h = 1800, 2400
    elif cat_prod_id == 198:
        area_w, area_h = 6975, 6000
    elif cat_prod_id == 272:
        area_w, area_h = 3750, 5250
    else:
        area_w, area_h = 2250, 2700

    w = area_w
    art_w = art_file.get("width") or 4000
    art_h = art_file.get("height") or 4000
    h = int(art_h * area_w / art_w)
    if h > area_h:
        h = area_h
        w = int(art_w * area_h / art_h)
    top = cfg.get("top", 0 if not is_model else 200)
    left = max(0, (area_w - w) // 2)

    files_payload = []
    for plc in placements:
        files_payload.append({
            "placement": plc,
            "image_url": art_file["preview_url"],
            "position": {
                "area_width": area_w,
                "area_height": area_h,
                "width": w,
                "height": h,
                "top": top,
                "left": left
            }
        })

    payload = {
        "variant_ids": list(missing_for_task.keys()),
        "format": "jpg",
        "width": 2000,
        "option_groups": [cfg["option_group"]],
        "options": [cfg["option"]],
        "files": files_payload
    }

    results = {}
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
                            target_filename = f"{target_prefix}_{c_slug}.jpg"
                            target_path = os.path.join(IMAGES_DIR, target_filename)
                            target_rel = f"/assets/images/products/{target_filename}"
                            img_content = requests.get(m["mockup_url"], timeout=20).content
                            save_clean_image(img_content, target_path)
                            results[c_name] = target_rel
                            kind_str = "model" if is_model else "flat"
                            print(f"    ✓ Saved 2000px {kind_str}: {c_name} -> {target_rel}")
                    break
                elif status == "failed":
                    print(f"    Warning: Mockup generation task failed for {target_prefix}: {poll_res}")
                    break
        else:
            print(f"    Warning: Failed to queue mockup task for {target_prefix}: {task_res}")
    except Exception as e:
        print(f"    Warning: Exception generating mockups for {target_prefix}: {e}")

    return results

def sync_model_mockups(pid, prod_slug, variants, color_groups, custom_meta, existing_prod_data=None, model_prefix_override=None, model_cfg_override=None, existing_key="model_image"):
    """
    Ensures high-resolution (2000px) colorway model mockups exist for each color of the product,
    saving them with clean white or lifestyle backgrounds (no black backgrounds).
    Guarantees that previously chosen mockups for the store are never replaced or overwritten.
    Returns (product_model_image_rel, dict_of_color_to_model_image_rel).
    """
    model_prefix = model_prefix_override or custom_meta.get("model_prefix", f"model_{prod_slug}")
    model_cfg = model_cfg_override or custom_meta.get("model_config")
    existing_prod_data = existing_prod_data or {}

    # Check if existing product already has a primary model image
    prev_primary_rel = existing_prod_data.get(existing_key)
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
        prev_color_model = existing_prod_data.get("colors", {}).get(color, {}).get(existing_key)
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
        art_file = next((f for f in v0.get("files", []) if f.get("type") in ("front_large", "default", "front") and f.get("preview_url")), None)
        if not art_file:
            art_file = next((f for f in v0.get("files", []) if f.get("preview_url")), None)

        if cat_prod_id and art_file and art_file.get("preview_url"):
            print(f"  Generating {len(missing_for_task)} missing 2000px model mockups for {model_prefix}...")
            new_models = generate_printful_mockups(cat_prod_id, art_file, missing_for_task, model_cfg, model_prefix, is_model=True)
            color_model_images.update(new_models)

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
    res = stripe.PaymentLink.list(limit=100, starting_after=starting_after, expand=["data.line_items"])
    for pl in res.data:
        meta = pl.metadata.to_dict() if hasattr(pl.metadata, "to_dict") else dict(pl.metadata or {})
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
garment_to_cat_id = {}

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
    cat_prod_id = first_var.get("product", {}).get("product_id")
    if garment_model and cat_prod_id:
        garment_to_cat_id[garment_model] = cat_prod_id

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

    # Determine unisex status
    is_unisex = custom_meta.get("is_unisex", True if ("Dress" not in garment_model and "Swimsuit" not in garment_model) else False)
    prod_entry["is_unisex"] = is_unisex

    # Sync male model mockups
    male_cfg = custom_meta.get("male_model_config")
    male_prefix = custom_meta.get("male_model_prefix", f"model_{prod_slug}_male")
    primary_male_rel, color_male_rels = None, {}
    if male_cfg or is_unisex:
        primary_male_rel, color_male_rels = sync_model_mockups(
            pid, prod_slug, variants, color_groups, custom_meta,
            existing_prod_data=existing_prod_data,
            model_prefix_override=male_prefix,
            model_cfg_override=male_cfg,
            existing_key="male_model_image"
        )
        if primary_male_rel:
            prod_entry["male_model_image"] = primary_male_rel

    # Sync female model mockups
    female_cfg = custom_meta.get("female_model_config")
    female_prefix = custom_meta.get("female_model_prefix", f"model_{prod_slug}_female")
    primary_female_rel, color_female_rels = None, {}
    if female_cfg or not is_unisex:
        primary_female_rel, color_female_rels = sync_model_mockups(
            pid, prod_slug, variants, color_groups, custom_meta,
            existing_prod_data=existing_prod_data,
            model_prefix_override=female_prefix,
            model_cfg_override=female_cfg,
            existing_key="female_model_image"
        )
        if primary_female_rel:
            prod_entry["female_model_image"] = primary_female_rel

    prod_entry["model_image"] = primary_male_rel or primary_female_rel

    # Check if flat_config is provided to generate clean flat mockups
    flat_cfg = custom_meta.get("flat_config")
    if flat_cfg:
        missing_flats = {}
        for color, var_list in color_groups.items():
            color_slug = slugify(color)
            local_img_path = os.path.join(IMAGES_DIR, f"{prod_slug}_{color_slug}.jpg")
            if not os.path.exists(local_img_path) or os.path.getsize(local_img_path) == 0:
                cat_vid = var_list[0].get("variant_id")
                if cat_vid:
                    missing_flats[cat_vid] = color
        if missing_flats:
            v0 = variants[0] if variants else {}
            cat_prod_id = v0.get("product", {}).get("product_id")
            art_file = next((f for f in v0.get("files", []) if f.get("type") in ("front_large", "default", "front") and f.get("preview_url")), None)
            if not art_file:
                art_file = next((f for f in v0.get("files", []) if f.get("preview_url")), None)
            if cat_prod_id and art_file:
                print(f"  Generating {len(missing_flats)} missing 2000px flat mockups for {prod_slug}...")
                generate_printful_mockups(cat_prod_id, art_file, missing_flats, flat_cfg, prod_slug, is_model=False)

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
        if primary_male_rel or color_male_rels:
            prod_entry["colors"][color]["male_model_image"] = color_male_rels.get(color, primary_male_rel)
        if primary_female_rel or color_female_rels:
            prod_entry["colors"][color]["female_model_image"] = color_female_rels.get(color, primary_female_rel)
        prod_entry["colors"][color]["model_image"] = (
            color_male_rels.get(color) or color_female_rels.get(color) or primary_male_rel or primary_female_rel
        )

        for v in var_list:
            sync_variant_id = str(v["id"])
            active_printful_variant_ids.add(sync_variant_id)
            size = v.get("size", "M")

            raw_price = v.get("retail_price", "26.87")
            # Use Printful retail price as-is without subtractions
            price_cents = int(Decimal(raw_price) * 100)
            amount_str = f"${(price_cents / 100):.2f}"
            currency = v.get("currency", "USD").lower()

            # Check if this variant already exists in Stripe
            existing_plink = existing_links_by_sync_id.get(sync_variant_id)
            existing_prod = existing_products_by_sync_id.get(sync_variant_id)

            # Check if the existing payment link matches the current price
            link_matches_price = False
            if existing_plink and existing_prod:
                pl_cents = None
                if hasattr(existing_plink, "line_items") and existing_plink.line_items and existing_plink.line_items.data:
                    pl_cents = existing_plink.line_items.data[0].price.unit_amount
                else:
                    pl_meta = existing_plink.metadata.to_dict() if hasattr(existing_plink.metadata, "to_dict") else dict(existing_plink.metadata or {})
                    if pl_meta.get("price_cents"):
                        pl_cents = int(pl_meta["price_cents"])

                if pl_cents and pl_cents == price_cents:
                    link_matches_price = True

            if existing_plink and existing_prod and link_matches_price:
                plink_url = existing_plink.url
                prod_id = existing_prod.id
                print(f"  [Cached] {color} - {size} ({amount_str}) -> {plink_url}")
            else:
                prod_id = existing_prod.id if existing_prod else None
                if not prod_id:
                    variant_title = f"{product_name} - {color} (Size {size})"
                    print(f"  [Creating Product] {variant_title} ({amount_str})...")

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
                    existing_products_by_sync_id[sync_variant_id] = stripe_prod

                # If existing link has outdated price, deactivate it
                if existing_plink and not link_matches_price:
                    try:
                        stripe.PaymentLink.modify(existing_plink.id, active=False)
                        print(f"  [Price Changed] Deactivated outdated payment link for {color} - {size}")
                    except Exception as e:
                        print(f"  [Warning] Could not deactivate old payment link: {e}")

                variant_title = f"{product_name} - {color} (Size {size})"
                print(f"  [Updating Price & Link] {variant_title} ({amount_str})...")

                # Create Price
                stripe_price = stripe.Price.create(
                    product=prod_id,
                    unit_amount=price_cents,
                    currency=currency,
                    nickname=f"{color} - Size {size}",
                    metadata={
                        "printful_sync_variant_id": sync_variant_id,
                        "color": color,
                        "size": size,
                        "price_cents": str(price_cents)
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
                        "size": size,
                        "price_cents": str(price_cents)
                    }
                )
                plink_url = plink.url
                existing_links_by_sync_id[sync_variant_id] = plink
                print(f"    ✓ New Link ({amount_str}): {plink_url}")

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

# Sync Printful garment size guides and measurement illustrations
if garment_to_cat_id:
    sync_garment_size_guides(garment_to_cat_id)

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