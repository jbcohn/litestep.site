---
layout: default
title: Home
---

<!-- FULL-BLEED HERO -->
<div class="site-hero" style="margin: -2.5rem -1.25rem 2.5rem; width: calc(100% + 2.5rem);">
  <div class="site-hero-bg" style="background-image: url('{{ "/assets/images/paragliding_sierra_granite.jpg" | relative_url }}');"></div>
  <div class="site-hero-overlay"></div>
  <div class="site-hero-content">
    <h1>Hey, I'm <span style="color: #f0921e; -webkit-text-fill-color: #f0921e;">Josh Cohn</span>.</h1>
    <p>Welcome to <strong>LiteStep</strong> — custom ultralight paragliding speed bars, open-source aviation tools, generative apparel, and engineering notes.</p>
  </div>
</div>

<!-- ================= SPOTLIGHT: LITESTEP SPEED BAR ================= -->
<div class="spotlight-card">
  <div class="spotlight-header">
    <span class="spotlight-tag">⭐ Featured Gear</span>
    <span style="font-size: 0.85rem; color: var(--text-muted); font-weight: 500;">Ultralight • Competition-Grade • Custom Made</span>
  </div>
  <div>
    <h2 class="spotlight-title">LiteStep Ultralight Speed Bar</h2>
    <p style="margin: 0.75rem 0 1.25rem 0; font-size: 1.05rem; color: var(--text-main);">
      Precision-engineered 3-step paragliding speed system designed for maximum stiffness, effortless engagement, and minimal weight. Built in Spain and distributed in the US from here.
    </p>
    <div class="button-group">
      <a href="{{ '/speedbar/' | relative_url }}" class="btn btn-primary">View Speed Bar Specs & Orders &rarr;</a>
      <a href="{{ '/speedbar/' | relative_url }}#rigging-specs" class="btn btn-secondary">Rigging & Setup Guide</a>
    </div>
  </div>
</div>

<hr>

<!-- ================= FEATURED PROJECTS ================= -->
<section style="margin: 3rem 0;">
  <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 1rem;">
    <h2>Featured Projects</h2>
    <a href="{{ '/projects/' | relative_url }}" style="font-size: 0.95rem; font-weight: 600;">View all projects &rarr;</a>
  </div>
  
  <div class="grid">
    <div class="card">
      <a href="https://jbcohn.github.io/pg-race-analyzer/" target="_blank" rel="noopener" style="text-decoration: none; color: inherit;">
        <img src="{{ '/assets/images/pg_race_analyzer.png' | relative_url }}" alt="PG Race Analyzer Interface" class="card-img">
        <div style="font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: var(--speedbar-accent); margin-bottom: 0.25rem;">Live Web App</div>
        <h3 class="card-title">Paragliding Race Analyzer</h3>
        <p class="card-desc">Interactive browser-based competition race analysis and GPS track visualization over 3D terrain.</p>
      </a>
      <div style="display: flex; gap: 0.5rem; margin-top: auto; padding-top: 0.75rem;">
        <a href="https://jbcohn.github.io/pg-race-analyzer/" target="_blank" rel="noopener" class="btn btn-primary" style="font-size: 0.8rem; padding: 0.35rem 0.65rem; flex: 1; text-align: center;">🚀 Launch App</a>
        <a href="{{ '/projects/' | relative_url }}#race-analyzer" class="btn btn-secondary" style="font-size: 0.8rem; padding: 0.35rem 0.65rem;">Details</a>
      </div>
    </div>

    <div class="card">
      <a href="https://jbcohn.github.io/Form-Constant-Visualizer/" target="_blank" rel="noopener" style="text-decoration: none; color: inherit;">
        <img src="{{ '/assets/images/form_constant.png' | relative_url }}" alt="Generative Geometry & Mandalas" class="card-img">
        <div style="font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: var(--speedbar-accent); margin-bottom: 0.25rem;">Live Web App</div>
        <h3 class="card-title">Form Constant Visualizer</h3>
        <p class="card-desc">Real-time procedural visualizer for Klüver form constants, fractal mandalas, and audio-reactive geometry.</p>
      </a>
      <div style="display: flex; gap: 0.5rem; margin-top: auto; padding-top: 0.75rem;">
        <a href="https://jbcohn.github.io/Form-Constant-Visualizer/" target="_blank" rel="noopener" class="btn btn-primary" style="font-size: 0.8rem; padding: 0.35rem 0.65rem; flex: 1; text-align: center;">🎨 Launch App</a>
        <a href="{{ '/projects/' | relative_url }}#form-constants" class="btn btn-secondary" style="font-size: 0.8rem; padding: 0.35rem 0.65rem;">Details</a>
      </div>
    </div>

    <div class="card">
      <a href="https://jbcohn.github.io/xc-simulator/" target="_blank" rel="noopener" style="text-decoration: none; color: inherit;">
        <img src="{{ '/assets/images/xc_simulator.png' | relative_url }}" alt="Paragliding XC Simulator Interface" class="card-img">
        <div style="font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: var(--speedbar-accent); margin-bottom: 0.25rem;">Live Web App</div>
        <h3 class="card-title">Paragliding XC Simulator</h3>
        <p class="card-desc">Interactive XC task planning, FAI triangle validation, and real-time XContest flight scoring over satellite maps.</p>
      </a>
      <div style="display: flex; gap: 0.5rem; margin-top: auto; padding-top: 0.75rem;">
        <a href="https://jbcohn.github.io/xc-simulator/" target="_blank" rel="noopener" class="btn btn-primary" style="font-size: 0.8rem; padding: 0.35rem 0.65rem; flex: 1; text-align: center;">🚀 Launch App</a>
        <a href="{{ '/projects/' | relative_url }}#xc-simulator" class="btn btn-secondary" style="font-size: 0.8rem; padding: 0.35rem 0.65rem;">Details</a>
      </div>
    </div>

    <div class="card">
      <a href="https://jbcohn.github.io/Ridgeline-3D-Explorer/" target="_blank" rel="noopener" style="text-decoration: none; color: inherit;">
        <img src="{{ '/assets/images/shasta_ridgeline.png' | relative_url }}" alt="Ridgeline 3D Explorer" class="card-img" style="object-fit: contain; background: #000;">
        <div style="font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: var(--speedbar-accent); margin-bottom: 0.25rem;">Live Web App</div>
        <h3 class="card-title">Ridgeline 3D Explorer</h3>
        <p class="card-desc">Interactive WebGL elevation explorer transforming USGS DEM rasters into customizable stacked contour ridgelines, topographic and finite element mesh 3d maps.</p>
      </a>
      <div style="display: flex; gap: 0.5rem; margin-top: auto; padding-top: 0.75rem;">
        <a href="https://jbcohn.github.io/Ridgeline-3D-Explorer/" target="_blank" rel="noopener" class="btn btn-primary" style="font-size: 0.8rem; padding: 0.35rem 0.65rem; flex: 1; text-align: center;">🏔️ Launch App</a>
        <a href="{{ '/projects/' | relative_url }}#ridgeline-explorer" class="btn btn-secondary" style="font-size: 0.8rem; padding: 0.35rem 0.65rem;">Details</a>
      </div>
    </div>
  </div>
