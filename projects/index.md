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

    <img src="{{ '/assets/images/pg_race_analyzer.png' | relative_url }}" alt="PG Race Analyzer Interface" style="width: 100%; border-radius: var(--radius-md); margin: 1rem 0; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">

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
      An interactive cross-country flight planning and task scoring web application. Import GPS tracklogs (.IGC, .GPX, .KML) or interactively draw routes to calculate real-time XContest scoring, FAI triangle validation, and closing gap optimizations over high-resolution satellite maps.
    </p>

    <img src="{{ '/assets/images/xc_simulator.png' | relative_url }}" alt="XC Simulator Interface" style="width: 100%; border-radius: var(--radius-md); margin: 1rem 0; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">

    <ul>
      <li><strong>Automatic FAI Triangle Validation</strong>: Real-time rendering of FAI turnpoint sectors ensuring shortest leg &ge; 28% perimeter constraints.</li>
      <li><strong>XContest Rules & Multipliers</strong>: Live point calculation for Free Flights (1.0 pt/km), Free Triangles (1.2–1.4 pts/km), and Closed FAI Triangles (1.6 pts/km).</li>
      <li><strong>Tracklog Import & Route Export</strong>: Load flight logs or design upcoming XC flights with interactive waypoints.</li>
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

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin: 1.5rem 0;">
      <div>
        <img src="{{ '/assets/images/dem_contour_gradient.png' | relative_url }}" alt="3D DEM Contour Gradient" style="width: 100%; height: 240px; object-fit: cover; border-radius: var(--radius-md); border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">
        <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.35rem; text-align: center;">Topographic elevation gradient contours</p>
      </div>
      <div>
        <img src="{{ '/assets/images/dem_wireframe_black.png' | relative_url }}" alt="3D DEM Wireframe Mesh" style="width: 100%; height: 240px; object-fit: cover; background: #000; border-radius: var(--radius-md); border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">
        <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.35rem; text-align: center;">High-density 3D wireframe elevation matrix</p>
      </div>
    </div>

    <ul>
      <li><strong>3D Mesh Controls</strong>: Dynamic vertical exaggeration, line density, perspective azimuth, and lighting angles.</li>
      <li><strong>Vector Export</strong>: High-DPI export pipeline formatted for print and apparel production.</li>
    </ul>
  </section>

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
