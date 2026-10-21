---
layout: page
title: "Merch & Apparel"
description: "Original apparel featuring digital elevation art, geometric fractals, and mathematical designs printed on Bella + Canvas tees."
permalink: /merch/
hero_image: /assets/images/paragliding_plains_cloudscape.jpg
---

<p style="font-size: 1.1rem; color: var(--text-muted); margin-bottom: 1.25rem;">
  Original apparel designs generated from geospatial elevation profiles, fractal mathematics, and algorithmic geometry. Printed on-demand on premium garments and shipped directly to your door.
</p>

<!-- Shipping & Multi-Item Cart Promo Banner -->
<div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 1rem; background: linear-gradient(135deg, #f8fafc 0%, #eff6ff 100%); border: 1px solid #bfdbfe; border-radius: 8px; padding: 0.85rem 1.25rem; margin-bottom: 2rem;">
  <div style="display: flex; align-items: center; gap: 0.65rem; font-size: 0.95rem; color: #1e3a8a;">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0;">
      <rect x="1" y="3" width="15" height="13"></rect>
      <polygon points="16 8 20 8 23 11 23 16 16 16 16 8"></polygon>
      <circle cx="5.5" cy="18.5" r="2.5"></circle>
      <circle cx="18.5" cy="18.5" r="2.5"></circle>
    </svg>
    <span><strong>Mix &amp; Match Any Designs:</strong> Standard US Shipping is $4.79 — or get <strong>FREE US Shipping</strong> when you order 2 or more items!</span>
  </div>
  <button
    type="button"
    id="merch-header-cart-btn"
    style="background: #111827; color: #ffffff; border: none; border-radius: 6px; padding: 0.5rem 1rem; font-size: 0.88rem; font-weight: 600; display: inline-flex; align-items: center; gap: 0.5rem; cursor: pointer; transition: opacity 0.15s ease;"
  >
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="9" cy="21" r="1"></circle>
      <circle cx="20" cy="21" r="1"></circle>
      <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>
    </svg>
    <span>Cart (<span class="merch-cart-count">0</span>)</span>
  </button>
</div>

<div class="grid merch-grid" style="grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.75rem;">

  {% for product_entry in site.data.merch_products %}
    {% assign prod_slug = product_entry[0] %}
    {% assign prod = product_entry[1] %}
    {% assign first_color_pair = prod.colors | first %}
    {% assign default_color_name = first_color_pair[0] %}
    {% assign default_color = first_color_pair[1] %}
    {% assign default_size_data = default_color.sizes['M'] %}
    {% assign default_size_name = 'M' %}
    {% unless default_size_data %}
      {% assign default_size_pair = default_color.sizes | first %}
      {% assign default_size_name = default_size_pair[0] %}
      {% assign default_size_data = default_size_pair[1] %}
    {% endunless %}

    {% assign initial_img = default_color.image %}
    {% if prod.model_image %}
      {% if default_color.model_image %}
        {% assign initial_img = default_color.model_image %}
      {% else %}
        {% assign initial_img = prod.model_image %}
      {% endif %}
    {% endif %}

    <div class="card merch-card" id="{{ prod_slug }}" data-slug="{{ prod_slug }}" style="padding: 0; overflow: hidden; display: flex; flex-direction: column; transition: box-shadow 0.25s ease, border-color 0.25s ease;">
      <div class="merch-img-container" style="position: relative; display: flex; align-items: center; justify-content: center; height: 320px; background: #ffffff; cursor: pointer; overflow: hidden;" title="Click to zoom in on design">
        <img
          class="merch-shirt-img"
          src="{{ initial_img | relative_url }}"
          alt="{{ prod.name }} - {% if prod.model_image %}Model View ({{ default_color_name }}){% else %}{{ default_color_name }}{% endif %}"
          style="max-width: 100%; max-height: 310px; object-fit: contain; display: block; transition: opacity 0.2s ease;"
        >

        {% if prod.model_image %}
          {% assign toggle_view_name = 'Shirt View' %}
          {% if prod.garment contains 'Dress' or prod.garment contains 'Swimsuit' %}
            {% assign toggle_view_name = 'Product View' %}
          {% endif %}
          <!-- View Toggle Button (Tee vs Model) -->
          <button
            type="button"
            class="merch-view-toggle"
            aria-label="Toggle between product and model view"
            style="position: absolute; top: 12px; right: 12px; background: rgba(255, 255, 255, 0.92); color: #111827; border: 1px solid rgba(0, 0, 0, 0.15); border-radius: 20px; padding: 4px 10px; font-size: 0.72rem; font-weight: 600; display: flex; align-items: center; gap: 4px; backdrop-filter: blur(4px); cursor: pointer; box-shadow: 0 2px 6px rgba(0,0,0,0.08); transition: all 0.15s ease;"
          >
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
              <circle cx="12" cy="7" r="4"></circle>
            </svg>
            <span class="toggle-label">{{ toggle_view_name }}</span>
          </button>
        {% endif %}

        <!-- Zoom Pill -->
        <button
          type="button"
          class="merch-zoom-badge"
          aria-label="Zoom in on design"
          style="position: absolute; bottom: 10px; right: 10px; background: rgba(0, 0, 0, 0.7); color: #ffffff; border: none; border-radius: 20px; padding: 4px 10px; font-size: 0.72rem; font-weight: 600; display: flex; align-items: center; gap: 4px; backdrop-filter: blur(4px); cursor: pointer; transition: background 0.15s ease;"
        >
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            <line x1="11" y1="8" x2="11" y2="14"></line>
            <line x1="8" y1="11" x2="14" y2="11"></line>
          </svg>
          Zoom 3x
        </button>
      </div>

      <div style="padding: 1.25rem; display: flex; flex-direction: column; flex-grow: 1;">
        <div style="font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: var(--text-muted); margin-bottom: 0.35rem;">
          {{ prod.tag }}
        </div>
        <h3 style="margin: 0 0 0.5rem 0; font-size: 1.15rem; line-height: 1.35;">
          {{ prod.name }}
        </h3>
        <p style="font-size: 0.85rem; font-weight: 500; color: var(--text-color, #333); margin-bottom: 0.5rem;">
          {{ prod.garment }}
        </p>
        <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1.25rem;">
          {{ prod.description }}
        </p>

        <div style="margin-top: auto;">
          <!-- Interactive Selectors -->
          <div style="display: flex; gap: 0.5rem; margin-bottom: 0.85rem;">
            <div style="flex: 1.2;">
              <label style="display: block; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; margin-bottom: 0.25rem; color: var(--text-muted);">Color</label>
              <select class="merch-color-select" style="width: 100%; padding: 0.45rem 0.5rem; border-radius: 4px; border: 1px solid var(--border); background: var(--bg-card, #fff); color: inherit; font-size: 0.88rem; cursor: pointer;">
                {% for color_entry in prod.colors %}
                  {% assign color_name = color_entry[0] %}
                  <option value="{{ color_name }}" {% if color_name == default_color_name %}selected{% endif %}>{{ color_name }}</option>
                {% endfor %}
              </select>
            </div>
            <div style="flex: 0.85;">
              <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.25rem;">
                <label style="font-size: 0.75rem; font-weight: 600; text-transform: uppercase; color: var(--text-muted); margin: 0;">Size</label>
                <button
                  type="button"
                  class="merch-size-guide-trigger"
                  data-garment="{{ prod.garment | escape }}"
                  title="View {{ prod.garment | escape }} size chart and measurements"
                  style="background: none; border: none; padding: 0; font-size: 0.72rem; color: #2563eb; font-weight: 600; text-decoration: underline; cursor: pointer; display: inline-flex; align-items: center; gap: 3px;"
                >
                  <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21.3 15.3l-6.6-6.6a2.4 2.4 0 0 0-3.4 0L2.7 17.3a2.4 2.4 0 0 0 0 3.4l.6.6a2.4 2.4 0 0 0 3.4 0l8.6-8.6"></path>
                    <line x1="8.5" y1="11.5" x2="10" y2="13"></line>
                    <line x1="12" y1="15" x2="13.5" y2="16.5"></line>
                    <line x1="5" y1="8" x2="6.5" y2="9.5"></line>
                  </svg>
                  Size Guide
                </button>
              </div>
              <select class="merch-size-select" style="width: 100%; padding: 0.45rem 0.5rem; border-radius: 4px; border: 1px solid var(--border); background: var(--bg-card, #fff); color: inherit; font-size: 0.88rem; cursor: pointer;">
                {% for size_entry in default_color.sizes %}
                  {% assign size_name = size_entry[0] %}
                  {% assign size_info = size_entry[1] %}
                  <option value="{{ size_name }}" {% if size_name == default_size_name %}selected{% endif %}>{{ size_name }} ({{ size_info.price }})</option>
                {% endfor %}
              </select>
            </div>
          </div>

          <div style="display: flex; gap: 0.5rem;">
            <button
              type="button"
              class="btn btn-primary merch-add-cart-btn"
              style="flex: 1.15; text-align: center; cursor: pointer; border: none; font-size: 0.9rem; padding: 0.65rem 0.75rem;"
            >
              Add to Cart — <span class="merch-btn-price">{{ default_size_data.price }}</span>
            </button>
            <button
              type="button"
              class="btn merch-buy-now-btn"
              style="flex: 0.85; text-align: center; cursor: pointer; background: transparent; border: 1px solid var(--border, #d1d5db); color: inherit; font-size: 0.88rem; font-weight: 600; padding: 0.65rem 0.6rem; border-radius: 6px;"
              title="Instant checkout via Stripe"
            >
              Buy Now →
            </button>
          </div>
        </div>
      </div>
    </div>
  {% endfor %}

</div>

<!-- Floating Shopping Cart Pill -->
<div>
  <button type="button" id="merch-floating-cart-btn" aria-label="Open shopping cart" style="display: none; position: fixed; bottom: 24px; right: 24px; z-index: 9990; background: #111827; color: #ffffff; border: 2px solid #ffffff; border-radius: 999px; padding: 0.75rem 1.25rem; font-size: 0.95rem; font-weight: 700; align-items: center; gap: 0.6rem; cursor: pointer; box-shadow: 0 10px 25px rgba(0, 0, 0, 0.35); transition: transform 0.15s ease;">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="9" cy="21" r="1"></circle>
      <circle cx="20" cy="21" r="1"></circle>
      <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>
    </svg>
    <span>Cart (<span class="merch-cart-count">0</span>)</span>
    <span id="merch-floating-cart-total" style="background: #2563eb; padding: 2px 8px; border-radius: 999px; font-size: 0.82rem;">$0.00</span>
  </button>
</div>

<!-- Slide-Out Shopping Cart Drawer -->
<div id="merch-cart-backdrop" style="display: none; position: fixed; inset: 0; z-index: 9995; background: rgba(0, 0, 0, 0.55); backdrop-filter: blur(3px); opacity: 0; transition: opacity 0.2s ease;"></div>
<aside id="merch-cart-drawer" aria-label="Shopping Cart" style="position: fixed; top: 0; right: 0; bottom: 0; width: 100%; max-width: 420px; z-index: 9996; background: #ffffff; color: #111827; box-shadow: -10px 0 30px rgba(0,0,0,0.25); transform: translateX(100%); transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1); display: flex; flex-direction: column;">
  <!-- Drawer Header -->
  <div style="display: flex; align-items: center; justify-content: space-between; padding: 1.15rem 1.25rem; border-bottom: 1px solid #e5e7eb;">
    <div style="display: flex; align-items: center; gap: 0.5rem;">
      <h3 style="margin: 0; font-size: 1.15rem; font-weight: 700; color: #111827;">Your Cart</h3>
      <span style="background: #f3f4f6; color: #374151; font-size: 0.8rem; font-weight: 600; padding: 2px 8px; border-radius: 999px;"><span class="merch-cart-count">0</span> items</span>
    </div>
    <button type="button" id="merch-cart-close" aria-label="Close cart" style="background: transparent; border: none; font-size: 1.65rem; line-height: 1; color: #6b7280; cursor: pointer; padding: 0.2rem 0.4rem;">&times;</button>
  </div>

  <!-- Free Shipping Progress Banner -->
  <div id="merch-cart-shipping-banner" style="background: #eff6ff; border-bottom: 1px solid #dbeafe; padding: 0.65rem 1.25rem; font-size: 0.85rem; color: #1e40af; text-align: center; font-weight: 500;">
    Add 2+ items for <strong>FREE US Shipping</strong>!
  </div>

  <!-- Cart Items List -->
  <div id="merch-cart-items" style="flex: 1; overflow-y: auto; padding: 1rem 1.25rem; display: flex; flex-direction: column; gap: 1rem;">
    <!-- Populated by JS -->
  </div>

  <!-- Drawer Footer -->
  <div id="merch-cart-footer" style="border-top: 1px solid #e5e7eb; padding: 1.15rem 1.25rem; background: #f9fafb;">
    <div style="display: flex; justify-content: space-between; font-size: 0.9rem; color: #4b5563; margin-bottom: 0.4rem;">
      <span>Subtotal</span>
      <span id="merch-cart-subtotal" style="font-weight: 600; color: #111827;">$0.00</span>
    </div>
    <div style="display: flex; justify-content: space-between; font-size: 0.9rem; color: #4b5563; margin-bottom: 0.85rem;">
      <span>US Shipping</span>
      <span id="merch-cart-shipping" style="font-weight: 600; color: #111827;">$4.79</span>
    </div>
    <div style="display: flex; justify-content: space-between; font-size: 1.05rem; font-weight: 700; color: #111827; padding-top: 0.65rem; border-top: 1px solid #e5e7eb; margin-bottom: 1rem;">
      <span>Estimated Total <span style="font-weight: 400; font-size: 0.78rem; color: #6b7280;">(before tax)</span></span>
      <span id="merch-cart-total">$0.00</span>
    </div>
    <div id="merch-cart-error" style="display: none; color: #dc2626; font-size: 0.82rem; margin-bottom: 0.65rem; text-align: center;"></div>
    <button
      type="button"
      id="merch-cart-checkout-btn"
      class="btn btn-primary"
      style="width: 100%; padding: 0.85rem 1rem; font-size: 1rem; font-weight: 700; border: none; border-radius: 6px; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 0.5rem;"
    >
      <span>Checkout via Stripe →</span>
    </button>
  </div>
</aside>

<!-- Interactive High-Res Magnifier / Zoom Modal -->
<div id="merch-zoom-modal" style="display: none; position: fixed; inset: 0; z-index: 9999; background: rgba(0, 0, 0, 0.85); backdrop-filter: blur(8px); align-items: center; justify-content: center; padding: 1.5rem; box-sizing: border-box; opacity: 0; transition: opacity 0.2s ease;">
  <div style="position: relative; max-width: 950px; width: 100%; max-height: 92vh; background: #ffffff; border-radius: 8px; overflow: hidden; display: flex; flex-direction: column; box-shadow: 0 25px 50px rgba(0,0,0,0.6);">
    <!-- Modal Header -->
    <div style="display: flex; align-items: center; justify-content: space-between; padding: 0.85rem 1.25rem; border-bottom: 1px solid #e5e7eb; background: #fafafa;">
      <div>
        <h4 id="zoom-modal-title" style="margin: 0; font-size: 1.05rem; color: #111827; font-weight: 600;">Product Title</h4>
        <div id="zoom-modal-subtitle" style="font-size: 0.8rem; color: #6b7280; margin-top: 0.15rem;">Selected Color · High-Resolution (2000px) Inspection</div>
      </div>
      <button id="zoom-modal-close" type="button" aria-label="Close zoom modal" style="background: transparent; border: none; font-size: 1.75rem; line-height: 1; cursor: pointer; color: #4b5563; padding: 0.25rem 0.5rem; border-radius: 4px;">&times;</button>
    </div>

    <!-- Modal Image Area with Smooth 3x Pan -->
    <div id="zoom-image-viewport" style="position: relative; overflow: hidden; height: 65vh; min-height: 420px; max-height: 700px; display: flex; align-items: center; justify-content: center; background: #f3f4f6; cursor: crosshair;">
      <img
        id="zoom-modal-img"
        src=""
        alt="Magnified Design View"
        style="max-width: 95%; max-height: 95%; object-fit: contain; display: block; transform-origin: center center; transition: transform 0.08s ease-out; user-select: none; image-rendering: auto;"
      >
      <!-- Mode Toggle pill in modal -->
      <div style="position: absolute; bottom: 12px; left: 50%; transform: translateX(-50%); background: rgba(17, 24, 39, 0.8); color: #fff; padding: 5px 16px; border-radius: 20px; font-size: 0.78rem; pointer-events: none; backdrop-filter: blur(4px); white-space: nowrap;">
        Pan cursor over image for 3.2x high-resolution detail inspection
      </div>
    </div>
  </div>
</div>

<!-- Interactive Size Guide Modal -->
<div id="merch-size-guide-modal" style="display: none; position: fixed; inset: 0; z-index: 9999; background: rgba(0, 0, 0, 0.75); backdrop-filter: blur(6px); align-items: center; justify-content: center; padding: 1.25rem; box-sizing: border-box; opacity: 0; transition: opacity 0.2s ease;">
  <div style="position: relative; max-width: 840px; width: 100%; max-height: 92vh; background: #ffffff; color: #111827; border-radius: 10px; overflow: hidden; display: flex; flex-direction: column; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.35);">
    
    <!-- Modal Header -->
    <div style="display: flex; align-items: center; justify-content: space-between; padding: 1rem 1.5rem; border-bottom: 1px solid #e5e7eb; background: #fafafa;">
      <div style="display: flex; align-items: center; gap: 0.65rem;">
        <div style="width: 32px; height: 32px; border-radius: 6px; background: #eff6ff; color: #2563eb; display: flex; align-items: center; justify-content: center;">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21.3 15.3l-6.6-6.6a2.4 2.4 0 0 0-3.4 0L2.7 17.3a2.4 2.4 0 0 0 0 3.4l.6.6a2.4 2.4 0 0 0 3.4 0l8.6-8.6"></path>
            <line x1="8.5" y1="11.5" x2="10" y2="13"></line>
            <line x1="12" y1="15" x2="13.5" y2="16.5"></line>
            <line x1="5" y1="8" x2="6.5" y2="9.5"></line>
          </svg>
        </div>
        <div>
          <h3 id="size-guide-modal-title" style="margin: 0; font-size: 1.15rem; font-weight: 700; color: #111827;">Size Guide</h3>
          <div id="size-guide-modal-subtitle" style="font-size: 0.82rem; color: #6b7280; margin-top: 0.1rem;">Garment Sizing &amp; Measurement Guide</div>
        </div>
      </div>
      <button id="size-guide-modal-close" type="button" aria-label="Close size guide" style="background: transparent; border: none; font-size: 1.75rem; line-height: 1; cursor: pointer; color: #4b5563; padding: 0.25rem 0.5rem; border-radius: 4px;">&times;</button>
    </div>

    <!-- Garment Selector & Unit Switcher Controls Bar -->
    <div style="padding: 0.85rem 1.5rem; background: #f3f4f6; border-bottom: 1px solid #e5e7eb; display: flex; flex-wrap: wrap; gap: 0.85rem; align-items: center; justify-content: space-between;">
      <!-- Garment Picker -->
      <div style="display: flex; align-items: center; gap: 0.5rem; flex: 1; min-width: 250px;">
        <label for="size-guide-garment-select" style="font-size: 0.8rem; font-weight: 700; color: #4b5563; text-transform: uppercase; letter-spacing: 0.03em;">Garment:</label>
        <select id="size-guide-garment-select" style="flex: 1; padding: 0.45rem 0.65rem; border-radius: 6px; border: 1px solid #d1d5db; font-size: 0.88rem; font-weight: 500; background: #ffffff; color: #111827; cursor: pointer;">
          <!-- Options populated from SIZE_GUIDES -->
        </select>
      </div>

      <!-- Unit Switcher (Inches / Centimeters) -->
      <div style="display: inline-flex; background: #e5e7eb; border-radius: 6px; padding: 2px;">
        <button type="button" id="size-unit-inches" class="size-unit-btn" style="border: none; border-radius: 4px; padding: 5px 14px; font-size: 0.82rem; font-weight: 600; cursor: pointer; background: #ffffff; color: #111827; box-shadow: 0 1px 3px rgba(0,0,0,0.1); transition: all 0.15s ease;">Inches</button>
        <button type="button" id="size-unit-cm" class="size-unit-btn" style="border: none; border-radius: 4px; padding: 5px 14px; font-size: 0.82rem; font-weight: 600; cursor: pointer; background: transparent; color: #4b5563; transition: all 0.15s ease;">Centimeters</button>
      </div>
    </div>

    <!-- Mode Tabs: Product Measurements vs Measure Yourself -->
    <div style="display: flex; border-bottom: 1px solid #e5e7eb; padding: 0 1.5rem; background: #ffffff;">
      <button type="button" id="size-mode-product" class="size-mode-tab" style="padding: 0.85rem 1.15rem; border: none; background: none; font-size: 0.92rem; font-weight: 700; color: #2563eb; border-bottom: 2px solid #2563eb; cursor: pointer; transition: color 0.15s ease;">
        Product measurements
      </button>
      <button type="button" id="size-mode-body" class="size-mode-tab" style="padding: 0.85rem 1.15rem; border: none; background: none; font-size: 0.92rem; font-weight: 500; color: #6b7280; border-bottom: 2px solid transparent; cursor: pointer; transition: color 0.15s ease;">
        Measure yourself
      </button>
    </div>

    <!-- Scrollable Content Area -->
    <div id="size-guide-content-area" style="overflow-y: auto; padding: 1.35rem 1.5rem; flex-grow: 1;">
      <!-- Populated dynamically via renderSizeGuide() -->
    </div>

    <!-- Modal Footer -->
    <div style="padding: 0.75rem 1.5rem; border-top: 1px solid #e5e7eb; background: #fafafa; display: flex; align-items: center; justify-content: space-between; font-size: 0.82rem; color: #6b7280;">
      <span>Measurements are provided by suppliers. May vary by up to 2″ (5 cm).</span>
      <button type="button" id="size-guide-done-btn" class="btn btn-primary" style="padding: 0.45rem 1.25rem; font-size: 0.85rem; cursor: pointer;">Done</button>
    </div>

  </div>
</div>

<hr style="margin: 3rem 0 2rem 0;">

<div class="spec-box" style="text-align: center; padding: 2.25rem 1.5rem; margin-top: 2rem;">
  <h2 style="border: none; margin-top: 0;">Direct Print-on-Demand Fulfillment</h2>
  <p style="max-width: 620px; margin: 0.5rem auto 0 auto; color: var(--text-muted);">
    All apparel orders are processed securely via Stripe Checkout and automatically fulfilled by Printful on premium Bella + Canvas combed ring-spun and tri-blend garments.
  </p>
</div>

<!-- Structured Data (JSON-LD) for Google Merchant Center & Rich Product Snippets -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {% for product_entry in site.data.merch_products %}
      {% assign p_slug = product_entry[0] %}
      {% assign p = product_entry[1] %}
      {% assign c_pair = p.colors | first %}
      {% assign c_name = c_pair[0] %}
      {% assign c_data = c_pair[1] %}
      {% assign s_data = c_data.sizes['M'] | default: c_data.sizes.first[1] %}
      {
        "@type": "Product",
        "@id": "https://litestep.us/merch/#{{ p_slug }}",
        "name": {{ p.name | jsonify }},
        "description": {{ p.description | jsonify }},
        "image": [
          "https://litestep.us{{ p.model_image | default: c_data.image }}",
          "https://litestep.us{{ c_data.image }}"
        ],
        "brand": {
          "@type": "Brand",
          "name": "Litestep"
        },
        "offers": {
          "@type": "Offer",
          "url": "https://litestep.us/merch/?product={{ p_slug }}",
          "priceCurrency": "USD",
          "price": "{{ s_data.price | remove: '$' }}",
          "availability": "https://schema.org/InStock",
          "itemCondition": "https://schema.org/NewCondition",
          "shippingDetails": {
            "@type": "OfferShippingDetails",
            "shippingRate": {
              "@type": "MonetaryAmount",
              "value": "4.79",
              "currency": "USD"
            },
            "shippingDestination": {
              "@type": "DefinedRegion",
              "addressCountry": "US"
            }
          }
        }
      }{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ]
}
</script>

