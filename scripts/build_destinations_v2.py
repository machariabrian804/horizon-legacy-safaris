#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Horizon Legacy Safaris - Destination System Build Generator
Generates:
1. Website/assets/js/destinations-data.js (Client-side database)
2. Website/packages/destinations/<slug>/index.html (52 dedicated detail pages)
3. Website/sitemap.xml (Comprehensive XML sitemap)
"""

import os
import json
import html
from destinations_dataset import DESTINATIONS, PACKAGES
from safari_packages_dataset import SAFARI_PACKAGES

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEBSITE_DIR = os.path.join(BASE_DIR, 'Website')
DEST_DIR = os.path.join(WEBSITE_DIR, 'packages', 'destinations')

os.makedirs(DEST_DIR, exist_ok=True)

# -----------------------------------------------------------------------------
# SHARED HELPERS
# -----------------------------------------------------------------------------
SITE_URL = "https://horizonlegacysafaris.com"


def abs_url(path):
    """Turn a root-relative asset path into an absolute URL for OG/schema."""
    if path.startswith("http"):
        return path
    return SITE_URL + path


# -----------------------------------------------------------------------------
# 1. GENERATE JAVASCRIPT DATA FILE
# -----------------------------------------------------------------------------
def generate_js_data():
    js_path = os.path.join(WEBSITE_DIR, 'assets', 'js', 'destinations-data.js')
    os.makedirs(os.path.dirname(js_path), exist_ok=True)
    
    content = f"""/**
 * HORIZON LEGACY SAFARIS - CENTRAL DESTINATIONS & PACKAGES DATABASE
 * Auto-generated single source of truth for 52 global destinations and tour packages.
 */

window.DESTINATIONS_DATA = {json.dumps(DESTINATIONS, indent=2, ensure_ascii=False)};

window.PACKAGES_DATA = {json.dumps(PACKAGES, indent=2, ensure_ascii=False)};

window.SAFARI_PACKAGES_DATA = {json.dumps(SAFARI_PACKAGES, indent=2, ensure_ascii=False)};

window.getDestinationBySlug = function(slug) {{
  if (!window.DESTINATIONS_DATA) return null;
  return window.DESTINATIONS_DATA.find(function(d) {{
    return d.slug === slug || d.id === slug;
  }}) || null;
}};

