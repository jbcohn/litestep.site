---
layout: page
title: "Projects (Readability Preview)"
description: "Interactive preview testing semi-opaque text backgrounds over the topographic mountain contours."
permalink: /projects/preview/
hero_image: /assets/images/paragliding_dolomites_gaggle.jpg
---

<style>
  :root {
    --preview-opacity: 0.88;
    --preview-blur: blur(8px);
  }

  /* Mode 1: Text Boxes Only */
  body.preview-textbox .readability-box {
    background: rgba(255, 255, 255, var(--preview-opacity));
    backdrop-filter: var(--preview-blur);
    -webkit-backdrop-filter: var(--preview-blur);
    border: 1px solid rgba(203, 213, 225, 0.85);
    border-radius: 10px;
    padding: 1.1rem 1.35rem;
    margin: 1rem 0;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);
  }

  /* Mode 2: Section Cards */
  body.preview-card .project-section {
    background: rgba(255, 255, 255, var(--preview-opacity));
    backdrop-filter: var(--preview-blur);
    -webkit-backdrop-filter: var(--preview-blur);
    border: 1px solid rgba(203, 213, 225, 0.85);
    border-radius: 16px;
    padding: 2rem;
    margin-bottom: 3rem;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.05);
  }

  /* Mode 3: Unified Reading Column */
  body.preview-column .site-content .site-container {
    background: rgba(255, 255, 255, var(--preview-opacity));
    backdrop-filter: var(--preview-blur);
    -webkit-backdrop-filter: var(--preview-blur);
    border-left: 1px solid rgba(203, 213, 225, 0.85);
    border-right: 1px solid rgba(203, 213, 225, 0.85);
    border-radius: 20px;
    padding: 2.25rem 2rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.06);
    margin-top: 1.5rem;
    margin-bottom: 2rem;
  }

  /* Mode 4: Current Site (None) */
  body.preview-none .readability-box,
  body.preview-none .project-section,
  body.preview-none .site-content .site-container {
    background: transparent !important;
    backdrop-filter: none !important;
    -webkit-backdrop-filter: none !important;
    border-color: transparent !important;
    box-shadow: none !important;
  }

  /* Floating control dock */
  .preview-dock {
    position: fixed;
    bottom: 1.25rem;
    left: 50%;
    transform: translateX(-50%);
    z-index: 9999;
    background: rgba(15, 23, 42, 0.95);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.18);
    border-radius: 16px;
    padding: 0.75rem 1.25rem;
    box-shadow: 0 12px 36px rgba(0, 0, 0, 0.4);
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 1rem;
    max-width: 95vw;
    color: #f8fafc;
    font-size: 0.85rem;
  }

  .preview-dock-btn {
    background: rgba(255, 255, 255, 0.1);
    color: #e2e8f0;
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 8px;
    padding: 0.35rem 0.7rem;
    font-size: 0.8rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.15s ease;
  }

  .preview-dock-btn:hover {
    background: rgba(255, 255, 255, 0.2);
    color: #ffffff;
  }

  .preview-dock-btn.active {
    background: #d95c12 !important;
    border-color: #f0921e !important;
    color: #ffffff !important;
    box-shadow: 0 2px 10px rgba(217, 92, 18, 0.4);
  }
</style>

<div style="background: rgba(217, 92, 18, 0.1); border: 1px solid rgba(217, 92, 18, 0.35); border-radius: 10px; padding: 0.85rem 1.25rem; margin-bottom: 2rem; font-size: 0.9rem; color: #9a3412;">
  <strong>💡 Live Readability Testing Dock:</strong> Use the floating dock at the bottom of your screen to toggle between <strong>Option 1 (Text Boxes Only)</strong>, <strong>Option 2 (Section Cards)</strong>, and <strong>Option 3 (Reading Column)</strong>, or slide the opacity up and down to see the real Whitney contour lines directly behind the text.
</div>

