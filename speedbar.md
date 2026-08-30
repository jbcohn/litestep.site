---
layout: page
title: "LiteStep Speed Bar"
description: "Ultralight, competition-grade paragliding speed bar designed for clean foot placement, zero bulk, and effortless engagement."
permalink: /speedbar/
hero_image: /assets/images/hero_aerial.jpg
---

<!-- STOCK / AVAILABILITY ALERT -->
<div style="background: var(--speedbar-bg); border: 1px solid var(--speedbar-border); border-radius: var(--radius-md); padding: 1.1rem 1.25rem; margin-bottom: 2rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.75rem;">
  <div>
    <span class="spotlight-tag" style="margin-right: 0.5rem;">Inventory Status</span>
    <span>As of <strong>{{ site.data.inventory.last_updated | date: "%B %-d, %Y" }}</strong>: </span>
    <span style="display: inline-block; margin-left: 0.25rem;">
      <span style="color: {% if site.data.inventory.light_stock > 0 %}#3fb950{% else %}var(--speedbar-accent){% endif %}; font-weight: 700;">{{ site.data.inventory.light_stock }} Light</span>,
      <span style="color: {% if site.data.inventory.comp_stock > 0 %}#3fb950{% else %}var(--speedbar-accent){% endif %}; font-weight: 700;">{{ site.data.inventory.comp_stock }} Comp</span> in stock.
    </span>
    {% if site.data.inventory.status_message %}
      <div style="font-size: 0.9rem; color: var(--text-muted); margin-top: 0.25rem;">{{ site.data.inventory.status_message }}</div>
    {% endif %}
  </div>
  <a href="mailto:jbcohn@gmail.com?subject=LiteStep%20Availability%20Inquiry" class="btn btn-secondary" style="font-size: 0.85rem; padding: 0.35rem 0.75rem;">Check Lead Times</a>
</div>

<!-- PILOT REVIEWS -->
<section style="margin: 2rem 0;">
  <h2>What Pilots Are Saying</h2>
  <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); margin-top: 1rem;">
    
    <div class="card" style="background: var(--bg-surface-elevated);">
      <p style="font-style: italic; font-size: 0.95rem; margin-bottom: 0.75rem; color: var(--text-main);">
        &ldquo;Litestep is the best. I recently flew Bullet on my XC kit after racing on a Litestep all season and I was surprised at how clunky it was. No need for all the extra plastic on the top step, nor the wide webbing straps. Litestep is easy to adjust, has better materials, and less bulk to crowd out your feet.&rdquo;
      </p>
      <div style="font-weight: 700; font-size: 0.85rem; color: var(--accent);">&mdash; Evan Bouchier</div>
    </div>

    <div class="card" style="background: var(--bg-surface-elevated);">
      <p style="font-style: italic; font-size: 0.95rem; margin-bottom: 0.75rem; color: var(--text-main);">
        &ldquo;Switched to these bars on both my harnesses and only wish I had sooner honestly.&rdquo;
      </p>
      <div style="font-weight: 700; font-size: 0.85rem; color: var(--accent);">&mdash; Pete Thompson</div>
    </div>

    <div class="card" style="background: var(--bg-surface-elevated);">
      <p style="font-style: italic; font-size: 0.95rem; margin-bottom: 0.75rem; color: var(--text-main);">
        &ldquo;Litestep is smaller and cleaner design. New version with narrow top step is nice. I find it easier to push full bar evenly than with the wider top step of the bullet.&rdquo;
      </p>
      <div style="font-weight: 700; font-size: 0.85rem; color: var(--accent);">&mdash; Ben Pedersen-Wedlock</div>
    </div>

    <div class="card" style="background: var(--bg-surface-elevated);">
      <p style="font-style: italic; font-size: 0.95rem; margin-bottom: 0.75rem; color: var(--text-main);">
        &ldquo;I own 4 of them.&rdquo;
      </p>
      <div style="font-weight: 700; font-size: 0.85rem; color: var(--accent);">&mdash; Korey Curtis</div>
    </div>

  </div>
</section>

<hr>

