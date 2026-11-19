#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Horizon Legacy Safaris - Safari Packages Build Generator

Generates from scripts/safari_packages_dataset.py:
1. Website/safari-packages/index.html          (complete catalogue)
2. Website/safari-packages/<slug>/index.html   (11 detail pages)
"""

import os
import html

from safari_packages_dataset import SAFARI_PACKAGES, SAFARI_PACKAGE_GROUPS

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEBSITE_DIR = os.path.join(BASE_DIR, "Website")
PKG_ROOT = os.path.join(WEBSITE_DIR, "safari-packages")
SITE_URL = "https://horizonlegacysafaris.com"
WA_PHONE = "254762251566"

WHATSAPP_ICON = (
    '<svg class="icon-sm" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766 0-3.18-2.588-5.771-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.312.045-.698.077-1.134-.063-.275-.088-.63-.205-1.178-.444-2.336-1.019-3.844-3.394-3.96-3.551-.116-.157-.945-1.258-.945-2.4 0-1.141.597-1.701.81-1.932.213-.23.465-.288.621-.288.155 0 .31.002.446.009.144.007.336-.055.525.4.195.469.664 1.62.723 1.738.058.118.098.257.02.413-.078.156-.118.256-.234.394-.117.137-.246.307-.352.413-.118.118-.241.246-.104.482.138.236.611 1.008 1.309 1.63.898.799 1.656 1.047 1.892 1.164.236.117.373.103.51-.055.138-.157.588-.686.744-.922.157-.236.314-.196.529-.118.216.079 1.372.647 1.607.765.236.118.393.177.451.275.059.098.059.57-.085.975z"/></svg>'
)


def wa_link(text):
    from urllib.parse import quote
    return f"https://wa.me/{WA_PHONE}?text={quote(text, safe='')}"


# -----------------------------------------------------------------------------
# SHARED PAGE SHELL
# -----------------------------------------------------------------------------
def page_head(title, description, canonical, og_image, schema=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(description)}">
  <link rel="canonical" href="{canonical}">

  <link rel="icon" type="image/png" href="/assets/images/favicon.png">

  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(description)}">
  <meta property="og:image" content="{SITE_URL}{og_image}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:type" content="website">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="/style.css">
  <link rel="stylesheet" href="/assets/css/destinations.css">
{schema}
</head>
<body>"""


def top_bar():
    return """
  <div class="top-bar">
    <div class="container top-bar-content">
      <div class="top-bar-left">
        <span class="badge-pulse"></span>
        <span>Curated Bespoke Journeys Across East Africa &amp; Worldwide</span>
      </div>
      <div class="top-bar-right">
        <a href="tel:+254762251566" class="contact-link">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          +254 762 251 566
        </a>
        <span class="divider">|</span>
        <a href="mailto:holidays@horizonlegacysafaris.com" class="contact-link">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
          holidays@horizonlegacysafaris.com
        </a>
      </div>
    </div>
  </div>"""


def header(active="packages"):
    def link(href, label, key):
        if key == active:
            return f'<li><a href="{href}" class="nav-link" style="color: var(--color-gold-deep); font-weight: 700;" aria-current="page">{label}</a></li>'
        return f'<li><a href="{href}" class="nav-link">{label}</a></li>'

    nav = "\n          ".join([
        link("/", "Home", "home"),
        link("/", "Destinations", "destinations"),
        link("/safari-packages/", "Safari Packages", "packages"),
        link("/?category=Luxury+Getaways#discoveryGridAnchor", "Getaways", "getaways"),
        link("/#about", "About Us", "about"),
        link("/#contact", "FAQs &amp; Contact", "contact"),
    ])

    return f"""
  <header class="header" id="header">
    <div class="container header-container">
      <a href="/" class="logo-brand" aria-label="Horizon Legacy Safaris">
        <img src="/assets/images/logo.jpg" alt="Horizon Legacy - Luxury Safaris &amp; Bespoke Travel" class="header-logo-img">
      </a>

      <nav class="nav-menu" id="navMenu" aria-label="Main navigation">
        <ul class="nav-list">
          {nav}
        </ul>
      </nav>

      <div class="header-actions">
        <a href="{wa_link('Hello Horizon Legacy Safaris, I would like to ask about your safari packages.')}" target="_blank" rel="noopener noreferrer" class="btn btn-outline-header">
          {WHATSAPP_ICON}
          WhatsApp
        </a>
        <button class="btn btn-primary" onclick="openBookingModal('Safari Packages')">Book Now</button>
        <button class="mobile-toggle" id="mobileToggle" aria-label="Toggle Navigation">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>"""