<div class="projects-list">

  <!-- ================= SOAP BUBBLE STUDIO ================= -->
  <section id="soap-bubble-studio" class="project-section" style="margin-bottom: 3.5rem;">
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
      <p style="margin: 0;">
        Real-time interactive physics engine and generative surface design studio simulating 2D foam clusters, Plateau borders, and thin-film optical iridescence directly in the browser.
      </p>
    </div>

    <div style="margin: 1.5rem 0; text-align: center;">
      <img src="{{ '/assets/images/bubble_surface_studio.png' | relative_url }}" alt="Soap Bubble Surface Studio Output" style="width: 100%; max-height: 480px; object-fit: contain; background: #060812; border-radius: var(--radius-md); border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">
    </div>

    <div class="readability-box">
      <ul style="margin: 0; padding-left: 1.25rem;">
        <li><strong>Foam Mechanics & Plateau Laws</strong>: Dual-tier spatial hash grid calculating non-linear capillary attraction, repulsion, and 120&deg; contact junction equilibrium at 60–120 FPS.</li>
        <li><strong>Michel-L&eacute;vy Optical Iridescence</strong>: Physical thin-film interference simulation with Fresnel edge reflectance and spectral wavelength mapping.</li>
        <li><strong>Interactive Fluid Tools & Audio</strong>: Swirl fluid currents, blow continuous bubble streams with a wand, pop bubbles with a needle tool, and synthesized cavity resonance audio.</li>
        <li><strong>High-DPI Master Export</strong>: Vector SVG and transparent 4500&times;5400 PNG export ready for direct-to-garment apparel printing.</li>
      </ul>
    </div>
  </section>

  <hr>

  <!-- ================= RIDGELINE 3D EXPLORER ================= -->
  <section id="ridgeline-explorer" class="project-section" style="margin-bottom: 3.5rem;">
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
      <p style="margin: 0;">
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
      <ul style="margin: 0; padding-left: 1.25rem;">
        <li><strong>3D Mesh Controls</strong>: Dynamic vertical exaggeration, line density, perspective azimuth, and lighting angles.</li>
        <li><strong>Vector Export</strong>: High-DPI export pipeline formatted for print and apparel production.</li>
      </ul>
    </div>
  </section>

  <hr>

  <!-- ================= FORM CONSTANT VISUALIZER ================= -->
  <section id="form-constants" class="project-section" style="margin-bottom: 3.5rem;">
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
      <p style="margin: 0;">
        Real-time procedural visualizer exploring Klüver form constants, geometric mandalas, fractal patterns, and audio-reactive harmonic symmetries directly in the browser.
      </p>
    </div>

    <div style="margin: 1.5rem 0; text-align: center;">
      <img src="{{ '/assets/images/form_constant_black.png' | relative_url }}" alt="Form Constant Geometry" style="width: 100%; max-height: 480px; object-fit: contain; background: #000; border-radius: var(--radius-md); border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">
    </div>

    <div class="readability-box">
      <ul style="margin: 0; padding-left: 1.25rem;">
        <li><strong>Procedural Geometry</strong>: Interactive parameter sliders for ray counts, spiral angles, and wave frequencies.</li>
        <li><strong>Audio & Kinetic Modulation</strong>: Sound-reactive animations and real-time SVG/PNG export for artwork and apparel.</li>
      </ul>
    </div>
  </section>

</div>

<!-- FLOATING CONTROLLER -->
<div class="preview-dock">
  <div style="display: flex; align-items: center; gap: 0.35rem;">
    <span style="font-weight: 700; color: #94a3b8; font-size: 0.75rem; text-transform: uppercase;">Style:</span>
    <button class="preview-dock-btn active" id="btn-p1" onclick="setPreviewMode('textbox')">1. Text Boxes</button>
    <button class="preview-dock-btn" id="btn-p2" onclick="setPreviewMode('card')">2. Section Cards</button>
    <button class="preview-dock-btn" id="btn-p3" onclick="setPreviewMode('column')">3. Reading Column</button>
    <button class="preview-dock-btn" id="btn-p4" onclick="setPreviewMode('none')">4. None (Current)</button>
  </div>

  <div style="display: flex; align-items: center; gap: 0.5rem; background: rgba(255,255,255,0.08); padding: 0.25rem 0.65rem; border-radius: 8px;">
    <span style="color: #94a3b8; font-size: 0.75rem;">White Opacity:</span>
    <input type="range" id="p-slider" min="40" max="100" value="88" style="width: 80px; accent-color: #d95c12; cursor: pointer;" oninput="setPreviewOpacity(this.value)">
    <span id="p-label" style="font-family: monospace; font-weight: 700; color: #facc15;">88%</span>
  </div>

  <div style="display: flex; align-items: center; gap: 0.35rem;">
    <span style="font-weight: 700; color: #94a3b8; font-size: 0.75rem;">Blur:</span>
    <button class="preview-dock-btn active" id="btn-pblur" onclick="togglePreviewBlur()">ON</button>
  </div>
</div>

<script>
  let pMode = 'textbox';
  let pBlur = true;

  document.body.classList.add('preview-textbox');

  function setPreviewMode(mode) {
    pMode = mode;
    document.body.classList.remove('preview-textbox', 'preview-card', 'preview-column', 'preview-none');
    document.body.classList.add('preview-' + mode);
    ['textbox', 'card', 'column', 'none'].forEach((m, i) => {
      document.getElementById('btn-p' + (i+1)).classList.toggle('active', m === mode);
    });
  }

  function setPreviewOpacity(val) {
    const op = val / 100;
    document.getElementById('p-label').textContent = val + '%';
    document.documentElement.style.setProperty('--preview-opacity', op);
  }

  function togglePreviewBlur() {
    pBlur = !pBlur;
    const btn = document.getElementById('btn-pblur');
    btn.textContent = pBlur ? 'ON' : 'OFF';
    btn.classList.toggle('active', pBlur);
    document.documentElement.style.setProperty('--preview-blur', pBlur ? 'blur(8px)' : 'none');
  }
</script>
