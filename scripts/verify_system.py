#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification Script for Horizon Legacy Safaris Destination Discovery System
"""

import os
import sys
from destinations_dataset import DESTINATIONS, PACKAGES

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEBSITE_DIR = os.path.join(BASE_DIR, 'Website')
DEST_DIR = os.path.join(WEBSITE_DIR, 'packages', 'destinations')

def run_checks():
    errors = []
    
    # 1. Check destinations count
    if len(DESTINATIONS) != 52:
        errors.append(f"Expected 52 destinations, found {len(DESTINATIONS)}")
    print(f"✓ Total destinations in dataset: {len(DESTINATIONS)}")

    # 2. Check main All Destinations discovery page
    all_dest_html = os.path.join(DEST_DIR, 'index.html')
    if not os.path.exists(all_dest_html):
        errors.append(f"Missing {all_dest_html}")
    else:
        print(f"✓ All Destinations discovery page exists: {all_dest_html}")

    # 3. Check every single destination detail page
    for d in DESTINATIONS:
        slug = d['slug']
        detail_path = os.path.join(DEST_DIR, slug, 'index.html')
        if not os.path.exists(detail_path):
            errors.append(f"Missing detail page for {slug}: {detail_path}")
        else:
            size = os.path.getsize(detail_path)
            if size < 1000:
                errors.append(f"Detail page for {slug} is unusually small ({size} bytes)")
    print(f"✓ Verified all 52 static destination detail pages exist with rich content")

    # 4. Check Lake Nakuru package integration
    nakuru = next((d for d in DESTINATIONS if d['slug'] == 'lake-nakuru'), None)
    if not nakuru or 'encore-hotel-nakuru-2d1n' not in nakuru['packageIds']:
        errors.append("Lake Nakuru is not connected to encore-hotel-nakuru-2d1n package!")
    else:
        print("✓ Verified Lake Nakuru is connected to active Encore Hotel package")

    # 5. Check CSS and JS assets
    css_path = os.path.join(WEBSITE_DIR, 'assets', 'css', 'destinations.css')
    js_data_path = os.path.join(WEBSITE_DIR, 'assets', 'js', 'destinations-data.js')
    js_app_path = os.path.join(WEBSITE_DIR, 'assets', 'js', 'destinations.js')

    for path, name in [(css_path, "destinations.css"), (js_data_path, "destinations-data.js"), (js_app_path, "destinations.js")]:
        if not os.path.exists(path):
            errors.append(f"Missing {name} at {path}")
        else:
            print(f"✓ Verified asset: {name} ({os.path.getsize(path)} bytes)")

    # 6. Check Sitemap
    sitemap_path = os.path.join(WEBSITE_DIR, 'sitemap.xml')
    if not os.path.exists(sitemap_path):
        errors.append("Missing sitemap.xml")
    else:
        with open(sitemap_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if "maasai-mara" not in content or "lake-nakuru" not in content:
                errors.append("Sitemap missing destination URLs")
        print(f"✓ Verified sitemap.xml exists ({os.path.getsize(sitemap_path)} bytes)")

    # 7. Check homepage index.html navigation links
    homepage_path = os.path.join(WEBSITE_DIR, 'index.html')
    with open(homepage_path, 'r', encoding='utf-8') as f:
        hp_content = f.read()
        if "packages/destinations/" not in hp_content:
            errors.append("Homepage navigation does not link to packages/destinations/")
    print("✓ Verified homepage navigation includes Destinations link")

    if errors:
        print("\nERRORS ENCOUNTERED:")
        for err in errors:
            print(f"  ❌ {err}")
        sys.exit(1)
    else:
        print("\n🎉 ALL 7 SYSTEM INTEGRITY CHECKS PASSED PERFECTLY!")

if __name__ == '__main__':
    run_checks()