window.getPackagesForDestination = function(destId) {{
  if (!window.PACKAGES_DATA) return [];
  return window.PACKAGES_DATA.filter(function(pkg) {{
    return pkg.destinationId === destId;
  }});
}};
"""
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated {js_path} ({len(DESTINATIONS)} destinations)")


# -----------------------------------------------------------------------------
# 2. GENERATE ALL-DESTINATIONS DISCOVERY LANDING PAGE
# -----------------------------------------------------------------------------
def generate_discovery_index():
    """The /packages/destinations/ landing that lists every destination overview."""

    destination_cards = []
    for dest in DESTINATIONS:
        destination_cards.append(
            f'<article class="dest-card">'
            f'<div class="dest-card-media">'
            f'<img src="{html.escape(dest["cardImage"])}" alt="{html.escape(dest["name"])}" class="dest-card-img" loading="lazy">'
            f'<div class="dest-card-badges">'
            f'<span class="dest-badge-region">{html.escape(dest["region"])}</span>'
            f'<span class="dest-badge-country">{html.escape(dest["country"])}</span>'
            f'</div>'
            f'</div>'
            f'<div class="dest-card-body">'
            f'<h3 class="dest-card-title">{html.escape(dest["name"])}</h3>'
            f'<p class="dest-card-desc">{html.escape(dest.get("shortDescription", ""))}</p>'
            f'<div class="dest-card-footer">'
            f'<a href="packages/destinations/{dest["slug"]}/" class="dest-btn-explore"><span>Explore Destination</span> &rarr;</a>'
            f'</div>'
            f'</div>'
            f'</article>'
        )

    cards_html = "".join(destination_cards)
    page = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>All Destinations | Horizon Legacy Safaris</title>
  <meta name="description" content="Explore 52 dreams: luxury safaris, private tours and bespoke travel across Kenya, East Africa and worldwide with Horizon Legacy Safaris.">
  <link rel="canonical" href="https://horizonlegacysafaris.com/packages/destinations/">

  <link rel="icon" type="image/png" href="/assets/images/favicon.png">

  <meta property="og:title" content="All Destinations | Horizon Legacy Safaris">
  <meta property="og:description" content="Explore 52 dreams: luxury safaris, private tours and bespoke travel across Kenya, East Africa and worldwide with Horizon Legacy Safaris.">
  <meta property="og:image" content="https://horizonlegacysafaris.com/assets/images/logo.jpg">
  <meta property="og:url" content="https://horizonlegacysafaris.com/packages/destinations/">
  <meta property="og:type" content="website">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,600;1,400&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="/style.css">
  <link rel="stylesheet" href="/assets/css/destinations.css">
</head>
<body>

  <div class="top-bar">
    <div class="container top-bar-content">
      <div class="top-bar-left">
        <span class="badge-pulse"></span>
        <span>Curated Bespoke Journeys Across East Africa &amp; Worldwide</span>
      </div>
      <div class="top-bar-right">
        <a href="https://wa.me/254762251566?text=Hello%20Horizon%20Legacy%20Safaris,%20I%20am%20exploring%20our%20destinations%20and%20would%20like%20to%20plan%20a%20journey." target="_blank" rel="noopener noreferrer" class="contact-link">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 1 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          +254 762 251 566
        </a>
        <span class="divider">|</span>
        <a href="mailto:holidays@horizonlegacysafaris.com" class="contact-link">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
          holidays@horizonlegacysafaris.com
        </a>
      </div>
    </div>
  </div>

  <header class="header" id="header">
    <div class="container header-container">
      <a href="/" class="logo-brand" aria-label="Horizon Legacy Safaris">
        <img src="/assets/images/logo.jpg" alt="Horizon Legacy - Luxury Safaris &amp; Bespoke Travel" class="header-logo-img">
      </a>

      <nav class="nav-menu" id="navMenu">
        <ul class="nav-list">
          <li><a href="/" class="nav-link">Home</a></li>
          <li><a href="/packages/destinations/" class="nav-link active" style="color: var(--color-primary); font-weight: 700;" aria-current="page">Destinations</a></li>
          <li><a href="/safari-packages/" class="nav-link">Safari Packages</a></li>
          <li><a href="/safari-packages/#kenya-getaways" class="nav-link">Getaways</a></li>
          <li><a href="/#about" class="nav-link">About Us</a></li>
          <li><a href="/#contact" class="nav-link">FAQs &amp; Contact</a></li>
        </ul>
      </nav>

      <div class="header-actions">
        <a href="https://wa.me/254762251566?text=Hello%20Horizon%20Legacy%20Safaris,%20I%20am%20exploring%20our%20destinations%20and%20would%20like%20to%20plan%20a%20journey." target="_blank" rel="noopener noreferrer" class="btn btn-outline-header">
          <svg class="icon-sm" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766 0-3.18-2.588-5.771-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.312.045-.698.077-1.134-.063-.275-.088-.63-.205-1.178-.444-2.336-1.019-3.844-3.394-3.96-3.551-.116-.157-.945-1.258-.945-2.4 0-1.141.597-1.701.81-1.932.213-.23.465-.288.621-.288.155 0 .31.002.446.009.144.007.336-.055.525.4.195.469.664 1.62.723 1.738.058.118.098.257.02.413-.078.156-.118.256-.234.394-.117.137-.246.307-.352.413-.118.118-.241.246-.104.482.138.236.611 1.008 1.309 1.63.898.799 1.656 1.047 1.892 1.164.236.117.373.103.51-.055.138-.157.588-.686.744-.922.157-.236.314-.196.529-.118.216.079 1.372.647 1.607.765.236.118.393.177.451.275.059.098.059.57-.085.975z"/></svg>
          WhatsApp
        </a>
        <button class="btn btn-primary" onclick="openBookingModal('Tailor-Made Custom Journey')">Book Now</button>
        <button class="mobile-toggle" id="mobileToggle" aria-label="Toggle Navigation">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>

  <section class="destinations-hero pkg-hero">
    <div class="container">
      <div class="destinations-hero-content">
        <div class="hero-pill-badge">
          <span class="pulse-dot"></span>
          <span>52 Global Destinations</span>
        </div>
        <h1>All Destinations</h1>
        <p class="hero-lead">Discover extraordinary places to explore with Horizon Legacy Safaris — from the great parks of East Africa to the wildlife and coast of worldwide. Search, filter and book a journey that fits you.</p>
        <div class="hero-cta-row">
          <a href="#destination-grid" class="btn btn-hero-primary">Browse Destinations</a>
          <a href="#about" class="btn btn-hero-ghost">Tell Us About Your Trip</a>
        </div>
      </div>
    </div>
  </section>

  <section id="destination-grid">
    <div class="container">
      <div class="pkg-group-head">
        <div>
          <span class="pkg-eyebrow">Discover</span>
          <h2 class="dest-section-title">Every Destination We Cover</h2>
        </div>
        <span class="pkg-count">{len(DESTINATIONS)} destinations</span>
      </div>
      <div class="destinations-grid pkg-grid" id="destination-grid">
{cards_html}
      </div>
    </div>
  </section>

  <section class="pkg-cta-band">
    <div class="container">
      <div class="pkg-cta-inner">
        <div>
          <h2>Looking for a journey we have not mapped out yet?</h2>
          <p>Tell us where you want to go and what you want to do, and we will build a bespoke itinerary around your dates.</p>
        </div>
        <div class="pkg-cta-actions">
          <a href="https://wa.me/254762251566?text=Hello%20Horizon%20Legacy%20Safaris,%20I%20would%20like%20a%20custom%20itinerary%20for%20a%20destination%20of%20my%20choice." target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp-solid">Inquire on WhatsApp</a>
          <button class="btn btn-primary" onclick="openBookingModal('Tailor-Made Custom Journey')">Request a Custom Quote</button>
        </div>
      </div>
    </div>
  </section>

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
        <h4 class="footer-title">Quick Links</h4>
        <ul class="footer-links">
          <li><a href="/safari-packages/">Safari Packages</a></li>
          <li><a href="/safari-packages/#kenya-getaways">Kenya Getaways</a></li>
          <li><a href="/packages/encore-hotel-nakuru/">Encore Hotel Nakuru Getaway</a></li>
          <li><a href="/#about">About Us</a></li>
          <li><a href="/#contact">Contact &amp; Reservations</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4 class="footer-title">Destinations</h4>
        <ul class="footer-links">
          <li><a href="packages/destinations/maasai-mara/">Maasai Mara National Reserve</a></li>
          <li><a href="packages/destinations/amboseli/">Amboseli National Park</a></li>
          <li><a href="packages/destinations/lake-nakuru/">Lake Nakuru National Park</a></li>
          <li><a href="packages/destinations/serengeti/">Serengeti National Park</a></li>
          <li><a href="/#contact">All Destinations</a></li>
        </ul>
      </div>
      <div class="footer-col contact-col">
        <h4 class="footer-title">Contact &amp; Reservations</h4>
        <p class="contact-item"><strong>Direct Line:</strong><a href="tel:+254762251566"> +254 762 251 566</a></p>
        <p class="contact-item"><strong>WhatsApp Concierge:</strong><a href="https://wa.me/254762251566" target="_blank" rel="noopener noreferrer"> +254 762 251 566</a></p>
        <p class="contact-item"><strong>Email:</strong><a href="mailto:reservations@horizonlegacysafaris.com"> reservations@horizonlegacysafaris.com</a></p>
      </div>
    </div>
  </footer>

  <script src="/script.js"></script>
</body>
</html>
"""
    with open(os.path.join(DEST_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(page)
    print(f"Generated All Destinations discovery landing: {os.path.join(DEST_DIR, 'index.html')} ({len(DESTINATIONS)} destinations)")



def generate_destination_detail_pages():
    for dest in DESTINATIONS:
        dest_slug = dest['slug']
        dest_dir = os.path.join(DEST_DIR, dest_slug)
        os.makedirs(dest_dir, exist_ok=True)
        page_path = os.path.join(dest_dir, 'index.html')

        # Highlights HTML
        highlights_html = "\n".join([
            f'          <div class="highlight-box">'
            f'<svg class="highlight-check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>'
            f'<span class="highlight-text">{html.escape(h)}</span></div>'
            for h in dest.get('highlights', [])
        ])

        # Activities HTML
        activities_html = "\n".join([
            f'          <div class="activity-tag-card">'
            f'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>'
            f'<span>{html.escape(a)}</span></div>'
            for a in dest.get('activities', [])
        ])

        # Gallery HTML
        gallery_items = dest.get('gallery', [])
        gallery_html = "\n".join([
            f'          <div class="dest-gallery-item" onclick="openLightbox(this)">'
            f'<img src="{html.escape(img["url"])}" alt="{html.escape(img.get("caption", dest["name"]))}" loading="lazy">'
            f'<div class="gallery-caption-overlay">{html.escape(img.get("caption", dest["name"]))}</div></div>'
            for img in gallery_items
        ])

        # Accommodations HTML
        accomm_html = "\n".join([
            f'          <div class="accomm-card">'
            f'<span class="accomm-tier-badge">{html.escape(acc.get("tier", "Luxury Stay"))}</span>'
            f'<h4 class="accomm-name">{html.escape(acc["name"])}</h4>'
            f'<span class="accomm-location"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg> {html.escape(acc.get("location", dest["name"]))}</span>'
            f'<p class="accomm-desc">{html.escape(acc.get("description", ""))}</p>'
            f'<a href="https://wa.me/254762251566?text=Hello%20Horizon%20Legacy,%20I%20would%20like%20to%20book%20a%20stay%20at%20{html.escape(acc["name"])}%20in%20{html.escape(dest["name"])}." target="_blank" class="btn btn-sm btn-outline" style="align-self: flex-start; margin-top: auto;">Inquire About Stay</a>'
            f'</div>'
            for acc in dest.get('accommodations', [])
        ])

        # Packages HTML
        packages = [pkg for pkg in PACKAGES if pkg['id'] in dest.get('packageIds', []) or pkg['destinationId'] == dest['id']]
        if packages:
            packages_cards_html = "\n".join([
                f'          <div class="package-card">'
                f'<img src="{html.escape(pkg["image"])}" alt="{html.escape(pkg["title"])}" class="package-card-img" loading="lazy">'
                f'<div class="package-card-body">'
                f'<span class="package-badge">{html.escape(pkg.get("badge", "Featured Package"))}</span>'
                f'<h3 class="package-title">{html.escape(pkg["title"])}</h3>'
                f'<p style="color: var(--color-text-muted); font-size: 0.9375rem; line-height: 1.5; margin-bottom: 12px;">{html.escape(pkg.get("description", ""))}</p>'
                f'<div class="package-price-wrap">'
                f'<div><span style="font-size: 0.75rem; color: var(--color-text-light); text-transform: uppercase;">Duration</span><br><strong>{html.escape(pkg.get("duration", "2D/1N"))}</strong></div>'
                f'<div style="text-align: right;"><span style="font-size: 0.75rem; color: var(--color-text-light); text-transform: uppercase;">Starting Rate</span><br><span class="package-price-val">{html.escape(pkg.get("price", ""))}</span></div>'
                f'</div>'
                f'<div style="display: flex; gap: 10px; margin-top: auto;">'
                f'<a href="{html.escape(pkg.get("url", "/?category=Wildlife+Safaris#discoveryGridAnchor"))}" class="btn btn-primary" style="flex: 1; text-align: center;">View Package Details</a>'
                f'<a href="https://wa.me/254762251566?text=Hello%20Horizon%20Legacy,%20I%20am%20interested%20in%20booking%20the%20{html.escape(pkg["title"])}." target="_blank" class="btn btn-whatsapp-solid" style="padding: 10px 14px;" aria-label="Inquire on WhatsApp">'
                f'<svg class="icon-sm" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>'
                f'</a>'
                f'</div>'
                f'</div>'
                f'</div>'
                for pkg in packages
            ])
            packages_html = f"""
            <div class="package-cards-grid">
              {packages_cards_html}
            </div>
            """
        else:
            packages_html = f"""
            <div class="bespoke-inquiry-box" style="margin-top: 0;">
              <div class="bespoke-text">
                <span style="font-size: 0.8125rem; font-weight: 700; color: #fce79f; text-transform: uppercase; letter-spacing: 0.08em; display: inline-block; margin-bottom: 6px;">Bespoke & Tailor-Made Departure</span>
                <h3>Custom Private Tour & Safari Planning for {html.escape(dest['name'])}</h3>
                <p>
                  While we do not have a fixed group departure scheduled on the calendar for this exact destination right now, our safari and holiday consultants specialize in creating fully customized private itineraries for couples, families, and corporate groups.
                </p>
              </div>
              <div class="bespoke-btns">
                <a href="https://wa.me/254762251566?text=Hello%20Horizon%20Legacy%20Safaris,%20I%20would%20like%20a%20custom%20itinerary%20quote%20for%20{html.escape(dest['name'])}." target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp-solid">
                  Inquire on WhatsApp
                </a>
                <button class="btn btn-primary" onclick="openBookingModal('{html.escape(dest['name'])}')">
                  Request Custom Quote
                </button>
              </div>
            </div>
            """

        # Related Destinations HTML
        related_destinations = [d for d in DESTINATIONS if d['slug'] in dest.get('relatedSlugs', [])][:3]
        if not related_destinations:
            related_destinations = [d for d in DESTINATIONS if d['slug'] != dest['slug'] and d['region'] == dest['region']][:3]

        related_html = "\n".join([
            f'          <article class="dest-card">'
            f'<div class="dest-card-media">'
            f'<img src="{html.escape(rd.get("cardImage", rd["heroImage"]))}" alt="{html.escape(rd["name"])}" class="dest-card-img" loading="lazy">'
            f'<div class="dest-card-badges">'
            f'<span class="dest-badge-region">{html.escape(rd["region"])}</span>'
            f'<span class="dest-badge-country">{html.escape(rd["country"])}</span>'
            f'</div>'
            f'</div>'
            f'<div class="dest-card-body">'
            f'<h3 class="dest-card-title">{html.escape(rd["name"])}</h3>'
            f'<p class="dest-card-desc">{html.escape(rd.get("shortDescription", ""))}</p>'
            f'<div class="dest-card-footer">'
            f'<a href="../{rd["slug"]}/" class="dest-btn-explore"><span>Explore Destination</span> &rarr;</a>'
            f'</div>'
            f'</div>'
            f'</article>'
            for rd in related_destinations
        ])

        # FAQs HTML
        faqs_items = dest.get('faqs', [
            {"q": f"How do I book a private holiday or safari to {dest['name']}?", "a": f"You can book directly by clicking 'Book Now' on this page, or chatting directly with our holiday concierge on WhatsApp (+254 762251566). We arrange accommodations, transport, park fees, and private guides."},
            {"q": f"What is the best time of year to visit {dest['name']}?", "a": dest.get('bestTimeToVisit', 'Please check our Best Time to Visit section above for detailed seasonal recommendations.')}
        ])
        faqs_html = "\n".join([
            f'        <div class="faq-item">'
            f'<button class="faq-question" aria-expanded="false">'
            f'<span>{html.escape(faq["q"])}</span>'
            f'<span class="faq-icon">+</span>'
            f'</button>'
            f'<div class="faq-answer"><p>{html.escape(faq["a"])}</p></div>'
            f'</div>'
            for faq in faqs_items
        ])

        # Quick Facts
        qf = dest.get('quickFacts', {})
        best_time = qf.get('bestTime', dest.get('bestTimeToVisit', 'All Year Round'))
        ideal_dur = qf.get('idealDuration', '3 – 5 Days')
        lang = qf.get('language', 'English')
        curr = qf.get('currency', 'Local Currency & USD')
        visa = qf.get('visa', 'Tourist Visa / eVisa')
        climate = qf.get('climate', 'Pleasant')

        # Categories list
        categories_badges = " ".join([
            f'<span class="dest-category-pill">{html.escape(c)}</span>'
            for c in dest.get('categories', [])
        ])

        # JSON-LD Schema
        schema_json = json.dumps({
            "@context": "https://schema.org",
            "@type": "TouristDestination",
            "name": dest['name'],
            "description": dest['shortDescription'],
            "image": abs_url(dest['heroImage']),
            "touristType": dest.get('categories', []),
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": dest['coordinates'][0],
                "longitude": dest['coordinates'][1]
            },
            "containedInPlace": {
                "@type": "Country",
                "name": dest['country']
            }
        }, ensure_ascii=False)

        breadcrumb_schema = json.dumps({
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://horizonlegacysafaris.com/"},
                {"@type": "ListItem", "position": 2, "name": "Destinations", "item": "https://horizonlegacysafaris.com/packages/destinations/"},
                {"@type": "ListItem", "position": 3, "name": dest['name'], "item": f"https://horizonlegacysafaris.com/packages/destinations/{dest_slug}/"}
            ]
        }, ensure_ascii=False)

        detail_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(dest['name'])}, {html.escape(dest['country'])} | Horizon Legacy Safaris</title>
  <meta name="description" content="{html.escape(dest['shortDescription'])} Plan luxury travel, bespoke tours, and safari getaways with Horizon Legacy Safaris.">
  <meta name="keywords" content="{html.escape(dest['name'])}, {html.escape(dest['country'])}, {html.escape(dest['region'])}, {', '.join(dest.get('categories', []))}, Horizon Legacy Safaris">
  <link rel="canonical" href="https://horizonlegacysafaris.com/packages/destinations/{dest_slug}/">

  <!-- Favicon -->
  <link rel="icon" type="image/png" href="../../../assets/images/favicon.png">

  <!-- Open Graph -->
  <meta property="og:title" content="{html.escape(dest['name'])} Travel Guide | Horizon Legacy Safaris">
  <meta property="og:description" content="{html.escape(dest['shortDescription'])}">
  <meta property="og:image" content="{html.escape(abs_url(dest['heroImage']))}">
  <meta property="og:url" content="https://horizonlegacysafaris.com/packages/destinations/{dest_slug}/">
  <meta property="og:type" content="article">

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&display=swap" rel="stylesheet">

  <!-- Core & Destinations Stylesheets -->
  <link rel="stylesheet" href="../../../style.css">
  <link rel="stylesheet" href="../../../assets/css/destinations.css">

  <!-- Structured Data Schema -->
  <script type="application/ld+json">
    {schema_json}
  </script>
  <script type="application/ld+json">
    {breadcrumb_schema}
  </script>