<!-- PRICING & ORDERING -->
<section style="margin: 2.5rem 0;">
  <h2>Pricing & Direct Ordering</h2>
  <p style="color: var(--text-muted);">
    All prices include delivery in the continental US via USPS. Ordering multiple bars to the same address? Take <strong>$10 off</strong> each additional bar!
  </p>

  <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); margin-top: 1.5rem;">
    
    <!-- LIGHT VERSION CARD -->
    <div class="card" style="border: 2px solid var(--border-color); position: relative;">
      <div style="font-size: 0.85rem; text-transform: uppercase; font-weight: 700; color: var(--text-muted); margin-bottom: 0.25rem;">Ultralight XC</div>
      <h3 style="margin: 0 0 0.5rem 0; font-size: 1.5rem;">Light Version</h3>
      <div style="font-size: 2rem; font-weight: 800; color: var(--text-main); margin-bottom: 0.25rem;">
        $145 <span style="font-size: 0.9rem; font-weight: 400; color: var(--text-muted);">/ $157 in CA (incl. tax)</span>
      </div>
      <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1.25rem;">
        Featherweight <strong>71g</strong> design featuring 25mm steps. Perfect for hike & fly, light XC pods, and clean cockpits.
      </p>
      <div style="display: flex; flex-direction: column; gap: 0.5rem; margin-top: auto;">
        <a href="https://venmo.com/?txn=pay&audience=private&recipients=@Josh-Cohn-10&amount=145&note=1%20Light%20Litestep" target="_blank" rel="noopener" class="btn btn-primary" style="text-align: center;">
          Venmo $145 (Non-CA)
        </a>
        <a href="https://account.venmo.com/payment-link?audience=private&amount=157&note=1%20Light%20Litestep%20CA&recipients=%2CJosh-Cohn-10&txn=pay" target="_blank" rel="noopener" class="btn btn-secondary" style="text-align: center;">
          Venmo $157 (California)
        </a>
      </div>
    </div>

    <!-- COMP VERSION CARD -->
    <div class="card" style="border: 2px solid var(--speedbar-accent); position: relative;">
      <div class="spotlight-tag" style="position: absolute; top: 1rem; right: 1rem;">Most Popular</div>
      <div style="font-size: 0.85rem; text-transform: uppercase; font-weight: 700; color: var(--speedbar-accent); margin-bottom: 0.25rem;">Competition & Race</div>
      <h3 style="margin: 0 0 0.5rem 0; font-size: 1.5rem;">Comp Version</h3>
      <div style="font-size: 2rem; font-weight: 800; color: var(--text-main); margin-bottom: 0.25rem;">
        $180 <span style="font-size: 0.9rem; font-weight: 400; color: var(--text-muted);">/ $195 in CA (incl. tax)</span>
      </div>
      <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1.25rem;">
        Robust <strong>112g</strong> design with 35mm steps for maximum pushing comfort. Includes extra-long replacement lines for riser integration.
      </p>
      <div style="display: flex; flex-direction: column; gap: 0.5rem; margin-top: auto;">
        <a href="https://venmo.com/?txn=pay&audience=private&recipients=@Josh-Cohn-10&amount=180&note=1%20Comp%20Litestep%20for%20Sub" target="_blank" rel="noopener" class="btn btn-primary" style="text-align: center;">
          Venmo $180 (Non-CA)
        </a>
        <a href="https://account.venmo.com/payment-link?audience=private&amount=195&note=1%20Comp%20Litestep%20CA&recipients=%2CJosh-Cohn-10&txn=pay" target="_blank" rel="noopener" class="btn btn-secondary" style="text-align: center;">
          Venmo $195 (California)
        </a>
      </div>
    </div>

  </div>

  <div class="spec-box" style="margin-top: 1.5rem;">
    <h3 style="margin-top: 0;">Payment Instructions & Options</h3>
    <ul>
      <li><strong>Venmo</strong>: Click payment buttons above or send to <code>@Josh-Cohn-10</code>.</li>
      <li><strong>PayPal</strong>: Send via <em>Friends &amp; Family</em> to <a href="mailto:jbcohn@gmail.com">jbcohn@gmail.com</a>.</li>
      <li><strong>Important</strong>: Please include your <strong>shipping address</strong> and <strong>email</strong> in the payment notes so tracking updates are sent to you automatically.</li>
    </ul>
  </div>
</section>

<hr>

<!-- PHOTO GALLERY -->
<section style="margin: 2.5rem 0;">
  <h2>Product Gallery</h2>
  <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));">
    
    <div>
      <img src="{{ '/assets/images/speedbar_light.png' | relative_url }}" alt="LiteStep Light Version" style="width: 100%; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
      <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.5rem; text-align: center;">
        <strong>Fig. 1:</strong> Light version (71g, $145)
      </p>
    </div>

    <div>
      <img src="{{ '/assets/images/speedbar_comp.png' | relative_url }}" alt="LiteStep Comp Version" style="width: 100%; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
      <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.5rem; text-align: center;">
        <strong>Fig. 2:</strong> Comp version (112g, $180)
      </p>
    </div>

    <div>
      <img src="{{ '/assets/images/speedbar_installed.png' | relative_url }}" alt="Comp Version Installed in Harness" style="width: 100%; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
      <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.5rem; text-align: center;">
        <strong>Fig. 3:</strong> Comp version installed in harness pod
      </p>
    </div>

    <div>
      <img src="{{ '/assets/images/speedbar_steps_comparison.jpg' | relative_url }}" alt="25mm Light vs 35mm Comp Step Comparison" style="width: 100%; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
      <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.5rem; text-align: center;">
        <strong>Fig. 4:</strong> 25mm (Light) vs. 35mm (Comp) step profiles
      </p>
    </div>

  </div>
