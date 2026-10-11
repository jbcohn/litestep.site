---
layout: page
title: "Merch & Apparel"
description: "Original apparel featuring digital elevation art, geometric fractals, and mathematical designs printed on premium Bella + Canvas tees."
permalink: /merch/
hero_image: /assets/images/paragliding_plains_cloudscape.jpg
---

<p style="font-size: 1.1rem; color: var(--text-muted); margin-bottom: 2rem;">
  Original apparel designs generated from geospatial elevation profiles, fractal mathematics, and algorithmic geometry. Printed on-demand on premium Bella + Canvas tees and shipped directly to your door with automatic sales tax calculation.
</p>

<div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.75rem;">

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

    <div class="card merch-card" data-slug="{{ prod_slug }}" style="padding: 0; overflow: hidden; display: flex; flex-direction: column;">
      <a class="merch-img-link" href="{{ default_size_data.url }}" target="_blank" rel="noopener" style="display: block; text-decoration: none !important;">
        <div style="display: flex; align-items: center; justify-content: center; height: 280px; background: #ffffff;">
          <img
            class="merch-shirt-img"
            src="{{ default_color.image | relative_url }}"
            alt="{{ prod.name }} - {{ default_color_name }}"
            style="max-width: 100%; max-height: 270px; object-fit: contain; display: block; transition: opacity 0.2s ease;"
          >
        </div>
      </a>
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
            <div style="flex: 0.8;">
              <label style="display: block; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; margin-bottom: 0.25rem; color: var(--text-muted);">Size</label>
              <select class="merch-size-select" style="width: 100%; padding: 0.45rem 0.5rem; border-radius: 4px; border: 1px solid var(--border); background: var(--bg-card, #fff); color: inherit; font-size: 0.88rem; cursor: pointer;">
                {% for size_entry in default_color.sizes %}
                  {% assign size_name = size_entry[0] %}
                  {% assign size_info = size_entry[1] %}
                  <option value="{{ size_name }}" {% if size_name == default_size_name %}selected{% endif %}>{{ size_name }} ({{ size_info.price }})</option>
                {% endfor %}
              </select>
            </div>
          </div>

          <a
            class="btn btn-primary merch-buy-btn"
            href="{{ default_size_data.url }}"
            target="_blank"
            rel="noopener"
            style="width: 100%; text-align: center; display: block; box-sizing: border-box;"
          >
            Buy Direct — <span class="merch-btn-price">{{ default_size_data.price }}</span> →
          </a>
        </div>
      </div>
    </div>
  {% endfor %}

</div>

<hr style="margin: 3rem 0 2rem 0;">

<div class="spec-box" style="text-align: center; padding: 2.25rem 1.5rem; margin-top: 2rem;">
  <h2 style="border: none; margin-top: 0;">Direct Print-on-Demand Fulfillment</h2>
  <p style="max-width: 620px; margin: 0.5rem auto 1.5rem auto; color: var(--text-muted);">
    All apparel orders are processed securely via Stripe Checkout and automatically fulfilled by Printful on premium Bella + Canvas combed ring-spun and tri-blend garments.
  </p>
  <a href="https://www.amazon.com/s?k=litestep" target="_blank" rel="noopener" class="btn" style="font-size: 0.95rem; padding: 0.65rem 1.5rem; border: 1px solid var(--border);">
    View Legacy Merch on Amazon &rarr;
  </a>
</div>

<script>
(function() {
  const catalog = {{ site.data.merch_products | jsonify }};
  if (!catalog) return;

  const baseUrl = "{{ '' | relative_url }}";

  document.querySelectorAll('.merch-card').forEach(card => {
    const slug = card.getAttribute('data-slug');
    const prodData = catalog[slug];
    if (!prodData) return;

    const colorSelect = card.querySelector('.merch-color-select');
    const sizeSelect = card.querySelector('.merch-size-select');
    const imgEl = card.querySelector('.merch-shirt-img');
    const imgLink = card.querySelector('.merch-img-link');
    const buyBtn = card.querySelector('.merch-buy-btn');
    const priceSpan = card.querySelector('.merch-btn-price');

    if (!colorSelect || !sizeSelect) return;

    function updateSizes(selectedColor, preserveSize) {
      const colorInfo = prodData.colors[selectedColor];
      if (!colorInfo) return;

      // Swap preview image
      if (colorInfo.image && imgEl) {
        imgEl.style.opacity = '0.3';
        imgEl.src = baseUrl + colorInfo.image;
        imgEl.alt = prodData.name + ' - ' + selectedColor;
        setTimeout(() => { imgEl.style.opacity = '1'; }, 80);
      }

      // Populate size dropdown
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

      if (variantData) {
        if (buyBtn) buyBtn.href = variantData.url;
        if (imgLink) imgLink.href = variantData.url;
        if (priceSpan) priceSpan.textContent = variantData.price;
      }
    }

    colorSelect.addEventListener('change', () => {
      updateSizes(colorSelect.value, sizeSelect.value);
    });

    sizeSelect.addEventListener('change', updateButton);

    // Initial setup with preserved default size
    updateSizes(colorSelect.value, sizeSelect.value || 'M');
  });
})();
</script>