def breadcrumbs(items):
    parts = []
    for i, (label, href) in enumerate(items):
        if i:
            parts.append('<li class="breadcrumb-separator">/</li>')
        if href:
            parts.append(f'<li class="breadcrumb-item"><a href="{href}">{label}</a></li>')
        else:
            parts.append(f'<li class="breadcrumb-item active" aria-current="page">{label}</li>')
    return f"""
  <nav class="breadcrumb-nav" aria-label="Breadcrumb">
    <div class="container">
      <ol class="breadcrumb-list">
        {"".join(parts)}
      </ol>
    </div>
  </nav>"""


def footer():
    return """
  <footer class="footer">
    <div class="container footer-container">
      <div class="footer-col brand-col">
        <div class="footer-logo">
          <img src="/assets/images/logo.jpg" alt="Horizon Legacy - Luxury Safaris &amp; Bespoke Travel" class="footer-logo-img">
        </div>
        <p class="footer-desc">
          Premier luxury safari and bespoke travel company in Kenya crafting tailor-made wilderness safaris, luxury hotel getaways, and romantic honeymoons across East Africa and worldwide.
        </p>
        <div class="footer-certs">
          <span class="cert-badge">Licensed by Tourism Regulatory Authority (TRA)</span>
          <span class="cert-badge">KATO Member Bonded</span>
        </div>
      </div>

      <div class="footer-col">
        <h4 class="footer-title">Safari Packages</h4>
        <ul class="footer-links">
          <li><a href="/safari-packages/amboseli-festive/">Amboseli - Festive Season</a></li>
          <li><a href="/safari-packages/maasai-mara-festive/">Maasai Mara - Festive Season</a></li>
          <li><a href="/safari-packages/samburu-festive/">Samburu - Festive Season</a></li>
          <li><a href="/safari-packages/tsavo-festive/">Tsavo - Festive Season</a></li>
          <li><a href="/safari-packages/uganda-gorilla-trekking/">Uganda Gorilla Trekking</a></li>
          <li><a href="/safari-packages/">All Safari Packages</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4 class="footer-title">Destinations</h4>
        <ul class="footer-links">
          <li><a href="/packages/destinations/maasai-mara/">Maasai Mara</a></li>
          <li><a href="/packages/destinations/amboseli/">Amboseli</a></li>
          <li><a href="/packages/destinations/samburu/">Samburu</a></li>
          <li><a href="/packages/destinations/tsavo-national-parks/">Tsavo</a></li>
          <li><a href="/packages/destinations/bwindi-impenetrable-forest/">Bwindi Forest</a></li>
          <li><a href="/">All Destinations</a></li>
        </ul>
      </div>

      <div class="footer-col contact-col">
        <h4 class="footer-title">Contact &amp; Reservations</h4>
        <p class="contact-item">
          <strong>Direct Line:</strong>
          <a href="tel:+254762251566">+254 762 251 566</a>
        </p>
        <p class="contact-item">
          <strong>WhatsApp Concierge:</strong>
          <a href="https://wa.me/254762251566" target="_blank" rel="noopener noreferrer">+254 762 251 566</a>
        </p>
        <p class="contact-item">
          <strong>Email:</strong>
          <a href="mailto:reservations@horizonlegacysafaris.com">reservations@horizonlegacysafaris.com</a>
        </p>
      </div>
    </div>

    <div class="footer-bottom">
      <div class="container footer-bottom-inner">
        <p>© 2026 Horizon Legacy Safaris Ltd. All rights reserved. Photography via Wikimedia Commons contributors.</p>
        <div class="payment-methods">
          <span>Payment accepted via:</span>
          <strong>Lipa Na M-PESA</strong> • <strong>Visa</strong> • <strong>Mastercard</strong> • <strong>Bank Transfer</strong>
        </div>
      </div>
    </div>
  </footer>"""


