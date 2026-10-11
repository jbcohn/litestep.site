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
      <div class="merch-img-container" style="position: relative; display: flex; align-items: center; justify-content: center; height: 290px; background: #ffffff; cursor: pointer; overflow: hidden;" title="Click to zoom in on design">
        <img
          class="merch-shirt-img"
          src="{{ default_color.image | relative_url }}"
          alt="{{ prod.name }} - {{ default_color_name }}"
          style="max-width: 100%; max-height: 280px; object-fit: contain; display: block; transition: opacity 0.2s ease;"
        >
        <button
          type="button"
          class="merch-zoom-badge"
          aria-label="Zoom in on design"
          style="position: absolute; bottom: 10px; right: 10px; background: rgba(0, 0, 0, 0.65); color: #ffffff; border: none; border-radius: 20px; padding: 4px 10px; font-size: 0.75rem; font-weight: 600; display: flex; align-items: center; gap: 4px; backdrop-filter: blur(4px); cursor: pointer; pointer-events: auto; transition: background 0.15s ease;"
        >
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="display: block;">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            <line x1="11" y1="8" x2="11" y2="14"></line>
            <line x1="8" y1="11" x2="14" y2="11"></line>
          </svg>
          Zoom Design
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

<!-- Interactive Magnifier / Zoom Modal -->
<div id="merch-zoom-modal" style="display: none; position: fixed; inset: 0; z-index: 9999; background: rgba(0, 0, 0, 0.82); backdrop-filter: blur(6px); align-items: center; justify-content: center; padding: 1.5rem; box-sizing: border-box; opacity: 0; transition: opacity 0.2s ease;">
  <div style="position: relative; max-width: 900px; width: 100%; max-height: 90vh; background: #ffffff; border-radius: 8px; overflow: hidden; display: flex; flex-direction: column; box-shadow: 0 20px 40px rgba(0,0,0,0.5);">
    <!-- Modal Header -->
    <div style="display: flex; align-items: center; justify-content: space-between; padding: 0.85rem 1.25rem; border-bottom: 1px solid #e5e7eb; background: #fafafa;">
      <div>
        <h4 id="zoom-modal-title" style="margin: 0; font-size: 1.05rem; color: #111827; font-weight: 600;">Product Title</h4>
        <div id="zoom-modal-subtitle" style="font-size: 0.8rem; color: #6b7280; margin-top: 0.15rem;">Selected Color · Click or drag to inspect fabric & print details</div>
      </div>
      <button id="zoom-modal-close" type="button" aria-label="Close zoom modal" style="background: transparent; border: none; font-size: 1.75rem; line-height: 1; cursor: pointer; color: #4b5563; padding: 0.25rem 0.5rem; border-radius: 4px;">&times;</button>
    </div>

    <!-- Modal Image Area with Magnifier Pan -->
    <div id="zoom-image-viewport" style="position: relative; overflow: hidden; height: 60vh; min-height: 380px; max-height: 640px; display: flex; align-items: center; justify-content: center; background: #f3f4f6; cursor: crosshair;">
      <img
        id="zoom-modal-img"
        src=""
        alt="Magnified Design View"
        style="max-width: 95%; max-height: 95%; object-fit: contain; display: block; transform-origin: center center; transition: transform 0.1s ease-out; user-select: none;"
      >
      <!-- Mode Toggle pill in modal -->
      <div style="position: absolute; bottom: 12px; left: 50%; transform: translateX(-50%); background: rgba(17, 24, 39, 0.75); color: #fff; padding: 5px 14px; border-radius: 20px; font-size: 0.78rem; pointer-events: none; backdrop-filter: blur(4px);">
        Move cursor over image to magnify design details (2.5x)
      </div>
    </div>
  </div>
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
    modalSubtitle.textContent = `${color} · Pan cursor to inspect texture & graphic detail`;
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

  if (modalClose) {
    modalClose.addEventListener('click', closeZoomModal);
  }
  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeZoomModal();
    });
  }
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal && modal.style.display === 'flex') {
      closeZoomModal();
    }
  });

  // Pan / Magnify functionality inside modal viewport
  if (zoomViewport && modalImg) {
    zoomViewport.addEventListener('mousemove', (e) => {
      const rect = zoomViewport.getBoundingClientRect();
      const x = ((e.clientX - rect.left) / rect.width) * 100;
      const y = ((e.clientY - rect.top) / rect.height) * 100;
      modalImg.style.transformOrigin = `${x}% ${y}%`;
      modalImg.style.transform = 'scale(2.5)';
    });

    zoomViewport.addEventListener('mouseleave', () => {
      modalImg.style.transformOrigin = 'center center';
      modalImg.style.transform = 'scale(1)';
    });
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
        if (priceSpan) priceSpan.textContent = variantData.price;
      }
    }

    // Clicking image or zoom button opens the magnifier modal for currently selected color
    if (imgContainer) {
      imgContainer.addEventListener('click', () => {
        const currentColor = colorSelect.value;
        const colorInfo = prodData.colors[currentColor];
        const currentImgSrc = (colorInfo && colorInfo.image) ? (baseUrl + colorInfo.image) : (imgEl ? imgEl.src : '');
        openZoomModal(prodData.name, currentColor, currentImgSrc);
      });
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
