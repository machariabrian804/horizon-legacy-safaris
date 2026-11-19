# -*- coding: utf-8 -*-
"""
Horizon Legacy Safaris - Safari Packages Database
Single source of truth for every package published at /safari-packages/.

Contents:
  * the 11 seasonal offers published earlier, still live and still linked
  * the Encore Hotel Nakuru getaway, derived from its bookable PACKAGES record
  * the 30 researched package concepts, imported from safari_catalogue.py

Content rules for this dataset:
  * No prices are published. Every package carries priceNote = "Price on request"
    and the pages never render a figure. Records can carry price=None only.
  * No travel dates, availability calendars, or lodge partnerships are invented.
    Seasons are described generically ("Festive season", "Shoulder season").
  * Accommodation entries describe tiers and locations, not named properties.
"""

from destinations_dataset import PACKAGES as _BOOKABLE_PACKAGES, DESTINATIONS as _DESTINATIONS
from safari_catalogue import (
    CATALOGUE_PACKAGES,
    SAFARI_GROUPS,
    SAMPLE_ITINERARIES,
    COUNTRY_ORDER,
    LUXURY_LEVELS,
)
from safari_packages_base import BASE_TRAVEL_INFO, duration_bucket

SAFARI_PACKAGES = [
    # =========================================================================
    # KENYA SAFARIS
    # =========================================================================
    {
        "id": "amboseli-festive",
        "slug": "amboseli-festive",
        "title": "Amboseli National Park Safari - Festive Season",
        "shortTitle": "Amboseli Festive Safari",
        "group": "Kenya Safaris",
        "country": "Kenya",
        "destinationSlug": "amboseli",
        "destinationName": "Amboseli National Park",
        "season": "Festive season",
        "duration": "3 Days / 2 Nights",
        "durationDays": 3,
        "startsFrom": "Nairobi",
        "travelStyle": "Private 4x4 safari",
        "priceNote": "Price on request",
        "tagline": "Elephants beneath Kilimanjaro during Kenya's festive season",
        "summary": (
            "A short, high-impact safari for the festive holiday window. Amboseli's swamps draw "
            "some of Africa's last great tuskers, and the snow-capped summit of Kilimanjaro frames "
            "almost every game drive. Festive departures fill quickly, so we plan road and air "
            "logistics around the dates you hold."
        ),
        "heroImage": "/assets/images/destinations/amboseli.jpg",
        "cardImage": "/assets/images/destinations/amboseli-card.jpg",
        "gallery": [
            {"url": "/assets/images/destinations/amboseli.jpg", "caption": "Elephant herd beneath the snows of Kilimanjaro"},
            {"url": "/assets/images/destinations/amboseli-card.jpg", "caption": "Elephants crossing the Amboseli plains"},
            {"url": "/assets/images/destinations/kilimanjaro.jpg", "caption": "Kibo rising beyond the savannah"},
        ],
        "highlights": [
            "Big-tusker elephant herds in the Enkongo Narok and Longinye swamps",
            "Kilimanjaro views at first light and again at sunset",
            "Observation Hill panoramas across the dried Lake Amboseli bed",
            "Festive-period game drives paced for families and mixed-age groups",
            "Optional Maasai community visit arranged with local hosts",
        ],
        "itinerary": [
            {
                "day": "Day 1",
                "title": "Nairobi to Amboseli",
                "detail": (
                    "Depart Nairobi after breakfast and drive south through the Kapiti plains, "
                    "dropping into the Amboseli basin by early afternoon. Settle in, then take a "
                    "late-afternoon game drive toward the swamps as elephants move in to drink."
                ),
            },
            {
                "day": "Day 2",
                "title": "Full day in the park",
                "detail": (
                    "A dawn game drive when Kilimanjaro is usually clearest, back for breakfast, "
                    "then out again through the middle of the day to Observation Hill and the "
                    "Longinye swamp circuit. Sundowners on the plains before returning to camp."
                ),
            },
            {
                "day": "Day 3",
                "title": "Morning drive and return",
                "detail": (
                    "Final early game drive, breakfast at camp, then the drive back to Nairobi "
                    "with a picnic stop en route, arriving late afternoon."
                ),
            },
        ],
        "accommodation": [
            {"tier": "Luxury", "description": "Tented suites or lodge rooms inside or bordering the park, full board, with views toward the mountain."},
            {"tier": "Mid-range", "description": "Comfortable lodges on the park boundary, full board, with pool and family rooms available."},
            {"tier": "Family-friendly", "description": "Lodges with interconnecting rooms and flexible meal times for younger children."},
        ],
        "inclusions": [
            "Private 4x4 safari vehicle with pop-up roof and professional driver-guide",
            "Two nights full-board accommodation in Amboseli",
            "All park entry and conservancy fees for the itinerary as drawn",
            "Unlimited game drives within park hours",
            "Bottled drinking water in the vehicle throughout",
            "Round-trip road transfers from Nairobi",
            "24/7 WhatsApp support from your Horizon Legacy consultant",
        ],
        "exclusions": [
            "International flights and domestic flights unless quoted",
            "Kenya eTA, visas and travel insurance",
            "Alcoholic drinks, premium beverages and laundry",
            "Optional hot air balloon safari or Maasai village visit",
            "Gratuities for guides and camp staff",
            "Any item not listed under inclusions",
        ],
        "bestFor": "Families and couples travelling over the festive break with three days to spare",
    },
    {
        "id": "amboseli-shoulder",
        "slug": "amboseli-shoulder",
        "title": "Amboseli National Park Safari - Shoulder Season",
        "shortTitle": "Amboseli Shoulder Season Safari",
        "group": "Kenya Safaris",
        "country": "Kenya",
        "destinationSlug": "amboseli",
        "destinationName": "Amboseli National Park",
        "season": "Shoulder season",
        "duration": "3 Days / 2 Nights",
        "durationDays": 3,
        "startsFrom": "Nairobi",
        "travelStyle": "Private 4x4 safari",
        "priceNote": "Price on request",
        "tagline": "Quieter plains, clearer mountain, fewer vehicles",
        "summary": (
            "Outside the festive rush, Amboseli settles into its best photographic rhythm: "
            "cleaner air, fewer vehicles at a sighting, and elephants relaxed around the swamps. "
            "The same three-day shape as the festive itinerary, with more room to sit with a herd."
        ),
        "heroImage": "/assets/images/destinations/amboseli-card.jpg",
        "cardImage": "/assets/images/destinations/amboseli.jpg",
        "gallery": [
            {"url": "/assets/images/destinations/amboseli-card.jpg", "caption": "Elephants crossing the Amboseli plains"},
            {"url": "/assets/images/destinations/amboseli.jpg", "caption": "Elephant herd beneath the snows of Kilimanjaro"},
            {"url": "/assets/images/destinations/kilimanjaro-card.jpg", "caption": "The eastern icefields of Kilimanjaro"},
        ],
        "highlights": [
            "Low-season game viewing with far fewer vehicles at each sighting",
            "Long, unhurried sessions with the swamp elephant herds",
            "Clearer mountain views in the cooler shoulder months",
            "Birding across the marshes — 400+ recorded species",
            "Flexible pacing for photographers who want to wait for light",
        ],
        "itinerary": [
            {
                "day": "Day 1",
                "title": "Nairobi to Amboseli",
                "detail": (
                    "Mid-morning departure from Nairobi, arriving in time for lunch and a "
                    "settling-in game drive as the heat lifts off the plains."
                ),
            },
            {
                "day": "Day 2",
                "title": "Swamps, hill and plains",
                "detail": (
                    "Sunrise drive to the swamp edges, a slow middle-of-the-day circuit to "
                    "Observation Hill, and a final golden-hour drive before dinner."
                ),
            },
            {
                "day": "Day 3",
                "title": "Last light, then Nairobi",
                "detail": (
                    "Early drive if the mountain is clear, breakfast, and the road back to "
                    "Nairobi with a stop in the Chyulu foothills."
                ),
            },
        ],
        "accommodation": [
            {"tier": "Luxury", "description": "Tented suites inside or bordering the park with mountain-facing decks."},
            {"tier": "Mid-range", "description": "Boundary lodges with full board, pool and easy gate access."},
            {"tier": "Photographer's choice", "description": "Camps with early gate access so you are out before first light."},
        ],
        "inclusions": [
            "Private 4x4 safari vehicle with pop-up roof and professional driver-guide",
            "Two nights full-board accommodation in Amboseli",
            "All park entry fees for the itinerary as drawn",
            "Unlimited game drives within park hours",
            "Bottled drinking water in the vehicle throughout",
            "Round-trip road transfers from Nairobi",
            "24/7 WhatsApp support from your Horizon Legacy consultant",
        ],
        "exclusions": [
            "International flights and domestic flights unless quoted",
            "Kenya eTA, visas and travel insurance",
            "Alcoholic drinks, premium beverages and laundry",
            "Optional hot air balloon safari or Maasai village visit",
            "Gratuities for guides and camp staff",
            "Any item not listed under inclusions",
        ],
        "bestFor": "Photographers and couples who value solitude over the holiday bustle",
    },
    {
        "id": "maasai-mara-festive",
        "slug": "maasai-mara-festive",
        "title": "Maasai Mara National Reserve - Festive Season",
        "shortTitle": "Maasai Mara Festive Safari",
        "group": "Kenya Safaris",
        "country": "Kenya",
        "destinationSlug": "maasai-mara",
        "destinationName": "Maasai Mara National Reserve",
        "season": "Festive season",
        "duration": "4 Days / 3 Nights",
        "durationDays": 4,
        "startsFrom": "Nairobi",
        "travelStyle": "Private 4x4 or fly-in safari",
        "priceNote": "Price on request",
        "tagline": "Four days in the Mara when the reserve is at its busiest and most alive",
        "summary": (
            "The Mara over the festive holidays is a spectacle of big cats, open plains and "
            "long light. Four days gives you time for the reserve's core, a conservancy "
            "afternoon, and a sunrise balloon if you want one. Holiday-season camps release "
            "space early, so we advise confirming dates well ahead."
        ),
        "heroImage": "/assets/images/destinations/maasai-mara.jpg",
        "cardImage": "/assets/images/destinations/maasai-mara-card.jpg",
        "gallery": [
            {"url": "/assets/images/destinations/maasai-mara.jpg", "caption": "Lion pride resting in the golden Mara grass"},
            {"url": "/assets/images/destinations/maasai-mara-card.jpg", "caption": "Wildebeest and zebra at a Mara River crossing"},
            {"url": "/assets/images/destinations/maasai-mara-balloon.jpg", "caption": "Sunrise balloon flight over the Mara"},
        ],
        "highlights": [
            "Big cat tracking with lions, cheetahs and leopards across the triangle",
            "Mara River frontage and the reserve's resident pods of hippo",
            "Optional sunrise hot air balloon with a bush breakfast",
            "Afternoon in a private conservancy for off-road and night drives",
            "Maasai cultural visit arranged directly with a local boma",
        ],
        "itinerary": [
            {
                "day": "Day 1",
                "title": "Nairobi to the Mara",
                "detail": (
                    "Either a scheduled light-aircraft flight to a Mara airstrip or the scenic "
                    "road transfer through Narok. Afternoon game drive on arrival, dinner in camp."
                ),
            },
            {
                "day": "Day 2",
                "title": "Full day in the reserve",
                "detail": (
                    "Full day out with a picnic lunch: the Mara Triangle, the river bends and "
                    "the open plains where the prides hold territory."
                ),
            },
            {
                "day": "Day 3",
                "title": "Conservancy and culture",
                "detail": (
                    "Morning drive in the reserve, then an afternoon in a neighbouring "
                    "conservancy for quieter viewing, or a Maasai boma visit if you prefer."
                ),
            },
            {
                "day": "Day 4",
                "title": "Sunrise drive and departure",
                "detail": (
                    "Optional balloon at first light, otherwise an early game drive, then "
                    "breakfast and the flight or drive back to Nairobi."
                ),
            },
        ],
        "accommodation": [
            {"tier": "Luxury", "description": "Tented camps in the reserve or a bordering conservancy, full board, with river or escarpment views."},
            {"tier": "Mid-range", "description": "Comfortable camps and lodges with full board and pool, close to the main gates."},
            {"tier": "Family-friendly", "description": "Camps with family tents and flexible game-drive timings for children."},
        ],
        "inclusions": [
            "Private 4x4 safari vehicle with pop-up roof and professional driver-guide",
            "Three nights full-board accommodation in the Mara",
            "All reserve and conservancy fees for the itinerary as drawn",
            "Morning, afternoon and full-day game drives",
            "Bottled drinking water in the vehicle throughout",
            "Airstrip or road transfers from Nairobi as quoted",
            "24/7 WhatsApp support from your Horizon Legacy consultant",
        ],
        "exclusions": [
            "Hot air balloon safari (quoted separately on request)",
            "International flights and domestic flights unless quoted",
            "Kenya eTA, visas and travel insurance",
            "Alcoholic drinks, premium beverages and laundry",
            "Maasai village entry fees where applicable",
            "Gratuities for guides and camp staff",
        ],
        "bestFor": "Families and groups who want the full Mara experience over the holidays",
    },
    {
        "id": "maasai-mara-shoulder",
        "slug": "maasai-mara-shoulder",
        "title": "Maasai Mara National Reserve - Shoulder Season",
        "shortTitle": "Maasai Mara Shoulder Safari",
        "group": "Kenya Safaris",
        "country": "Kenya",
        "destinationSlug": "maasai-mara",
        "destinationName": "Maasai Mara National Reserve",
        "season": "Shoulder season",
        "duration": "3 Days / 2 Nights",
        "durationDays": 3,
        "startsFrom": "Nairobi",
        "travelStyle": "Private 4x4 or fly-in safari",
        "priceNote": "Price on request",
        "tagline": "Three focused days of cats, plains and quiet conservancy roads",
        "summary": (
            "In the shoulder months the Mara's grass is shorter and its cats are easier to "
            "follow, with a fraction of the holiday traffic. Three days is enough for two full "
            "game-drive days and a conservancy afternoon if you fly in."
        ),
        "heroImage": "/assets/images/destinations/maasai-mara-card.jpg",
        "cardImage": "/assets/images/destinations/maasai-mara.jpg",
        "gallery": [
            {"url": "/assets/images/destinations/maasai-mara-card.jpg", "caption": "Wildebeest and zebra at a Mara River crossing"},
            {"url": "/assets/images/destinations/maasai-mara.jpg", "caption": "Lion pride resting in the golden Mara grass"},
            {"url": "/assets/images/destinations/maasai-mara-balloon.jpg", "caption": "Sunrise balloon flight over the Mara"},
        ],
        "highlights": [
            "Resident big cats with far fewer vehicles around a sighting",
            "Short-grass months that make wildlife easier to spot",
            "Conservancy access for walking safaris and night drives",
            "Excellent birdlife as the plains green up",
            "Fly-in option from Wilson Airport to save a day of driving",
        ],
        "itinerary": [
            {
                "day": "Day 1",
                "title": "Into the Mara",
                "detail": (
                    "Morning flight or road transfer, lunch in camp, then an afternoon game "
                    "drive across the plains as the light drops."
                ),
            },
            {
                "day": "Day 2",
                "title": "Full day out",
                "detail": (
                    "Sunrise departure with a picnic breakfast, tracking the resident prides "
                    "and cheetah coalitions, returning for a late lunch and an evening drive."
                ),
            },
            {
                "day": "Day 3",
                "title": "Morning drive and home",
                "detail": (
                    "Final early drive, breakfast, then the flight or road transfer back to "
                    "Nairobi."
                ),
            },
        ],
        "accommodation": [
            {"tier": "Luxury", "description": "Tented camps in a conservancy or the reserve, full board."},
            {"tier": "Mid-range", "description": "Comfortable camps near the gates with full board and pool."},
            {"tier": "Fly-in friendly", "description": "Camps close to an airstrip to minimise transit time."},
        ],
        "inclusions": [
            "Private 4x4 safari vehicle with pop-up roof and professional driver-guide",
            "Two nights full-board accommodation in the Mara",
            "All reserve and conservancy fees for the itinerary as drawn",
            "Game drives morning and afternoon, plus one full day out",
            "Bottled drinking water in the vehicle throughout",
            "Airstrip or road transfers from Nairobi as quoted",
            "24/7 WhatsApp support from your Horizon Legacy consultant",
        ],
        "exclusions": [
            "Hot air balloon safari (quoted separately on request)",
            "International flights and domestic flights unless quoted",
            "Kenya eTA, visas and travel insurance",
            "Alcoholic drinks, premium beverages and laundry",
            "Gratuities for guides and camp staff",
            "Any item not listed under inclusions",
        ],
        "bestFor": "Couples and small groups on a tight calendar who still want big-cat country",
    },
    {
        "id": "samburu-festive",
        "slug": "samburu-festive",
        "title": "Samburu National Reserve - Festive Season",
        "shortTitle": "Samburu Festive Safari",
        "group": "Kenya Safaris",
        "country": "Kenya",
        "destinationSlug": "samburu",
        "destinationName": "Samburu National Reserve",
        "season": "Festive season",
        "duration": "3 Days / 2 Nights",
        "durationDays": 3,
        "startsFrom": "Nairobi",
        "travelStyle": "Private 4x4 or fly-in safari",
        "priceNote": "Price on request",
        "tagline": "Kenya's northern frontier over the holidays",
        "summary": (
            "Samburu is the Mara's quieter northern cousin: doum palms along the Ewaso Ng'iro, "
            "dry-country species you will not see further south, and a far gentler pace over the "
            "festive break."
        ),
        "heroImage": "/assets/images/destinations/samburu.jpg",
        "cardImage": "/assets/images/destinations/samburu-card.jpg",
        "gallery": [
            {"url": "/assets/images/destinations/samburu.jpg", "caption": "The Ewaso Ng'iro river through Samburu"},
            {"url": "/assets/images/destinations/samburu-card.jpg", "caption": "Reticulated giraffe country in the north"},
            {"url": "/assets/images/destinations/mount-kenya.jpg", "caption": "Mount Kenya on the road north"},
        ],
        "highlights": [
            "The Samburu Special Five: reticulated giraffe, Grevy's zebra, gerenuk, beisa oryx and Somali ostrich",
            "Elephant herds along the Ewaso Ng'iro river",
            "Crocodile and birdlife at the river crossings",
            "Northern-frontier landscapes with a fraction of the crowds",
            "Optional Samburu community visit arranged with local hosts",
        ],
        "itinerary": [
            {
                "day": "Day 1",
                "title": "Nairobi to Samburu",
                "detail": (
                    "Drive north past Mount Kenya into Laikipia and down to the Ewaso Ng'iro, "
                    "or fly to a reserve airstrip. Afternoon game drive before dinner."
                ),
            },
            {
                "day": "Day 2",
                "title": "River and plains",
                "detail": (
                    "Full day along the river and into the doum palm thickets, with a picnic "
                    "lunch and a slow afternoon tracking the northern species."
                ),
            },
            {
                "day": "Day 3",
                "title": "Final drive and return",
                "detail": (
                    "Early game drive, breakfast, then the drive or flight back to Nairobi."
                ),
            },
        ],
        "accommodation": [
            {"tier": "Luxury", "description": "Tented camps along the Ewaso Ng'iro, full board, with river-facing decks."},
            {"tier": "Mid-range", "description": "Lodges on the reserve boundary with full board and pool."},
            {"tier": "Fly-in friendly", "description": "Camps close to the airstrip for shorter transfers."},
        ],
        "inclusions": [
            "Private 4x4 safari vehicle with pop-up roof and professional driver-guide",
            "Two nights full-board accommodation in Samburu",
            "All reserve entry fees for the itinerary as drawn",
            "Game drives morning and afternoon plus one full day out",
            "Bottled drinking water in the vehicle throughout",
            "Airstrip or road transfers from Nairobi as quoted",
            "24/7 WhatsApp support from your Horizon Legacy consultant",
        ],
        "exclusions": [
            "International flights and domestic flights unless quoted",
            "Kenya eTA, visas and travel insurance",
            "Alcoholic drinks, premium beverages and laundry",
            "Optional community visit fees",
            "Gratuities for guides and camp staff",
            "Any item not listed under inclusions",
        ],
        "bestFor": "Travellers who want a quieter festive safari with species you cannot see in the Mara",
    },
    {
        "id": "samburu-shoulder",
        "slug": "samburu-shoulder",
        "title": "Samburu National Reserve - Shoulder Season",
        "shortTitle": "Samburu Shoulder Season Safari",
        "group": "Kenya Safaris",
        "country": "Kenya",
        "destinationSlug": "samburu",
        "destinationName": "Samburu National Reserve",
        "season": "Shoulder season",
        "duration": "4 Days / 3 Nights",
        "durationDays": 4,
        "startsFrom": "Nairobi",
        "travelStyle": "Private 4x4 or fly-in safari",
        "priceNote": "Price on request",
        "tagline": "Four unhurried days in Kenya's dry north",
        "summary": (
            "The extra day lets the itinerary stretch beyond the reserve gate — Buffalo Springs, "
            "a conservancy walk, or a full morning with a river herd — which is what the "
            "shoulder season is for."
        ),
        "heroImage": "/assets/images/destinations/samburu-card.jpg",
        "cardImage": "/assets/images/destinations/samburu.jpg",
        "gallery": [
            {"url": "/assets/images/destinations/samburu-card.jpg", "caption": "Reticulated giraffe country in the north"},
            {"url": "/assets/images/destinations/samburu.jpg", "caption": "The Ewaso Ng'iro river through Samburu"},
            {"url": "/assets/images/destinations/mount-kenya-card.jpg", "caption": "Mount Kenya's peaks on the northern road"},
        ],
        "highlights": [
            "Samburu and Buffalo Springs reserves across three full days",
            "Dedicated time with the river elephant herds",
            "Guided walking in a neighbouring conservancy where permitted",
            "Birding along the Ewaso Ng'iro — hornbills, kingfishers and raptors",
            "Space to wait at a sighting instead of moving on",
        ],
        "itinerary": [
            {
                "day": "Day 1",
                "title": "Nairobi to Samburu",
                "detail": "Road or air transfer north, lunch in camp, late-afternoon game drive.",
            },
            {
                "day": "Day 2",
                "title": "Samburu reserve, full day",
                "detail": (
                    "Sunrise drive along the river, picnic breakfast, and a slow circuit through "
                    "the doum palms and lava ridges."
                ),
            },
            {
                "day": "Day 3",
                "title": "Buffalo Springs and the conservancy",
                "detail": (
                    "Cross into Buffalo Springs for the morning, then a guided conservancy walk "
                    "or community visit in the afternoon."
                ),
            },
            {
                "day": "Day 4",
                "title": "Last drive and return",
                "detail": "Early game drive, breakfast, and the transfer back to Nairobi.",
            },
        ],
        "accommodation": [
            {"tier": "Luxury", "description": "River-front tented camps, full board."},
            {"tier": "Mid-range", "description": "Boundary lodges with full board and pool."},
            {"tier": "Conservancy", "description": "Private conservancy camps with walking access and fewer vehicles."},
        ],
        "inclusions": [
            "Private 4x4 safari vehicle with pop-up roof and professional driver-guide",
            "Three nights full-board accommodation in Samburu",
            "All reserve and conservancy fees for the itinerary as drawn",
            "Game drives morning and afternoon across three days",
            "Guided conservancy walk where permitted",
            "Bottled drinking water in the vehicle throughout",
            "24/7 WhatsApp support from your Horizon Legacy consultant",
        ],
        "exclusions": [
            "International flights and domestic flights unless quoted",
            "Kenya eTA, visas and travel insurance",
            "Alcoholic drinks, premium beverages and laundry",
            "Optional community visit fees",
            "Gratuities for guides and camp staff",
            "Any item not listed under inclusions",
        ],
        "bestFor": "Returning safari travellers and birders who want depth over distance",
    },
    {
        "id": "sand-river-maasai-mara",
        "slug": "sand-river-maasai-mara",
        "title": "Sand River Maasai Mara Special",
        "shortTitle": "Sand River Maasai Mara Special",
        "group": "Kenya Safaris",
        "country": "Kenya",
        "destinationSlug": "maasai-mara",
        "destinationName": "Maasai Mara National Reserve",
        "season": "Year-round private conservancy",
        "duration": "4 Days / 3 Nights",
        "durationDays": 4,
        "startsFrom": "Nairobi",
        "travelStyle": "Private conservancy safari",
        "priceNote": "Price on request",
        "tagline": "A conservancy-first Mara stay along the Sand River",
        "summary": (
            "Built around the Sand River corridor on the reserve's southern edge, this itinerary "
            "trades gate queues for conservancy access: off-road tracking, night drives and "
            "walking, with the national reserve still within reach for a full day."
        ),
        "heroImage": "/assets/images/destinations/maasai-mara-balloon.jpg",
        "cardImage": "/assets/images/destinations/maasai-mara.jpg",
        "gallery": [
            {"url": "/assets/images/destinations/maasai-mara-balloon.jpg", "caption": "Sunrise balloon flight over the Mara"},
            {"url": "/assets/images/destinations/maasai-mara.jpg", "caption": "Lion pride resting in the golden Mara grass"},
            {"url": "/assets/images/destinations/maasai-mara-card.jpg", "caption": "Wildebeest and zebra at a Mara River crossing"},
        ],
        "highlights": [
            "Conservancy game drives with off-road access and night drives",
            "Guided walking safaris with a Maasai naturalist",
            "Sand River and Mara River frontage for wildlife movement",
            "One full day inside the national reserve",
            "Lower vehicle density than the reserve's main circuits",
        ],
        "itinerary": [
            {
                "day": "Day 1",
                "title": "Nairobi to the conservancy",
                "detail": (
                    "Fly or drive to the Mara, transfer to a Sand River camp, and take an "
                    "afternoon drive along the river line."
                ),
            },
            {
                "day": "Day 2",
                "title": "Conservancy day",
                "detail": (
                    "Sunrise drive with off-road tracking, a walking safari after breakfast, "
                    "and a night drive after dinner."
                ),
            },
            {
                "day": "Day 3",
                "title": "The national reserve",
                "detail": (
                    "Full day inside the reserve with a picnic lunch — the triangle, the river "
                    "crossings and the open plains."
                ),
            },
            {
                "day": "Day 4",
                "title": "Balloon option and departure",
                "detail": (
                    "Optional sunrise balloon with a bush breakfast, otherwise a final "
                    "conservancy drive before the flight or road transfer back."
                ),
            },
        ],
        "accommodation": [
            {"tier": "Luxury conservancy camp", "description": "Tented suites on the Sand River line, full board, with private decks."},
            {"tier": "Classic tented camp", "description": "Full-board tented rooms with en-suite bathrooms and river access."},
            {"tier": "Family tent", "description": "Larger tents or interconnecting rooms for families travelling together."},
        ],
        "inclusions": [
            "Private 4x4 safari vehicle with pop-up roof and professional driver-guide",
            "Three nights full-board accommodation in the conservancy",
            "Conservancy fees plus one day of national reserve entry",
            "Off-road game drives, night drives and a guided walking safari",
            "Bottled drinking water in the vehicle throughout",
            "Airstrip or road transfers from Nairobi as quoted",
            "24/7 WhatsApp support from your Horizon Legacy consultant",
        ],
        "exclusions": [
            "Hot air balloon safari (quoted separately on request)",
            "International flights and domestic flights unless quoted",
            "Kenya eTA, visas and travel insurance",
            "Alcoholic drinks, premium beverages and laundry",
            "Gratuities for guides and camp staff",
            "Any item not listed under inclusions",
        ],
        "bestFor": "Photographers and repeat Mara visitors who want walking and night drives",
    },
    {
        "id": "tsavo-festive",
        "slug": "tsavo-festive",
        "title": "Tsavo National Park - Festive Season",
        "shortTitle": "Tsavo Festive Safari",
        "group": "Kenya Safaris",
        "country": "Kenya",
        "destinationSlug": "tsavo-national-parks",
        "destinationName": "Tsavo East & Tsavo West National Parks",
        "season": "Festive season",
        "duration": "3 Days / 2 Nights",
        "durationDays": 3,
        "startsFrom": "Nairobi or Mombasa",
        "travelStyle": "Private 4x4 safari",
        "priceNote": "Price on request",
        "tagline": "Red elephants, lava flows and the road to the coast",
        "summary": (
            "Tsavo is the easiest big-park safari to bolt onto a coastal holiday: two parks, one "
            "trip, and a landscape of red dust, lava ridges and spring-fed pools. Ideal if you "
            "are flying into Mombasa for the festive break."
        ),
        "heroImage": "/assets/images/destinations/tsavo.jpg",
        "cardImage": "/assets/images/destinations/tsavo-card.jpg",
        "gallery": [
            {"url": "/assets/images/destinations/tsavo.jpg", "caption": "Elephants at a waterhole in Tsavo West"},
            {"url": "/assets/images/destinations/tsavo-card.jpg", "caption": "A red-dust elephant in the Tsavo scrub"},
            {"url": "/assets/images/destinations/hero-safari.jpg", "caption": "Acacia savannah on the Tsavo road"},
        ],
        "highlights": [
            "Tsavo's famous red-dust elephants, often in large herds",
            "Mzima Springs — crystal-clear pools with hippo and crocodile",
            "Shetani lava flows and the Chyulu Hills viewpoints",
            "Lugard Falls and the Galana River in Tsavo East",
            "Convenient start or finish for a Mombasa or Diani beach stay",
        ],
        "itinerary": [
            {
                "day": "Day 1",
                "title": "Nairobi or Mombasa to Tsavo West",
                "detail": (
                    "Drive in via Mtito Andei or from the coast, lunch in camp, then an "
                    "afternoon drive to Mzima Springs and the surrounding lava country."
                ),
            },
            {
                "day": "Day 2",
                "title": "Tsavo East",
                "detail": (
                    "Cross into Tsavo East for the day: the Galana River, Lugard Falls and the "
                    "long red-earth plains where the big herds move."
                ),
            },
            {
                "day": "Day 3",
                "title": "Morning drive and onward",
                "detail": (
                    "Early game drive, breakfast, then onward to Nairobi, Mombasa or your "
                    "coastal hotel."
                ),
            },
        ],
        "accommodation": [
            {"tier": "Luxury", "description": "Lodges or camps with waterhole frontage in Tsavo West or East, full board."},
            {"tier": "Mid-range", "description": "Comfortable park lodges with full board and pool."},
            {"tier": "Coast combination", "description": "Lodges positioned for an easy transfer to Mombasa or Diani."},
        ],
        "inclusions": [
            "Private 4x4 safari vehicle with pop-up roof and professional driver-guide",
            "Two nights full-board accommodation in Tsavo",
            "Park entry fees for Tsavo East and Tsavo West as drawn",
            "Game drives morning and afternoon plus one full day across both parks",
            "Bottled drinking water in the vehicle throughout",
            "Transfers from Nairobi or the coast as quoted",
            "24/7 WhatsApp support from your Horizon Legacy consultant",
        ],
        "exclusions": [
            "International flights and domestic flights unless quoted",
            "Kenya eTA, visas and travel insurance",
            "Alcoholic drinks, premium beverages and laundry",
            "Gratuities for guides and lodge staff",
            "Any item not listed under inclusions",
        ],
        "bestFor": "Families combining a festive beach stay with a short, big-park safari",
    },
    {
        "id": "tsavo-seasonal",
        "slug": "tsavo-seasonal",
        "title": "Tsavo National Park - Seasonal Safari",
        "shortTitle": "Tsavo Seasonal Safari",
        "group": "Kenya Safaris",
        "country": "Kenya",
        "destinationSlug": "tsavo-national-parks",
        "destinationName": "Tsavo East & Tsavo West National Parks",
        "season": "Year-round",
        "duration": "4 Days / 3 Nights",
        "durationDays": 4,
        "startsFrom": "Nairobi or Mombasa",
        "travelStyle": "Private 4x4 safari",
        "priceNote": "Price on request",
        "tagline": "Four days across both Tsavos, at the pace the season allows",
        "summary": (
            "A longer Tsavo itinerary for travellers who are not tied to the holiday calendar. "
            "The extra day opens up the quieter corners: Lake Jipe, the Taita Hills and the "
            "western lava fields, without rushing the classic Mzima and Galana stops."
        ),
        "heroImage": "/assets/images/destinations/tsavo-card.jpg",
        "cardImage": "/assets/images/destinations/tsavo.jpg",
        "gallery": [
            {"url": "/assets/images/destinations/tsavo-card.jpg", "caption": "A red-dust elephant in the Tsavo scrub"},
            {"url": "/assets/images/destinations/tsavo.jpg", "caption": "Elephants at a waterhole in Tsavo West"},
            {"url": "/assets/images/destinations/hero-safari.jpg", "caption": "Acacia savannah on the Tsavo road"},
        ],
        "highlights": [
            "Both Tsavo parks without a rushed transfer day",
            "Lake Jipe birdlife on the Tanzanian border",
            "Taita Hills scenery and the road through the Sagala hills",
            "Mzima Springs and Shetani lava flows with time to linger",
            "Easy to combine with Amboseli or a coastal finish",
        ],
        "itinerary": [
            {
                "day": "Day 1",
                "title": "Arrive Tsavo West",
                "detail": "Transfer in, lunch, and an afternoon drive to Mzima Springs.",
            },
            {
                "day": "Day 2",
                "title": "Tsavo West in depth",
                "detail": (
                    "Shetani lava flows, the Chyulu viewpoints and the western waterholes, "
                    "with a picnic lunch in the park."
                ),
            },
            {
                "day": "Day 3",
                "title": "Tsavo East",
                "detail": (
                    "Cross into Tsavo East for the Galana River, Lugard Falls and the red "
                    "plains, returning to camp after sunset."
                ),
            },
            {
                "day": "Day 4",
                "title": "Lake Jipe or the Taita Hills",
                "detail": (
                    "A final morning toward Lake Jipe or the Taita Hills before the transfer "
                    "onward to Nairobi, Mombasa or Amboseli."
                ),
            },
        ],
        "accommodation": [
            {"tier": "Luxury", "description": "Waterhole-facing lodges or tented camps, full board, one night in each park."},
            {"tier": "Mid-range", "description": "Park lodges with full board and pool, positioned for short transfers."},
            {"tier": "Photographer's choice", "description": "Camps with early gate access and waterhole frontage."},
        ],
        "inclusions": [
            "Private 4x4 safari vehicle with pop-up roof and professional driver-guide",
            "Three nights full-board accommodation across both parks",
            "Park entry fees for Tsavo East and Tsavo West",
            "Game drives morning and afternoon across three full days",
            "Bottled drinking water in the vehicle throughout",
            "Transfers from Nairobi or the coast as quoted",
            "24/7 WhatsApp support from your Horizon Legacy consultant",
        ],
        "exclusions": [
            "International flights and domestic flights unless quoted",
            "Kenya eTA, visas and travel insurance",
            "Alcoholic drinks, premium beverages and laundry",
            "Gratuities for guides and lodge staff",
            "Any item not listed under inclusions",
        ],
        "bestFor": "Travellers with flexible dates who want both Tsavos plus the quieter corners",
    },
    # =========================================================================
    # UGANDA SAFARIS
    # =========================================================================
    {
        "id": "uganda-gorilla-kigali",
        "slug": "uganda-gorilla-kigali",
        "title": "Uganda Gorilla Trekking via Kigali",
        "shortTitle": "Gorilla Trekking via Kigali",
        "group": "Uganda Safaris",
        "country": "Uganda",
        "destinationSlug": "bwindi-impenetrable-forest",
        "destinationName": "Bwindi Impenetrable Forest",
        "season": "Year-round",
        "duration": "5 Days / 4 Nights",
        "durationDays": 5,
        "startsFrom": "Kigali, Rwanda",
        "travelStyle": "Private 4x4 with gorilla permit",
        "priceNote": "Price on request",
        "tagline": "Kigali, the volcanoes and a morning with mountain gorillas",
        "summary": (
            "The shortest route to Bwindi runs through Rwanda: fly into Kigali, drive west "
            "through the Virunga foothills, and trek in Uganda's Impenetrable Forest. The extra "
            "day in Kigali adds the Genocide Memorial and the city's craft and coffee scene."
        ),
        "heroImage": "/assets/images/destinations/uganda-gorilla.jpg",
        "cardImage": "/assets/images/destinations/uganda-gorilla-card.jpg",
        "gallery": [
            {"url": "/assets/images/destinations/uganda-gorilla.jpg", "caption": "A mountain gorilla feeding in Bwindi's undergrowth"},
            {"url": "/assets/images/destinations/uganda-gorilla-card.jpg", "caption": "Close encounter with a Bwindi gorilla family"},
            {"url": "/assets/images/destinations/hero-safari.jpg", "caption": "The road west from Kigali"},
        ],
        "highlights": [
            "One full guided gorilla trek in Bwindi Impenetrable Forest",
            "Kigali Genocide Memorial and city orientation",
            "The Virunga volcanoes on the drive to the trailhead",
            "Batwa and community experiences around the forest edge",
            "Gorilla permits arranged on your behalf at the official rate",
        ],
        "itinerary": [
            {
                "day": "Day 1",
                "title": "Arrive Kigali",
                "detail": (
                    "Airport meet and transfer, then a guided visit to the Genocide Memorial "
                    "and an orientation drive through the city."
                ),
            },
            {
                "day": "Day 2",
                "title": "Kigali to Bwindi",
                "detail": (
                    "Drive west through Ruhengeri and the Virunga foothills, crossing into "
                    "Uganda at Cyanika or Katuna. Afternoon arrival at your lodge near the "
                    "trailhead."
                ),
            },
            {
                "day": "Day 3",
                "title": "Gorilla trekking day",
                "detail": (
                    "Early briefing at the park headquarters, then trekking with rangers and "
                    "trackers to a habituated family. One hour with the gorillas, then back to "
                    "the lodge for the afternoon at rest."
                ),
            },
            {
                "day": "Day 4",
                "title": "Community and Lake Bunyonyi",
                "detail": (
                    "A Batwa or community visit in the morning, then the drive to Lake Bunyonyi "
                    "for the afternoon and a quiet night on the water."
                ),
            },
            {
                "day": "Day 5",
                "title": "Return to Kigali",
                "detail": (
                    "Drive back across the border and transfer to Kigali airport for your "
                    "onward flight."
                ),
            },
        ],
        "accommodation": [
            {"tier": "Luxury", "description": "Forest-edge lodges with private decks near the trailhead, full board."},
            {"tier": "Mid-range", "description": "Comfortable lodges close to the park headquarters, full board."},
            {"tier": "Kigali city", "description": "City hotel for the arrival night, breakfast included."},
        ],
        "inclusions": [
            "Private 4x4 vehicle with driver-guide throughout",
            "Four nights accommodation as per the itinerary, full board in Bwindi",
            "Gorilla permit secured on your behalf (permit fee quoted at the official rate)",
            "Kigali Genocide Memorial visit and city orientation",
            "Community or Batwa experience",
            "Bottled drinking water in the vehicle throughout",
            "24/7 WhatsApp support from your Horizon Legacy consultant",
        ],
        "exclusions": [
            "International flights",
            "Rwanda and Uganda visas",
            "Travel insurance",
            "Gorilla permit fee itself (quoted separately at the official rate)",
            "Alcoholic drinks, premium beverages and laundry",
            "Gratuities for guides, trackers and lodge staff",
            "Any item not listed under inclusions",
        ],
        "bestFor": "Travellers flying into Kigali who want the shortest route to the gorillas",
    },
    {
        "id": "uganda-gorilla-trekking",
        "slug": "uganda-gorilla-trekking",
        "title": "Uganda Gorilla Trekking Safari",
        "shortTitle": "Uganda Gorilla Trekking Safari",
        "group": "Uganda Safaris",
        "country": "Uganda",
        "destinationSlug": "bwindi-impenetrable-forest",
        "destinationName": "Bwindi Impenetrable Forest",
        "season": "Year-round",
        "duration": "4 Days / 3 Nights",
        "durationDays": 4,
        "startsFrom": "Entebbe or Kampala",
        "travelStyle": "Private 4x4 with gorilla permit",
        "priceNote": "Price on request",
        "tagline": "Entebbe to the Impenetrable Forest and back",
        "summary": (
            "A focused Uganda-only gorilla trip. Fly into Entebbe, drive southwest through "
            "Kabale's terraced hills to Bwindi, trek with the gorillas, and return through "
            "Lake Bunyonyi. Four days, no border crossing."
        ),
        "heroImage": "/assets/images/destinations/uganda-gorilla-card.jpg",
        "cardImage": "/assets/images/destinations/uganda-gorilla.jpg",
        "gallery": [
            {"url": "/assets/images/destinations/uganda-gorilla-card.jpg", "caption": "Close encounter with a Bwindi gorilla family"},
            {"url": "/assets/images/destinations/uganda-gorilla.jpg", "caption": "A mountain gorilla feeding in Bwindi's undergrowth"},
            {"url": "/assets/images/destinations/hero-safari.jpg", "caption": "Terraced hills on the road to Bwindi"},
        ],
        "highlights": [
            "One full guided gorilla trek in Bwindi Impenetrable Forest",
            "The terraced hills of Kabale and Lake Bunyonyi",
            "Community coffee and craft visits en route",
            "Time to rest at the lodge after the trek",
            "Gorilla permits arranged on your behalf at the official rate",
        ],
        "itinerary": [
            {
                "day": "Day 1",
                "title": "Entebbe to Bwindi",
                "detail": (
                    "Early departure from Entebbe or Kampala, driving southwest through Mbarara "
                    "and Kabale to the forest edge. Evening arrival."
                ),
            },
            {
                "day": "Day 2",
                "title": "Gorilla trekking",
                "detail": (
                    "Briefing at the park headquarters, trekking with rangers and trackers, "
                    "and one hour with a habituated gorilla family. Afternoon at leisure."
                ),
            },
            {
                "day": "Day 3",
                "title": "Forest edge and Lake Bunyonyi",
                "detail": (
                    "Community visit or a second trek if permits allow, then the drive to "
                    "Lake Bunyonyi for the afternoon."
                ),
            },
            {
                "day": "Day 4",
                "title": "Return to Entebbe",
                "detail": (
                    "Drive back to Entebbe with a stop in Mbarara, arriving in the evening for "
                    "your onward flight."
                ),
            },
        ],
        "accommodation": [
            {"tier": "Luxury", "description": "Forest-edge lodges with private decks near the trailhead, full board."},
            {"tier": "Mid-range", "description": "Comfortable lodges close to the park headquarters, full board."},
            {"tier": "Lakeside", "description": "Lake Bunyonyi cottages for the final night, bed and breakfast."},
        ],
        "inclusions": [
            "Private 4x4 vehicle with driver-guide throughout",
            "Three nights accommodation as per the itinerary, full board in Bwindi",
            "Gorilla permit secured on your behalf (permit fee quoted at the official rate)",
            "Community or coffee experience",
            "Bottled drinking water in the vehicle throughout",
            "24/7 WhatsApp support from your Horizon Legacy consultant",
        ],
        "exclusions": [
            "International flights",
            "Uganda visa",
            "Travel insurance",
            "Gorilla permit fee itself (quoted separately at the official rate)",
            "Alcoholic drinks, premium beverages and laundry",
            "Gratuities for guides, trackers and lodge staff",
            "Any item not listed under inclusions",
        ],
        "bestFor": "Travellers who want a compact Uganda-only gorilla trip",
    },
]