def floating_whatsapp(text, label="Chat with a Holiday Specialist"):
    return f"""
  <a href="{wa_link(text)}" target="_blank" rel="noopener noreferrer" class="floating-whatsapp" aria-label="{label}">
    <div class="whatsapp-pulse"></div>
    <div class="whatsapp-tooltip">{label}</div>
    <svg class="whatsapp-icon" viewBox="0 0 24 24" fill="currentColor">
      <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/>
    </svg>
  </a>"""


def booking_modal(context):
    return f"""
  <div class="modal-backdrop" id="bookingModal" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-header">
        <div>
          <h3 class="modal-title">Enquire About {html.escape(context)}</h3>
          <p class="modal-subtitle">Horizon Legacy Safaris • Instant WhatsApp Assistance</p>
        </div>
        <button class="modal-close" onclick="closeBookingModal()" aria-label="Close dialog">&times;</button>
      </div>

      <form class="modal-form" id="bookingForm" onsubmit="handleBookingSubmit(event)">
        <div class="form-grid">
          <div class="form-group">
            <label for="fullName">Full Name *</label>
            <input type="text" id="fullName" required placeholder="e.g. Dennis Mwangi">
          </div>
          <div class="form-group">
            <label for="phoneNumber">WhatsApp / Phone Number *</label>
            <input type="tel" id="phoneNumber" required placeholder="e.g. +254 700 000 000">
          </div>
          <div class="form-group">
            <label for="emailAddress">Email Address</label>
            <input type="email" id="emailAddress" placeholder="e.g. dennis@example.com">
          </div>
          <div class="form-group">
            <label for="travelDate">Preferred Travel Date *</label>
            <input type="date" id="travelDate" required>
          </div>
          <div class="form-group">
            <label for="roomCategory">Package / Accommodation *</label>
            <select id="roomCategory" required>
              <option value="{html.escape(context)} (Featured)" selected>{html.escape(context)}</option>
              <option value="Tailor-Made Custom Package">Tailor-Made Custom Package</option>
            </select>
          </div>
          <div class="form-group">
            <label for="transportPreference">Travel Style *</label>
            <select id="transportPreference" required>
              <option value="4x4 Safari Land Cruiser">4x4 Safari Land Cruiser + Guide</option>
              <option value="Scenic Flight / Fly-in Safari">Scenic Flight / Fly-in Package</option>
            </select>
          </div>
          <div class="form-group">
            <label for="adultsCount">Adults (12+ yrs)</label>
            <select id="adultsCount">
              <option value="1 Adult">1 Adult</option>
              <option value="2 Adults" selected>2 Adults</option>
              <option value="3 Adults">3 Adults</option>
              <option value="4 Adults">4 Adults</option>
              <option value="5+ Adults">5+ Adults (Group)</option>
            </select>
          </div>
          <div class="form-group">
            <label for="childrenCount">Children (Below 12 yrs)</label>
            <select id="childrenCount">
              <option value="0 Children" selected>0 Children</option>
              <option value="1 Child">1 Child</option>
              <option value="2 Children">2 Children</option>
              <option value="3+ Children">3+ Children</option>
            </select>
          </div>
        </div>

        <div class="form-group">
          <label for="specialRequests">Notes / Custom Preferences</label>
          <textarea id="specialRequests" rows="3" placeholder="e.g. Honeymoon setup, dietary requirements, or flight transfer requests..."></textarea>
        </div>

        <div class="modal-footer">
          <button type="submit" class="btn btn-whatsapp-submit">
            {WHATSAPP_ICON}
            <span>Send WhatsApp Inquiry</span>
          </button>
        </div>
      </form>
    </div>
  </div>

  <div class="lightbox-backdrop" id="imageLightbox" aria-hidden="true" onclick="closeLightbox(event)">
    <div class="lightbox-dialog">
      <button class="lightbox-close" onclick="closeLightbox(event)" aria-label="Close image lightbox">&times;</button>
      <div class="lightbox-image-wrap">
        <img src="" alt="Enlarged photo" id="lightboxImg">
      </div>
      <div class="lightbox-caption" id="lightboxCaption"></div>
    </div>
  </div>

  <script src="/script.js"></script>
</body>
</html>
"""