</head>
<body>

  <!-- Top Announcement Bar -->
  <div class="top-bar">
    <div class="container top-bar-content">
      <div class="top-bar-left">
        <span class="badge-pulse"></span>
        <span>Curated Bespoke Journeys Across East Africa & Worldwide</span>
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
  </div>

  <!-- Header / Navigation -->
  <header class="header" id="header">
    <div class="container header-container">
      <a href="../../../index.html" class="logo-brand" aria-label="Horizon Legacy Safaris">
        <img src="../../../assets/images/logo.jpg" alt="Horizon Legacy - Luxury Safaris & Bespoke Travel" class="header-logo-img">
      </a>

      <nav class="nav-menu" id="navMenu">
        <ul class="nav-list">
          <li><a href="../../../index.html" class="nav-link">Home</a></li>
          <li><a href="/" class="nav-link" style="color: var(--color-primary); font-weight: 700;">Destinations</a></li>
          <li><a href="/safari-packages/" class="nav-link">Safari Packages</a></li>
          <li><a href="/safari-packages/#kenya-getaways" class="nav-link">Getaways</a></li>
          <li><a href="/#about" class="nav-link">About Us</a></li>
          <li><a href="/#contact" class="nav-link">FAQs & Contact</a></li>
        </ul>
      </nav>

      <div class="header-actions">
        <a href="https://wa.me/254762251566?text=Hello%20Horizon%20Legacy%20Safaris,%20I%20am%20interested%20in%20traveling%20to%20{html.escape(dest['name'])}." target="_blank" rel="noopener noreferrer" class="btn btn-outline-header">
          <svg class="icon-sm" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766 0-3.18-2.588-5.771-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.312.045-.698.077-1.134-.063-.275-.088-.63-.205-1.178-.444-2.336-1.019-3.844-3.394-3.96-3.551-.116-.157-.945-1.258-.945-2.4 0-1.141.597-1.701.81-1.932.213-.23.465-.288.621-.288.155 0 .31.002.446.009.144.007.336-.055.525.4.195.469.664 1.62.723 1.738.058.118.098.257.02.413-.078.156-.118.256-.234.394-.117.137-.246.307-.352.413-.118.118-.241.246-.104.482.138.236.611 1.008 1.309 1.63.898.799 1.656 1.047 1.892 1.164.236.117.373.103.51-.055.138-.157.588-.686.744-.922.157-.236.314-.196.529-.118.216.079 1.372.647 1.607.765.236.118.393.177.451.275.059.098.059.57-.085.975z"/></svg>
          WhatsApp
        </a>
        <button class="btn btn-primary" onclick="openBookingModal('{html.escape(dest['name'])}')">Book Now</button>
        <button class="mobile-toggle" id="mobileToggle" aria-label="Toggle Navigation">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>

  <!-- Breadcrumbs -->
  <nav class="breadcrumb-nav" aria-label="Breadcrumb">
    <div class="container">
      <ol class="breadcrumb-list">
        <li class="breadcrumb-item"><a href="../../../index.html">Home</a></li>
        <li class="breadcrumb-separator">/</li>
        <li class="breadcrumb-item"><a href="/">Destinations</a></li>
        <li class="breadcrumb-separator">/</li>
        <li class="breadcrumb-item"><a href="/?region={dest['region'].lower()}">{html.escape(dest['region'])}</a></li>
        <li class="breadcrumb-separator">/</li>
        <li class="breadcrumb-item active" aria-current="page">{html.escape(dest['name'])}</li>
      </ol>
    </div>
  </nav>

  <!-- 1. DESTINATION HERO SECTION -->
  <section class="destination-detail-hero" style="background-image: url('{html.escape(dest['heroImage'])}');">
    <div class="container">
      <div class="detail-hero-content">
        <div class="detail-hero-badges">
          <span class="detail-region-tag">{html.escape(dest['region'])}</span>
          <span class="detail-country-tag">{html.escape(dest['country'])}</span>
          {categories_badges}
        </div>
        <h1 class="detail-hero-title">{html.escape(dest['name'])}</h1>
        <p class="detail-hero-tagline">{html.escape(dest.get('tagline', dest.get('shortDescription', '')))}</p>
        <div class="detail-hero-actions">
          <a href="https://wa.me/254762251566?text=Hello%20Horizon%20Legacy%20Safaris,%20I%20would%20like%20to%20plan%20a%20private%20safari%20or%20holiday%20to%20{html.escape(dest['name'])}." target="_blank" rel="noopener noreferrer" class="btn btn-hero-whatsapp">
            <svg class="icon-whatsapp" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
            <span>Inquire on WhatsApp</span>
          </a>
          <button class="btn btn-hero-primary" onclick="openBookingModal('{html.escape(dest['name'])}')">
            <span>Book / Custom Quote</span>
            <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- 2. QUICK FACTS STRIP -->
  <div class="quick-facts-bar">
    <div class="container">
      <div class="quick-facts-grid">
        <div class="quick-fact-item">
          <div class="quick-fact-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg></div>
          <div><div class="quick-fact-label">Best Time to Visit</div><div class="quick-fact-val">{html.escape(best_time)}</div></div>
        </div>
        <div class="quick-fact-item">
          <div class="quick-fact-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg></div>
          <div><div class="quick-fact-label">Ideal Duration</div><div class="quick-fact-val">{html.escape(ideal_dur)}</div></div>
        </div>
        <div class="quick-fact-item">
          <div class="quick-fact-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg></div>
          <div><div class="quick-fact-label">Languages</div><div class="quick-fact-val">{html.escape(lang)}</div></div>
        </div>
        <div class="quick-fact-item">
          <div class="quick-fact-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"></rect><line x1="1" y1="10" x2="23" y2="10"></line></svg></div>
          <div><div class="quick-fact-label">Currency</div><div class="quick-fact-val">{html.escape(curr)}</div></div>
        </div>
        <div class="quick-fact-item">
          <div class="quick-fact-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg></div>
          <div><div class="quick-fact-label">Visa Info</div><div class="quick-fact-val">{html.escape(visa)}</div></div>
        </div>
      </div>
    </div>
  </div>

  <!-- In-page Navigation Strip -->
  <div class="dest-nav-strip">
    <div class="container">
      <ul class="dest-nav-links">
        <li><a href="#overview">Overview</a></li>
        <li><a href="#gallery">Photo Gallery</a></li>
        <li><a href="#highlights">Top Attractions</a></li>
        <li><a href="#activities">Experiences</a></li>
        <li><a href="#best-time">Best Time to Visit</a></li>
        <li><a href="#accommodations">Where to Stay</a></li>
        <li><a href="#packages">Available Packages</a></li>
        <li><a href="#faqs">Travel FAQs</a></li>
      </ul>
    </div>
  </div>

  <!-- 3. OVERVIEW & INTRODUCTION SECTION -->
  <section class="dest-content-section" id="overview">
    <div class="container">
      <div style="max-width: 840px;">
        <span style="font-size: 0.8125rem; font-weight: 700; color: var(--color-accent-warm); text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 8px;">Destination Overview</span>
        <h2 class="dest-section-title">Introduction to {html.escape(dest['name'])}</h2>
        <div style="font-size: 1.0625rem; line-height: 1.8; color: var(--color-text-main); margin-bottom: 24px;">
          {''.join([f'<p style="margin-bottom: 16px;">{html.escape(p)}</p>' for p in dest.get('overview', '').split(chr(10)+chr(10))])}
        </div>
      </div>
    </div>
  </section>

  <!-- 4. PHOTO GALLERY -->
  <section class="dest-content-section" id="gallery" style="background-color: #ffffff;">
    <div class="container">
      <span style="font-size: 0.8125rem; font-weight: 700; color: var(--color-accent-warm); text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 8px;">Visual Journey</span>
      <h2 class="dest-section-title">Photo Gallery</h2>
      <p class="dest-section-subtitle">Click on any image to enlarge and experience the beauty of {html.escape(dest['name'])}.</p>
      <div class="dest-gallery-grid">
{gallery_html}
      </div>
    </div>
  </section>

  <!-- 5. TOP ATTRACTIONS & HIGHLIGHTS -->
  <section class="dest-content-section" id="highlights">
    <div class="container">
      <span style="font-size: 0.8125rem; font-weight: 700; color: var(--color-accent-warm); text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 8px;">Must-See Highlights</span>
      <h2 class="dest-section-title">Top Attractions & Sights</h2>
      <p class="dest-section-subtitle">The defining landmarks, wonders, and iconic sights that make {html.escape(dest['name'])} extraordinary.</p>
      <div class="highlights-card-grid">
{highlights_html}
      </div>
    </div>
  </section>

  <!-- 6. ACTIVITIES & EXPERIENCES -->
  <section class="dest-content-section" id="activities" style="background-color: #ffffff;">
    <div class="container">
      <span style="font-size: 0.8125rem; font-weight: 700; color: var(--color-accent-warm); text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 8px;">Things to Do</span>
      <h2 class="dest-section-title">Activities & Experiences</h2>
      <p class="dest-section-subtitle">Signature safari, adventure, cultural, and relaxation activities we curate for our travelers.</p>
      <div class="activities-tag-grid">
{activities_html}
      </div>
    </div>
  </section>

  <!-- 7. BEST TIME TO VISIT & TRAVEL INFO -->
  <section class="dest-content-section" id="best-time">
    <div class="container">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 36px; align-items: flex-start;">
        <div>
          <span style="font-size: 0.8125rem; font-weight: 700; color: var(--color-accent-warm); text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 8px;">Planning Guide</span>
          <h2 class="dest-section-title">Best Time to Visit</h2>
          <p style="font-size: 1.0625rem; line-height: 1.7; color: var(--color-text-main); margin-bottom: 20px;">
            {html.escape(dest.get('bestTimeToVisit', ''))}
          </p>
          <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: 20px; box-shadow: var(--shadow-xs);">
            <h4 style="font-family: var(--font-serif); font-size: 1.125rem; color: var(--color-text-main); margin-bottom: 8px;">Climate & Seasonal Notes</h4>
            <p style="font-size: 0.9375rem; color: var(--color-text-muted); line-height: 1.5;">{html.escape(climate)}</p>
          </div>
        </div>

        <div>
          <span style="font-size: 0.8125rem; font-weight: 700; color: var(--color-accent-warm); text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 8px;">Essential Logistics</span>
          <h2 class="dest-section-title">Travel Practical Information</h2>
          <div style="background: #ffffff; border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: 24px; box-shadow: var(--shadow-sm);">
            <div style="margin-bottom: 16px;">
              <strong style="color: var(--color-primary); display: block; font-size: 0.875rem; text-transform: uppercase; margin-bottom: 4px;">Entry & Visa Requirements:</strong>
              <p style="color: var(--color-text-muted); font-size: 0.9375rem; line-height: 1.5; margin: 0;">{html.escape(visa)}</p>
            </div>
            <div style="margin-bottom: 16px;">
              <strong style="color: var(--color-primary); display: block; font-size: 0.875rem; text-transform: uppercase; margin-bottom: 4px;">Currency & Payment Methods:</strong>
              <p style="color: var(--color-text-muted); font-size: 0.9375rem; line-height: 1.5; margin: 0;">{html.escape(curr)}. Major credit cards and USD cash are widely utilized across luxury lodges.</p>
            </div>
            <div>
              <strong style="color: var(--color-primary); display: block; font-size: 0.875rem; text-transform: uppercase; margin-bottom: 4px;">How Horizon Legacy Handles Your Trip:</strong>
              <p style="color: var(--color-text-muted); font-size: 0.9375rem; line-height: 1.5; margin: 0;">We arrange private airport pickups, domestic bush charter flights or private 4x4 Land Cruisers, park admission permits, and dedicated professional driver guides.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 8. RECOMMENDED ACCOMMODATIONS -->
  <section class="dest-content-section" id="accommodations" style="background-color: #ffffff;">
    <div class="container">
      <span style="font-size: 0.8125rem; font-weight: 700; color: var(--color-accent-warm); text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 8px;">Handpicked Stays</span>
      <h2 class="dest-section-title">Recommended Luxury Accommodations</h2>
      <p class="dest-section-subtitle">We partner with premier lodges, luxury camps, and five-star resorts to ensure maximum comfort and genuine hospitality.</p>
      <div class="accomm-grid">
{accomm_html}
      </div>
    </div>
  </section>

  <!-- 9. AVAILABLE HORIZON LEGACY PACKAGES (PACKAGE INTEGRATION) -->
  <section class="packages-section-wrap" id="packages">
    <div class="container">
      <span style="font-size: 0.8125rem; font-weight: 700; color: var(--color-accent-warm); text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 8px;">Itineraries & Packages</span>
      <h2 class="dest-section-title">Available Tour Packages for {html.escape(dest['name'])}</h2>
      <p class="dest-section-subtitle">Real packages currently available for booking with Horizon Legacy Safaris.</p>
{packages_html}
    </div>
  </section>

  <!-- 10. RELATED DESTINATIONS -->
  <section class="dest-content-section" style="background-color: #ffffff;">
    <div class="container">
      <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 30px; flex-wrap: wrap; gap: 14px;">
        <div>
          <span style="font-size: 0.8125rem; font-weight: 700; color: var(--color-accent-warm); text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 8px;">Continue Exploring</span>
          <h2 class="dest-section-title" style="margin-bottom: 0;">Related Destinations</h2>
        </div>
        <a href="/" class="btn btn-outline" style="font-size: 0.875rem;">View All 52 Destinations &rarr;</a>
      </div>
      <div class="destinations-grid">
{related_html}
      </div>
    </div>
  </section>

  <!-- 11. FAQS ACCORDION -->
  <section class="dest-content-section" id="faqs">
    <div class="container" style="max-width: 860px;">
      <span style="font-size: 0.8125rem; font-weight: 700; color: var(--color-accent-warm); text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 8px; text-align: center;">Got Questions?</span>
      <h2 class="dest-section-title" style="text-align: center;">Frequently Asked Questions</h2>
      <p class="dest-section-subtitle" style="text-align: center; margin-left: auto; margin-right: auto;">Everything you need to know about planning your holiday to {html.escape(dest['name'])}.</p>
      <div class="faq-accordion">
{faqs_html}
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="container footer-container">
      <div class="footer-col brand-col">
        <div class="footer-logo">
          <img src="../../../assets/images/logo.jpg" alt="Horizon Legacy - Luxury Safaris & Bespoke Travel" class="footer-logo-img">
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
        <h4 class="footer-title">Top Destinations</h4>
        <ul class="footer-links">
          <li><a href="../maasai-mara/">Maasai Mara National Reserve</a></li>
          <li><a href="../amboseli/">Amboseli National Park</a></li>
          <li><a href="../lake-nakuru/">Lake Nakuru & Great Rift Valley</a></li>
          <li><a href="../diani-beach/">Diani Beach Luxury Escapes</a></li>
          <li><a href="../zanzibar/">Zanzibar Island & Stone Town</a></li>
          <li><a href="../serengeti/">Serengeti National Park</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4 class="footer-title">Global Regions</h4>
        <ul class="footer-links">
          <li><a href="/?region=kenya">Kenya Wildlife & Beaches</a></li>
          <li><a href="/?region=east+africa">East Africa Safaris</a></li>
          <li><a href="/?region=africa">Africa Wilderness Expeditions</a></li>
          <li><a href="/?region=asia">Asia & Island Escapes</a></li>
          <li><a href="/?region=europe">European Grand Tours</a></li>
          <li><a href="/?region=antarctica">Antarctica Polar Expeditions</a></li>
        </ul>
      </div>

      <div class="footer-col contact-col">
        <h4 class="footer-title">Contact & Reservations</h4>
        <p class="contact-item">
          <strong>Direct Line:</strong>
          <a href="tel:+254762251566">+254 762 251 566</a>
        </p>
        <p class="contact-item">
          <strong>WhatsApp Concierge:</strong>
          <a href="https://wa.me/254762251566" target="_blank">+254 762 251 566</a>
        </p>
        <p class="contact-item">
          <strong>Email:</strong>
          <a href="mailto:reservations@horizonlegacysafaris.com">reservations@horizonlegacysafaris.com</a>
        </p>
      </div>
    </div>

    <div class="footer-bottom">
      <div class="container footer-bottom-inner">
        <p>© 2026 Horizon Legacy Safaris Ltd. All rights reserved. Designed for luxury traveler experiences.</p>
        <div class="payment-methods">
          <span>Payment accepted via:</span>
          <strong>Lipa Na M-PESA</strong> • <strong>Visa</strong> • <strong>Mastercard</strong> • <strong>Bank Transfer</strong>
        </div>
      </div>
    </div>
  </footer>

  <!-- Sticky WhatsApp Floating Button -->
  <a href="https://wa.me/254762251566?text=Hello%20Horizon%20Legacy%20Safaris,%20I%20am%20inquiring%20about%20traveling%20to%20{html.escape(dest['name'])}." 
     target="_blank" 
     rel="noopener noreferrer" 
     class="floating-whatsapp" 
     id="floatingWhatsapp" 
     aria-label="Chat with our safari expert on WhatsApp">
    <div class="whatsapp-pulse"></div>
    <div class="whatsapp-tooltip">Chat with a Holiday Specialist</div>
    <svg class="whatsapp-icon" viewBox="0 0 24 24" fill="currentColor">
      <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/>
    </svg>
  </a>

  <!-- Mobile Bottom Sticky Booking Bar -->
  <div class="mobile-sticky-bar">
    <div class="mobile-sticky-inner">
      <div class="sticky-price-block">
        <span class="sub">{html.escape(dest['country'])}</span>
        <div class="price-val" style="font-size: 0.95rem;"><strong>{html.escape(dest['name'])}</strong></div>
      </div>
      <div class="sticky-actions">
        <a href="https://wa.me/254762251566?text=Hello%20Horizon%20Legacy%20Safaris,%20I%20am%20inquiring%20about%20visiting%20{html.escape(dest['name'])}." class="btn btn-sm btn-whatsapp-icon" aria-label="WhatsApp">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
        </a>
        <button class="btn btn-sm btn-primary" onclick="openBookingModal('{html.escape(dest['name'])}')">Book / Inquire</button>
      </div>
    </div>
  </div>

  <!-- BOOKING INQUIRY MODAL -->
  <div class="modal-backdrop" id="bookingModal" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-header">
        <div>
          <h3 class="modal-title">Book / Inquire About {html.escape(dest['name'])}</h3>
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
            <label for="roomCategory">Destination / Accommodation *</label>
            <select id="roomCategory" required>
              <option value="{html.escape(dest['name'])} (Featured)" selected>{html.escape(dest['name'])} (Standard / Luxury)</option>
              <option value="{html.escape(dest['name'])} (Ultra-Luxury Suite)">{html.escape(dest['name'])} (Ultra-Luxury Suite / Camp)</option>
              <option value="Tailor-Made Custom Package">Tailor-Made Custom Package</option>
            </select>
          </div>
          <div class="form-group">
            <label for="transportPreference">Travel Style *</label>
            <select id="transportPreference" required>
              <option value="4x4 Safari Tour Cruiser">4x4 Safari Land Cruiser + Guide</option>
              <option value="Scenic Flight / Fly-in Safari">Scenic Flight / Fly-in Package</option>
              <option value="Self Drive / Hotel Only">Hotel / Lodge Only</option>
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
          <textarea id="specialRequests" rows="3" placeholder="e.g. Honeymoon setup, specific safari lodges, dietary requirements, or flight transfer requests..."></textarea>
        </div>

        <div class="modal-footer">
          <button type="submit" class="btn btn-whatsapp-submit">
            <svg class="icon-whatsapp" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
            <span>Send WhatsApp Inquiry</span>
          </button>
        </div>
      </form>
    </div>
  </div>

  <!-- IMAGE LIGHTBOX MODAL -->
  <div class="lightbox-backdrop" id="imageLightbox" aria-hidden="true" onclick="closeLightbox(event)">
    <div class="lightbox-dialog">
      <button class="lightbox-close" onclick="closeLightbox(event)" aria-label="Close image lightbox">&times;</button>
      <div class="lightbox-image-wrap">
        <img src="" alt="Enlarged photo" id="lightboxImg">
      </div>
      <div class="lightbox-caption" id="lightboxCaption"></div>
    </div>
  </div>

  <!-- Scripts -->
  <script src="../../../script.js"></script>
