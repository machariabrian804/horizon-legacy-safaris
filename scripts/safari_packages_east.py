# -*- coding: utf-8 -*-
"""Tanzania, Uganda and Rwanda safari packages (21-30)."""

from safari_packages_base import pkg

TANZANIA_PACKAGES = [
    # 21 -----------------------------------------------------------------
    pkg(
        slug="serengeti-migration",
        title="Serengeti Great Migration Safari",
        short="Serengeti Migration",
        group="Tanzania Safaris",
        country="Tanzania",
        destination="Serengeti National Park",
        destination_slug="serengeti",
        days=6,
        duration="6 Days / 5 Nights",
        safari_type="Great Migration",
        luxury="Mid-range",
        tagline="The long plains, the herds and nowhere else to be",
        summary=(
            "The Serengeti is roughly fourteen thousand square kilometres of grass and granite, and "
            "the migration moves across it through the year. Six days gives you time to follow the "
            "herds rather than chase them: river crossings in the north when the season is right, "
            "calving grounds in the south-east when it is not, and lion, cheetah and leopard working "
            "the same country throughout."
        ),
        card="Six days across the Serengeti with the route set by the herds.",
        hero="serengeti.jpg",
        gallery=[
            ("serengeti.jpg", "Wildebeest crossing the Serengeti plains"),
            ("serengeti-plains.jpg", "The migration herds spread across the grassland"),
            ("ngorongoro.jpg", "The highlands above the Serengeti"),
        ],
        highlights=[
            "Herd tracking across the central and northern Serengeti",
            "Seronera's resident lion, leopard and cheetah",
            "River-crossing watch points when the herds are in the north",
            "Granite kopjes and the Moru kopjes rock art country",
            "A full day with no set route beyond following the wildlife",
        ],
        itinerary=[
            ("Arusha to the central Serengeti",
             "Collect in Arusha, drive via the Ngorongoro highlands and into the park, with a "
             "game drive en route to camp at Seronera. Evening drive."),
            ("Seronera",
             "Full day in the central Serengeti: the river lines, the kopjes and the big-cat "
             "territories around the Seronera valley."),
            ("Central to the north or south",
             "Move with the herds, north toward the Mara river if the season is right, or south "
             "toward the short-grass plains when they are not."),
            ("North or south",
             "Full day in whichever sector the herds are using, with a picnic lunch and an "
             "unhurried pace."),
            ("Return toward the central plains",
             "A last morning drive in the herd sector, then south toward the Naabi gate area."),
            ("Serengeti to Arusha",
             "Early game drive out of the park, then the drive back to Arusha, arriving in the "
             "evening."),
        ],
        accommodation=[
            ("Luxury", "Tented suites in the park's central and northern sectors, full board."),
            ("Mid-range", "Public campsites and seasonal camps, full board."),
            ("Mobile-style", "Camps that move with the herds, full board, booked well ahead."),
        ],
        activities=[
            "Migration-season game drives",
            "River-crossing watch points in season",
            "Big-cat tracking around the kopjes",
            "Picnic lunches in the park",
            "Optional balloon safari at extra cost",
            "Birding along the Seronera river",
        ],
        best_for="Wildlife travellers who can be flexible on dates and want the herds",
        starts="Arusha",
        style="Private 4x4 safari with a campsite or lodge base",
    ),
    # 22 -----------------------------------------------------------------
    pkg(
        slug="ngorongoro-crater",
        title="Ngorongoro Crater Wildlife Safari",
        short="Ngorongoro Crater",
        group="Tanzania Safaris",
        country="Tanzania",
        destination="Ngorongoro Crater",
        destination_slug="ngorongoro",
        days=3,
        duration="3 Days / 2 Nights",
        safari_type="Big Five Wildlife",
        luxury="Mid-range",
        tagline="A collapsed volcano, a full floor of wildlife, one honest day inside it",
        summary=(
            "The crater is a caldera roughly twenty kilometres across with a self-contained population "
            "of lion, elephant, buffalo, black rhino and flamingo on the floor. It is also one of the "
            "busiest sites in East Africa, so this short break is built to get you down early and out "
            "ahead of the midday convoy, with the surrounding highlands and a Maasai area on the "
            "second day."
        ),
        card="Early descent into the crater for rhino, lion and flamingo, before the crowds.",
        hero="ngorongoro.jpg",
        gallery=[
            ("ngorongoro.jpg", "The crater floor and Lake Magadi"),
            ("ngorongoro-plains.jpg", "Zebra and buffalo on the crater floor"),
            ("tarangire.jpg", "Elephant country on the drive between parks"),
        ],
        highlights=[
            "An early descent into the crater, ahead of the main convoy",
            "Black rhino and lion on the crater floor",
            "Flamingo and soda lake scenery at Lake Magadi",
            "Crater-rim viewpoints across the caldera",
            "Highland forest and a Maasai area visit on the second day",
        ],
        itinerary=[
            ("Arusha to the crater rim",
             "Drive via Karatu and up through the highland forest to the rim, arriving for lunch. "
             "Afternoon at leisure with the caldera below."),
            ("Down into the crater",
             "Early descent through the forest, then a full morning on the floor working the "
             "rhino areas and the Lerai forest. Picnic lunch by the lake, back up by mid-afternoon."),
            ("Highlands and return",
             "Morning in the highlands or a Maasai area visit, then the drive back to Arusha, "
             "arriving in the afternoon."),
        ],
        accommodation=[
            ("Luxury", "Crater-rim lodges with caldera views, full board."),
            ("Mid-range", "Rim and highland lodges, full board."),
            ("Comfort", "Highland guesthouses near Karatu, dinner, bed and breakfast."),
        ],
        activities=[
            "Crater floor game drive",
            "Crater-rim viewpoint stops",
            "Lake Magadi flamingo viewing",
            "Highland forest walk",
            "Maasai area visit arranged locally",
            "Optional visit to a coffee farm near Karatu",
        ],
        best_for="Short trips out of Arusha and travellers adding Tanzania to a Kenya safari",
        starts="Arusha",
    ),
    # 23 -----------------------------------------------------------------
    pkg(
        slug="tarangire-ngorongoro",
        title="Tarangire and Ngorongoro Safari",
        short="Tarangire & Ngorongoro",
        group="Tanzania Safaris",
        country="Tanzania",
        destination="Tarangire \\u0026 Ngorongoro",
        regions=["Tarangire National Park", "Ngorongoro Crater"],
        destination_slug="ngorongoro",
        days=4,
        duration="4 Days / 3 Nights",
        safari_type="Big Five Wildlife",
        luxury="Mid-range",
        tagline="Baobabs and elephant herds, then down into the caldera",
        summary=(
            "Tarangire is the park people underestimate: huge elephant herds in the dry months, "
            "ancient baobabs, and a river valley that pulls wildlife in from the surrounding "
            "steppe. Combined with the Ngorongoro crater it makes a compact northern-circuit "
            "trip with two very different landscapes, and it avoids the long haul up to the "
            "Serengeti if your time is short."
        ),
        card="Tarangire's baobabs and elephant herds, paired with the Ngorongoro crater floor.",
        hero="tarangire.jpg",
        gallery=[
            ("tarangire.jpg", "Elephants in Tarangire National Park"),
            ("ngorongoro.jpg", "The crater floor and Lake Magadi"),
            ("ngorongoro-plains.jpg", "Zebra and buffalo on the crater floor"),
        ],
        highlights=[
            "Large elephant herds along the Tarangire river in the dry months",
            "Ancient baobabs and the park's swampy river valley",
            "Crater floor access for black rhino and lion",
            "Highland forest on the crater rim",
            "A short northern circuit without the Serengeti drive",
        ],
        itinerary=[
            ("Arusha to Tarangire",
             "Drive south via Makuyuni and into the park, arriving for lunch. Afternoon game "
             "drive along the river."),
            ("Tarangire to the crater highlands",
             "Morning drive in Tarangire, then north through Karatu and up to the crater rim for "
             "the night."),
            ("Ngorongoro Crater",
             "Early descent into the crater, full morning on the floor, picnic lunch by the lake, "
             "back up in the afternoon."),
            ("Highlands and return",
             "Morning drive back toward Arusha with a stop near Lake Manyara, arriving in the "
             "afternoon."),
        ],
        accommodation=[
            ("Luxury", "Lodge and rim accommodation with full board throughout."),
            ("Mid-range", "Park lodges and highland camps, full board."),
            ("Comfort", "Guesthouses near Karatu, dinner, bed and breakfast."),
        ],
        activities=[
            "Tarangire river-valley game drives",
            "Elephant herd viewing in the dry season",
            "Crater floor game drive",
            "Highland viewpoints",
            "Maasai area visit arranged locally",
            "Birding in the Tarangire swamps",
        ],
        best_for="Short northern-circuit trips and travellers who want two landscapes in four days",
        starts="Arusha",
    ),
    # 24 -----------------------------------------------------------------
    pkg(
        slug="tanzania-northern-luxury",
        title="Tanzania Northern Circuit Luxury Safari",
        short="Northern Circuit Luxury",
        group="Tanzania Safaris",
        country="Tanzania",
        destination="Tarangire, Serengeti \\u0026 Ngorongoro",
        regions=["Tarangire National Park", "Serengeti National Park", "Ngorongoro Crater"],
        destination_slug="serengeti",
        days=8,
        duration="8 Days / 7 Nights",
        safari_type="Fly-in Luxury",
        luxury="Luxury",
        tagline="The northern circuit at its own pace, with light-aircraft hops",
        summary=(
            "Tarangire, the Serengeti and the Ngorongoro crater, joined by light aircraft rather than "
            "long road transfers. The savings in time go into the parks: two nights in Tarangire, "
            "three in the Serengeti moving between sectors, and a crater-rim night before an early "
            "descent. High-end camps throughout, with a private vehicle in each park."
        ),
        card="Tarangire, the Serengeti and the crater, joined by light aircraft.",
        hero="serengeti-plains.jpg",
        gallery=[
            ("serengeti-plains.jpg", "The migration herds spread across the grassland"),
            ("ngorongoro.jpg", "The crater floor and Lake Magadi"),
            ("tarangire.jpg", "Elephants in Tarangire National Park"),
        ],
        highlights=[
            "Light-aircraft transfers between Arusha, Tarangire, the Serengeti and the crater highlands",
            "Two Serengeti sectors rather than one static camp",
            "High-end tented suites throughout",
            "Crater descent from a rim lodge, early in the morning",
            "Tarangire's elephant herds at the start of the trip",
        ],
        itinerary=[
            ("Arusha to Tarangire",
             "Light-aircraft hop or a short road transfer into Tarangire, arriving for lunch. "
             "Afternoon game drive along the river."),
            ("Full day in Tarangire",
             "Dawn drive for elephant and baobab country, a long lunch, then an evening drive."),
            ("Tarangire to the Serengeti",
             "Fly from the Tarangire airstrip to the Serengeti, met and driven to camp with a "
             "game drive en route."),
            ("Serengeti",
             "Full day following the herds in the sector they are using."),
            ("Serengeti",
             "Second full day, moving camp or driving a different circuit for big cats."),
            ("Serengeti to the crater highlands",
             "Morning game drive, then a flight or drive to the crater highlands for the night."),
            ("Ngorongoro Crater",
             "Early descent into the crater, full morning on the floor, back up for the afternoon."),
            ("Departure",
             "Drive or fly back to Arusha for your onward connection."),
        ],
        accommodation=[
            ("Luxury", "High-end tented suites in Tarangire and the Serengeti, rim lodge at the crater, full board."),
            ("Luxury family", "Two-bedroom tents and a rim suite for families, full board."),
            ("Classic luxury", "Long-established camps with full board and a private vehicle."),
        ],
        activities=[
            "Game drives in three parks",
            "Light-aircraft transfers between sectors",
            "Big-cat tracking in the Serengeti",
            "Crater floor game drive",
            "Bush breakfasts and sundowners",
            "Optional balloon safari over the Serengeti",
        ],
        best_for="Travellers who want the full northern circuit without long road days",
        starts="Arusha",
        style="Private fly-in safari",
        inclusions=[
            "Internal light-aircraft flights within Tanzania as scheduled",
            "Private 4x4 vehicle and driver-guide in each park",
            "Seven nights full-board luxury accommodation",
            "All park, crater and concession fees for the itinerary as drawn",
            "Airstrip transfers and game drives as scheduled",
            "House beverages as offered by the camps",
            "24/7 WhatsApp support from your Horizon Legacy consultant",
        ],
    ),
    # 25 -----------------------------------------------------------------
    pkg(
        slug="tanzania-zanzibar",
        title="Tanzania Safari and Zanzibar Beach Holiday",
        short="Tanzania & Zanzibar",
        group="Tanzania Safaris",
        country="Tanzania",
        destination="Serengeti, Ngorongoro \\u0026 Zanzibar",
        regions=["Serengeti National Park", "Ngorongoro Crater", "Zanzibar"],
        destination_slug="zanzibar",
        days=9,
        duration="9 Days / 8 Nights",
        safari_type="Beach & Bush",
        luxury="Luxury",
        tagline="Migration country, a crater morning, then the Indian Ocean",
        summary=(
            "Five days on the northern safari circuit and four on Zanzibar, joined by a short flight "
            "from Arusha. The safari half covers Tarangire, the Serengeti and the Ngorongoro crater; "
            "the coastal half is Stone Town's lanes and then a beach on the north or east coast. "
            "It is the most popular Tanzanian combination for a reason, and it works for honeymoons "
            "and for families with older children alike."
        ),
        card="Serengeti and the crater, then four nights on Zanzibar.",
        hero="zanzibar.jpg",
        gallery=[
            ("serengeti.jpg", "Wildebeest crossing the Serengeti plains"),
            ("ngorongoro.jpg", "The crater floor and Lake Magadi"),
            ("zanzibar.jpg", "Dhow sailing at sunset off Stone Town"),
            ("zanzibar-card.jpg", "Turquoise water off the Zanzibar coast"),
        ],
        highlights=[
            "Serengeti game drives and big-cat country",
            "An early descent into the Ngorongoro crater",
            "A flight from Arusha to Zanzibar instead of a long transfer",
            "Stone Town's alleys, doors and waterfront at sunset",
            "Three nights of beach time on the coast",
        ],
        itinerary=[
            ("Arusha to Tarangire",
             "Drive into Tarangire for lunch and an afternoon game drive."),
            ("Tarangire to the Serengeti",
             "Morning drive, then on through the highlands into the Serengeti for the evening."),
            ("Serengeti",
             "Full day following the herds and the cats."),
            ("Serengeti to the crater highlands",
             "Morning game drive, then south to the crater rim for the night."),
            ("Crater and flight to Zanzibar",
             "Early descent into the crater, then transfer to Arusha for the afternoon flight to "
             "Zanzibar. Transfer to Stone Town or the coast."),
            ("Zanzibar",
             "Stone Town walking tour in the morning, then transfer to the beach for the afternoon."),
            ("Zanzibar",
             "Full beach day: reef, dhow or simply the sand."),
            ("Zanzibar",
             "Second beach day with optional spice-farm or snorkelling excursion."),
            ("Departure",
             "Breakfast and transfer to Zanzibar airport for your flight home."),
        ],
        accommodation=[
            ("Luxury", "Tented suites on safari and a beachfront suite on Zanzibar, half board on the coast."),
            ("Luxury family", "Family tents on safari and a two-bedroom beach villa."),
            ("Boutique", "Small safari camps and a boutique Stone Town or beach hotel."),
        ],
        activities=[
            "Game drives in Tarangire, the Serengeti and the crater",
            "Stone Town walking tour",
            "Dhow sailing and sunset cruises",
            "Reef snorkelling and diving",
            "Spice farm visit",
            "Optional balloon safari over the Serengeti",
        ],
        best_for="Honeymoons and long-haul trips that want safari plus a real beach",
        starts="Arusha",
        style="Private safari with a coastal stay",
    ),
]

