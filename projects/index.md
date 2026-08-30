---
layout: page
title: "Projects & Engineering"
description: "Interactive web applications, aviation simulation, 3D elevation explorers, and open-source tools."
permalink: /projects/
hero_image: /assets/images/paragliding_dolomites_gaggle.jpg
---

<div class="projects-list">

  <!-- ================= PG RACE ANALYZER ================= -->
  <section id="race-analyzer" style="margin-bottom: 3.5rem;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 0.5rem;">
      <h2 style="margin-top: 0; border: none; padding: 0;">Paragliding Race Analyzer</h2>
      <div class="button-group">
        <a href="https://jbcohn.github.io/pg-race-analyzer/" target="_blank" rel="noopener" class="btn btn-primary" style="font-size: 0.9rem; padding: 0.45rem 0.9rem;">
          🚀 Launch Live Web App &rarr;
        </a>
        <a href="https://github.com/jbcohn/pg-race-analyzer" target="_blank" rel="noopener" class="btn btn-secondary" style="font-size: 0.85rem; padding: 0.45rem 0.75rem;">
          GitHub Source
        </a>
      </div>
    </div>

    <p>
      An interactive race analyzer for competition paragliding tracklogs. Visualizes GPS trajectories, task turnpoint cylinders, start gates, thermal climbs, and speed-to-fly performance breakdowns in the browser.
    </p>

    <img src="{{ '/assets/images/bay_area_flights.png' | relative_url }}" alt="PG Race Analyzer" style="width: 100%; border-radius: var(--radius-md); margin: 1rem 0; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">

    <ul>
      <li><strong>Turnpoint & Task Breakdown</strong>: Automatic detection of turnpoint cylinder entry/exit, start gate timing, and glide speeds.</li>
      <li><strong>Interactive Track Analysis</strong>: Color-coded climb rates, altitude profiles, and synchronized multi-pilot playback.</li>
    </ul>
  </section>

  <hr>

  <!-- ================= XC SIMULATOR ================= -->
  <section id="xc-simulator" style="margin-bottom: 3.5rem;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 0.5rem;">
      <h2 style="margin-top: 0; border: none; padding: 0;">Paragliding XC Simulator</h2>
      <div class="button-group">
        <a href="https://jbcohn.github.io/xc-simulator/" target="_blank" rel="noopener" class="btn btn-primary" style="font-size: 0.9rem; padding: 0.45rem 0.9rem;">
          🚀 Launch Simulator &rarr;
        </a>
        <a href="https://github.com/jbcohn/xc-simulator" target="_blank" rel="noopener" class="btn btn-secondary" style="font-size: 0.85rem; padding: 0.45rem 0.75rem;">
          GitHub Source
        </a>
      </div>
    </div>

    <p>
      Cross-country flight simulation tool modeling thermal generation, drift, cloud street physics, and decision-making for cross-country pilots.
    </p>

    <ul>
      <li><strong>Thermal Modeling</strong>: Real-time simulation of lift strength, sink margins, and wind shear.</li>
      <li><strong>Flight Path Optimization</strong>: Experiment with speed-to-fly tactics and glide glide-angle calculations under simulated meteorological conditions.</li>
    </ul>
  </section>

  <hr>

  <!-- ================= FORM CONSTANT VISUALIZER ================= -->
  <section id="form-constants" style="margin-bottom: 3.5rem;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 0.5rem;">
      <h2 style="margin-top: 0; border: none; padding: 0;">Form Constant Visualizer</h2>
      <div class="button-group">
        <a href="https://jbcohn.github.io/Form-Constant-Visualizer/" target="_blank" rel="noopener" class="btn btn-primary" style="font-size: 0.9rem; padding: 0.45rem 0.9rem;">
          🎨 Launch Visualizer &rarr;
        </a>
        <a href="https://github.com/jbcohn/Form-Constant-Visualizer" target="_blank" rel="noopener" class="btn btn-secondary" style="font-size: 0.85rem; padding: 0.45rem 0.75rem;">
          GitHub Source
        </a>
      </div>
    </div>

    <p>
      Real-time procedural visualizer exploring Klüver form constants, geometric mandalas, fractal patterns, and audio-reactive harmonic symmetries directly in the browser.
    </p>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; margin: 1.5rem 0;">
      <img src="{{ '/assets/images/form_constant.png' | relative_url }}" alt="Form Constant Geometry" style="width: 100%; border-radius: var(--radius-md); border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">
      <img src="{{ '/assets/images/stay_golden.png' | relative_url }}" alt="Geometric Symmetry" style="width: 100%; border-radius: var(--radius-md); border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">
    </div>

    <ul>
      <li><strong>Procedural Geometry</strong>: Interactive parameter sliders for ray counts, spiral angles, and wave frequencies.</li>
      <li><strong>Audio & Kinetic Modulation</strong>: Sound-reactive animations and real-time SVG/PNG export for artwork and apparel.</li>
    </ul>
  </section>

  <hr>

  <!-- ================= RIDGELINE 3D EXPLORER ================= -->
  <section id="ridgeline-explorer" style="margin-bottom: 3.5rem;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 0.5rem;">
      <h2 style="margin-top: 0; border: none; padding: 0;">Ridgeline 3D Explorer</h2>
      <div class="button-group">
        <a href="https://jbcohn.github.io/Ridgeline-3D-Explorer/" target="_blank" rel="noopener" class="btn btn-primary" style="font-size: 0.9rem; padding: 0.45rem 0.9rem;">
          🏔️ Launch 3D Explorer &rarr;
        </a>
        <a href="https://github.com/jbcohn/Ridgeline-3D-Explorer" target="_blank" rel="noopener" class="btn btn-secondary" style="font-size: 0.85rem; padding: 0.45rem 0.75rem;">
          GitHub Source
        </a>
      </div>
    </div>

    <p>
      WebGL and 3D elevation model visualizer converting USGS Digital Elevation Model (DEM) data into customizable stacked contour lines and topographic ridgeline art for California peaks.
    </p>

    <img src="{{ '/assets/images/shasta_ridgeline.png' | relative_url }}" alt="Topographic Contour Art" style="width: 100%; max-height: 380px; object-fit: contain; background: #000; border-radius: var(--radius-md); margin: 1rem 0; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">

    <ul>
      <li><strong>3D Mesh Controls</strong>: Dynamic vertical exaggeration, line density, perspective azimuth, and lighting angles.</li>
      <li><strong>Vector Export</strong>: High-DPI export pipeline formatted for print and apparel production.</li>
    </ul>
  </section>

  <hr>

  <!-- ================= DATA WORKFLOWS & AUTOMATION ================= -->
  <section id="workflows" style="margin-bottom: 3.5rem;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 0.5rem;">
      <h2 style="margin-top: 0; border: none; padding: 0;">Data Workflows & Automation</h2>
      <a href="https://github.com/jbcohn/CHR-Workflows" target="_blank" rel="noopener" class="btn btn-secondary" style="font-size: 0.85rem; padding: 0.45rem 0.75rem;">
        GitHub Source &rarr;
      </a>
    </div>

    <p>
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
    <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 0.5rem;">
      <h2 style="margin-top: 0; border: none; padding: 0;">LiteStep Speed Systems</h2>
      <a href="https://github.com/jbcohn/litestep.site" target="_blank" rel="noopener" class="btn btn-secondary" style="font-size: 0.85rem; padding: 0.45rem 0.75rem;">
        Site Source &rarr;
      </a>
    </div>

    <p>
      Mechanical design and composite fabrication of ultralight speed systems for performance paragliders.
    </p>

    <div style="margin-top: 1rem;">
      <a href="{{ '/speedbar/' | relative_url }}" class="btn btn-primary">Visit Dedicated Speed Bar Page &rarr;</a>
    </div>
  </section>

</div>
