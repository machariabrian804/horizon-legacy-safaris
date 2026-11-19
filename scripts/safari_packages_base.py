# -*- coding: utf-8 -*-
"""
Shared helpers for the Horizon Legacy safari package catalogue.

Every package record is built with pkg(), so the fields the page builder needs
are always present and every record stays readable and editable:

    slug / title / short / group / country / destination
    days, nights, duration
    safari_type, luxury, tagline, summary, card
    hero, gallery, highlights, itinerary, accommodation, activities
    inclusions, exclusions, travel_info, best_for
    price, validity, status   <- publish/draft switch lives here

Editorial rules (enforced by the absence of fields, not by convention):
  * price is None and priceNote is "Price on request" - no figures are invented.
  * validity describes a season, never a fixed departure date.
  * accommodation is described by area and tier, never as a named partner.
"""

IMG = "/assets/images/destinations/"

BASE_INCLUSIONS = [
    "Private safari vehicle with pop-up roof and professional driver-guide",
    "Accommodation on the nights shown, full board unless the day plan says otherwise",
    "All park and conservancy entry fees for the itinerary as drawn",
    "Game drives and activities listed in the day-by-day plan",
    "Bottled drinking water in the vehicle throughout",
    "Round-trip road transfers from Nairobi unless the plan starts elsewhere",
    "24/7 WhatsApp support from your Horizon Legacy consultant",
]

BASE_EXCLUSIONS = [
    "International flights and any domestic flight unless quoted",
    "Visas, eTA and travel insurance",
    "Alcoholic drinks, premium beverages and laundry",
    "Optional extras marked as optional in the day plan",
    "Gratuities for guides and camp staff",
    "Any item not listed under inclusions",
]

BASE_TRAVEL_INFO = [
    "This is a suggested outline. Dates, pace, lodges and road-versus-fly legs are all set at quotation.",
    "Wildlife sightings are never guaranteed. Guides pace each day around what is actually moving.",
    "Park fees, permits and concession fees are quoted at the official rate current at the time of booking.",
    "Dry seasons (roughly January-February and June-October) usually give the easiest game viewing; the itinerary itself runs year-round.",
]

DURATION_BUCKETS = ["1 Day", "2-3 Days", "4-6 Days", "7-9 Days", "10+ Days"]


def duration_bucket(days):
    if days <= 1:
        return "1 Day"
    if days <= 3:
        return "2-3 Days"
    if days <= 6:
        return "4-6 Days"
    if days <= 9:
        return "7-9 Days"
    return "10+ Days"


def _gallery(items):
    return [{"url": IMG + name if not name.startswith("/") else name, "caption": caption} for name, caption in items]


def _itinerary(steps):
    out = []
    for index, step in enumerate(steps, start=1):
        if isinstance(step, dict):
            out.append(step)
        else:
            title, detail = step
            out.append({"day": f"Day {index}", "title": title, "detail": detail})
    return out


def _accommodation(items):
    return [{"tier": tier, "description": description} for tier, description in items]


def pkg(
    slug,
    title,
    short,
    group,
    country,
    destination,
    days,
    duration,
    safari_type,
    luxury,
    tagline,
    summary,
    card,
    hero,
    gallery,
    highlights,
    itinerary,
    accommodation,
    activities,
    best_for,
    inclusions=None,
    exclusions=None,
    travel_info=None,
    overview=None,
    destination_slug=None,
    regions=None,
    starts="Nairobi",
    style="Private 4x4 safari",
    validity="Year-round - quoted for your dates",
    price=None,
    status="published",
    detail_path=None,
):
    """One catalogue record. Everything the catalogue, filters and pages read."""
    return {
        "id": slug,
        "slug": slug,
        "title": title,
        "shortTitle": short,
        "group": group,
        "country": country,
        "destinationName": destination,
        "destinationSlug": destination_slug,
        "destinationOverview": overview,
        "regions": regions or [destination],
        "duration": duration,
        "durationDays": days,
        "durationBucket": duration_bucket(days),
        "safariType": safari_type,
        "luxuryLevel": luxury,
        "tagline": tagline,
        "summary": summary,
        "cardSummary": card,
        "heroImage": IMG + hero if not hero.startswith("/") else hero,
        "cardImage": IMG + hero if not hero.startswith("/") else hero,
        "gallery": _gallery(gallery),
        "highlights": highlights,
        "itinerary": _itinerary(itinerary),
        "accommodation": _accommodation(accommodation),
        "activities": activities,
        "inclusions": inclusions or list(BASE_INCLUSIONS),
        "exclusions": exclusions or list(BASE_EXCLUSIONS),
        "travelInfo": travel_info or list(BASE_TRAVEL_INFO),
        "bestFor": best_for,
        "startsFrom": starts,
        "travelStyle": style,
        "season": validity,
        "validity": validity,
        "price": price,
        "priceNote": "Price on request" if price is None else price,
        "status": status,
        "detailPath": detail_path,
    }
