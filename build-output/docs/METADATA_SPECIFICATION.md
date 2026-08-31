# Bridge Group Solutions - Canonical Metadata Specification (BGS-047)

This document establishes the single source of truth for site-wide HTML `<head>` metadata, OpenGraph tags, Twitter cards, and canonical URL structure across all static pages on `testing.bridgegroupsolutions.com` and `www.bridgegroupsolutions.com`.

---

## 1. Canonical Schema Patterns

### A. Main Pages (`index.html`, `about.html`, `why-bgs.html`, `portfolio.html`, `gallery.html`, `contact.html`)
```html
<title>{Page Name} | Bridge Group Solutions</title>
<meta name="description" content="{Concise description under 160 characters describing the page.}">
<meta name="robots" content="all">
<meta property="og:locale" content="en">
<meta property="og:site_name" content="Bridge Group Solutions">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.bridgegroupsolutions.com/{page.html}">
<meta property="og:title" content="{Page Name} | Bridge Group Solutions">
<meta property="og:description" content="{Concise description under 160 characters.}">
<meta property="og:image" content="assets/logo.webp">
<meta property="og:image:alt" content="Bridge Group Solutions Logo">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{Page Name} | Bridge Group Solutions">
<meta name="twitter:description" content="{Concise description under 160 characters.}">
<meta name="twitter:image" content="assets/logo.webp">
<meta name="twitter:image:alt" content="Bridge Group Solutions Logo">
<link rel="canonical" href="{page.html}">
<link rel="home" href="index.html">
```

### B. Service Pages (`services/erp.html`, `services/web.html`, `services/app.html`, `services/crm.html`, `services/data.html`, `services/project.html`)
```html
<title>{Service Name} Solutions | Bridge Group Solutions</title>
<meta name="description" content="{Service specific capability summary under 160 characters.}">
<meta property="og:site_name" content="Bridge Group Solutions">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.bridgegroupsolutions.com/services/{service.html}">
<meta property="og:title" content="{Service Name} Solutions | Bridge Group Solutions">
<meta property="og:description" content="{Service specific capability summary.}">
<meta property="og:image" content="../assets/logo.webp">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{service.html}">
<link rel="home" href="../index.html">
```

### C. Legal Pages (`legal/privacy-policy.html`, `legal/terms-and-conditions.html`, `legal/cookie-policy.html`, `legal/disclaimer.html`)
```html
<title>{Document Name} | Bridge Group Solutions</title>
<meta name="description" content="{Legal document summary.}">
<meta property="og:title" content="{Document Name} | Bridge Group Solutions">
<meta property="og:url" content="https://www.bridgegroupsolutions.com/legal/{document.html}">
<link rel="canonical" href="{document.html}">
<link rel="home" href="../index.html">
```

---

## 2. Centralized Page Registry

Refer to [`metadata.json`](../metadata.json) for the machine-readable registry containing all page titles, descriptions, and canonical URLs.
