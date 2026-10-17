---
layout: page
title: "Order Confirmed — Thank You!"
description: "Your Litestep apparel order has been received and sent to production."
permalink: /merch/thank-you/
---

<div class="card" style="max-width: 640px; margin: 2rem auto; padding: 2.5rem 2rem; text-align: center;">
  <div style="width: 56px; height: 56px; border-radius: 50%; background: #dcfce7; color: #16a34a; display: inline-flex; align-items: center; justify-content: center; margin-bottom: 1.25rem;">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.75" stroke-linecap="round" stroke-linejoin="round">
      <polyline points="20 6 9 17 4 12"></polyline>
    </svg>
  </div>

  <h2 style="margin: 0 0 0.75rem 0; font-size: 1.65rem;">Thank You for Your Order!</h2>
  <p style="font-size: 1.02rem; color: var(--text-muted); margin: 0 auto 1.5rem auto; max-width: 480px;">
    Your payment has been processed via Stripe and your apparel order has been automatically queued for printing and fulfillment. You will receive an email receipt and tracking link as soon as your order ships.
  </p>

  <div id="order-summary-box" style="display: none; background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 8px; padding: 1rem 1.25rem; margin-bottom: 1.75rem; text-align: left; font-size: 0.92rem; color: #374151;">
    <div style="display: flex; justify-content: space-between; margin-bottom: 0.35rem;">
      <span style="color: #6b7280;">Order Reference:</span>
      <span id="order-ref-id" style="font-family: monospace; font-weight: 600; color: #111827;">—</span>
    </div>
    <div style="display: flex; justify-content: space-between;">
      <span style="color: #6b7280;">Total Paid:</span>
      <span id="order-total-paid" style="font-weight: 700; color: #111827;">—</span>
    </div>
  </div>

  <a href="{{ '/merch/' | relative_url }}" class="btn btn-primary" style="display: inline-block; padding: 0.75rem 1.5rem;">
    ← Back to Merch &amp; Apparel
  </a>
</div>

<script>
(function() {
  // 1. Clear shopping cart after completed checkout
  try {
    localStorage.removeItem('litestep_merch_cart_v1');
  } catch (e) {}

  // 2. Fetch session details for order confirmation & Google Ads conversion tracking
  const params = new URLSearchParams(window.location.search);
  const sessionId = params.get('session_id');
  if (!sessionId || !sessionId.startsWith('cs_')) return;

  const summaryBox = document.getElementById('order-summary-box');
  const refEl = document.getElementById('order-ref-id');
  const totalEl = document.getElementById('order-total-paid');

  fetch('https://litestep-printful-webhook.jbcohn.workers.dev/session-status?session_id=' + encodeURIComponent(sessionId))
    .then(r => r.ok ? r.json() : null)
    .then(data => {
      if (!data || !data.id) return;
      const totalDollars = (data.amount_total || 0) / 100;

      if (summaryBox && refEl && totalEl) {
        refEl.textContent = data.id.slice(-12).toUpperCase();
        totalEl.textContent = '$' + totalDollars.toFixed(2) + ' ' + (data.currency || 'USD');
        summaryBox.style.display = 'block';
      }

      // Deduplicate purchase conversion per session_id
      const trackedKey = 'litestep_tracked_' + data.id;
      if (sessionStorage.getItem(trackedKey)) return;
      sessionStorage.setItem(trackedKey, '1');

      if (typeof window.gtag === 'function') {
        window.gtag('event', 'purchase', {
          transaction_id: data.id,
          value: totalDollars,
          currency: data.currency || 'USD'
        });
        if (window.LITESTEP_ADS_CONVERSION_SEND_TO) {
          window.gtag('event', 'conversion', {
            send_to: window.LITESTEP_ADS_CONVERSION_SEND_TO,
            value: totalDollars,
            currency: data.currency || 'USD',
            transaction_id: data.id
          });
        }
      }
    })
    .catch(() => {});
})();
</script>