</section>

<hr>

<!-- ================= MERCH & DESIGNS ================= -->
<section style="margin: 3rem 0;">
  <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 1rem;">
    <h2>Merch & Apparel</h2>
    <a href="{{ '/merch/' | relative_url }}" style="font-size: 0.95rem; font-weight: 600;">Explore Merch &rarr;</a>
  </div>
  <p style="color: var(--text-muted); margin-bottom: 1.5rem;">
    Original apparel and prints featuring California topographic ridgelines, peak contours (Mt. Shasta, Mt. Diablo, Mt. Tam), and mathematical form constant geometry.
  </p>
  
  <div class="grid">
    <a href="{{ '/merch/' | relative_url }}" class="card">
      <img src="{{ '/assets/images/bay_area_ridgeline.png' | relative_url }}" alt="Bay Area Ridgeline Shirt" class="card-img">
      <h3 class="card-title">Bay Area Topo Ridgelines</h3>
      <p class="card-desc">Stacked contour relief plotting capturing coastal ranges and bay elevation.</p>
    </a>

    <a href="{{ '/merch/' | relative_url }}" class="card">
      <img src="{{ '/assets/images/shasta_ridgeline.png' | relative_url }}" alt="Mt. Shasta Ridgeline" class="card-img">
      <h3 class="card-title">Mt. Shasta Elevation Relief</h3>
      <p class="card-desc">High-amplitude elevation contours of California's volcanic jewel.</p>
    </a>

    <a href="{{ '/merch/' | relative_url }}" class="card">
      <img src="{{ '/assets/images/stay_golden.png' | relative_url }}" alt="Stay Golden Design" class="card-img">
      <h3 class="card-title">Stay Golden Series</h3>
      <p class="card-desc">Iconic Bay Area inspired graphic apparel and custom prints.</p>
    </a>
  </div>
</section>

<hr>

<!-- ================= LATEST POSTS ================= -->
<section style="margin: 3rem 0;">
  <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 1rem;">
    <h2>Recent Writing & Logs</h2>
    <a href="{{ '/blog/' | relative_url }}" style="font-size: 0.95rem; font-weight: 600;">All posts &rarr;</a>
  </div>

  <ul class="post-list">
    {% for post in site.posts limit:3 %}
      <li class="post-item">
        <div class="post-item-date">{{ post.date | date: "%B %-d, %Y" }}</div>
        <h3 class="post-item-title">
          <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        </h3>
        <p class="post-item-excerpt">
          {% if post.description %}
            {{ post.description }}
          {% else %}
            {{ post.excerpt | strip_html | truncatewords: 30 }}
          {% endif %}
        </p>
      </li>
    {% else %}
      <li class="post-item">
        <p style="color: var(--text-muted);">New posts coming soon!</p>
      </li>
    {% endfor %}
  </ul>
</section>