# -----------------------------------------------------------------------------
# EXISTING BOOKABLE GETAWAY
# -----------------------------------------------------------------------------
# The Encore Hotel Nakuru getaway already sells from /packages/encore-hotel-nakuru/.
# It is listed here so every bookable package sits in one catalogue, but its
# record is derived from the live PACKAGES entry rather than copied, and its
# card links straight to the page that already prices and sells it.
_ENCORE = next(p for p in _BOOKABLE_PACKAGES if p["id"] == "encore-hotel-nakuru-2d1n")

SAFARI_PACKAGES.append({
    "id": _ENCORE["id"],
    "slug": "encore-hotel-nakuru",
    "title": _ENCORE["title"],
    "shortTitle": "Encore Hotel Nakuru Getaway",
    "group": "Kenya Getaways",
    "country": "Kenya",
    "safariType": "Hotel Getaway",
    "luxuryLevel": "Luxury",
    "regions": ["Lake Nakuru"],
    "destinationSlug": _ENCORE["destinationId"],
    "destinationName": "Lake Nakuru",
    "season": "Year-round",
    "duration": _ENCORE["duration"],
    "durationDays": 2,
    "startsFrom": "Nakuru (self-drive)",
    "travelStyle": "Hotel stay with optional game drive",
    "priceNote": _ENCORE["price"],
    "detailPath": _ENCORE["url"],
    "tagline": "One night of full-board comfort in Nakuru, minutes from the park gate",
    "summary": (
        "The shortest bookable escape on this page: a two-and-a-half hour drive from Nairobi "
        "to The Encore Hotel Nakuru for a night of full-board dining, a heated pool and "
        "gardens, with Lake Nakuru's rhino and flamingo shores a short drive away. Self-drive "
        "and transport-inclusive rates are published on the package page."
    ),
    "heroImage": "/assets/images/destinations/lake-nakuru.jpg",
    "cardImage": "/assets/images/destinations/lake-nakuru-card.jpg",
    "gallery": [
        {"url": "/assets/images/destinations/lake-nakuru.jpg", "caption": "Lake Nakuru and its shoreline"},
        {"url": "/assets/images/destinations/lake-nakuru-card.jpg", "caption": "Flamingo-pink water at Lake Nakuru"},
    ],
    "highlights": [
        "One night at The Encore Hotel Nakuru in your chosen room category",
        "Full board: breakfast, two lunches and dinner",
        "Heated pool, gym and landscaped gardens",
        "Optional early-morning Lake Nakuru game drive",
        "Weekend-friendly: leave Nairobi in the morning, back the next afternoon",
    ],
    "itinerary": [
        {
            "day": "Day 1",
            "title": "Nairobi to Nakuru",
            "detail": (
                "Depart Nairobi in the morning with a stop at the Rift Valley viewpoint, arrive "
                "in Nakuru for check-in and buffet lunch, then spend the afternoon at the pool or "
                "on an optional Menengai Crater excursion. Dinner at the hotel."
            ),
        },
        {
            "day": "Day 2",
            "title": "Lake Nakuru and return",
            "detail": (
                "Optional dawn game drive in Lake Nakuru National Park for rhino, Rothschild "
                "giraffe and flamingo, breakfast back at the hotel, then a leisurely check-out "
                "and the drive back to Nairobi."
            ),
        },
    ],
    "accommodation": [
        {"tier": "Deluxe", "description": "Standard room with balcony and garden view, full board."},
        {"tier": "Executive", "description": "Suite with a separate living area and pool view, full board."},
        {"tier": "Presidential", "description": "Top-floor suite with private jacuzzi and panoramic Rift Valley views, full board."},
    ],
    "inclusions": [
        "One night at The Encore Hotel Nakuru in the selected room category",
        "Full board meal plan (breakfast, two lunches, one dinner)",
        "Hotel amenities: heated pool, gym and gardens",
        "Complimentary high-speed WiFi",
        "Secure on-site parking",
        "Government taxes and service charges",
        "Pre-trip WhatsApp support from the Horizon Legacy team",
    ],
    "exclusions": [
        "Transport unless the transport-inclusive rate is selected",
        "Lake Nakuru National Park entry fees",
        "Alcoholic and specialty beverages",
        "Spa treatments",
        "Personal expenses and gratuities",
        "Travel and medical insurance",
    ],
    "bestFor": "Couples, families and weekending residents who want comfort without a long drive",
})


