---
layout: page
title: "Projects & Engineering"
description: "A showcase of aviation software, GIS & elevation modeling, music workflows, and generative art."
permalink: /projects/
hero_image: /assets/images/paragliding_dolomites_gaggle.jpg
---

<div class="projects-list">

  <section id="igc-plotter" style="margin-bottom: 3.5rem;">
    <h2>Paragliding IGC & DEM Elevation Visualizer</h2>
    <p>
      An advanced Python geospatial pipeline for rendering paragliding GPS tracklogs (.IGC files) over high-resolution Digital Elevation Models (DEMs).
    </p>
    <img src="{{ '/assets/images/bay_area_flights.png' | relative_url }}" alt="IGC Flight Plotting" style="width: 100%; border-radius: var(--radius-md); margin: 1rem 0; border: 1px solid var(--border-color);">
    <ul>
      <li><strong>Terrain Integration</strong>: Merges 30m / 10m USGS DEMs and GeoTIFF data with glide ratio and barometric altimetry.</li>
      <li><strong>Thermal & XC Visualization</strong>: Colorizes thermalling efficiency, climb rates, and glide transitions across complex mountain topography.</li>
      <li><strong>Competition Race Analysis</strong>: Automated task turnpoint cylinder detection and speed-section breakdowns.</li>
    </ul>
  </section>

  <hr>

  <section id="generative-art" style="margin-bottom: 3.5rem;">
    <h2>Generative Art & Form Constants</h2>
    <p>
      Exploring mathematical symmetry, visual perception theories, and algorithmic geometry through interactive canvas applications and Python rendering scripts.
    </p>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; margin: 1.5rem 0;">
      <img src="{{ '/assets/images/form_constant.png' | relative_url }}" alt="Form Constant Geometry" style="width: 100%; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
      <img src="{{ '/assets/images/shasta_ridgeline.png' | relative_url }}" alt="Topographic Contour Art" style="width: 100%; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
    </div>
    <ul>
      <li><strong>Mandala Web Application</strong>: Real-time procedural rendering of harmonic circular symmetries with sound interaction.</li>
      <li><strong>Form Constant Engines</strong>: Algorithmic modeling of geometric visual patterns (Kl&uuml;ver form constants) in high-resolution vector and raster formats.</li>
      <li><strong>Topographic Relief Line Work</strong>: Converting raw elevation raster matrices into stacked contour ridgeline art for print and apparel.</li>
    </ul>
  </section>

  <hr>

  <section id="rekordbox-tools" style="margin-bottom: 3.5rem;">
    <h2>Rekordbox DJ Tools & Music Intelligence</h2>
    <p>
      Automated Python tools designed to manage large electronic music collections, parse Pioneer Rekordbox XML databases, and enrich DJ metadata.
    </p>
    <ul>
      <li><strong>Automated Genre Enrichment</strong>: Ingests raw track titles/artists and classifies micro-genres via external music ontology APIs.</li>
      <li><strong>XML Database Synchronization</strong>: Bi-directional reconciliation between Rekordbox collection exports and streaming backup databases.</li>
      <li><strong>Key & Energy Harmonization</strong>: Optimizes playlist transition compatibility based on Camelot wheel data and frequency profile analysis.</li>
    </ul>
  </section>

  <hr>

  <section id="custom-speedbars" style="margin-bottom: 2rem;">
    <h2>LiteStep Speed Systems</h2>
    <p>
      Mechanical design and composite fabrication of ultralight speed systems for performance paragliders.
    </p>
    <div style="margin-top: 1rem;">
      <a href="{{ '/speedbar/' | relative_url }}" class="btn btn-primary">Visit Dedicated Speed Bar Page &rarr;</a>
    </div>
  </section>

</div>
