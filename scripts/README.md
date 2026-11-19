# Safari catalogue — editing guide

The 30-package safari catalogue is generated from plain Python records. One edit
updates the catalogue card, the filters and the detail page together.

## Where the data lives

| File | What it holds |
| --- | --- |
| `scripts/safari_packages_kenya.py` | The 20 Kenya catalogue records |
| `scripts/safari_packages_east.py` | The 5 Tanzania, 3 Uganda and 2 Rwanda records |
| `scripts/safari_catalogue.py` | The single exported `CATALOGUE_PACKAGES` list and `SAMPLE_ITINERARIES` |
| `scripts/safari_packages_base.py` | The `pkg()` helper, shared inclusions/exclusions and travel notes |
| `scripts/safari_packages_dataset.py` | Imported catalogue plus the existing seasonal offers and Encore getaway |

`CATALOGUE_PACKAGES` in `scripts/safari_catalogue.py` is the central list. It
combines the two package modules, so the builder, catalogue and sitemap all
read the same records.

## Edit a package

Open the record in `safari_packages_kenya.py` or `safari_packages_east.py`.
These are the editable fields:

| Field | Purpose |
| --- | --- |
| `slug` | URL: `/safari-packages/<slug>/` |
| `title`, `short`, `tagline` | Page and card wording |
| `country`, `destination`, `regions` | Country grouping and destination filters |
| `days`, `duration` | Card duration, quick facts and duration filter |
| `safari_type`, `luxury` | Safari type and luxury-level filters |
| `summary`, `card` | Long description and short card description |
| `hero`, `gallery` | Hero image and gallery images |
| `highlights` | “Trip Highlights” panel |
| `itinerary` | Day-by-day list; either `(title, detail)` tuples or full dicts |
| `accommodation` | Area/tier suggestions only — never named partner claims |
| `activities` | “What you will do” tags |
| `inclusions`, `exclusions` | Included / not included lists |
| `travel_info` | Practical travel notes |
| `price`, `validity` | Price (leave `None` until verified) and season/validity wording |
| `status` | `"published"` or `"draft"` |

Drafts are excluded from the catalogue and are skipped by the page builder, so
they can be prepared without going live. Set `status="published"` and rebuild
when the record is ready.

Only publish a price when it has been verified. With `price=None`, every card
and page shows **Price on request** and no figure is rendered. Accommodation is
described by area and budget band only; do not add hotel names or claim a
partnership.

## Edit the sample itinerary

`SAMPLE_ITINERARIES` in `scripts/safari_catalogue.py` holds the 7-Day Best of
Kenya Safari. Edit the `route`, `stops` (day, destination, title, detail, image,
stay, transfer) and `notes`. The published route is Amboseli → Lake Naivasha →
Lake Nakuru → Maasai Mara. Keep it illustrative: no fixed dates, hotel names,
booking references or availability promises.

## Rebuild the pages

From the repository root:

```bash
cd scripts

# Rebuild the catalogue and the 30 catalogue detail pages.
python3 - <<'PY'
from build_safari_packages import build_catalogue, build_detail
from safari_catalogue import CATALOGUE_PACKAGES

build_catalogue()
for pkg in CATALOGUE_PACKAGES:
    if pkg.get("status", "published") == "published":
        build_detail(pkg)
PY
```

`python3 build_safari_packages.py` rebuilds every published record, including
the older seasonal offers. Use the selective command above when you only want
to refresh the 30-package catalogue.

Then check the generated files under `Website/safari-packages/`, update
`Website/sitemap.xml` if a slug changed, and preview `Website/` over HTTP (for
example `python3 -m http.server 4173 --directory Website`).