# -----------------------------------------------------------------------------
# CARD BLURBS
# -----------------------------------------------------------------------------
# One short, self-contained sentence per seasonal package so a card never has to
# clip a longer paragraph mid-word. The 30 catalogue concepts carry their own
# cardSummary from safari_packages_base.pkg().
_CARD_SUMMARIES = {
    "amboseli-festive": "Festive-season elephants beneath Kilimanjaro, with the swamps busy and the light clear.",
    "amboseli-shoulder": "Quieter Amboseli: cleaner air, fewer vehicles at every sighting, elephants relaxed in the swamps.",
    "maasai-mara-festive": "Big cats, open plains and long festive light - the Mara at its most theatrical.",
    "maasai-mara-shoulder": "Short grass, easier cats and a fraction of the holiday traffic across the Mara.",
    "samburu-festive": "Doum palms, dry-country species and the Ewaso Ng'iro at a gentler festive pace.",
    "samburu-shoulder": "An extra day for Buffalo Springs, a conservancy walk or a slow morning with a river herd.",
    "sand-river-maasai-mara": "Conservancy access on the Sand River: off-road tracking, night drives and walking.",
    "tsavo-festive": "Tsavo East and West in one trip - red dust, lava ridges and spring-fed pools.",
    "tsavo-seasonal": "A longer Tsavo loop for travellers who are not tied to the holiday calendar.",
    "uganda-gorilla-kigali": "Fly into Kigali, cross into Bwindi and trek the Impenetrable Forest.",
    "uganda-gorilla-trekking": "A compact Uganda-only gorilla trek built around one permit and one forest.",
    "encore-hotel-nakuru": "One night of full-board comfort in Nakuru, with Lake Nakuru's rhinos a short drive away.",
}