# -----------------------------------------------------------------------------
# CARDS
# -----------------------------------------------------------------------------
def package_href(pkg):
    """Packages that already sell from their own page link straight to it."""
    return pkg.get("detailPath") or f"/safari-packages/{pkg['slug']}/"


def package_card(pkg):
    return f"""
        <a class="dest-card pkg-card" href="{package_href(pkg)}">
          <div class="dest-card-media">
            <img src="{pkg['cardImage']}" alt="{html.escape(pkg['title'])}" class="dest-card-img" loading="lazy">
            <div class="dest-card-badges">
              <span class="dest-badge-region">{html.escape(pkg['country'])}</span>
              <span class="dest-badge-country">{html.escape(pkg['season'])}</span>
            </div>
          </div>
          <div class="dest-card-body">
            <h3 class="dest-card-title">{html.escape(pkg['title'])}</h3>
            <p class="dest-card-desc">{html.escape(pkg['cardSummary'])}</p>
            <div class="pkg-card-meta">
              <span class="pkg-meta-item">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                {html.escape(pkg['duration'])}
              </span>
              <span class="pkg-meta-item">{html.escape(pkg['priceNote'])}</span>
            </div>
            <div class="dest-card-footer">
              <span class="pkg-card-link">View Package</span>
              <span class="dest-btn-explore" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
              </span>
            </div>
          </div>
        </a>"""


