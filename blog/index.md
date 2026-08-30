---
layout: page
title: "Blog & Field Notes"
description: "Flight analysis, engineering logs, design processes, and software writeups."
permalink: /blog/
---

<ul class="post-list">
  {% for post in site.posts %}
    <li class="post-item">
      <div class="post-item-date">{{ post.date | date: "%B %-d, %Y" }}</div>
      <h2 class="post-item-title" style="margin: 0 0 0.5rem 0; border: none;">
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      </h2>
      <p class="post-item-excerpt">
        {% if post.description %}
          {{ post.description }}
        {% else %}
          {{ post.excerpt | strip_html | truncatewords: 35 }}
        {% endif %}
      </p>
      <a href="{{ post.url | relative_url }}" style="font-weight: 600; font-size: 0.9rem;">Read article &rarr;</a>
    </li>
  {% else %}
    <li class="post-item">
      <p style="color: var(--text-muted);">No posts found yet.</p>
    </li>
  {% endfor %}
</ul>
