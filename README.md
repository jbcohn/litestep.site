# LiteStep.us

Source code for [litestep.us](https://litestep.us), hosted natively on **GitHub Pages** with Jekyll.

## 📁 Repository Structure

```
├── _config.yml               # Site settings, nav links, and metadata
├── CNAME                     # Domain configuration (litestep.us)
├── _layouts/                 # HTML templates (default, page, post)
├── _includes/                # Header nav, footer
├── assets/
│   ├── css/style.css         # Modern responsive CSS styles
│   └── images/               # Preview images and graphics
├── index.md                  # Homepage with Speed Bar spotlight & projects
├── speedbar.md               # Dedicated Speed Bar product & rigging page
├── projects/index.md         # Projects hub
├── merch/index.md            # Merch & apparel gallery
├── blog/index.md             # Blog post archive
└── _posts/                   # Markdown blog articles (YYYY-MM-DD-title.md)
```

## ✍️ How to Add a New Blog Post

Create a new markdown file inside `_posts/` with the naming convention `YYYY-MM-DD-title.md`:

```markdown
---
layout: post
title: "My New Article Title"
date: 2026-09-01
author: Josh Cohn
categories: [Paragliding, Speedbar]
description: "A short summary for previews and search engines."
---

Your markdown content here...
```

Commit and push to `main` — GitHub Pages deploys your changes automatically.

---

## 🚀 Setting Up on GitHub

1. Create a new repository on GitHub (e.g. `litestep-site` or `yourusername.github.io`).
2. Push this directory:
   ```bash
   cd /Users/joshcohn/Developer/litestep-site
   git init
   git add .
   git commit -m "Initial commit of litestep.us Jekyll site"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git push -u origin main
   ```
3. Go to **Settings > Pages** in your GitHub repository:
   - Source: **Deploy from a branch**
   - Branch: `main` / `root`
   - Custom Domain: `litestep.us` (check **Enforce HTTPS** once DNS resolves)

---

## 🌐 DNS Configuration at Your Domain Registrar

To point `litestep.us` from your old forwarding rule directly to your GitHub Pages site, update your registrar's DNS records:

### 1. Apex Domain (`litestep.us`)
Add four **A** records pointing to GitHub's IP addresses:
```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

### 2. Subdomain (`www.litestep.us`)
Add a **CNAME** record:
```
Type:  CNAME
Host:  www
Value: <your-username>.github.io
```