UGANDA_RWANDA_PACKAGES = [
    # 26 -----------------------------------------------------------------
    pkg(
        slug="bwindi-gorilla-trekking",
        title="Bwindi Mountain Gorilla Trekking",
        short="Bwindi Gorilla Trekking",
        group="Uganda Safaris",
        country="Uganda",
        destination="Bwindi Impenetrable Forest",
        destination_slug="bwindi-impenetrable-forest",
        days=4,
        duration="4 Days / 3 Nights",
        safari_type="Primates & Gorillas",
        luxury="Mid-range",
        tagline="One hour with a gorilla family, and a very long walk to get there",
        summary=(
            "Bwindi is a 25,000-year-old forest on the Albertine rift, and the trek to a habituated "
            "gorilla family can take anywhere from two to eight hours depending on where they nested "
            "the night before. You get one hour with them when you arrive. This itinerary keeps a "
            "spare day in Bwindi so a permit day is not lost to a travel delay, and pairs the trek "
            "with Lake Bunyonyi on the way out."
        ),
        card="A gorilla family in Bwindi, with a spare day built in around the trek.",
        hero="uganda-gorilla.jpg",
        gallery=[
            ("uganda-gorilla.jpg", "Mountain gorilla in the Bwindi forest"),
            ("uganda-gorilla-card.jpg", "Gorilla family in the Impenetrable Forest"),
            ("rwanda-hills.jpg", "The Albertine rift highlands"),
        ],
        highlights=[
            "A permit-secured trek to a habituated mountain gorilla family",
            "One hour with the family, with porters and rangers throughout",
            "The Buhoma or Nkuringo trailheads, matched to fitness and permit availability",
            "Lake Bunyonyi for the final night",
            "A spare day so a travel delay does not cost the trek",
        ],
        itinerary=[
            ("Entebbe to Bwindi",
             "Early start from Entebbe or Kampala for the long drive southwest through Mbarara and "
             "Kabale, arriving in Bwindi in the evening. Alternatively fly to Kihihi and drive in."),
            ("Gorilla trekking",
             "Briefing at the park headquarters, then trekking with rangers and trackers. One hour "
             "with the family, then back to the lodge for a late lunch and a quiet afternoon."),
            ("Bwindi to Lake Bunyonyi",
             "A community or coffee experience in the morning, then the drive to Lake Bunyonyi for "
             "the afternoon and night."),
            ("Return to Entebbe",
             "Drive back to Entebbe with a stop in Mbarara, arriving in the evening for your "
             "onward flight."),
        ],
        accommodation=[
            ("Luxury", "Forest-edge lodges with private decks near the trailhead, full board."),
            ("Mid-range", "Comfortable lodges close to the park headquarters, full board."),
            ("Lakeside", "Lake Bunyonyi cottages for the final night, bed and breakfast."),
        ],
        activities=[
            "Mountain gorilla trekking with rangers and trackers",
            "Community or coffee experience near the park",
            "Lake Bunyonyi boat trip",
            "Forest birding along the trailheads",
            "Optional second trek if permits allow",
            "Optional Batwa cultural experience arranged locally",
        ],
        best_for="Travellers whose main reason for the trip is seeing mountain gorillas",
        starts="Entebbe",
        inclusions=[
            "Private 4x4 vehicle with driver-guide throughout",
            "Three nights accommodation as per the itinerary, full board in Bwindi",
            "Gorilla permit secured on your behalf (permit fee quoted at the official rate)",
            "Community or coffee experience",
            "Bottled drinking water in the vehicle throughout",
            "24/7 WhatsApp support from your Horizon Legacy consultant",
        ],
        exclusions=[
            "International flights",
            "Uganda visa",
            "Travel insurance",
            "Gorilla permit fee itself (quoted separately at the official rate)",
            "Alcoholic drinks, premium beverages and laundry",
            "Gratuities for guides, trackers and lodge staff",
            "Any item not listed under inclusions",
        ],
        travel_info=[
            "Gorilla permits are limited and are secured against a confirmed trek date. Permit fees are quoted at the official rate.",
            "Trekking can last from two to eight hours on uneven, often wet forest ground. A reasonable level of fitness helps.",
            "Porters can be hired locally to carry bags; this is arranged at the trailhead.",
            "One hour with the gorilla family is the park rule, and it is enforced by the rangers.",
            "The drive from Entebbe is long. Flying to Kihihi shortens it and can be quoted instead.",
        ],
    ),
    # 27 -----------------------------------------------------------------
    pkg(
        slug="queen-elizabeth-national-park",
        title="Queen Elizabeth National Park Safari",
        short="Queen Elizabeth Safari",
        group="Uganda Safaris",
        country="Uganda",
        destination="Queen Elizabeth National Park",
        destination_slug="uganda",
        days=4,
        duration="4 Days / 3 Nights",
        safari_type="Big Five Wildlife",
        luxury="Mid-range",
        tagline="Kazinga Channel, tree-climbing lions and crater lakes",
        summary=(
            "Uganda's most visited park earns it with variety: the Kazinga Channel boat trip past "
            "hippo and buffalo, lion in the Ishasha sector that habitually rest in fig trees, and a "
            "chain of explosion craters east of the park. Four days also leaves room for the "
            "Kyambura gorge and the park's remarkable bird list, which passes 600 species."
        ),
        card="A Kazinga Channel boat, Ishasha's tree lions and crater country.",
        hero="queen-elizabeth.jpg",
        gallery=[
            ("queen-elizabeth.jpg", "Lioness at first light in Queen Elizabeth National Park"),
            ("queen-elizabeth-kob.jpg", "Ugandan kob on the park's grasslands"),
            ("rwanda-hills.jpg", "The Albertine rift highlands"),
        ],
        highlights=[
            "Kazinga Channel boat safari past hippo, buffalo and elephant",
            "Tree-climbing lion in the Ishasha sector",
            "The explosion crater drive east of the park",
            "Kyambura gorge and its chimpanzee population",
            "Birding across grassland, wetland and forest habitat",
        ],
        itinerary=[
            ("Entebbe or Kampala to Queen Elizabeth",
             "Drive west through Fort Portal and Kasese, arriving at the park in the afternoon. "
             "Evening drive on the northern tracks."),
            ("Kazinga Channel and the craters",
             "Morning game drive, then the Kazinga Channel boat trip, then the crater drive in the "
             "late afternoon."),
            ("Ishasha sector",
             "Full day south to Ishasha for tree-climbing lion, with a picnic lunch in the sector."),
            ("Kyambura and return",
             "Morning at Kyambura gorge or a final game drive, then the drive back to Entebbe, "
             "arriving in the evening."),
        ],
        accommodation=[
            ("Luxury", "Lodges on the channel with private decks, full board."),
            ("Mid-range", "Safari lodges and tented camps inside the park, full board."),
            ("Comfort", "Guesthouses near the park gate, dinner, bed and breakfast."),
        ],
        activities=[
            "Kazinga Channel boat safari",
            "Game drives on the northern tracks",
            "Ishasha tree-lion drive",
            "Explosion crater drive",
            "Kyambura gorge walk",
            "Birding across the park's habitats",
        ],
        best_for="Travellers combining gorillas with a savannah park in Uganda",
        starts="Entebbe",
        style="Private 4x4 safari with a boat excursion",
    ),
    # 28 -----------------------------------------------------------------
    pkg(
        slug="murchison-falls",
        title="Murchison Falls Wildlife Adventure",
        short="Murchison Falls",
        group="Uganda Safaris",
        country="Uganda",
        destination="Murchison Falls National Park",
        days=4,
        duration="4 Days / 3 Nights",
        safari_type="Big Five Wildlife",
        luxury="Mid-range",
        tagline="The Nile squeezed through a seven-metre gap, and the plains around it",
        summary=(
            "Uganda's largest park is built around the Nile, which forces itself through a narrow "
            "gorge in a roar you can feel. The boat trip upriver to the falls is the centrepiece, "
            "with hippo, crocodile and waterbuck on the banks, and the northern bank adds lion, "
            "elephant, giraffe and a very good chance of shoebill in the papyrus."
        ),
        card="A boat up the Nile to the falls, then game drives on the northern bank.",
        hero="murchison-falls.jpg",
        gallery=[
            ("murchison-falls.jpg", "The Nile forcing through Murchison Falls"),
            ("murchison-nile.jpg", "The Nile at Murchison Falls National Park"),
            ("queen-elizabeth-kob.jpg", "Ugandan kob on the northern bank"),
        ],
        highlights=[
            "Boat trip up the Nile to the base of the falls",
            "A walk to the top of the falls where the river narrows",
            "Lion, elephant and giraffe on the northern bank",
            "Shoebill search in the papyrus on the Victoria Nile delta",
            "Nile perch and tigerfish country for anyone who fishes",
        ],
        itinerary=[
            ("Entebbe to Murchison Falls",
             "Drive north through Ziwa and Masindi, entering the park in the afternoon. Evening "
             "drive on the northern bank."),
            ("Northern bank and the falls",
             "Morning game drive, then the afternoon boat trip upriver, with the optional walk to "
             "the top of the falls."),
            ("Delta and shoebill",
             "Early boat toward the Nile delta to look for shoebill, then a relaxed afternoon and "
             "a night drive where permitted."),
            ("Morning drive and return",
             "Final game drive, breakfast, then the drive back to Entebbe, arriving in the evening."),
        ],
        accommodation=[
            ("Luxury", "River-facing lodges with private decks, full board."),
            ("Mid-range", "Safari lodges on the southern and northern banks, full board."),
            ("Comfort", "Guesthouses near the park gate, dinner, bed and breakfast."),
        ],
        activities=[
            "Nile boat safari to the falls",
            "Top-of-the-falls walk",
            "Northern bank game drives",
            "Shoebill search in the delta",
            "Night drive where permitted",
            "Optional sport fishing for Nile perch",
        ],
        best_for="Travellers who want a boat-based safari and Uganda's biggest waterfall",
        starts="Entebbe",
        style="Private 4x4 safari with boat excursions",
    ),
    # 29 -----------------------------------------------------------------
    pkg(
        slug="rwanda-gorilla-trekking",
        title="Rwanda Gorilla Trekking Experience",
        short="Rwanda Gorilla Trekking",
        group="Rwanda Safaris",
        country="Rwanda",
        destination="Volcanoes National Park",
        destination_slug="volcanoes-national-park",
        days=3,
        duration="3 Days / 2 Nights",
        safari_type="Primates & Gorillas",
        luxury="Luxury",
        tagline="Kigali to the Virunga foothills in one afternoon",
        summary=(
            "Rwanda's version of the gorilla trek is the shortest and most polished: a drive from "
            "Kigali to the Virunga foothills in a few hours, an early briefing at the park "
            "headquarters, and a trek into the bamboo and hagenia forest above the farmland. Three "
            "days is realistic, and it leaves a morning for Kigali's genocide memorial before the "
            "flight home."
        ),
        card="Three days from Kigali to a gorilla family in the Virunga foothills.",
        hero="rwanda-gorilla.jpg",
        gallery=[
            ("rwanda-gorilla.jpg", "Mountain gorilla mother and baby"),
            ("rwanda-hills.jpg", "The Virunga volcanoes above the foothills"),
            ("uganda-gorilla.jpg", "Gorilla in the bamboo zone"),
        ],
        highlights=[
            "Gorilla trekking in Volcanoes National Park with park rangers",
            "A short drive from Kigali, with no long transfer days",
            "Virunga volcano scenery from the lodge garden",
            "Optional golden monkey trek on the second morning",
            "Kigali Genocide Memorial visit before departure",
        ],
        itinerary=[
            ("Kigali to Volcanoes National Park",
             "Met at the airport or your hotel and driven northwest through Musanze to the park "
             "area, arriving in the afternoon. Evening briefing at the lodge."),
            ("Gorilla trekking",
             "Early briefing at the park headquarters, then trekking with rangers. One hour with "
             "the family, then back for a late lunch. Afternoon at leisure."),
            ("Golden monkeys and Kigali",
             "Optional golden monkey trek or a community visit in the morning, then the drive back "
             "to Kigali, with the Genocide Memorial if time allows and an airport transfer."),
        ],
        accommodation=[
            ("Luxury", "Foothill lodges with volcano views and full board."),
            ("Mid-range", "Comfortable lodges near Musanze, full board."),
            ("Boutique", "Small guesthouses with hosted dining near the park."),
        ],
        activities=[
            "Mountain gorilla trekking",
            "Optional golden monkey trek",
            "Community and cultural visits arranged locally",
            "Volcano-view walks from the lodge",
            "Kigali Genocide Memorial visit",
            "Optional Dian Fossey grave hike",
        ],
        best_for="Travellers with three days who want the shortest route to a gorilla family",
        starts="Kigali",
        inclusions=[
            "Private vehicle and driver-guide from Kigali and back",
            "Two nights accommodation as per the itinerary, full board",
            "Gorilla permit secured on your behalf (permit fee quoted at the official rate)",
            "Park briefing and ranger fees",
            "Bottled drinking water in the vehicle throughout",
            "24/7 WhatsApp support from your Horizon Legacy consultant",
        ],
        exclusions=[
            "International flights",
            "Rwanda visa",
            "Travel insurance",
            "Gorilla permit fee itself (quoted separately at the official rate)",
            "Golden monkey permit unless added",
            "Alcoholic drinks, premium beverages and laundry",
            "Gratuities for guides, trackers and lodge staff",
            "Any item not listed under inclusions",
        ],
        travel_info=[
            "Gorilla permits are limited and are secured against a confirmed trek date. Permit fees are quoted at the official rate.",
            "Trekking can last several hours on steep, often muddy ground. Porters can be hired locally.",
            "One hour with the gorilla family is the park rule and is enforced by the rangers.",
            "Rwanda requires a visa for some nationalities; check the current rule before booking flights.",
            "Golden monkey trekking is a separate permit and is quoted on request.",
        ],
    ),
    # 30 -----------------------------------------------------------------
    pkg(
        slug="rwanda-akagera-big-five",
        title="Rwanda Akagera Big Five Safari",
        short="Akagera Big Five",
        group="Rwanda Safaris",
        country="Rwanda",
        destination="Akagera National Park",
        days=4,
        duration="4 Days / 3 Nights",
        safari_type="Big Five Wildlife",
        luxury="Mid-range",
        tagline="Lion, rhino and a lake-and-wetland park in the east",
        summary=(
            "Akagera was restocked with lion and rhino after years of decline and now holds the Big "
            "Five again, in a landscape of papyrus lakes, acacia woodland and rolling hills along the "
            "Tanzanian border. It is a fraction of the Serengeti's size and sees a fraction of its "
            "visitors. Four days allows the northern lakes, the southern savannah and a boat trip on "
            "Lake Ihema."
        ),
        card="Lion, rhino and papyrus lakes in Rwanda's quiet eastern park.",
        hero="akagera-giraffes.jpg",
        gallery=[
            ("akagera-giraffes.jpg", "Giraffe in Akagera National Park"),
            ("akagera.jpg", "Lakes and wetlands in Akagera"),
            ("rwanda-hills.jpg", "Rwanda's rolling hill country"),
        ],
        highlights=[
            "Big Five game drives in a park that sees few visitors",
            "Lion and rhino, both reintroduced and closely monitored",
            "Lake Ihema boat trip past hippo and crocodile",
            "Papyrus wetlands with shoebill and other waterbirds",
            "Northern lakes and southern savannah in a single trip",
        ],
        itinerary=[
            ("Kigali to Akagera",
             "Drive east through Rwamagana to the park, arriving for lunch. Afternoon game drive "
             "on the southern tracks."),
            ("Northern Akagera",
             "Full day north through the lakes and woodland, looking for lion, elephant and giraffe, "
             "with a picnic lunch."),
            ("Lake Ihema and the south",
             "Morning boat trip on Lake Ihema, then an afternoon drive on the southern plains for "
             "rhino and buffalo."),
            ("Morning drive and return",
             "Final early game drive, breakfast, then the drive back to Kigali for your afternoon "
             "or evening flight."),
        ],
        accommodation=[
            ("Luxury", "Lakeside lodges with private decks, full board."),
            ("Mid-range", "Park camps and lodges, full board."),
            ("Comfort", "Guesthouses near the park boundary, dinner, bed and breakfast."),
        ],
        activities=[
            "Big Five game drives",
            "Lake Ihema boat safari",
            "Northern lakes circuit",
            "Birding for shoebill and waterbirds",
            "Night drive where permitted",
            "Optional community visits arranged locally",
        ],
        best_for="Travellers adding a savannah park to a Rwanda gorilla trip",
        starts="Kigali",
        style="Private 4x4 safari with a boat excursion",
    ),
]