</body>
</html>
"""
        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(detail_content)

    print(f"Generated all {len(DESTINATIONS)} static destination detail pages in {DEST_DIR}/<slug>/index.html")

# -----------------------------------------------------------------------------
# 4. GENERATE XML SITEMAP
# -----------------------------------------------------------------------------
def generate_sitemap():
    sitemap_path = os.path.join(WEBSITE_DIR, 'sitemap.xml')
    urls = [
        "https://horizonlegacysafaris.com/"
    ]
    for d in DESTINATIONS:
        urls.append(f"https://horizonlegacysafaris.com/packages/destinations/{d['slug']}/")
    urls.append("https://horizonlegacysafaris.com/safari-packages/")
    for pkg in SAFARI_PACKAGES:
        path = pkg.get("detailPath") or f"/safari-packages/{pkg['slug']}/"
        urls.append(f"https://horizonlegacysafaris.com{path}")

    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    for url in urls:
        priority = "1.0" if url == "https://horizonlegacysafaris.com/" else ("0.9" if url.endswith("/destinations/") else "0.8")
        xml_lines.append(f"  <url>\n    <loc>{url}</loc>\n    <changefreq>weekly</changefreq>\n    <priority>{priority}</priority>\n  </url>")
    xml_lines.append('</urlset>')

    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(xml_lines))
    print(f"Generated Sitemap with {len(urls)} URLs: {sitemap_path}")

if __name__ == '__main__':
    generate_js_data()
    generate_destination_detail_pages()
    generate_discovery_index()
    generate_sitemap()
    print("ALL DESTINATIONS SYSTEM BUILD COMPLETE!")