# -----------------------------------------------------------------------------
# 1. CATALOGUE PAGE  /safari-packages/
# -----------------------------------------------------------------------------
def build_catalogue():
    groups_html = ""
    for group in SAFARI_PACKAGE_GROUPS:
        pkgs = [p for p in SAFARI_PACKAGES if p["group"] == group]
        if not pkgs:
            continue
        anchor = group.lower().replace(" ", "-")
        cards = "\n".join(package_card(p) for p in pkgs)
        groups_html += f"""
  <section class="pkg-group" id="{anchor}">
    <div class="container">
      <div class="pkg-group-head">
        <div>
          <span class="pkg-eyebrow">{html.escape(group.split()[0])}</span>
          <h2 class="dest-section-title">{html.escape(group)}</h2>
        </div>
        <span class="pkg-count">{len(pkgs)} package{'s' if len(pkgs) != 1 else ''}</span>
      </div>
      <div class="destinations-grid pkg-grid" id="{anchor}-grid">
{cards}
      </div>
    </div>
  </section>"""

    schema = f"""
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "Horizon Legacy Safaris - Safari Packages",
    "numberOfItems": {len(SAFARI_PACKAGES)},
    "itemListElement": [
{",".join([f'      {{"@type": "ListItem", "position": {i+1}, "name": "{p["title"]}", "url": "{SITE_URL}/safari-packages/{p["slug"]}/"}}' for i, p in enumerate(SAFARI_PACKAGES)])}
    ]
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type": "ListItem", "position": 1, "name": "Home", "item": "{SITE_URL}/"}},
      {{"@type": "ListItem", "position": 2, "name": "Safari Packages", "item": "{SITE_URL}/safari-packages/"}}
    ]
  }}
  </script>"""

    count = len(SAFARI_PACKAGES)
    page = page_head(
        f"Safari Packages | {count} Curated Kenya & Uganda Safaris & Getaways | Horizon Legacy",
        f"Browse all {count} Horizon Legacy safari packages and getaways across Kenya and Uganda, from Amboseli and the Maasai Mara to Samburu, Tsavo, Bwindi gorilla trekking and the Encore Hotel Nakuru getaway. Prices on request.",
        f"{SITE_URL}/safari-packages/",
        "/assets/images/destinations/hero-safari.jpg",
        schema,
    )
    page += top_bar() + header("packages")
    page += breadcrumbs([("Home", "/"), ("Safari Packages", None)])
    page += f"""
  <section class="destinations-hero pkg-hero">
    <div class="container">
      <div class="destinations-hero-content">
        <div class="hero-pill-badge">
          <span class="pulse-dot"></span>
          <span>{count} Curated Safari Packages</span>
        </div>
        <h1>Safari Packages</h1>
        <p class="hero-lead">
          Kenya and Uganda, planned end to end. Every package below is a private journey with a
          dedicated driver-guide, park fees arranged, and accommodation matched to your travel style.
          Prices are quoted on request for your dates and party.
        </p>
        <div class="hero-cta-row">
          <a href="{wa_link('Hello Horizon Legacy Safaris, I would like help choosing a safari package.')}" target="_blank" rel="noopener noreferrer" class="btn btn-hero-primary">Talk to a Specialist</a>
          <a href="#kenya-safaris-grid" class="btn btn-hero-ghost">Browse Kenya Safaris</a>
        </div>
        <p class="pkg-hero-note">Seasonal packages run in the festive and shoulder windows. Ask us for the current seasonal calendar — we publish no fixed departure dates.</p>
      </div>
    </div>
  </section>
{groups_html}

  <section class="pkg-cta-band">
    <div class="container">
      <div class="pkg-cta-inner">
        <div>
          <h2>Nothing here fits your dates?</h2>
          <p>Every itinerary on this page can be rebuilt around your calendar, your budget band and the lodges you prefer. Tell us the shape of the trip and we will price it properly.</p>
        </div>
        <div class="pkg-cta-actions">
          <a href="{wa_link('Hello Horizon Legacy Safaris, I would like a tailor-made safari quote.')}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp-solid">Inquire on WhatsApp</a>
          <button class="btn btn-primary" onclick="openBookingModal('Tailor-Made Safari')">Request a Quote</button>
        </div>
      </div>
    </div>
  </section>
"""
    page += footer()
    page += floating_whatsapp("Hello Horizon Legacy Safaris, I am browsing your safari packages and would like some help.")
    page += booking_modal("Safari Packages")

    os.makedirs(PKG_ROOT, exist_ok=True)
    with open(os.path.join(PKG_ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(page)
    print(f"Generated catalogue: {os.path.join(PKG_ROOT, 'index.html')} ({len(SAFARI_PACKAGES)} packages)")


# -----------------------------------------------------------------------------
# 2. DETAIL PAGES  /safari-packages/<slug>/
# -----------------------------------------------------------------------------
def build_detail(pkg):
    slug = pkg["slug"]

    highlights_html = "\n".join(
        f'<div class="highlight-box"><svg class="highlight-check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg><span class="highlight-text">{html.escape(h)}</span></div>'
        for h in pkg["highlights"]
    )

    itinerary_html = "\n".join([
        f"""
        <li class="pkg-step">
          <div class="pkg-step-marker"><span>{html.escape(step['day'])}</span></div>
          <div class="pkg-step-body">
            <h3 class="pkg-step-title">{html.escape(step['title'])}</h3>
            <p class="pkg-step-text">{html.escape(step['detail'])}</p>
          </div>
        </li>"""
        for step in pkg["itinerary"]
    ])

    accomm_html = "\n".join(
        f'<div class="accomm-card"><span class="accomm-tier-badge">{html.escape(a["tier"])}</span><p class="accomm-desc">{html.escape(a["description"])}</p></div>'
        for a in pkg["accommodation"]
    )

    inclusions_html = "\n".join(
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg><span>{html.escape(i)}</span></li>'
        for i in pkg["inclusions"]
    )
    exclusions_html = "\n".join(
        f'<li class="is-excluded"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span>{html.escape(e)}</span></li>'
        for e in pkg["exclusions"]
    )

    gallery_html = "\n".join(
        f'<div class="dest-gallery-item" onclick="openLightbox(this)"><img src="{html.escape(g["url"])}" alt="{html.escape(g.get("caption", pkg["title"]))}" loading="lazy"><div class="gallery-caption-overlay">{html.escape(g.get("caption", pkg["title"]))}</div></div>'
        for g in pkg["gallery"]
    )

    # Two sibling packages from the same group, then anything else.
    siblings = [p for p in SAFARI_PACKAGES if p["group"] == pkg["group"] and p["slug"] != slug][:2]
    if len(siblings) < 2:
        siblings += [p for p in SAFARI_PACKAGES if p["slug"] != slug and p not in siblings][: 2 - len(siblings)]
    related_html = "\n".join(package_card(p) for p in siblings)

    wa_text = f"Hello Horizon Legacy Safaris, I am interested in the {pkg['title']} package and would like a quotation."

    schema = f"""
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "TouristTrip",
    "name": "{pkg['title']}",
    "description": "{pkg['summary'].replace(chr(34), "'")[:300]}",
    "image": "{SITE_URL}{pkg['heroImage']}",
    "itinerary": {{
      "@type": "ItemList",
      "numberOfItems": {len(pkg['itinerary'])}
    }},
    "provider": {{"@type": "TravelAgency", "name": "Horizon Legacy Safaris", "url": "{SITE_URL}/"}}
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type": "ListItem", "position": 1, "name": "Home", "item": "{SITE_URL}/"}},
      {{"@type": "ListItem", "position": 2, "name": "Safari Packages", "item": "{SITE_URL}/safari-packages/"}},
      {{"@type": "ListItem", "position": 3, "name": "{pkg['title']}", "item": "{SITE_URL}/safari-packages/{slug}/"}}
    ]
  }}
  </script>"""

    page = page_head(
        f"{pkg['title']} | Horizon Legacy Safaris",
        pkg["summary"][:250],
        f"{SITE_URL}/safari-packages/{slug}/",
        pkg["heroImage"],
        schema,
    )
    page += top_bar() + header("packages")
    page += breadcrumbs([("Home", "/"), ("Safari Packages", "/safari-packages/"), (html.escape(pkg["shortTitle"]), None)])
    page += f"""
  <section class="destination-detail-hero" style="background-image: url('{pkg['heroImage']}');">
    <div class="container">
      <div class="detail-hero-content">
        <div class="detail-hero-badges">
          <span class="detail-region-tag">{html.escape(pkg['group'])}</span>
          <span class="detail-country-tag">{html.escape(pkg['country'])}</span>
          <span class="dest-category-pill">{html.escape(pkg['season'])}</span>
        </div>
        <h1 class="detail-hero-title">{html.escape(pkg['title'])}</h1>
        <p class="detail-hero-tagline">{html.escape(pkg['tagline'])}</p>
        <div class="detail-hero-actions">
          <a href="{wa_link(wa_text)}" target="_blank" rel="noopener noreferrer" class="btn btn-hero-whatsapp">
            <svg class="icon-whatsapp" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
            <span>Inquire on WhatsApp</span>
          </a>
          <button class="btn btn-hero-primary" onclick="openBookingModal('{html.escape(pkg['title'])}')">
            <span>Request a Quotation</span>
            <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </button>
        </div>
      </div>
    </div>
  </section>

  <div class="pkg-back-bar">
    <div class="container pkg-back-inner">
      <a href="/safari-packages/" class="pkg-back-link">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg>
        Back to Safari Packages
      </a>
      <span class="pkg-back-count">All {len(SAFARI_PACKAGES)} packages</span>
    </div>
  </div>

  <div class="quick-facts-bar">
    <div class="container">
      <div class="quick-facts-grid">
        <div class="quick-fact-item">
          <div class="quick-fact-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div>
          <div><div class="quick-fact-label">Duration</div><div class="quick-fact-val">{html.escape(pkg['duration'])}</div></div>
        </div>
        <div class="quick-fact-item">
          <div class="quick-fact-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></div>
          <div><div class="quick-fact-label">Starts From</div><div class="quick-fact-val">{html.escape(pkg['startsFrom'])}</div></div>
        </div>
        <div class="quick-fact-item">
          <div class="quick-fact-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg></div>
          <div><div class="quick-fact-label">Season</div><div class="quick-fact-val">{html.escape(pkg['season'])}</div></div>
        </div>
        <div class="quick-fact-item">
          <div class="quick-fact-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg></div>
          <div><div class="quick-fact-label">Travel Style</div><div class="quick-fact-val">{html.escape(pkg['travelStyle'])}</div></div>
        </div>
        <div class="quick-fact-item">
          <div class="quick-fact-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg></div>
          <div><div class="quick-fact-label">Rate</div><div class="quick-fact-val">{html.escape(pkg['priceNote'])}</div></div>
        </div>
      </div>
    </div>
  </div>

  <section class="dest-content-section" id="overview">
    <div class="container">
      <div class="pkg-overview-grid">
        <div>
          <span class="pkg-eyebrow">Package Overview</span>
          <h2 class="dest-section-title">About this safari</h2>
          <p class="pkg-lead">{html.escape(pkg['summary'])}</p>
          <p class="pkg-note">Best for: {html.escape(pkg['bestFor'])}.</p>
        </div>
        <div class="pkg-highlight-panel">
          <h3 class="pkg-panel-title">Trip Highlights</h3>
          <div class="highlights-card-grid pkg-highlight-grid">
{highlights_html}
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="dest-content-section" id="itinerary" style="background-color: #ffffff;">
    <div class="container">
      <span class="pkg-eyebrow">Day by Day</span>
      <h2 class="dest-section-title">Your Itinerary</h2>
      <p class="dest-section-subtitle">A working outline. Every day can be re-paced, extended or swapped for a lodge you prefer.</p>
      <ol class="pkg-timeline">
{itinerary_html}
      </ol>
    </div>
  </section>

  <section class="dest-content-section" id="accommodation">
    <div class="container">
      <span class="pkg-eyebrow">Where You Stay</span>
      <h2 class="dest-section-title">Accommodation Options</h2>
      <p class="dest-section-subtitle">We match the property to your budget band and confirm current availability at the time of quotation. Property names are shared with your quote.</p>
      <div class="accomm-grid">
{accomm_html}
      </div>
    </div>
  </section>

  <section class="dest-content-section" id="inclusions" style="background-color: #ffffff;">
    <div class="container">
      <span class="pkg-eyebrow">The Detail</span>
      <h2 class="dest-section-title">What Is Included</h2>
      <div class="pkg-inc-exc">
        <div class="pkg-list-card">
          <h3 class="pkg-list-title is-included">Included</h3>
          <ul class="pkg-list">
{inclusions_html}
          </ul>
        </div>
        <div class="pkg-list-card">
          <h3 class="pkg-list-title is-excluded">Not Included</h3>
          <ul class="pkg-list">
{exclusions_html}
          </ul>
        </div>
      </div>
      <p class="pkg-note pkg-price-note">Prices are not published on this page. Rates depend on your dates, party size, season and accommodation band, and are quoted in writing before any booking.</p>
    </div>
  </section>

  <section class="dest-content-section" id="gallery">
    <div class="container">
      <span class="pkg-eyebrow">Visual Journey</span>
      <h2 class="dest-section-title">Photography</h2>
      <p class="dest-section-subtitle">Click any image to enlarge.</p>
      <div class="dest-gallery-grid">
{gallery_html}
      </div>
    </div>
  </section>

  <section class="pkg-cta-band">
    <div class="container">
      <div class="pkg-cta-inner">
        <div>
          <h2>Enquire about {html.escape(pkg['shortTitle'])}</h2>
          <p>Tell us your dates and party size and we will send a written quotation with the lodges we recommend and the season's availability.</p>
        </div>
        <div class="pkg-cta-actions">
          <a href="{wa_link(wa_text)}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp-solid">WhatsApp Enquiry</a>
          <button class="btn btn-primary" onclick="openBookingModal('{html.escape(pkg['title'])}')">Request a Quotation</button>
        </div>
      </div>
    </div>
  </section>

  <section class="dest-content-section" style="background-color: #ffffff;">
    <div class="container">
      <div class="pkg-group-head">
        <div>
          <span class="pkg-eyebrow">Keep Exploring</span>
          <h2 class="dest-section-title" style="margin-bottom: 0;">Other Safari Packages</h2>
        </div>
        <a href="/safari-packages/" class="btn btn-outline" style="font-size: 0.875rem;">All {len(SAFARI_PACKAGES)} Packages &rarr;</a>
      </div>
      <div class="destinations-grid pkg-grid" style="margin-top: 24px;">
{related_html}
      </div>
    </div>
  </section>
"""
    page += footer()
    page += floating_whatsapp(wa_text)
    page += booking_modal(pkg["title"])

    out_dir = os.path.join(PKG_ROOT, slug)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(page)
    return os.path.join(out_dir, "index.html")


def main():
    build_catalogue()
    built = 0
    for pkg in SAFARI_PACKAGES:
        if pkg.get("detailPath"):
            print(f"Linked existing page for {pkg['slug']}: {pkg['detailPath']}")
            continue
        print("Generated", build_detail(pkg))
        built += 1
    print(f"SAFARI PACKAGES BUILD COMPLETE — {len(SAFARI_PACKAGES)} listed, {built} detail pages + catalogue")


if __name__ == "__main__":
    main()
