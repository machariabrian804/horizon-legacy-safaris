# -*- coding: utf-8 -*-
"""
The Horizon Legacy safari catalogue: 30 researched package concepts plus the
sample itinerary builder.

Package records live in the three modules below so each file stays readable:

    safari_packages_kenya.py   - Kenya (20)
    safari_packages_east.py    - Tanzania (5), Uganda (3), Rwanda (2)

Everything is re-exported here as one list, which is what the page builder and
the site data file consume. Editing a record in those files changes the card,
the filters and the detail page together.
"""

from safari_packages_kenya import KENYA_PACKAGES
from safari_packages_east import TANZANIA_PACKAGES, UGANDA_RWANDA_PACKAGES

CATALOGUE_PACKAGES = KENYA_PACKAGES + TANZANIA_PACKAGES + UGANDA_RWANDA_PACKAGES

# Group order on the catalogue page. The seasonal offers and the Encore stay
# live at the end so the country sections read cleanly.
SAFARI_GROUPS = [
    "Kenya Safaris",
    "Tanzania Safaris",
    "Uganda Safaris",
    "Rwanda Safaris",
    "Kenya Getaways",
    "Seasonal & Festive Offers",
]

COUNTRY_ORDER = ["Kenya", "Tanzania", "Uganda", "Rwanda"]

LUXURY_LEVELS = ["Luxury", "Mid-range", "Comfort"]


# -----------------------------------------------------------------------------
# SAMPLE ITINERARY
# -----------------------------------------------------------------------------
# One polished route showing how Horizon Legacy joins several destinations in a
# single journey. Destinations and their sequence only - no hotel names, no
# booking references, no fixed dates and no prices.
SAMPLE_ITINERARIES = [
    {
        "slug": "seven-day-best-of-kenya",
        "title": "7-Day Best of Kenya Safari",
        "kicker": "Sample Safari Itineraries",
        "summary": (
            "A seven-day route that links the elephants of Amboseli with the Rift Valley lakes and "
            "finishes in the Maasai Mara. It is the shape we use most often when a first Kenya trip "
            "has one week: one southern park, two lakes, and three Mara nights for the big cats."
        ),
        "route": [
            "Amboseli National Park",
            "Lake Naivasha",
            "Lake Nakuru National Park",
            "Maasai Mara National Reserve",
        ],
        "duration": "7 days / 6 nights",
        "stops": [
            {
                "day": "Day 1",
                "destination": "Amboseli National Park",
                "title": "Arrival and first look at Amboseli",
                "detail": (
                    "Arrive in Amboseli and settle in, then take a late-afternoon drive into the park "
                    "as the light drops and the elephant herds move toward the swamps."
                ),
                "image": "/assets/images/destinations/amboseli.jpg",
                "caption": "Elephants beneath Kilimanjaro",
                "stay": "Amboseli area - camp or lodge matched to your budget band",
                "transfer": "Road transfer from Nairobi into Amboseli",
            },
            {
                "day": "Day 2",
                "destination": "Amboseli National Park",
                "title": "A full day with the elephants",
                "detail": (
                    "A dawn drive when Kilimanjaro is usually clearest, then the swamps and "
                    "Observation Hill through the middle of the day. Time with the big-tusker herds "
                    "is the point of the day, with the mountain behind them."
                ),
                "image": "/assets/images/destinations/amboseli-card.jpg",
                "caption": "Elephants crossing the Amboseli plains",
                "stay": "Amboseli area",
                "transfer": "Road transfer from Amboseli to Lake Naivasha",
            },
            {
                "day": "Day 3",
                "destination": "Lake Naivasha",
                "title": "North to the Rift Valley water",
                "detail": (
                    "Travel from Amboseli to Lake Naivasha, watching the country change as the road "
                    "climbs into the Rift Valley. The afternoon is left open for optional lake "
                    "experiences: a boat trip past hippo and fish eagle, or a walk on Crescent Island."
                ),
                "image": "/assets/images/destinations/lake-naivasha.jpg",
                "caption": "Lake Naivasha and its shoreline",
                "stay": "Naivasha lakeside",
                "transfer": "Road transfer from Naivasha to Lake Nakuru",
            },
            {
                "day": "Day 4",
                "destination": "Lake Nakuru National Park",
                "title": "Rhino and flamingo country",
                "detail": (
                    "Travel to Lake Nakuru National Park for a day of wildlife viewing: black and "
                    "white rhino, Rothschild giraffe, buffalo and flamingo along the alkaline shore. "
                    "Baboon Cliff and the northern shoreline give the widest views over the lake."
                ),
                "image": "/assets/images/destinations/lake-nakuru.jpg",
                "caption": "Lake Nakuru and its shoreline",
                "stay": "Nakuru area",
                "transfer": "Road transfer from Nakuru into the Maasai Mara",
            },
            {
                "day": "Day 5",
                "destination": "Maasai Mara National Reserve",
                "title": "Into the Mara",
                "detail": (
                    "Travel to the Maasai Mara and settle in. An afternoon game drive follows, "
                    "subject to arrival time, working the nearest river line as elephant and "
                    "buffalo come down to drink."
                ),
                "image": "/assets/images/destinations/maasai-mara.jpg",
                "caption": "Lion pride on the Mara plains",
                "stay": "Mara area - camp or lodge on the reserve or a bordering conservancy",
                "transfer": "Full day in the reserve, no transfer",
            },
            {
                "day": "Day 6",
                "destination": "Maasai Mara National Reserve",
                "title": "A full day in the Mara",
                "detail": (
                    "A full-day safari with opportunities for the Big Five and everything else the "
                    "reserve holds: lion, cheetah, elephant, buffalo and, with patience, leopard. "
                    "Picnic lunch on the plains and a late return to camp."
                ),
                "image": "/assets/images/destinations/maasai-mara-card.jpg",
                "caption": "Acacia and open savannah in the reserve",
                "stay": "Mara area",
                "transfer": "Final morning in the Mara, then departure",
            },
            {
                "day": "Day 7",
                "destination": "Maasai Mara National Reserve",
                "title": "Final morning and departure",
                "detail": (
                    "One last early game drive or a slow breakfast overlooking the plains, followed "
                    "by departure arrangements: the road back to Nairobi, or a light-aircraft flight "
                    "from a Mara airstrip."
                ),
                "image": "/assets/images/destinations/maasai-mara-balloon.jpg",
                "caption": "First light over the Mara",
                "stay": "Departure day",
                "transfer": None,
            },
        ],
        "notes": [
            "This is an illustrative itinerary, not a confirmed departure. Dates, lodges and the order of the middle days are set at quotation.",
            "Wildlife sightings - including elephants, rhino and the Big Five - are never guaranteed.",
            "Accommodation is suggested by area and budget band only. Property names are shared with your written quote.",
            "Any of the seven days can be extended, re-paced or swapped. Ask us to rebuild the route around your dates.",
        ],
    },
]