for _pkg in SAFARI_PACKAGES:
    if not _pkg.get("cardSummary"):
        _pkg["cardSummary"] = _CARD_SUMMARIES[_pkg["slug"]]


# -----------------------------------------------------------------------------
# THE 30 RESEARCHED CONCEPTS
# -----------------------------------------------------------------------------
# The seasonal offers keep their own section at the end of the catalogue so the
# country sections hold exactly the 30 concepts above.
for _pkg in SAFARI_PACKAGES:
    if _pkg["group"] in ("Kenya Safaris", "Uganda Safaris"):
        _pkg["group"] = "Seasonal & Festive Offers"

SAFARI_PACKAGES.extend(CATALOGUE_PACKAGES)


# -----------------------------------------------------------------------------
# NORMALISATION
# -----------------------------------------------------------------------------
# Older records predate some fields. Fill them here rather than editing eleven
# dicts, and pull destination copy from the destination dataset where a package
# points at a destination that already has a page.
_DESTINATION_BY_SLUG = {d["slug"]: d for d in _DESTINATIONS}

_LEGACY_SAFARI_TYPES = {
    "amboseli": "Elephant Safari",
    "maasai-mara": "Big Five Wildlife",
    "samburu": "Special Five Wildlife",
    "tsavo-national-parks": "Big Five Wildlife",
    "bwindi-impenetrable-forest": "Primates & Gorillas",
    "lake-nakuru": "Rift Valley Lakes",
}