</section>

<hr>

<!-- SETUP & INSTALLATION -->
<section style="margin: 2.5rem 0;">
  <h2>Setup & Installation</h2>

  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; border-radius: var(--radius-md); margin: 1.5rem 0; border: 1px solid var(--border-color);">
    <iframe src="https://www.youtube-nocookie.com/embed/pPAJ54xCTmc" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen title="LiteStep Installation Video"></iframe>
  </div>

  <p>
    Watch the step-by-step installation video above or join the discussion in the <a href="https://www.paraglidingforum.com/viewtopic.php?t=98169" target="_blank" rel="noopener">ParaglidingForum Thread &rarr;</a>.
  </p>

  <div style="background: rgba(234, 88, 12, 0.1); border-left: 4px solid var(--speedbar-accent); padding: 1rem 1.25rem; border-radius: 0 var(--radius-sm) var(--radius-sm) 0; margin: 1.5rem 0;">
    <strong style="color: var(--speedbar-accent);">⚠️ Setup Caution:</strong>
    <p style="margin: 0.5rem 0 0 0; font-size: 0.95rem;">
      When setting up your bar, verify that when you release it, the top step cannot get caught on the front edge of the seatboard. Having a speed bar stuck on in flight is dangerous (though if it ever catches, it can usually be freed by re-engaging and releasing with your foot held lower toward the ground).
    </p>
  </div>
</section>

<hr>

<!-- SERVICE & WARRANTY -->
<section style="margin: 2.5rem 0;">
  <h2>Service & Support</h2>
  <p>
    If you ever have trouble with setup, tuning, or maintenance, email me directly at <a href="mailto:jbcohn@gmail.com">jbcohn@gmail.com</a>. LiteStep bars are built to last through multiple seasons and gliders. If you experience premature wear or need replacement lines, let me know and I will do my best within reason to take care of you!
  </p>
</section>

<hr>

<!-- FREQUENTLY ASKED QUESTIONS -->
<section style="margin: 2.5rem 0;">
  <h2>Frequently Asked Questions</h2>

  <div style="margin-top: 1.5rem;">
    <div style="margin-bottom: 1.5rem;">
      <h3 style="font-size: 1.15rem; color: var(--text-main); margin-bottom: 0.35rem;">Q: Do you trim up the dangling lines past the stopper knots once adjusted, or leave them?</h3>
      <p style="color: var(--text-muted);">
        <strong>A:</strong> I don't trim them. They don't cause any issues in flight, and leaving them gives you full flexibility to readjust the bar when switching to a new glider or harness later on.
      </p>
    </div>

    <div style="margin-bottom: 1.5rem;">
      <h3 style="font-size: 1.15rem; color: var(--text-main); margin-bottom: 0.35rem;">Q: What are the main benefits of the Comp variant over the Light?</h3>
      <p style="color: var(--text-muted);">
        <strong>A:</strong> With 35mm wide steps, the Comp version is slightly smoother to find with your heel and offers increased surface area comfort when pushing bar for hours on long competition or XC glides. The Light version functions identically and saves ~40 grams.
      </p>
    </div>

    <div style="margin-bottom: 1.5rem;">
      <h3 style="font-size: 1.15rem; color: var(--text-main); margin-bottom: 0.35rem;">Q: Why did the design switch to a single top step instead of a wide step for two feet?</h3>
      <p style="color: var(--text-muted);">
        <strong>A:</strong> The single centered top step provides a definite improvement: it allows you to hold full bar evenly with one foot in the center, avoids asymmetric riser pulling, and makes stepping down back to the middle step effortless.
      </p>
    </div>

    <div style="margin-bottom: 1.5rem;">
      <h3 style="font-size: 1.15rem; color: var(--text-main); margin-bottom: 0.35rem;">Q: How do I connect the single footplate bungee attachment to a harness with two bungee points?</h3>
      <p style="color: var(--text-muted);">
        <strong>A:</strong> You can either attach the bungee to one side (I fly mine attached to one side and have no problem catching the bar), bridge the two harness points with a piece of line and attach to the center, or drill a clean center hole in your footplate. Adding two bungees is possible but generally adds unnecessary clutter for your feet.
      </p>
    </div>

    <div style="margin-bottom: 1.5rem;">
      <h3 style="font-size: 1.15rem; color: var(--text-main); margin-bottom: 0.35rem;">Q: There isn't a spliced loop on the end of the Light line. How do I attach it to my risers?</h3>
      <p style="color: var(--text-muted);">
        <strong>A:</strong> I recommend removing metal Brummel hooks entirely. Simply tie a clean overhand stopper knot in the LiteStep Dyneema line, and use a larks-head knot from the glider riser speed line to choke around it. This is lighter, cleaner, and cannot unhook in flight.
      </p>
    </div>
  </div>
</section>
