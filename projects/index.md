---
layout: page
title: "Projects & Engineering"
description: "Interactive web applications, aviation simulation, 3D elevation explorers, and open-source tools."
permalink: /projects/
hero_image: /assets/images/paragliding_dolomites_gaggle.jpg
---

<div class="projects-list">

  <!-- ================= FLIGHT MAP STUDIO ================= -->
  <section id="flight-map-studio" style="margin-bottom: 3.5rem;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 0.5rem;">
      <h2 style="margin-top: 0; border: none; padding: 0;">Flight Map Studio</h2>
      <div class="button-group">
        <a href="https://jbcohn.github.io/flight-map-studio/" target="_blank" rel="noopener" class="btn btn-primary" style="font-size: 0.9rem; padding: 0.45rem 0.9rem;">
          🗺️ Launch Flight Map Studio &rarr;
        </a>
        <a href="https://github.com/jbcohn/flight-map-studio" target="_blank" rel="noopener" class="btn btn-secondary" style="font-size: 0.85rem; padding: 0.45rem 0.75rem;">
          GitHub Source
        </a>
      </div>
    </div>

    <div class="readability-box">
      <p>
        An interactive paragliding and hang gliding flight track visualizer and cartographic poster studio. Renders IGC GPS tracklogs over continuous 30m Digital Elevation Models (DEM) with dynamic 3D directional hillshading, customizable hypsometric color ramps, place name overlays, and high-resolution print export.
      </p>
    </div>

    <img src="{{ '/assets/images/flight_map_studio.png' | relative_url }}" alt="Flight Map Studio Tracklog & DEM Interface" style="width: 100%; border-radius: var(--radius-md); margin: 1rem 0; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">

    <div class="readability-box">
      <ul>
        <li><strong>Continuous 30m Western US DEM</strong>: Real-time client-side tile shader computing 3D NW directional hillshading and altitude palettes directly in the browser across WA, OR, CA, NV, UT, AZ, CO, and ID.</li>
        <li><strong>Custom Track Styling & Analytics</strong>: Vibrant outer glow, continuous Turbo altitude gradients, climb/sink vario coloring, and individual flight color assignments.</li>
        <li><strong>Place Names & Reference Overlay</strong>: Interactive opacity slider for peaks, towns, and boundaries positioned beneath flight paths.</li>
        <li><strong>High-DPI Poster Studio</strong>: Multi-resolution canvas export (1&times;, 2&times;, 3&times;) generating framed, print-ready topographic flight posters.</li>
      </ul>
    </div>
  </section>

  <hr>

  <!-- ================= SOAP BUBBLE STUDIO ================= -->
  <section id="soap-bubble-studio" style="margin-bottom: 3.5rem;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 0.5rem;">
      <h2 style="margin-top: 0; border: none; padding: 0;">Soap Bubble Surface Studio</h2>
      <div class="button-group">
        <a href="https://jbcohn.github.io/Soap-Bubble-Studio/" target="_blank" rel="noopener" class="btn btn-primary" style="font-size: 0.9rem; padding: 0.45rem 0.9rem;">
          🫧 Launch Studio &rarr;
        </a>
        <a href="https://github.com/jbcohn/Soap-Bubble-Studio" target="_blank" rel="noopener" class="btn btn-secondary" style="font-size: 0.85rem; padding: 0.45rem 0.75rem;">
          GitHub Source
        </a>
      </div>
    </div>

    <div class="readability-box">
      <p>
        Real-time interactive physics engine and generative surface design studio simulating 2D foam clusters, Plateau borders, and thin-film optical iridescence directly in the browser.
      </p>
    </div>

    <div style="margin: 1.5rem 0; text-align: center;">
      <img src="{{ '/assets/images/bubble_surface_studio.png' | relative_url }}" alt="Soap Bubble Surface Studio Output" style="width: 100%; max-height: 480px; object-fit: contain; background: #060812; border-radius: var(--radius-md); border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">
    </div>

    <div class="readability-box">
      <ul>
        <li><strong>Foam Mechanics & Plateau Laws</strong>: Dual-tier spatial hash grid calculating non-linear capillary attraction, repulsion, and 120&deg; contact junction equilibrium at 60–120 FPS.</li>
        <li><strong>Michel-L&eacute;vy Optical Iridescence</strong>: Physical thin-film interference simulation with Fresnel edge reflectance and spectral wavelength mapping.</li>
        <li><strong>Interactive Fluid Tools & Audio</strong>: Swirl fluid currents, blow continuous bubble streams with a wand, pop bubbles with a needle tool, and synthesized cavity resonance audio.</li>
        <li><strong>High-DPI Master Export</strong>: Vector SVG and transparent 4500&times;5400 PNG export ready for direct-to-garment apparel printing.</li>
      </ul>
    </div>
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

    <div class="readability-box">
      <p>
        WebGL and 3D elevation model visualizer converting USGS Digital Elevation Model (DEM) data into customizable stacked contour lines and topographic ridgeline art for California peaks.
      </p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin: 1.5rem 0;">
      <div>
        <img src="{{ '/assets/images/ridgeline_3d_mesh.png' | relative_url }}" alt="3D Triangulated Mesh Peak" style="width: 100%; height: 240px; object-fit: cover; background: #000; border-radius: var(--radius-md); border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">
        <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.35rem; text-align: center;">Triangulated 3D terrain mesh & heatmap elevation model</p>
      </div>
      <div>
        <img src="{{ '/assets/images/dem_wireframe_black.png' | relative_url }}" alt="3D DEM Wireframe Mesh" style="width: 100%; height: 240px; object-fit: cover; background: #000; border-radius: var(--radius-md); border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">
        <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.35rem; text-align: center;">High-density 3D wireframe elevation matrix</p>
      </div>
    </div>

    <div class="readability-box">
      <ul>
        <li><strong>3D Mesh Controls</strong>: Dynamic vertical exaggeration, line density, perspective azimuth, and lighting angles.</li>
        <li><strong>Vector Export</strong>: High-DPI export pipeline formatted for print and apparel production.</li>
      </ul>
    </div>
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

    <div class="readability-box">
      <p>
        Real-time procedural visualizer exploring Klüver form constants, geometric mandalas, fractal patterns, and audio-reactive harmonic symmetries directly in the browser.
      </p>
    </div>

    <div style="margin: 1.5rem 0; text-align: center;">
      <img src="{{ '/assets/images/form_constant_black.png' | relative_url }}" alt="Form Constant Geometry" style="width: 100%; max-height: 480px; object-fit: contain; background: #000; border-radius: var(--radius-md); border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">
    </div>

    <div class="readability-box">
      <ul>
        <li><strong>Procedural Geometry</strong>: Interactive parameter sliders for ray counts, spiral angles, and wave frequencies.</li>
        <li><strong>Audio & Kinetic Modulation</strong>: Sound-reactive animations and real-time SVG/PNG export for artwork and apparel.</li>
      </ul>
    </div>
  </section>

  <hr>

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

    <div class="readability-box">
      <p>
        An interactive race analyzer for competition paragliding tracklogs. Visualizes GPS trajectories, task turnpoint cylinders, start gates, thermal climbs, and speed-to-fly performance breakdowns in the browser.
      </p>
    </div>

    <img src="{{ '/assets/images/pg_race_analyzer.png' | relative_url }}" alt="PG Race Analyzer Interface" style="width: 100%; border-radius: var(--radius-md); margin: 1rem 0; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">

    <div class="readability-box">
      <ul>
        <li><strong>Turnpoint & Task Breakdown</strong>: Automatic detection of turnpoint cylinder entry/exit, start gate timing, and glide speeds.</li>
        <li><strong>Interactive Track Analysis</strong>: Color-coded climb rates, altitude profiles, and synchronized multi-pilot playback.</li>
      </ul>
    </div>
  </section>

  <hr>

  <!-- ================= XC SIMULATOR ================= -->
  <section id="xc-simulator" style="margin-bottom: 2rem;">
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

    <div class="readability-box">
      <p>
        An interactive cross-country flight planning and task scoring web application. Import GPS tracklogs (.IGC, .GPX, .KML) or interactively draw routes to calculate real-time XContest scoring, FAI triangle validation, and closing gap optimizations over high-resolution satellite maps.
      </p>
    </div>

    <img src="{{ '/assets/images/xc_simulator.png' | relative_url }}" alt="XC Simulator Interface" style="width: 100%; border-radius: var(--radius-md); margin: 1rem 0; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">

    <div class="readability-box">
      <ul>
        <li><strong>Automatic FAI Triangle Validation</strong>: Real-time rendering of FAI turnpoint sectors ensuring shortest leg &ge; 28% perimeter constraints.</li>
        <li><strong>XContest Rules & Multipliers</strong>: Live point calculation for Free Flights (1.0 pt/km), Free Triangles (1.2–1.4 pts/km), and Closed FAI Triangles (1.6 pts/km).</li>
        <li><strong>Tracklog Import & Route Export</strong>: Load flight logs or design upcoming XC flights with interactive waypoints.</li>
      </ul>
    </div>
  </section>

</div>
