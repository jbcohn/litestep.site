---
layout: page
title: "Projects & Engineering"
description: "A showcase of open-source aviation software, GIS & elevation modeling, generative geometry, and data workflows."
permalink: /projects/
hero_image: /assets/images/paragliding_dolomites_gaggle.jpg
---

<div class="projects-list">

  <!-- ================= PG RACE ANALYZER & XC SIMULATOR ================= -->
  <section id="race-analyzer" style="margin-bottom: 3.5rem;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.5rem;">
      <h2 style="margin-top: 0; border: none; padding: 0;">Paragliding Race Analyzer & XC Simulator</h2>
      <div class="button-group">
        <a href="https://github.com/jbcohn/pg-race-analyzer" target="_blank" rel="noopener" class="btn btn-secondary" style="font-size: 0.85rem; padding: 0.35rem 0.75rem;">
          <span style="font-weight: 700;">GitHub:</span> pg-race-analyzer &rarr;
        </a>
        <a href="https://github.com/jbcohn/xc-simulator" target="_blank" rel="noopener" class="btn btn-secondary" style="font-size: 0.85rem; padding: 0.35rem 0.75rem;">
          <span style="font-weight: 700;">GitHub:</span> xc-simulator &rarr;
        </a>
      </div>
    </div>

    <p style="margin-top: 0.75rem;">
      High-resolution geospatial tools and flight race analyzers built in Python. Merges 3D Digital Elevation Models (DEMs), GPS tracklogs (.IGC), turnpoint cylinder triggers, and speed-to-fly optimization models.
    </p>

    <img src="{{ '/assets/images/bay_area_flights.png' | relative_url }}" alt="IGC Flight Plotting" style="width: 100%; border-radius: var(--radius-md); margin: 1rem 0; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">

    <ul>
      <li><strong>Terrain & DEM Rendering</strong>: Merges 30m / 10m USGS DEMs and GeoTIFF matrices with glide ratio and barometric altimetry.</li>
      <li><strong>Thermal & XC Efficiency</strong>: Computes thermalling efficiency, climb rates, and glide transitions across complex mountain topography.</li>
      <li><strong>Race Task Analysis</strong>: Automated task turnpoint cylinder detection, start gate timing, and speed section breakdowns.</li>
    </ul>
  </section>

  <hr>

  <!-- ================= GENERATIVE GEOMETRY & FORM CONSTANTS ================= -->
  <section id="generative-art" style="margin-bottom: 3.5rem;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.5rem;">
      <h2 style="margin-top: 0; border: none; padding: 0;">Form Constant Visualizer & Ridgeline 3D Explorer</h2>
      <div class="button-group">
        <a href="https://github.com/jbcohn/Form-Constant-Visualizer" target="_blank" rel="noopener" class="btn btn-secondary" style="font-size: 0.85rem; padding: 0.35rem 0.75rem;">
          <span style="font-weight: 700;">GitHub:</span> Form-Constant-Visualizer &rarr;
        </a>
        <a href="https://github.com/jbcohn/Ridgeline-3D-Explorer" target="_blank" rel="noopener" class="btn btn-secondary" style="font-size: 0.85rem; padding: 0.35rem 0.75rem;">
          <span style="font-weight: 700;">GitHub:</span> Ridgeline-3D-Explorer &rarr;
        </a>
      </div>
    </div>

    <p style="margin-top: 0.75rem;">
      Interactive canvas web applications and algorithmic generators exploring mathematical symmetry, visual perception theories (Klüver form constants), and 3D terrain wireframes.
    </p>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; margin: 1.5rem 0;">
      <img src="{{ '/assets/images/form_constant.png' | relative_url }}" alt="Form Constant Geometry" style="width: 100%; border-radius: var(--radius-md); border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">
      <img src="{{ '/assets/images/shasta_ridgeline.png' | relative_url }}" alt="Topographic Contour Art" style="width: 100%; border-radius: var(--radius-md); border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">
    </div>

    <ul>
      <li><strong>Mandala & Symmetry Engines</strong>: Real-time procedural rendering of harmonic circular symmetries, honeycomb tessellations, and spiral geometries.</li>
      <li><strong>3D Topographic Ridgelines</strong>: Translating raw elevation rasters into stacked vector ridgelines for web interaction and apparel print production.</li>
    </ul>
  </section>

  <hr>

  <!-- ================= DATA WORKFLOWS & AUTOMATION ================= -->
  <section id="workflows" style="margin-bottom: 3.5rem;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.5rem;">
      <h2 style="margin-top: 0; border: none; padding: 0;">Data Workflows & Automation</h2>
      <a href="https://github.com/jbcohn/CHR-Workflows" target="_blank" rel="noopener" class="btn btn-secondary" style="font-size: 0.85rem; padding: 0.35rem 0.75rem;">
        <span style="font-weight: 700;">GitHub:</span> CHR-Workflows &rarr;
      </a>
    </div>

    <p style="margin-top: 0.75rem;">
      Automated business logic, digital royalty reconciliation pipelines, inventory matching, and ERP system integrations.
    </p>

    <ul>
      <li><strong>Digital Royalty Pipeline</strong>: Automated data extraction, vendor report normalization, and reconciliation across digital distributors.</li>
      <li><strong>Inventory & PO Matching</strong>: Algorithmic log reconciliation between purchase orders and inventory databases.</li>
    </ul>
  </section>

  <hr>

  <!-- ================= LITESTEP SPEED SYSTEMS ================= -->
  <section id="custom-speedbars" style="margin-bottom: 2rem;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.5rem;">
      <h2 style="margin-top: 0; border: none; padding: 0;">LiteStep Speed Systems & Site Source</h2>
      <a href="https://github.com/jbcohn/litestep.site" target="_blank" rel="noopener" class="btn btn-secondary" style="font-size: 0.85rem; padding: 0.35rem 0.75rem;">
        <span style="font-weight: 700;">GitHub:</span> litestep.site &rarr;
      </a>
    </div>

    <p style="margin-top: 0.75rem;">
      Mechanical design and composite fabrication of ultralight speed systems for performance paragliders, paired with this open-source Jekyll documentation site.
    </p>

    <div style="margin-top: 1rem;">
      <a href="{{ '/speedbar/' | relative_url }}" class="btn btn-primary">Visit Dedicated Speed Bar Page &rarr;</a>
    </div>
  </section>

</div>