for _pkg in SAFARI_PACKAGES:
    _dest = _DESTINATION_BY_SLUG.get(_pkg.get("destinationSlug") or "")
    _pkg.setdefault("country", "Kenya")
    _pkg.setdefault("regions", [_pkg["destinationName"]])
    _pkg.setdefault("safariType", _LEGACY_SAFARI_TYPES.get(_pkg.get("destinationSlug"), "Seasonal Offer"))
    _pkg.setdefault("luxuryLevel", "Mid-range")
    _pkg.setdefault("durationBucket", duration_bucket(_pkg.get("durationDays", 3)))
    _pkg.setdefault("status", "published")
    _pkg.setdefault("validity", _pkg.get("season") or "Year-round - quoted for your dates")
    _pkg.setdefault("price", None)
    _pkg.setdefault("travelInfo", list(BASE_TRAVEL_INFO))
    _pkg.setdefault("activities", list(_dest["activities"]) if _dest else [])
    if not _pkg.get("destinationOverview"):
        _pkg["destinationOverview"] = _dest["overview"] if _dest else _pkg.get("summary", "")


# -----------------------------------------------------------------------------
# LOOKUPS AND VOCABULARIES
# -----------------------------------------------------------------------------
SAFARI_PACKAGES_BY_SLUG = {p["slug"]: p for p in SAFARI_PACKAGES}
SAFARI_PACKAGE_GROUPS = SAFARI_GROUPS

# Published records only - drafts stay in the data file and never reach a page.
PUBLISHED_PACKAGES = [p for p in SAFARI_PACKAGES if p.get("status", "published") == "published"]


def filter_options():
    """The values the catalogue filter bar offers, in catalogue order."""
    countries, destinations, types, buckets, levels = [], [], [], [], []
    for p in PUBLISHED_PACKAGES:
        if p["country"] not in countries:
            countries.append(p["country"])
        for region in p.get("regions", []):
            if region not in destinations:
                destinations.append(region)
        if p["safariType"] not in types:
            types.append(p["safariType"])
        if p["durationBucket"] not in buckets:
            buckets.append(p["durationBucket"])
        if p["luxuryLevel"] not in levels:
            levels.append(p["luxuryLevel"])
    country_order = [c for c in COUNTRY_ORDER if c in countries]
    country_order += [c for c in countries if c not in country_order]
    bucket_order = ["1 Day", "2-3 Days", "4-6 Days", "7-9 Days", "10+ Days"]
    level_order = [l for l in LUXURY_LEVELS if l in levels]
    return {
        "countries": country_order,
        "destinations": destinations,
        "types": types,
        "durations": [b for b in bucket_order if b in buckets],
        "luxury": level_order,
    }