<script>
(function() {
  const catalog = {{ site.data.merch_products | jsonify }};
  if (!catalog) return;

  const baseUrl = "{{ '' | relative_url }}";
  const CHECKOUT_WORKER_URL = "https://litestep-printful-webhook.jbcohn.workers.dev/create-checkout-session";
  const CART_STORAGE_KEY = "litestep_merch_cart_v1";

  // Parse URL parameters for Google Shopping deep-linking (?product=slug&color=...&size=...)
  const urlParams = new URLSearchParams(window.location.search);
  const pinnedProductSlug = urlParams.get('product') || (window.location.hash ? window.location.hash.replace('#', '') : null);
  const pinnedColorParam = urlParams.get('color');
  const pinnedSizeParam = urlParams.get('size');

  // --- Shopping Cart State Management ---
  let cart = [];
  try {
    const saved = localStorage.getItem(CART_STORAGE_KEY);
    if (saved) {
      const parsed = JSON.parse(saved);
      if (Array.isArray(parsed)) cart = parsed;
    }
  } catch (e) {}

  function saveCart() {
    try {
      localStorage.setItem(CART_STORAGE_KEY, JSON.stringify(cart));
    } catch (e) {}
    renderCart();
  }

  function addToCart(item) {
    const existing = cart.find(it => it.sync_variant_id === item.sync_variant_id);
    if (existing) {
      existing.quantity = Math.min(20, existing.quantity + (item.quantity || 1));
    } else {
      cart.push({
        sync_variant_id: String(item.sync_variant_id),
        product_id: item.product_id,
        slug: item.slug,
        name: item.name,
        color: item.color,
        size: item.size,
        price_cents: item.price_cents,
        image: item.image,
        quantity: item.quantity || 1
      });
    }
    saveCart();
    openCartDrawer();
    if (typeof window.gtag === 'function') {
      window.gtag('event', 'add_to_cart', {
        currency: 'USD',
        value: item.price_cents / 100,
        items: [{
          item_id: String(item.sync_variant_id),
          item_name: item.name,
          item_variant: `${item.color} / ${item.size}`,
          price: item.price_cents / 100,
          quantity: item.quantity || 1
        }]
      });
    }
  }

  function updateCartItemQty(syncVariantId, delta) {
    const idx = cart.findIndex(it => it.sync_variant_id === String(syncVariantId));
    if (idx === -1) return;
    cart[idx].quantity += delta;
    if (cart[idx].quantity <= 0) {
      cart.splice(idx, 1);
    } else if (cart[idx].quantity > 20) {
      cart[idx].quantity = 20;
    }
    saveCart();
  }

  // Cart UI Elements
  const cartBackdrop = document.getElementById('merch-cart-backdrop');
  const cartDrawer = document.getElementById('merch-cart-drawer');
  const cartCloseBtn = document.getElementById('merch-cart-close');
  const headerCartBtn = document.getElementById('merch-header-cart-btn');
  const floatingCartBtn = document.getElementById('merch-floating-cart-btn');
  const floatingCartTotal = document.getElementById('merch-floating-cart-total');
  const cartItemsContainer = document.getElementById('merch-cart-items');
  const cartShippingBanner = document.getElementById('merch-cart-shipping-banner');
  const cartSubtotalEl = document.getElementById('merch-cart-subtotal');
  const cartShippingEl = document.getElementById('merch-cart-shipping');
  const cartTotalEl = document.getElementById('merch-cart-total');
  const cartCheckoutBtn = document.getElementById('merch-cart-checkout-btn');
  const cartErrorEl = document.getElementById('merch-cart-error');

  function openCartDrawer() {
    if (!cartDrawer || !cartBackdrop) return;
    cartBackdrop.style.display = 'block';
    requestAnimationFrame(() => {
      cartBackdrop.style.opacity = '1';
      cartDrawer.style.transform = 'translateX(0)';
    });
  }

  function closeCartDrawer() {
    if (!cartDrawer || !cartBackdrop) return;
    cartBackdrop.style.opacity = '0';
    cartDrawer.style.transform = 'translateX(100%)';
    setTimeout(() => {
      cartBackdrop.style.display = 'none';
    }, 220);
  }

  if (headerCartBtn) headerCartBtn.addEventListener('click', openCartDrawer);
  if (floatingCartBtn) floatingCartBtn.addEventListener('click', openCartDrawer);
  if (cartCloseBtn) cartCloseBtn.addEventListener('click', closeCartDrawer);
  if (cartBackdrop) cartBackdrop.addEventListener('click', closeCartDrawer);

  function renderCart() {
    const totalQty = cart.reduce((sum, it) => sum + it.quantity, 0);
    const subtotalCents = cart.reduce((sum, it) => sum + it.price_cents * it.quantity, 0);
    const shippingCents = totalQty === 0 ? 0 : (totalQty >= 2 ? 0 : 479);
    const totalCents = subtotalCents + shippingCents;

    document.querySelectorAll('.merch-cart-count').forEach(el => {
      el.textContent = String(totalQty);
    });

    if (floatingCartBtn) {
      floatingCartBtn.style.display = totalQty > 0 ? 'inline-flex' : 'none';
    }
    if (floatingCartTotal) {
      floatingCartTotal.textContent = `$${(subtotalCents / 100).toFixed(2)}`;
    }

    if (cartShippingBanner) {
      if (totalQty === 0) {
        cartShippingBanner.style.background = '#eff6ff';
        cartShippingBanner.style.color = '#1e40af';
        cartShippingBanner.innerHTML = 'Order 2 or more items for <strong>FREE US Shipping</strong>!';
      } else if (totalQty === 1) {
        cartShippingBanner.style.background = '#fef3c7';
        cartShippingBanner.style.color = '#92400e';
        cartShippingBanner.innerHTML = 'Add <strong>1 more item</strong> to unlock <strong>FREE US Shipping</strong> (saves $4.79)!';
      } else {
        cartShippingBanner.style.background = '#dcfce7';
        cartShippingBanner.style.color = '#166534';
        cartShippingBanner.innerHTML = '✓ <strong>FREE US Shipping</strong> unlocked on your order!';
      }
    }

    if (cartSubtotalEl) cartSubtotalEl.textContent = `$${(subtotalCents / 100).toFixed(2)}`;
    if (cartShippingEl) {
      cartShippingEl.textContent = totalQty === 0 ? '$0.00' : (shippingCents === 0 ? 'FREE' : '$4.79');
      cartShippingEl.style.color = (totalQty >= 2) ? '#16a34a' : '#111827';
    }
    if (cartTotalEl) cartTotalEl.textContent = `$${(totalCents / 100).toFixed(2)}`;

    if (!cartItemsContainer) return;
    if (cart.length === 0) {
      cartItemsContainer.innerHTML = `
        <div style="text-align: center; padding: 3rem 1rem; color: #6b7280;">
          <p style="margin: 0 0 0.5rem 0; font-size: 1rem; font-weight: 600; color: #374151;">Your cart is empty</p>
          <p style="margin: 0; font-size: 0.88rem;">Choose any apparel design, color, and size to add it to your cart.</p>
        </div>
      `;
      if (cartCheckoutBtn) cartCheckoutBtn.disabled = true;
      return;
    }

    if (cartCheckoutBtn) cartCheckoutBtn.disabled = false;
    cartItemsContainer.innerHTML = '';

    cart.forEach(item => {
      const row = document.createElement('div');
      row.style.cssText = 'display: flex; gap: 0.85rem; align-items: center; padding-bottom: 0.85rem; border-bottom: 1px solid #f3f4f6;';
      row.innerHTML = `
        <img src="${baseUrl + item.image}" alt="${item.name}" style="width: 64px; height: 64px; object-fit: contain; background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 6px; flex-shrink: 0;">
        <div style="flex: 1; min-width: 0;">
          <div style="font-size: 0.9rem; font-weight: 600; color: #111827; line-height: 1.25; margin-bottom: 0.2rem; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${item.name}</div>
          <div style="font-size: 0.8rem; color: #6b7280; margin-bottom: 0.45rem;">${item.color} · Size ${item.size}</div>
          <div style="display: flex; align-items: center; justify-content: space-between;">
            <div style="display: inline-flex; align-items: center; border: 1px solid #d1d5db; border-radius: 4px; overflow: hidden;">
              <button type="button" class="cart-qty-minus" data-id="${item.sync_variant_id}" style="background: #f9fafb; border: none; padding: 2px 8px; cursor: pointer; font-weight: 700; color: #374151;">−</button>
              <span style="padding: 2px 10px; font-size: 0.82rem; font-weight: 600; color: #111827;">${item.quantity}</span>
              <button type="button" class="cart-qty-plus" data-id="${item.sync_variant_id}" style="background: #f9fafb; border: none; padding: 2px 8px; cursor: pointer; font-weight: 700; color: #374151;">+</button>
            </div>
            <div style="font-size: 0.9rem; font-weight: 700; color: #111827;">$${((item.price_cents * item.quantity) / 100).toFixed(2)}</div>
          </div>
        </div>
      `;
      cartItemsContainer.appendChild(row);
    });

    cartItemsContainer.querySelectorAll('.cart-qty-minus').forEach(btn => {
      btn.addEventListener('click', () => updateCartItemQty(btn.getAttribute('data-id'), -1));
    });
    cartItemsContainer.querySelectorAll('.cart-qty-plus').forEach(btn => {
      btn.addEventListener('click', () => updateCartItemQty(btn.getAttribute('data-id'), 1));
    });
  }

  async function startStripeCheckout(itemsToBuy, triggerBtn) {
    if (!itemsToBuy || itemsToBuy.length === 0) return;
    const originalText = triggerBtn ? triggerBtn.innerHTML : '';
    if (triggerBtn) {
      triggerBtn.disabled = true;
      triggerBtn.innerHTML = '<span>Redirecting to Stripe…</span>';
    }
    if (cartErrorEl) cartErrorEl.style.display = 'none';

    try {
      if (typeof window.gtag === 'function') {
        const valueDollars = itemsToBuy.reduce((acc, it) => acc + (it.price_cents || 2500) * it.quantity, 0) / 100;
        window.gtag('event', 'begin_checkout', {
          currency: 'USD',
          value: valueDollars
        });
      }

      const response = await fetch(CHECKOUT_WORKER_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          items: itemsToBuy.map(it => ({
            sync_variant_id: String(it.sync_variant_id),
            quantity: it.quantity
          }))
        })
      });

      const data = await response.json();
      if (!response.ok || !data.url) {
        throw new Error(data.error || 'Could not start Stripe Checkout.');
      }

      window.location.href = data.url;
    } catch (err) {
      if (cartErrorEl) {
        cartErrorEl.textContent = err.message;
        cartErrorEl.style.display = 'block';
      } else {
        alert(err.message);
      }
      if (triggerBtn) {
        triggerBtn.disabled = false;
        triggerBtn.innerHTML = originalText;
      }
    }
  }

  if (cartCheckoutBtn) {
    cartCheckoutBtn.addEventListener('click', () => startStripeCheckout(cart, cartCheckoutBtn));
  }

  // Modal elements
  const modal = document.getElementById('merch-zoom-modal');
  const modalImg = document.getElementById('zoom-modal-img');
  const modalTitle = document.getElementById('zoom-modal-title');
  const modalSubtitle = document.getElementById('zoom-modal-subtitle');
  const modalClose = document.getElementById('zoom-modal-close');
  const zoomViewport = document.getElementById('zoom-image-viewport');

  function openZoomModal(title, color, imgSrc) {
    if (!modal || !modalImg) return;
    modalTitle.textContent = title;
    modalSubtitle.textContent = `${color} · High-Resolution Detail (3.2x Pan Zoom)`;
    modalImg.src = imgSrc;
    modalImg.style.transform = 'scale(1)';
    modal.style.display = 'flex';
    requestAnimationFrame(() => {
      modal.style.opacity = '1';
    });
  }

  function closeZoomModal() {
    if (!modal) return;
    modal.style.opacity = '0';
    setTimeout(() => {
      modal.style.display = 'none';
      if (modalImg) modalImg.src = '';
    }, 200);
  }

  if (modalClose) modalClose.addEventListener('click', closeZoomModal);
  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeZoomModal();
    });
  }
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      if (modal && modal.style.display === 'flex') closeZoomModal();
      if (sizeGuideModal && sizeGuideModal.style.display === 'flex') closeSizeGuideModal();
      closeCartDrawer();
    }
  });

  // Size Guide Modal Logic
  const sizeGuides = {{ site.data.size_guides | jsonify }};
  const sizeGuideModal = document.getElementById('merch-size-guide-modal');
  const sizeGuideClose = document.getElementById('size-guide-modal-close');
  const sizeGuideDone = document.getElementById('size-guide-done-btn');
  const sizeGuideGarmentSelect = document.getElementById('size-guide-garment-select');
  const sizeGuideContent = document.getElementById('size-guide-content-area');
  const btnUnitInches = document.getElementById('size-unit-inches');
  const btnUnitCm = document.getElementById('size-unit-cm');
  const tabModeProduct = document.getElementById('size-mode-product');
  const tabModeBody = document.getElementById('size-mode-body');

  let currentGuideGarment = sizeGuides ? Object.keys(sizeGuides)[0] : '';
  let currentGuideUnit = 'inches'; // 'inches' | 'cm'
  let currentGuideMode = 'product_measure'; // 'product_measure' | 'measure_yourself'

  if (sizeGuideGarmentSelect && sizeGuides) {
    sizeGuideGarmentSelect.innerHTML = '';
    for (const gname of Object.keys(sizeGuides)) {
      const opt = document.createElement('option');
      opt.value = gname;
      opt.textContent = gname;
      sizeGuideGarmentSelect.appendChild(opt);
    }
    sizeGuideGarmentSelect.addEventListener('change', () => {
      currentGuideGarment = sizeGuideGarmentSelect.value;
      renderSizeGuideModal();
    });
  }

  function formatGuideNum(raw) {
    const num = parseFloat(raw);
    if (isNaN(num)) return raw;
    if (currentGuideUnit === 'cm') {
      return (Math.round(num * 10) / 10).toFixed(1);
    }
    // format fractions for inches
    const whole = Math.floor(num);
    const frac = Math.round((num - whole) * 1000) / 1000;
    if (Math.abs(frac - 0.5) < 0.01) return whole > 0 ? `${whole} ½` : '½';
    if (Math.abs(frac - 0.25) < 0.01) return whole > 0 ? `${whole} ¼` : '¼';
    if (Math.abs(frac - 0.75) < 0.01) return whole > 0 ? `${whole} ¾` : '¾';
    if (Math.abs(frac - 0.125) < 0.01) return whole > 0 ? `${whole} ⅛` : '⅛';
    if (Math.abs(frac - 0.375) < 0.01) return whole > 0 ? `${whole} ⅜` : '⅜';
    if (Math.abs(frac - 0.625) < 0.01) return whole > 0 ? `${whole} ⅝` : '⅝';
    if (Math.abs(frac - 0.875) < 0.01) return whole > 0 ? `${whole} ⅞` : '⅞';
    if (frac === 0) return `${whole}`;
    return num.toFixed(1);
  }

  function formatGuideValue(valObj) {
    if (!valObj) return '—';
    if (valObj.min_value && valObj.max_value) {
      return `${formatGuideNum(valObj.min_value)} - ${formatGuideNum(valObj.max_value)}`;
    }
    if (valObj.value !== undefined && valObj.value !== null) {
      return formatGuideNum(valObj.value);
    }
    return '—';
  }

  function renderSizeGuideModal() {
    if (!sizeGuideContent || !sizeGuides) return;
    const gData = sizeGuides[currentGuideGarment];
    if (!gData) {
      sizeGuideContent.innerHTML = '<p style="color: #6b7280; text-align: center; padding: 2rem;">Size guide not available for this item.</p>';
      return;
    }

    // Update tab styles
    if (tabModeProduct && tabModeBody) {
      if (currentGuideMode === 'product_measure') {
        tabModeProduct.style.color = '#2563eb';
        tabModeProduct.style.fontWeight = '700';
        tabModeProduct.style.borderBottom = '2px solid #2563eb';
        tabModeBody.style.color = '#6b7280';
        tabModeBody.style.fontWeight = '500';
        tabModeBody.style.borderBottom = '2px solid transparent';
      } else {
        tabModeBody.style.color = '#2563eb';
        tabModeBody.style.fontWeight = '700';
        tabModeBody.style.borderBottom = '2px solid #2563eb';
        tabModeProduct.style.color = '#6b7280';
        tabModeProduct.style.fontWeight = '500';
        tabModeProduct.style.borderBottom = '2px solid transparent';
      }
    }

    // Update unit button styles
    if (btnUnitInches && btnUnitCm) {
      if (currentGuideUnit === 'inches') {
        btnUnitInches.style.background = '#ffffff';
        btnUnitInches.style.color = '#111827';
        btnUnitInches.style.boxShadow = '0 1px 3px rgba(0,0,0,0.1)';
        btnUnitCm.style.background = 'transparent';
        btnUnitCm.style.color = '#4b5563';
        btnUnitCm.style.boxShadow = 'none';
      } else {
        btnUnitCm.style.background = '#ffffff';
        btnUnitCm.style.color = '#111827';
        btnUnitCm.style.boxShadow = '0 1px 3px rgba(0,0,0,0.1)';
        btnUnitInches.style.background = 'transparent';
        btnUnitInches.style.color = '#4b5563';
        btnUnitInches.style.boxShadow = 'none';
      }
    }

    const tables = gData[currentGuideUnit] || [];
    const activeTable = tables.find(t => t.type === currentGuideMode) || tables[0];
    if (!activeTable) {
      sizeGuideContent.innerHTML = '<p style="color: #6b7280; text-align: center; padding: 2rem;">Measurement table not available.</p>';
      return;
    }

    const imgUrl = activeTable.local_image_url || activeTable.image_url;
    const cleanDesc = activeTable.clean_description || '';
    const measurements = activeTable.measurements || [];
    const sizes = gData.available_sizes || [];

    let tableHtml = `
      <div style="overflow-x: auto; margin-top: 1rem; border: 1px solid #e5e7eb; border-radius: 8px;">
        <table style="width: 100%; border-collapse: collapse; font-size: 0.88rem; text-align: left;">
          <thead>
            <tr style="background: #f9fafb; border-bottom: 1px solid #e5e7eb;">
              <th style="padding: 0.65rem 1rem; font-weight: 700; color: #374151; white-space: nowrap;">Size Label</th>
    `;

    measurements.forEach(m => {
      const colLabel = m.display_label || m.type_label;
      tableHtml += `<th style="padding: 0.65rem 1rem; font-weight: 700; color: #374151; white-space: nowrap;">${colLabel}</th>`;
    });

    tableHtml += `
            </tr>
          </thead>
          <tbody>
    `;

    sizes.forEach((sz, idx) => {
      const bg = idx % 2 === 0 ? '#ffffff' : '#f9fafb';
      tableHtml += `<tr style="background: ${bg}; border-bottom: 1px solid #f3f4f6;">
        <td style="padding: 0.65rem 1rem; font-weight: 700; color: #111827;">${sz}</td>`;

      measurements.forEach(m => {
        const valObj = (m.values || []).find(v => v.size === sz);
        const displayVal = formatGuideValue(valObj);
        tableHtml += `<td style="padding: 0.65rem 1rem; color: #4b5563; font-variant-numeric: tabular-nums;">${displayVal}</td>`;
      });

      tableHtml += `</tr>`;
    });

    tableHtml += `
          </tbody>
        </table>
      </div>
    `;

    let html = '';

    if (currentGuideMode === 'product_measure') {
      html += `
        <div style="background: #eff6ff; border-left: 4px solid #2563eb; padding: 0.7rem 0.95rem; border-radius: 4px; margin-bottom: 1.15rem; font-size: 0.86rem; color: #1e40af;">
          <strong>Pro tip!</strong> Measure one of your favorite products at home and compare with the measurements you see in this guide.
        </div>
      `;
    }

    html += `
      <div style="display: flex; flex-wrap: wrap; gap: 1.25rem; align-items: center; margin-bottom: 1.25rem; background: #fafafa; border: 1px solid #e5e7eb; border-radius: 8px; padding: 1rem 1.25rem;">
        ${imgUrl ? `
          <div style="flex: 0 0 150px; max-width: 170px; background: #ffffff; border: 1px solid #e5e7eb; border-radius: 6px; padding: 0.4rem; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
            <img src="${baseUrl + imgUrl}" alt="Measurement diagram" style="max-width: 100%; height: auto; display: block; object-fit: contain;">
          </div>
        ` : ''}
        <div style="flex: 1; min-width: 240px; font-size: 0.86rem; line-height: 1.5; color: #374151;">
          ${cleanDesc}
        </div>
      </div>
    `;

    html += `
      <div>
        <div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.4rem;">
          <h4 style="margin: 0; font-size: 0.98rem; font-weight: 700; color: #111827;">Size chart</h4>
          <span style="font-size: 0.8rem; color: #6b7280; font-weight: 500;">Unit: ${currentGuideUnit === 'inches' ? 'Inches' : 'Centimeters'}</span>
        </div>
        ${tableHtml}
      </div>
    `;

    sizeGuideContent.innerHTML = html;
  }

  function openSizeGuideModal(garmentName) {
    if (!sizeGuideModal) return;
    if (garmentName && sizeGuides && sizeGuides[garmentName]) {
      currentGuideGarment = garmentName;
      if (sizeGuideGarmentSelect) sizeGuideGarmentSelect.value = garmentName;
    }
    renderSizeGuideModal();
    sizeGuideModal.style.display = 'flex';
    requestAnimationFrame(() => {
      sizeGuideModal.style.opacity = '1';
    });
    document.body.style.overflow = 'hidden';
  }

  function closeSizeGuideModal() {
    if (!sizeGuideModal) return;
    sizeGuideModal.style.opacity = '0';
    setTimeout(() => {
      sizeGuideModal.style.display = 'none';
      document.body.style.overflow = '';
    }, 200);
  }

  if (sizeGuideClose) sizeGuideClose.addEventListener('click', closeSizeGuideModal);
  if (sizeGuideDone) sizeGuideDone.addEventListener('click', closeSizeGuideModal);
  if (sizeGuideModal) {
    sizeGuideModal.addEventListener('click', (e) => {
      if (e.target === sizeGuideModal) closeSizeGuideModal();
    });
  }

  if (btnUnitInches) {
    btnUnitInches.addEventListener('click', () => {
      currentGuideUnit = 'inches';
      renderSizeGuideModal();
    });
  }
  if (btnUnitCm) {
    btnUnitCm.addEventListener('click', () => {
      currentGuideUnit = 'cm';
      renderSizeGuideModal();
    });
  }

  if (tabModeProduct) {
    tabModeProduct.addEventListener('click', () => {
      currentGuideMode = 'product_measure';
      renderSizeGuideModal();
    });
  }
  if (tabModeBody) {
    tabModeBody.addEventListener('click', () => {
      currentGuideMode = 'measure_yourself';
      renderSizeGuideModal();
    });
  }

  // Pan / Magnify functionality inside modal viewport at 3.2x zoom
  if (zoomViewport && modalImg) {
    zoomViewport.addEventListener('mousemove', (e) => {
      const rect = zoomViewport.getBoundingClientRect();
      const x = ((e.clientX - rect.left) / rect.width) * 100;
      const y = ((e.clientY - rect.top) / rect.height) * 100;
      modalImg.style.transformOrigin = `${x}% ${y}%`;
      modalImg.style.transform = 'scale(3.2)';
    });

    zoomViewport.addEventListener('mouseleave', () => {
      modalImg.style.transformOrigin = 'center center';
      modalImg.style.transform = 'scale(1)';
    });
  }

  // Show product cards in random order on page load, pinning ?product=slug first if deep-linked from Google Shopping
  const gridEl = document.querySelector('.merch-grid');
  if (gridEl) {
    const cards = Array.from(gridEl.querySelectorAll('.merch-card'));
    for (let i = cards.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [cards[i], cards[j]] = [cards[j], cards[i]];
    }
    if (pinnedProductSlug) {
      const pinnedIdx = cards.findIndex(c => c.getAttribute('data-slug') === pinnedProductSlug);
      if (pinnedIdx > 0) {
        const [pinnedCard] = cards.splice(pinnedIdx, 1);
        cards.unshift(pinnedCard);
      }
    }
    cards.forEach(card => gridEl.appendChild(card));
  }

  // Iterate over product cards
  document.querySelectorAll('.merch-card').forEach(card => {
    const slug = card.getAttribute('data-slug');
    const prodData = catalog[slug];
    if (!prodData) return;

    const colorSelect = card.querySelector('.merch-color-select');
    const sizeSelect = card.querySelector('.merch-size-select');
    const imgEl = card.querySelector('.merch-shirt-img');
    const imgContainer = card.querySelector('.merch-img-container');
    const viewToggleBtn = card.querySelector('.merch-view-toggle');
    const addCartBtn = card.querySelector('.merch-add-cart-btn');
    const buyNowBtn = card.querySelector('.merch-buy-now-btn');
    const priceSpan = card.querySelector('.merch-btn-price');

    if (!colorSelect || !sizeSelect) return;

    // View state: 'model' (default if model photo available) or 'color' (flat shirt)
    let currentView = prodData.model_image ? 'model' : 'color';

    // If deep-linked via ?product=slug, highlight and pre-select color/size if provided
    const isPinned = (slug === pinnedProductSlug);
    if (isPinned) {
      card.style.borderColor = '#2563eb';
      card.style.boxShadow = '0 0 0 2px rgba(37, 99, 235, 0.25)';
      if (pinnedColorParam && prodData.colors[pinnedColorParam]) {
        colorSelect.value = pinnedColorParam;
      }
    }

    function updateCardImage() {
      if (!imgEl) return;
      imgEl.style.opacity = '0.3';
      const currentColor = colorSelect.value;
      const colorInfo = prodData.colors[currentColor];
      if (currentView === 'model' && prodData.model_image) {
        const modelSrc = (colorInfo && colorInfo.model_image) ? colorInfo.model_image : prodData.model_image;
        imgEl.src = baseUrl + modelSrc;
        imgEl.alt = prodData.name + ' - Model View (' + currentColor + ')';
      } else {
        if (colorInfo && colorInfo.image) {
          imgEl.src = baseUrl + colorInfo.image;
          imgEl.alt = prodData.name + ' - ' + currentColor;
        }
      }
      setTimeout(() => { imgEl.style.opacity = '1'; }, 70);
    }

    if (viewToggleBtn && prodData.model_image) {
      const flatLabel = (prodData.garment && (prodData.garment.includes('Dress') || prodData.garment.includes('Swimsuit'))) ? 'Product View' : 'Shirt View';
      viewToggleBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        const label = viewToggleBtn.querySelector('.toggle-label');
        if (currentView === 'model') {
          currentView = 'color';
          if (label) label.textContent = 'Model View';
        } else {
          currentView = 'model';
          if (label) label.textContent = flatLabel;
        }
        updateCardImage();
      });
    }

    function updateSizes(selectedColor, preserveSize) {
      const colorInfo = prodData.colors[selectedColor];
      if (!colorInfo) return;

      updateCardImage();

      const sizes = colorInfo.sizes || {};
      const availableSizes = Object.keys(sizes);
      let targetSize = preserveSize && sizes[preserveSize] ? preserveSize : (sizes['M'] ? 'M' : availableSizes[0]);

      sizeSelect.innerHTML = '';
      for (const [sz, data] of Object.entries(sizes)) {
        const opt = document.createElement('option');
        opt.value = sz;
        opt.textContent = `${sz} (${data.price})`;
        if (sz === targetSize) opt.selected = true;
        sizeSelect.appendChild(opt);
      }

      updateButton();
    }

    function updateButton() {
      const currentColor = colorSelect.value;
      const currentSize = sizeSelect.value;
      const variantData = prodData.colors[currentColor]?.sizes?.[currentSize];

      if (variantData && priceSpan) {
        priceSpan.textContent = variantData.price;
      }
    }

    function getCurrentSelection() {
      const currentColor = colorSelect.value;
      const currentSize = sizeSelect.value;
      const colorInfo = prodData.colors[currentColor];
      const variantData = colorInfo?.sizes?.[currentSize];
      if (!variantData) return null;
      return {
        sync_variant_id: variantData.sync_variant_id,
        product_id: variantData.product_id,
        slug: slug,
        name: prodData.name,
        color: currentColor,
        size: currentSize,
        price_cents: variantData.price_cents,
        image: colorInfo.model_image || prodData.model_image || colorInfo.image,
        quantity: 1
      };
    }

    if (addCartBtn) {
      addCartBtn.addEventListener('click', () => {
        const item = getCurrentSelection();
        if (item) addToCart(item);
      });
    }

    if (buyNowBtn) {
      buyNowBtn.addEventListener('click', () => {
        const item = getCurrentSelection();
        if (item) startStripeCheckout([item], buyNowBtn);
      });
    }

    const sizeGuideBtn = card.querySelector('.merch-size-guide-trigger');
    if (sizeGuideBtn) {
      sizeGuideBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        openSizeGuideModal(prodData.garment);
      });
    }

    if (imgContainer) {
      imgContainer.addEventListener('click', () => {
        const currentColor = colorSelect.value;
        const colorInfo = prodData.colors[currentColor];
        if (currentView === 'model' && prodData.model_image) {
          const modelSrc = (colorInfo && colorInfo.model_image) ? colorInfo.model_image : prodData.model_image;
          openZoomModal(prodData.name, 'Model Photo (' + currentColor + ')', baseUrl + modelSrc);
        } else {
          const currentImgSrc = (colorInfo && colorInfo.image) ? (baseUrl + colorInfo.image) : (imgEl ? imgEl.src : '');
          openZoomModal(prodData.name, currentColor, currentImgSrc);
        }
      });
    }

    colorSelect.addEventListener('change', () => {
      updateSizes(colorSelect.value, sizeSelect.value);
    });

    sizeSelect.addEventListener('change', updateButton);

    const initialTargetSize = (isPinned && pinnedSizeParam) ? pinnedSizeParam : (sizeSelect.value || 'M');
    updateSizes(colorSelect.value, initialTargetSize);
  });

  renderCart();
})();
</script>
