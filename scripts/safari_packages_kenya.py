# -*- coding: utf-8 -*-
"""Kenya safari packages (1-20) for the Horizon Legacy catalogue."""

from safari_packages_base import pkg

KENYA_PACKAGES = [
    # 1 ------------------------------------------------------------------
    pkg(
        slug="maasai-mara-big-five",
        title="Maasai Mara Big Five Safari",
        short="Maasai Mara Big Five",
        group="Kenya Safaris",
        country="Kenya",
        destination="Maasai Mara National Reserve",
        destination_slug="maasai-mara",
        days=4,
        duration="4 Days / 3 Nights",
        safari_type="Big Five Wildlife",
        luxury="Mid-range",
        tagline="Four days in the Mara with the Big Five as the brief",
        summary=(
            "The Mara holds lion, leopard, elephant, buffalo and rhino in a single reserve, and four "
            "days is enough to work the river line, the Talek junctions and the open plains properly. "
            "This is a classic game-drive safari with unhurried mornings, a full day in the middle and "
            "a guide who reads the grass rather than the radio."
        ),
        card="Four unhurried Mara days built around big cats, the river line and the Big Five.",
        hero="maasai-mara.jpg",
        gallery=[
            ("maasai-mara.jpg", "Lion pride on the Mara plains"),
            ("maasai-mara-card.jpg", "Acacia and open savannah in the reserve"),
            ("maasai-mara-balloon.jpg", "First light over the Mara"),
        ],
        highlights=[
            "Mara River and Talek junction drives for lion, leopard and herd movement",
            "A full middle day in the reserve rather than two half days",
            "Black rhino in the Mara Triangle and the Oloololo escarpment views",
            "Big-cat tracking paced around dawn and late afternoon light",
            "Picnic breakfast under an acacia with no other vehicle in sight",
        ],
        itinerary=[
            ("Nairobi to the Mara",
             "Leave Nairobi after an early breakfast and drive down the escarpment into the Mara, "
             "arriving in time for lunch. A late-afternoon drive works the nearest river bend, when "
             "elephant and buffalo come down to drink."),
            ("Full day in the reserve",
             "Out at first light with a picnic breakfast, tracking along the Mara River and the Talek "
             "junction. Back to camp through the heat of the day, then out again for the golden hour."),
            ("Plains, kopjes and the Triangle",
             "A second full day with a different route: the Oloololo escarpment, the southern plains "
             "and the granite kopjes where leopard rest. Sundowners on the way back to camp."),
            ("Morning drive and return",
             "One last dawn drive, breakfast at camp, then the drive back to Nairobi with a picnic "
             "stop on the escarpment, arriving late afternoon."),
        ],
        accommodation=[
            ("Luxury", "Tented suites inside the reserve or on a bordering conservancy, full board, with private decks facing the plains."),
            ("Mid-range", "Comfortable tented camps on the reserve boundary, full board, with en-suite bathrooms and a central mess tent."),
            ("Family-friendly", "Camps with family tents or interconnecting rooms and flexible meal times for younger children."),
        ],
        activities=[
            "Twice-daily game drives in a private 4x4",
            "Big-cat tracking with your guide at dawn and dusk",
            "River-line drives for elephant, buffalo and hippo",
            "Picnic breakfasts and sundowners in the reserve",
            "Optional hot-air balloon safari at extra cost",
            "Optional Maasai community visit arranged with local hosts",
        ],
        best_for="First-time safari travellers who want the Big Five in one reserve without rushing",
    ),
    # 2 ------------------------------------------------------------------
    pkg(
        slug="luxury-maasai-mara-fly-in",
        title="Luxury Maasai Mara Fly-in Safari",
        short="Luxury Mara Fly-in",
        group="Kenya Safaris",
        country="Kenya",
        destination="Maasai Mara National Reserve",
        destination_slug="maasai-mara",
        days=3,
        duration="3 Days / 2 Nights",
        safari_type="Fly-in Luxury",
        luxury="Luxury",
        tagline="Three days, one short flight, no road transfer at either end",
        summary=(
            "A compact luxury Mara trip for travellers with a tight calendar. You fly from Wilson "
            "Airport to a reserve airstrip in the morning and are on a game drive within the hour, "
            "with two nights in a high-end tented suite and a private vehicle for the whole stay. "
            "The point is time: no six-hour drive at either end of a short safari."
        ),
        card="Fly in after breakfast, game drive before lunch: the Mara without the road transfer.",
        hero="maasai-mara-balloon.jpg",
        gallery=[
            ("maasai-mara-balloon.jpg", "First light over the Mara"),
            ("maasai-mara.jpg", "Lion pride on the Mara plains"),
            ("maasai-mara-card.jpg", "Acacia and open savannah in the reserve"),
        ],
        highlights=[
            "Scheduled light-aircraft flight from Wilson Airport to the Mara airstrip",
            "Private vehicle and guide for the whole stay, not a shared game drive",
            "Two nights in a high-end tented suite with full board",
            "A full day in the reserve with a picnic lunch on the plains",
            "Optional balloon safari on the middle morning",
        ],
        itinerary=[
            ("Fly in and drive out",
             "Check in at Wilson Airport for the morning flight to the Mara. Met at the airstrip, "
             "you drive straight into the reserve with a picnic lunch, arriving at camp in the "
             "afternoon for a late game drive and dinner."),
            ("Full day in the reserve",
             "Dawn balloon safari for those who want it, otherwise an early drive with breakfast "
             "in the bush. The rest of the day follows the herds and whatever the cats are doing."),
            ("Morning drive and flight out",
             "A final early drive, breakfast at camp, then the transfer to the airstrip for the "
             "return flight to Nairobi."),
        ],
        accommodation=[
            ("Luxury", "High-end tented suites on a private conservancy or river frontage, full board, with butler service and outdoor baths."),
            ("Luxury family", "Two-bedroom tented suites with a shared deck for families travelling together."),
            ("Classic luxury", "Long-established river-side camps with a quieter, older-style feel and full board."),
        ],
        activities=[
            "Private game drives twice daily",
            "Bush breakfast and picnic lunch in the reserve",
            "Optional hot-air balloon safari with a champagne breakfast",
            "Sundowners at a lookout over the plains",
            "Guided walking safari where the camp holds a walking licence",
        ],
        best_for="Travellers short on time who would rather fly than spend a day on the road",
        style="Private fly-in safari",
        inclusions=[
            "Return scheduled light-aircraft flights Wilson Airport to the Mara airstrip",
            "Private 4x4 safari vehicle with professional driver-guide for the whole stay",
            "Two nights full-board luxury tented accommodation",
            "All reserve entry fees for the itinerary as drawn",
            "Airstrip transfers and game drives as scheduled",
            "Bottled drinking water and house beverages as offered by the camp",
            "24/7 WhatsApp support from your Horizon Legacy consultant",
        ],
    ),
    # 3 ------------------------------------------------------------------
    pkg(
        slug="great-migration",
        title="Great Migration Experience",
        short="Great Migration",
        group="Kenya Safaris",
        country="Kenya",
        destination="Maasai Mara National Reserve",
        destination_slug="maasai-mara",
        days=5,
        duration="5 Days / 4 Nights",
        safari_type="Great Migration",
        luxury="Mid-range",
        tagline="Five days positioned for the herds rather than the itinerary",
        summary=(
            "The migration is a moving animal event, not a fixed attraction, so this safari is built "
            "with slack in it: four nights in the Mara and route decisions made on the ground as the "
            "herds report in. Expect long river sessions when crossings are imminent and quieter "
            "predator drives when they are not. We do not promise a crossing on any given day."
        ),
        card="Four Mara nights with the route set by where the herds actually are.",
        hero="maasai-mara-card.jpg",
        gallery=[
            ("maasai-mara-card.jpg", "Wildebeest herds on the move across the Mara"),
            ("maasai-mara.jpg", "Lion waiting out the migration season"),
            ("maasai-mara-balloon.jpg", "Dawn over the migration plains"),
        ],
        highlights=[
            "Four nights in the Mara so river crossings are not a one-day gamble",
            "Dawn-to-dusk positioning at the main crossing points when herds gather",
            "Predator activity that follows the herds through the reserve",
            "A guide who will change the day's route on the radio report alone",
            "Seasonal timing discussed honestly at quotation, without fixed departure claims",
        ],
        itinerary=[
            ("Nairobi to the Mara",
             "Drive or fly to the reserve depending on the plan agreed, settle in, then take a "
             "late-afternoon drive to read where the herds are holding."),
            ("Herd tracking",
             "An early start toward the river line the herds are using. The day is built around "
             "their movement, with a picnic lunch in the vehicle."),
            ("River crossings and predators",
             "Full day out, positioned at a crossing point if the herds are massing, otherwise "
             "tracking the cats that follow them."),
            ("Second full day",
             "A different sector of the reserve, usually the Triangle or the southern plains, with "
             "a relaxed middle of the day and a late drive back."),
            ("Morning drive and return",
             "A final dawn drive, breakfast at camp and the transfer out to Nairobi."),
        ],
        accommodation=[
            ("Luxury", "Tented suites near the river with full board and a private deck."),
            ("Mid-range", "Boundary camps with en-suite tents, full board and a pool."),
            ("Mobile-style", "Simple seasonal camps that move with the herds, full board, booked well ahead."),
        ],
        activities=[
            "Migration-season game drives",
            "River-crossing watch points at dawn and late afternoon",
            "Big-cat tracking with your guide",
            "Photographic sessions from a lowered vehicle",
            "Optional balloon safari at extra cost",
        ],
        best_for="Wildlife travellers who can be flexible on exact dates and want the herds, not a checklist",
    ),
    # 4 ------------------------------------------------------------------
    pkg(
        slug="amboseli-elephant-safari",
        title="Amboseli Elephant Safari",
        short="Amboseli Elephants",
        group="Kenya Safaris",
        country="Kenya",
        destination="Amboseli National Park",
        destination_slug="amboseli",
        days=3,
        duration="3 Days / 2 Nights",
        safari_type="Elephant Safari",
        luxury="Mid-range",
        tagline="Big tuskers, swamp light and Kilimanjaro behind them",
        summary=(
            "Amboseli's elephants are the reason to come: some of the last great tuskers in Africa "
            "moving between the swamps and the dry lake bed, with Kilimanjaro standing over the "
            "whole basin. Three days gives you two full shooting windows at the swamps and a "
            "mountain view at first light, which is when the summit is usually clean."
        ),
        card="Two days with Amboseli's tuskers, Kilimanjaro standing over the swamps.",
        hero="amboseli.jpg",
        gallery=[
            ("amboseli.jpg", "Elephant herd beneath the snows of Kilimanjaro"),
            ("amboseli-card.jpg", "Elephants crossing the Amboseli plains"),
            ("kilimanjaro.jpg", "Kibo rising beyond the savannah"),
        ],
        highlights=[
            "Enkongo Narok and Longinye swamps at first and last light",
            "Big-tusker bulls at close range with a guide who knows the herds",
            "Kilimanjaro views from Observation Hill and the eastern tracks",
            "Birdlife across the marshes, including pelican and crowned crane",
            "Optional Maasai community visit arranged with local hosts",
        ],
        itinerary=[
            ("Nairobi to Amboseli",
             "Drive south through the Kapiti plains and Emali, arriving in the park by early "
             "afternoon. Check in, then a late drive to the swamps as the herds come in."),
            ("Full day in the park",
             "Dawn drive when the mountain is clearest, breakfast at camp, then out again via "
             "Observation Hill and the swamp circuit with a picnic lunch."),
            ("Morning drive and return",
             "One final early drive, breakfast, then the road back to Nairobi with a picnic stop, "
             "arriving late afternoon."),
        ],
        accommodation=[
            ("Luxury", "Tented suites inside or bordering the park with mountain-facing decks, full board."),
            ("Mid-range", "Lodges on the park boundary with pool and family rooms, full board."),
            ("Family-friendly", "Lodges with interconnecting rooms and early dinner sittings for children."),
        ],
        activities=[
            "Swamp game drives for the big-tusker herds",
            "Kilimanjaro-view morning drives",
            "Observation Hill panoramas across the dry lake bed",
            "Birding in the marshes and along the channels",
            "Optional Maasai village visit",
            "Optional scenic flight over the park at extra cost",
        ],
        best_for="Elephant lovers and photographers who want one park done properly",
    ),
    # 5 ------------------------------------------------------------------
    pkg(
        slug="luxury-amboseli-escape",
        title="Luxury Amboseli Escape",
        short="Luxury Amboseli",
        group="Kenya Safaris",
        country="Kenya",
        destination="Amboseli National Park",
        destination_slug="amboseli",
        days=3,
        duration="3 Days / 2 Nights",
        safari_type="Fly-in Luxury",
        luxury="Luxury",
        tagline="Fly in, slow down, and let the mountain do the rest",
        summary=(
            "The same Amboseli wildlife with the logistics taken out: a light-aircraft hop from "
            "Wilson Airport, a private vehicle waiting at the airstrip, and two nights in a "
            "high-end camp with real space between the game drives. Built for travellers who want "
            "the landscape more than the mileage."
        ),
        card="A short flight and two nights of quiet luxury beneath Kilimanjaro.",
        hero="amboseli-card.jpg",
        gallery=[
            ("amboseli-card.jpg", "Elephants crossing the Amboseli plains"),
            ("amboseli.jpg", "Elephant herd beneath the snows of Kilimanjaro"),
            ("kilimanjaro-card.jpg", "The eastern icefields of Kilimanjaro"),
        ],
        highlights=[
            "Scheduled flight from Wilson Airport to the Amboseli airstrip",
            "Private vehicle and guide throughout the stay",
            "Two nights in a luxury camp with mountain-facing suites",
            "Sundowners on the plains with the summit in the background",
            "Optional spa treatment or private dinner in the bush",
        ],
        itinerary=[
            ("Fly in and settle",
             "Morning flight from Wilson, met at the airstrip and driven into the park with a "
             "picnic lunch. Afternoon at leisure, then a late drive to the swamps."),
            ("Full day in the park",
             "Dawn drive, breakfast at camp, a long middle-of-day rest, then out again through "
             "the swamp circuit for the last light."),
            ("Morning drive and flight out",
             "Final early drive, breakfast, and the transfer to the airstrip for the return flight."),
        ],
        accommodation=[
            ("Luxury", "Tented suites with private plunge pools or outdoor baths, full board."),
            ("Luxury family", "Two-bedroom suites with a shared deck for families."),
            ("Classic luxury", "Older-style lodges on the park edge with a garden and full board."),
        ],
        activities=[
            "Private morning and evening game drives",
            "Champagne sundowners on the plains",
            "Guided birding in the marshes",
            "Optional massage or spa treatment at camp",
            "Optional scenic helicopter flight over Kilimanjaro",
        ],
        best_for="Couples and solo travellers who want Amboseli without a long road transfer",
        style="Private fly-in safari",
        inclusions=[
            "Return scheduled light-aircraft flights Wilson Airport to Amboseli",
            "Private 4x4 safari vehicle with driver-guide for the whole stay",
            "Two nights full-board luxury accommodation",
            "All park entry fees for the itinerary as drawn",
            "Airstrip transfers and game drives as scheduled",
            "House beverages as offered by the camp",
            "24/7 WhatsApp support from your Horizon Legacy consultant",
        ],
    ),
    # 6 ------------------------------------------------------------------
    pkg(
        slug="samburu-special-five",
        title="Samburu Special Five Safari",
        short="Samburu Special Five",
        group="Kenya Safaris",
        country="Kenya",
        destination="Samburu National Reserve",
        destination_slug="samburu",
        days=4,
        duration="4 Days / 3 Nights",
        safari_type="Special Five Wildlife",
        luxury="Mid-range",
        tagline="Reticulated giraffe, Grevy's zebra and the dry-country specialists",
        summary=(
            "Samburu is where the species list changes. Reticulated giraffe, Grevy's zebra, gerenuk, "
            "beisa oryx and Somali ostrich all live here and nowhere else on a typical Kenya circuit. "
            "The Ewaso Ng'iro river keeps the reserve green while the surrounding country bakes, which "
            "concentrates wildlife along its banks and makes for very good, very uncrowded drives."
        ),
        card="The five dry-country specialists, along a river that concentrates everything.",
        hero="samburu.jpg",
        gallery=[
            ("samburu.jpg", "Reticulated giraffe in Samburu National Reserve"),
            ("samburu-card.jpg", "Doum palms along the Ewaso Ng'iro"),
            ("laikipia.jpg", "Dry-country escarpment and game country north of Mount Kenya"),
        ],
        highlights=[
            "All five Samburu specials: reticulated giraffe, Grevy's zebra, gerenuk, beisa oryx and Somali ostrich",
            "River-front drives along the Ewaso Ng'iro",
            "Elephant herds that are studied and relaxed around vehicles",
            "Buffalo Springs addition for a second reserve on the same trip",
            "A markedly quieter reserve than the Mara or Amboseli",
        ],
        itinerary=[
            ("Nairobi to Samburu",
             "North past Mount Kenya and Isiolo, crossing the equator at Nanyuki, arriving at the "
             "reserve in the early afternoon. Late drive along the river."),
            ("Full day in Samburu",
             "Dawn drive for the specials, breakfast at camp, then an afternoon out through the "
             "river bends and doum palm groves."),
            ("Buffalo Springs and community",
             "A morning in Buffalo Springs, then a community visit or a relaxed camp afternoon; "
             "another late drive before dinner."),
            ("Morning drive and return",
             "Final early drive, breakfast and the road back to Nairobi, arriving in the evening."),
        ],
        accommodation=[
            ("Luxury", "River-front tented suites with private decks, full board."),
            ("Mid-range", "Lodges beside the reserve with pool and full board."),
            ("Boutique", "Small camps with a handful of tents and a quiet, hosted feel, full board."),
        ],
        activities=[
            "Special-five species drives",
            "River-front elephant watching",
            "Buffalo Springs game drives",
            "Guided walk with a ranger where permitted",
            "Optional Samburu community visit",
            "Birding for dry-country species",
        ],
        best_for="Travellers who have done the Mara and want a different species list",
    ),
    # 7 ------------------------------------------------------------------
    pkg(
        slug="ol-pejeta-rhino-safari",
        title="Ol Pejeta Rhino and Chimpanzee Safari",
        short="Ol Pejeta Rhino Safari",
        group="Kenya Safaris",
        country="Kenya",
        destination="Ol Pejeta Conservancy",
        days=3,
        duration="3 Days / 2 Nights",
        safari_type="Conservation Safari",
        luxury="Mid-range",
        tagline="Rhino conservation, a chimp sanctuary and Mount Kenya on the skyline",
        summary=(
            "Ol Pejeta is a working conservancy, not just a park, and the visit reflects that: a "
            "session with the rhino-monitoring team, black and white rhino at close range, and the "
            "chimpanzee sanctuary on the Ewaso Ng'iro. Two nights on the Laikipia plateau, with "
            "Mount Kenya visible from much of the conservancy and far fewer vehicles than the Mara."
        ),
        card="Rhino monitoring, the chimp sanctuary and open Laikipia plains under Mount Kenya.",
        hero="ol-pejeta.jpg",
        gallery=[
            ("ol-pejeta.jpg", "Northern white rhino under guard at Ol Pejeta"),
            ("ol-pejeta-plains.jpg", "Open Laikipia plains inside the conservancy"),
            ("laikipia.jpg", "Escarpment country north of Mount Kenya"),
        ],
        highlights=[
            "Rhino-monitoring experience with the conservancy's tracking team",
            "Black and white rhino viewed on foot where conditions allow",
            "Sweetwaters chimpanzee sanctuary on the Ewaso Ng'iro",
            "Big Five game drives across open Laikipia grassland",
            "Mount Kenya views from the conservancy's northern boundary",
        ],
        itinerary=[
            ("Nairobi to Ol Pejeta",
             "Drive north through Nanyuki and into the conservancy, arriving for lunch. "
             "Afternoon game drive across the western sector with a stop at the rhino enclosure."),
            ("Full day in the conservancy",
             "Morning rhino-monitoring session, then the chimpanzee sanctuary, then an afternoon "
             "drive for lion, elephant and buffalo. Night drive where the conservancy permits."),
            ("Morning drive and return",
             "Early drive, breakfast, then the drive back to Nairobi via the Aberdare foothills."),
        ],
        accommodation=[
            ("Luxury", "Tented suites on the conservancy with Mount Kenya views, full board."),
            ("Mid-range", "Lodges inside or beside the conservancy, full board, with pool."),
            ("Family-friendly", "Cottages and family tents with flexible meal times."),
        ],
        activities=[
            "Rhino-monitoring with the conservancy team",
            "Chimpanzee sanctuary visit",
            "Big Five game drives",
            "Night drive where permitted",
            "Guided bush walk with an armed ranger",
            "Optional lion-tracking experience",
        ],
        best_for="Conservation-minded travellers and families with older children",
    ),
    # 8 ------------------------------------------------------------------
    pkg(
        slug="lake-nakuru-naivasha",
        title="Lake Nakuru and Naivasha Adventure",
        short="Nakuru & Naivasha",
        group="Kenya Safaris",
        country="Kenya",
        destination="Lake Nakuru National Park",
        destination_slug="lake-nakuru",
        days=3,
        duration="3 Days / 2 Nights",
        safari_type="Rift Valley Lakes",
        luxury="Comfort",
        tagline="Two Rift Valley lakes, rhino on one shore and hippo on the other",
        summary=(
            "A short Rift Valley loop that pairs Nakuru's rhino and flamingo shoreline with "
            "Naivasha's water. Nakuru is fenced, compact and reliable for both black and white "
            "rhino; Naivasha adds a boat trip past hippo and a walk on Crescent Island among "
            "giraffe and zebra with no predators. Good value, good for a first safari, easy on "
            "a short break from Nairobi."
        ),
        card="Rhino at Nakuru, hippo and a boat at Naivasha, all in one Rift Valley loop.",
        hero="lake-nakuru.jpg",
        gallery=[
            ("lake-nakuru.jpg", "Lake Nakuru and its shoreline"),
            ("lake-naivasha.jpg", "Boats and hippo water on Lake Naivasha"),
            ("lake-nakuru-card.jpg", "Flamingo-pink water at Lake Nakuru"),
        ],
        highlights=[
            "Black and white rhino in Lake Nakuru National Park",
            "Rothschild giraffe and the Baboon Cliff viewpoint",
            "Boat trip on Lake Naivasha past hippo and fish eagles",
            "Guided walk on Crescent Island among giraffe, zebra and wildebeest",
            "Rift Valley escarpment viewpoints on the drive down from Nairobi",
        ],
        itinerary=[
            ("Nairobi to Naivasha",
             "Drive down the escarpment with a stop at the viewpoint, then on to Naivasha for "
             "lunch. Afternoon boat trip and a walk on Crescent Island."),
            ("Naivasha to Nakuru",
             "Morning drive to Lake Nakuru National Park with a game drive en route to the lodge. "
             "Afternoon drive along the shoreline for rhino, giraffe and flamingo."),
            ("Nakuru and return",
             "Early game drive to Baboon Cliff and the northern shore, breakfast, then the drive "
             "back to Nairobi arriving early afternoon."),
        ],
        accommodation=[
            ("Luxury", "Lakeside lodges with private decks, full board."),
            ("Mid-range", "Lodges in or near the park with pool, full board."),
            ("Comfort", "Simple lakeside hotels with dinner, bed and breakfast near Naivasha."),
        ],
        activities=[
            "Game drives in Lake Nakuru National Park",
            "Boat safari on Lake Naivasha",
            "Guided walk on Crescent Island",
            "Baboon Cliff and Rift Valley viewpoints",
            "Birding for flamingo, pelican and fish eagle",
            "Optional Hell's Gate cycling add-on",
        ],
        best_for="Short-break travellers, first-time safari visitors and families",
    ),
    # 9 ------------------------------------------------------------------
    pkg(
        slug="hells-gate-cycling",
        title="Hell's Gate Cycling and Naivasha Safari",
        short="Hell's Gate Cycling",
        group="Kenya Safaris",
        country="Kenya",
        destination="Hell's Gate National Park",
        destination_slug="hells-gate",
        days=3,
        duration="3 Days / 2 Nights",
        safari_type="Walking & Cycling",
        luxury="Comfort",
        tagline="Cycle a gorge, walk a canyon and boat past hippo",
        summary=(
            "Hell's Gate is one of the few Kenyan parks you can explore on a bicycle, and that "
            "changes the whole feel of a safari: no vehicle roof between you and the cliffs, "
            "zebra and giraffe moving off the track ahead of you, and the chance to walk into the "
            "gorge with a guide. Paired with a Naivasha boat trip, it makes a very good short, "
            "active break out of Nairobi."
        ),
        card="Bicycles, a gorge walk and a boat on Naivasha instead of another game-drive loop.",
        hero="hells-gate.jpg",
        gallery=[
            ("hells-gate.jpg", "Cliffs and volcanic columns in Hell's Gate"),
            ("hells-gate-card.jpg", "The gorge track inside Hell's Gate National Park"),
            ("lake-naivasha.jpg", "Boats and hippo water on Lake Naivasha"),
        ],
        highlights=[
            "Cycling through Hell's Gate on a hired bike with a guide",
            "Guided walk into the gorge and past Fischer's Tower",
            "Wildlife on the move at eye level: zebra, giraffe, warthog and eland",
            "Boat trip on Lake Naivasha for hippo and fish eagle",
            "Steam vents and volcanic scenery you can walk right up to",
        ],
        itinerary=[
            ("Nairobi to Naivasha",
             "Drive down the escarpment to Naivasha, drop bags, then an afternoon boat trip on the "
             "lake and a walk on Crescent Island."),
            ("Hell's Gate by bike",
             "Morning at the park gate for bikes and a guide, cycling the main tracks toward the "
             "gorge. Picnic lunch, then the guided gorge walk before returning to Naivasha."),
            ("Morning at leisure and return",
             "A slow breakfast by the lake, optional visit to a flower farm or the Elsamere "
             "conservation centre, then the drive back to Nairobi."),
        ],
        accommodation=[
            ("Luxury", "Lakeside lodges with garden suites, full board."),
            ("Mid-range", "Lakeside lodges and tented camps, dinner, bed and breakfast."),
            ("Comfort", "Simple guesthouses and camps with breakfast included."),
        ],
        activities=[
            "Guided cycling in Hell's Gate",
            "Gorge walk and Fischer's Tower",
            "Lake Naivasha boat safari",
            "Crescent Island walking safari",
            "Birding and fish-eagle feeding",
            "Optional rock climbing or spa afternoon",
        ],
        best_for="Active travellers, couples and families with teenagers",
        style="Private road safari with cycling and walking",
    ),
    # 10 -----------------------------------------------------------------
    pkg(
        slug="tsavo-east-west",
        title="Tsavo East and West Safari",
        short="Tsavo East & West",
        group="Kenya Safaris",
        country="Kenya",
        destination="Tsavo National Parks",
        destination_slug="tsavo-national-parks",
        days=4,
        duration="4 Days / 3 Nights",
        safari_type="Big Five Wildlife",
        luxury="Comfort",
        tagline="Red dust, lava ridges and two very different halves of one park",
        summary=(
            "Tsavo is enormous, and its two halves behave like different parks. East is open red "
            "earth and the Galana river, known for dust-red elephants and the long Yatta plateau. "
            "West is denser bush, volcanic hills and Mzima Springs, where hippo can be watched "
            "through a glass tank. Four days covers both without rushing the drives between them."
        ),
        card="Dust-red elephants in the east, Mzima Springs and lava country in the west.",
        hero="tsavo.jpg",
        gallery=[
            ("tsavo.jpg", "Tsavo wilderness and red earth"),
            ("tsavo-card.jpg", "Elephants on the move in Tsavo"),
            ("taita-hills.jpg", "Savannah and hills on the Tsavo corridor"),
        ],
        highlights=[
            "Red-dust elephants along the Galana river in Tsavo East",
            "Lugard Falls and the Yatta plateau viewpoints",
            "Mzima Springs and its underwater hippo observation tank",
            "Shetani lava flows and the Chyulu hills in Tsavo West",
            "A far quieter safari than the Mara on the same number of days",
        ],
        itinerary=[
            ("Nairobi to Tsavo East",
             "Drive via Mtito Andei and the Buchuma gate, arriving for lunch. Afternoon game "
             "drive along the Galana river."),
            ("Full day in Tsavo East",
             "Dawn drive for elephant and lion, Lugard Falls and the long waterholes through the "
             "middle of the day, sundowners at a viewpoint."),
            ("Cross to Tsavo West",
             "Morning drive, then across to Tsavo West via Manyani. Afternoon at Mzima Springs, "
             "then a drive through the Shetani lava flows."),
            ("Morning drive and return",
             "Early drive toward the Chyulu hills or Kilaguni waterhole, breakfast, then the road "
             "back to Nairobi."),
        ],
        accommodation=[
            ("Luxury", "Lodges with waterhole-facing rooms, full board."),
            ("Mid-range", "Safari lodges inside the parks, full board, with pool."),
            ("Comfort", "Simple bandas and camps near the gates, dinner, bed and breakfast."),
        ],
        activities=[
            "Game drives in both Tsavo East and West",
            "Galana river and Lugard Falls drives",
            "Mzima Springs and the underwater observation tank",
            "Shetani lava flow and Chyulu hills excursions",
            "Birding along the river lines",
            "Optional night drive where permitted",
        ],
        best_for="Travellers driving between Nairobi and the coast, or wanting a crowd-free Big Five trip",
    ),
    # 11 -----------------------------------------------------------------
    pkg(
        slug="taita-hills-salt-lick",
        title="Taita Hills and Salt Lick Safari",
        short="Taita Hills Safari",
        group="Kenya Safaris",
        country="Kenya",
        destination="Taita Hills Wildlife Sanctuary",
        destination_slug="tsavo-national-parks",
        days=3,
        duration="3 Days / 2 Nights",
        safari_type="Big Five Wildlife",
        luxury="Mid-range",
        tagline="A private sanctuary on the Tsavo corridor, with a waterhole at eye level",
        summary=(
            "Between the Taita Hills and the western edge of Tsavo, this private sanctuary is small "
            "enough to feel uncrowded and well stocked enough to deliver elephant, lion, buffalo and "
            "a good chance of leopard. The draw is the waterhole: a stilted lodge looks straight down "
            "onto it, so the middle of the day is spent watching rather than driving. The drive from "
            "Nairobi is long, which keeps the sanctuary quiet."
        ),
        card="A quiet Taita sanctuary with a floodlit waterhole and the Tsavo plains next door.",
        hero="taita-hills.jpg",
        gallery=[
            ("taita-hills.jpg", "Elephants on the Taita Hills savannah"),
            ("tsavo-card.jpg", "Tsavo wilderness on the sanctuary boundary"),
            ("tsavo.jpg", "Open country along the Tsavo corridor"),
        ],
        highlights=[
            "Game viewing from a stilted lodge above a permanent waterhole",
            "Elephant, lion and buffalo in a sanctuary that sees few vehicles",
            "Night viewing at the waterhole, when the reserve comes to you",
            "Access to the Tsavo West circuit for a full day",
            "Taita Hills scenery and the road up to the lookout",
        ],
        itinerary=[
            ("Nairobi to the sanctuary",
             "Long drive southeast via Voi, arriving in the early afternoon. Check in above the "
             "waterhole, then an afternoon game drive across the sanctuary."),
            ("Full day in the sanctuary",
             "Dawn drive, then back to the lodge for the middle of the day with the waterhole in "
             "view. Late-afternoon drive and night viewing from the hide."),
            ("Tsavo West and return",
             "Early drive into Tsavo West for Mzima Springs and the lava flows, then the road back "
             "to Nairobi with a late arrival."),
        ],
        accommodation=[
            ("Luxury", "Stilted suites overlooking the waterhole, full board, with a private viewing deck."),
            ("Mid-range", "Waterhole-facing rooms with full board and a shared hide."),
            ("Comfort", "Lodge rooms in the sanctuary grounds, full board, without the waterhole frontage."),
        ],
        activities=[
            "Waterhole game viewing from the lodge",
            "Dawn and late-afternoon game drives",
            "Night viewing at the floodlit waterhole",
            "Full-day Tsavo West excursion",
            "Birding across the sanctuary",
            "Optional Taita Hills cultural visit",
        ],
        best_for="Travellers breaking the Nairobi to coast drive, and families who like a waterhole lodge",
    ),
    # 12 -----------------------------------------------------------------
    pkg(
        slug="aberdare-ark-getaway",
        title="Aberdare Forest and The Ark Getaway",
        short="Aberdare Forest Getaway",
        group="Kenya Safaris",
        country="Kenya",
        destination="Aberdare National Park",
        destination_slug="aberdare-national-park",
        days=3,
        duration="3 Days / 2 Nights",
        safari_type="Forest & Wildlife",
        luxury="Mid-range",
        tagline="Moorland, waterfalls and a night watch over a forest waterhole",
        summary=(
            "The Aberdares are a different Kenya: cold, high, furred with moss and cut by waterfalls, "
            "with elephants moving through bamboo and buffalo crossing the moorland tracks. The "
            "pattern of the trip is a night in a tree-hotel-style lodge above a waterhole, so the "
            "night shift does the watching while you sleep, and a day up on the high moor after "
            "Karuru Falls."
        ),
        card="Waterfalls, mossy forest and a night spent watching a floodlit waterhole.",
        hero="aberdare.jpg",
        gallery=[
            ("aberdare.jpg", "Waterfalls and forested gorges in the Aberdares"),
            ("mount-kenya.jpg", "Mount Kenya seen from the Aberdare highlands"),
            ("nanyuki.jpg", "Highland country along the Aberdare approach"),
        ],
        highlights=[
            "A night at a waterhole lodge with a ground-level viewing deck",
            "Karuru and Chania falls on the high moor",
            "Giant heather, podocarpus forest and bamboo country",
            "Elephant, buffalo and the rare bongo's highland habitat",
            "A cool, crowd-free alternative to the savannah parks",
        ],
        itinerary=[
            ("Nairobi to the Aberdares",
             "Drive north through Nyeri and up into the forest, arriving for lunch. Afternoon at "
             "the lodge watching the waterhole, with an evening talk from the resident naturalist."),
            ("High moor and waterfalls",
             "Morning drive to Karuru Falls and the moorland tracks, back for a late lunch, then "
             "the afternoon and night at the waterhole with the floodlights on."),
            ("Morning in the forest and return",
             "Early drive through the bamboo zone, breakfast, then the drive back to Nairobi via "
             "the tea country around Nyeri."),
        ],
        accommodation=[
            ("Luxury", "Waterhole-facing suites with private balconies, full board."),
            ("Mid-range", "Waterhole-facing rooms with full board and a shared viewing deck."),
            ("Comfort", "Forest lodge rooms with full board, a short drive from the waterhole."),
        ],
        activities=[
            "Waterhole watching from the lodge deck",
            "Karuru and Chania falls excursion",
            "High-moorland game drives",
            "Guided forest walk with a ranger",
            "Night viewing at the floodlit waterhole",
            "Birding for highland forest species",
        ],
        best_for="Travellers who want forest and mountains between savannah parks",
        style="Private road safari with lodge-based night viewing",
    ),
    # 13 -----------------------------------------------------------------
    pkg(
        slug="laikipia-mount-kenya",
        title="Laikipia and Mount Kenya Safari",
        short="Laikipia & Mount Kenya",
        group="Kenya Safaris",
        country="Kenya",
        destination="Laikipia Plateau",
        destination_slug="mount-kenya",
        days=5,
        duration="5 Days / 4 Nights",
        safari_type="Conservation Safari",
        luxury="Luxury",
        tagline="Big conservancies, rhino country and Africa's second-highest mountain",
        summary=(
            "Laikipia is a patchwork of private conservancies and working ranches north of Mount "
            "Kenya, run with real conservation intent: rhino densities that rival anywhere in Kenya, "
            "wild dog that move between properties, and a landscape that shifts from black cotton "
            "soil to cedar forest in an hour. Five days allows for walking, night drives and time "
            "on the mountain's forested lower slopes rather than just game drives."
        ),
        card="Rhino conservancies, night drives and the forested flanks of Mount Kenya.",
        hero="laikipia.jpg",
        gallery=[
            ("laikipia.jpg", "Escarpment country on the Laikipia plateau"),
            ("mount-kenya.jpg", "Batian peak on Mount Kenya seen from Point Lenana"),
            ("mount-kenya-card.jpg", "Mount Kenya forest and highland slopes"),
        ],
        highlights=[
            "Private conservancies with rhino, lion and wild dog",
            "Night drives, which national parks do not permit",
            "Guided walking safaris on the plateau",
            "Cedar forest and moorland on Mount Kenya's lower slopes",
            "Community-run conservation projects visiting as guests, not as a show",
        ],
        itinerary=[
            ("Nairobi to Laikipia",
             "Drive north past Nanyuki, arriving at the conservancy for lunch. Late-afternoon "
             "game drive and a night drive on the way back."),
            ("Conservancy day",
             "Dawn drive for rhino and lion, a long lunch, then a guided walk with an armed ranger "
             "through the whistling-thorn country."),
            ("Mount Kenya forest",
             "Drive to the mountain's lower slopes for a forest walk and views of the peaks, with "
             "lunch at a lodge on the mountain's shoulder."),
            ("Second conservancy",
             "A different property or sector for wild dog and elephant movement, with another night "
             "drive if conditions allow."),
            ("Morning drive and return",
             "Early drive, breakfast, then the road back to Nairobi, arriving late afternoon."),
        ],
        accommodation=[
            ("Luxury", "Conservancy homesteads and tented suites with full board and private vehicles."),
            ("Mid-range", "Camps on the plateau with full board and shared guiding."),
            ("Classic", "Old farmhouses converted to guest accommodation, full board."),
        ],
        activities=[
            "Day and night game drives on private land",
            "Guided walking safaris",
            "Rhino and wild dog tracking",
            "Mount Kenya forest walks",
            "Lion-tracking with the research team where available",
            "Optional horse-riding safari at extra cost",
        ],
        best_for="Repeat Kenya travellers and conservation-focused visitors who want walking and night drives",
        style="Private road safari with conservancy stays",
    ),
    # 14 -----------------------------------------------------------------
    pkg(
        slug="meru-national-park",
        title="Meru National Park Wilderness Safari",
        short="Meru Wilderness",
        group="Kenya Safaris",
        country="Kenya",
        destination="Meru National Park",
        days=4,
        duration="4 Days / 3 Nights",
        safari_type="Wilderness Safari",
        luxury="Mid-range",
        tagline="Thirteen rivers, no queues and the country that made Born Free famous",
        summary=(
            "Meru is one of Kenya's least-visited big parks and one of its prettiest: thirteen rivers "
            "cut through doum palm and riverine forest, rhino were reintroduced to a fenced sanctuary "
            "inside the park, and you can drive for hours without passing another vehicle. The access "
            "road keeps crowds away, which is exactly the point of coming. Four days is enough to "
            "work the rivers, the Rojewero and the Mulika swamp properly."
        ),
        card="Thirteen rivers, reintroduced rhino and drives where nobody else is around.",
        hero="meru-national-park.jpg",
        gallery=[
            ("meru-national-park.jpg", "Wildlife in Meru National Park"),
            ("laikipia.jpg", "Dry-country game land on the Meru approach"),
            ("mount-kenya-card.jpg", "Mount Kenya on the northern horizon"),
        ],
        highlights=[
            "The rhino sanctuary inside Meru National Park",
            "Riverine forest along the Tana tributaries, with good birding",
            "Elsa's Kopje country, without the Born Free mythology sold as fact",
            "Very low vehicle traffic compared with the Mara or Amboseli",
            "A full day on the Mulika swamp circuit",
        ],
        itinerary=[
            ("Nairobi to Meru",
             "Drive north via Nanyuki and Isiolo, arriving in the late afternoon. A short evening "
             "drive toward the nearest river line."),
            ("Rivers and rhino",
             "Dawn drive to the rhino sanctuary, then the river circuits through the middle of the "
             "day with a picnic lunch."),
            ("Mulika swamp and the north",
             "Full day out across the Mulika swamp and the northern boundary, looking for elephant, "
             "buffalo and lion."),
            ("Morning drive and return",
             "Final early game drive, breakfast, then the drive back to Nairobi, arriving in the "
             "evening."),
        ],
        accommodation=[
            ("Luxury", "Small camps on the river with private decks, full board."),
            ("Mid-range", "Lodges inside the park with full board and a pool."),
            ("Comfort", "Simple camps on the park boundary, dinner, bed and breakfast."),
        ],
        activities=[
            "Game drives along the park's river systems",
            "Rhino sanctuary visit",
            "Mulika swamp circuit",
            "Birding in riverine forest",
            "Guided walk where permitted",
            "Optional visit to the Meru community conservation area",
        ],
        best_for="Travellers who have done the classic circuit and want solitude",
    ),
    # 15 -----------------------------------------------------------------
    pkg(
        slug="maasai-mara-diani-beach",
        title="Maasai Mara Bush and Diani Beach Escape",
        short="Mara & Diani Beach",
        group="Kenya Safaris",
        country="Kenya",
        destination="Maasai Mara \u0026 Diani Beach",
        regions=["Maasai Mara National Reserve", "Diani Beach"],
        destination_slug="maasai-mara",
        days=7,
        duration="7 Days / 6 Nights",
        safari_type="Beach & Bush",
        luxury="Luxury",
        tagline="Three Mara days, then four on the Indian Ocean",
        summary=(
            "The classic Kenyan combination, done in the right order: the Mara while you still have "
            "the energy for dawn drives, then Diani to let the dust settle. Three nights in the "
            "reserve and three on the south coast, joined by a flight that skips the drive back "
            "through Nairobi. It works for honeymoons, and it works for families with older children."
        ),
        card="Big cats, then white sand: three Mara nights and three on Diani Beach.",
        hero="maasai-mara.jpg",
        gallery=[
            ("maasai-mara.jpg", "Lion pride on the Mara plains"),
            ("diani-beach.jpg", "White sand and turquoise water at Diani Beach"),
            ("diani-beach-card.jpg", "Palm shade on the south coast"),
        ],
        highlights=[
            "Three nights of game drives in the Maasai Mara",
            "A flight from the Mara toward the coast instead of a return to Nairobi",
            "Three nights on Diani Beach with the Indian Ocean at the door",
            "Optional dhow trip, reef snorkelling or kite-surfing lessons",
            "One trip, two completely different paces",
        ],
        itinerary=[
            ("Nairobi to the Mara",
             "Early departure for the reserve by road or air, arriving for lunch. Late-afternoon "
             "game drive."),
            ("Full day in the Mara",
             "Dawn drive with a picnic breakfast, a rest through the middle of the day, then a long "
             "evening drive."),
            ("Final Mara morning",
             "A last early drive, breakfast, then a flight toward the coast and a transfer to Diani. "
             "Evening at leisure."),
            ("Diani Beach",
             "A full day on the coast: reef snorkelling, a dhow trip or simply the beach and the pool."),
            ("Diani Beach",
             "Second coastal day, with optional kite-surfing, a marine park visit or a spa afternoon."),
            ("Diani Beach",
             "Third coastal day at your own pace, with dinner by the water."),
            ("Departure",
             "Breakfast, a final swim, then the transfer to Mombasa for your flight or the road "
             "back to Nairobi."),
        ],
        accommodation=[
            ("Luxury", "Mara tented suites followed by a beachfront suite on Diani, half board on the coast."),
            ("Luxury family", "Family tents in the Mara and a two-bedroom beach villa on the coast."),
            ("Boutique", "Small Mara camp and a boutique beach hotel, half board on the coast."),
        ],
        activities=[
            "Mara game drives and big-cat tracking",
            "Optional balloon safari in the Mara",
            "Reef snorkelling and diving on the south coast",
            "Dhow sailing and sunset cruises",
            "Kite-surfing and paddle-boarding lessons",
            "Optional marine park or Shimba Hills day trip",
        ],
        best_for="Honeymoons, anniversaries and families who want safari plus beach in one booking",
        style="Private safari with a coastal stay",
    ),
    # 16 -----------------------------------------------------------------
    pkg(
        slug="amboseli-tsavo-mombasa",
        title="Amboseli, Tsavo and Mombasa Safari",
        short="Amboseli, Tsavo & Mombasa",
        group="Kenya Safaris",
        country="Kenya",
        destination="Amboseli, Tsavo \u0026 Mombasa",
        regions=["Amboseli National Park", "Tsavo National Parks", "Mombasa"],
        destination_slug="amboseli",
        days=8,
        duration="8 Days / 7 Nights",
        safari_type="Classic Circuit",
        luxury="Mid-range",
        tagline="The southern circuit end to end, finishing at the coast",
        summary=(
            "A south-bound itinerary that never doubles back: Amboseli for elephants under "
            "Kilimanjaro, Tsavo West for Mzima Springs and lava country, then the railway line down "
            "to Mombasa for three nights on the coast. It is the most efficient way to see the "
            "southern parks and still end with sea air, and the road legs are all in the same "
            "direction."
        ),
        card="Elephants, lava flows and the Indian Ocean, with no backtracking.",
        hero="amboseli-card.jpg",
        gallery=[
            ("amboseli-card.jpg", "Elephants crossing the Amboseli plains"),
            ("tsavo.jpg", "Tsavo wilderness and red earth"),
            ("mombasa.jpg", "The Mombasa coastline"),
        ],
        highlights=[
            "Amboseli's swamp elephants against Kilimanjaro",
            "Mzima Springs and the Shetani lava flows in Tsavo West",
            "Three nights in Mombasa with the coast at the door",
            "A one-way route south, with no wasted driving",
            "Optional Fort Jesus and Old Town walk in Mombasa",
        ],
        itinerary=[
            ("Nairobi to Amboseli",
             "Drive south to Amboseli, arriving for lunch, then an afternoon drive to the swamps."),
            ("Full day in Amboseli",
             "Dawn drive for the mountain view, the rest of the day on the swamp circuit with a "
             "picnic lunch."),
            ("Amboseli to Tsavo West",
             "Morning drive, then east across the Chyulu hills to Tsavo West. Afternoon at Mzima "
             "Springs."),
            ("Tsavo West to Mombasa",
             "Early drive through the lava flows, then the road or rail transfer to Mombasa for "
             "three nights on the coast."),
            ("Mombasa",
             "Full day on the coast, with optional Old Town and Fort Jesus walk or a dhow trip."),
            ("Mombasa",
             "Second coastal day: beach, reef or a day trip to Shimba Hills."),
            ("Mombasa",
             "Third coastal day at leisure."),
            ("Departure",
             "Breakfast and transfer to Moi International Airport, or the road back to Nairobi."),
        ],
        accommodation=[
            ("Luxury", "Park lodges in Amboseli and Tsavo, then a beachfront suite in Mombasa."),
            ("Mid-range", "Lodges with pools in both parks, then a beach hotel on half board."),
            ("Comfort", "Simple park bandas and a coastal guesthouse on bed and breakfast."),
        ],
        activities=[
            "Amboseli swamp and mountain-view drives",
            "Mzima Springs and lava flow excursion",
            "Tsavo game drives",
            "Beach and reef time on the coast",
            "Fort Jesus and Old Town walk",
            "Optional Shimba Hills day trip",
        ],
        best_for="Travellers wanting a one-way southern circuit that ends at the sea",
    ),
    # 17 -----------------------------------------------------------------
    pkg(
        slug="best-of-kenya-grand-safari",
        title="Best of Kenya Grand Safari",
        short="Best of Kenya Grand Safari",
        group="Kenya Safaris",
        country="Kenya",
        destination="Samburu, Laikipia, Naivasha, Nakuru \u0026 the Mara",
        regions=["Samburu National Reserve", "Ol Pejeta Conservancy", "Lake Naivasha", "Lake Nakuru National Park", "Maasai Mara National Reserve"],
        destination_slug="maasai-mara",
        days=10,
        duration="10 Days / 9 Nights",
        safari_type="Grand Circuit",
        luxury="Luxury",
        tagline="Five ecosystems in ten days, in the order that makes them work",
        summary=(
            "Ten days is where a Kenya trip stops being a single safari and becomes a proper "
            "journey. This route runs north first, through Samburu and Laikipia, then down the Rift "
            "Valley to Naivasha and Nakuru, and finishes with three nights in the Mara. It is "
            "sequenced so each park adds a different landscape rather than repeating the last one."
        ),
        card="Samburu, Laikipia, the Rift Valley lakes and the Mara in one ten-day route.",
        hero="samburu.jpg",
        gallery=[
            ("samburu.jpg", "Reticulated giraffe in Samburu National Reserve"),
            ("laikipia.jpg", "Laikipia plateau country"),
            ("maasai-mara.jpg", "Lion pride on the Mara plains"),
            ("lake-nakuru.jpg", "Lake Nakuru and its shoreline"),
        ],
        highlights=[
            "Samburu's dry-country species along the Ewaso Ng'iro",
            "Rhino conservation work on the Laikipia plateau",
            "Boat and walking safari at Lake Naivasha",
            "Rhino and Rothschild giraffe at Lake Nakuru",
            "Three Mara nights with a full day in the reserve",
        ],
        itinerary=[
            ("Nairobi to Samburu",
             "North past Mount Kenya to Samburu, arriving in the afternoon for a river drive."),
            ("Full day in Samburu",
             "Dawn drive for the special five, afternoon on the river bends."),
            ("Samburu to Laikipia",
             "South to a Laikipia conservancy, afternoon drive and a night drive."),
            ("Laikipia",
             "Rhino monitoring, a guided walk and a full afternoon out on the conservancy."),
            ("Laikipia to Naivasha",
             "Drive south into the Rift Valley for a boat trip and a walk on Crescent Island."),
            ("Naivasha to Nakuru",
             "Morning at leisure, then into Lake Nakuru National Park for an afternoon drive."),
            ("Nakuru to the Mara",
             "Drive across the Rift and into the Mara for a late-afternoon game drive."),
            ("Full day in the Mara",
             "Dawn-to-dusk game viewing with a picnic lunch on the plains."),
            ("Second Mara day",
             "River-line drives and big-cat tracking, with a relaxed middle of the day."),
            ("Morning drive and return",
             "Final early drive, breakfast, then the road or flight back to Nairobi."),
        ],
        accommodation=[
            ("Luxury", "Tented suites and conservancy camps throughout, full board."),
            ("Mixed luxury", "Higher-grade camps in Samburu and the Mara, lodges elsewhere, full board."),
            ("Classic", "Long-established lodges and camps with full board."),
        ],
        activities=[
            "Game drives across five ecosystems",
            "Rhino monitoring on Laikipia",
            "Boat safari and Crescent Island walk at Naivasha",
            "Night drives where permitted on private land",
            "Guided bush walks with armed rangers",
            "Optional balloon safari in the Mara",
        ],
        best_for="Travellers making one long Kenya trip who want variety rather than one park",
    ),
    # 18 -----------------------------------------------------------------
    pkg(
        slug="northern-kenya-frontier",
        title="Northern Kenya Frontier Expedition",
        short="Northern Kenya Frontier",
        group="Kenya Safaris",
        country="Kenya",
        destination="Marsabit \u0026 Lake Turkana",
        regions=["Marsabit National Park", "Lake Turkana"],
        destination_slug="marsabit",
        days=8,
        duration="8 Days / 7 Nights",
        safari_type="Frontier Expedition",
        luxury="Comfort",
        tagline="Volcanic desert, cloud forest and the Jade Sea",
        summary=(
            "The far north is Kenya's other country: lava fields and dust roads, a cloud forest on "
            "Marsabit's mountain, and Lake Turkana, the largest desert lake on earth, held in by "
            "volcanoes. This is a road expedition with long, hot drives on rough tracks, and it is "
            "not for a first safari. What it gives back is space, solitude and landscapes no "
            "southern park can match."
        ),
        card="A road expedition to Marsabit's cloud forest and the shores of Lake Turkana.",
        hero="marsabit.jpg",
        gallery=[
            ("marsabit.jpg", "The road up Mount Marsabit"),
            ("turkana.jpg", "The southern shore of Lake Turkana"),
            ("samburu-card.jpg", "Dry-country landscape on the northern route"),
        ],
        highlights=[
            "Cloud forest on Mount Marsabit and its crater lakes",
            "The Chalbi desert crossing on the route north",
            "Lake Turkana's lava shores and Central Island",
            "Northern Kenya's arid-adapted species and birdlife",
            "Long, empty roads and very few other travellers",
        ],
        itinerary=[
            ("Nairobi to Samburu",
             "North past Isiolo, stopping overnight in Samburu to break the drive and start the "
             "species list."),
            ("Samburu to Marsabit",
             "Long drive north through Laisamis, climbing into Marsabit's forest and cooler air "
             "by the evening."),
            ("Marsabit",
             "Morning in the national park's forest, then out across the Chalbi desert track "
             "toward the lake shore."),
            ("Lake Turkana",
             "Full day at the lake: the shore, the volcanic country and, conditions permitting, "
             "a boat out toward Central Island."),
            ("Lake Turkana",
             "Second desert-lake day, with a community stop and a night under a very large sky."),
            ("Turkana to Marsabit",
             "Return across the Chalbi, back up into the forest for the night."),
            ("Marsabit to Samburu",
             "South down the highway with a picnic stop, overnight in Samburu."),
            ("Samburu to Nairobi",
             "Final long day south to Nairobi, arriving in the evening."),
        ],
        accommodation=[
            ("Comfort", "Rustic lodges and bandas on the route, full board where available."),
            ("Expedition", "Simple camps with basic ablutions and a support vehicle carrying supplies."),
            ("Lodge", "The best available lodge in Marsabit and Turkana for the nights in the north."),
        ],
        activities=[
            "Road expedition driving across northern Kenya",
            "Marsabit forest and crater lakes walk",
            "Chalbi desert crossing",
            "Lake Turkana shoreline and boat excursion",
            "Community visits arranged locally",
            "Birding in arid and lake habitats",
        ],
        best_for="Experienced travellers and photographers who want remoteness over comfort",
        style="4x4 road expedition with support vehicle",
        travel_info=[
            "This is a long-distance road expedition on rough tracks. Days 3 to 7 involve several hours of driving.",
            "Northern Kenya is hot and remote. A support vehicle, extra water and satellite communication are included in the plan.",
            "Camping or simple lodging is the norm in the far north; luxury options do not exist there.",
            "Route conditions are checked before departure and the itinerary may change for safety.",
            "Wildlife sightings are never guaranteed and the region is not a Big Five destination.",
        ],
    ),
    # 19 -----------------------------------------------------------------
    pkg(
        slug="maasai-mara-conservancy",
        title="Maasai Mara Private Conservancy Safari",
        short="Mara Private Conservancy",
        group="Kenya Safaris",
        country="Kenya",
        destination="Maasai Mara Conservancies",
        destination_slug="maasai-mara",
        days=3,
        duration="3 Days / 2 Nights",
        safari_type="Private Conservancy",
        luxury="Luxury",
        tagline="Off-road tracking, night drives and walking, away from the crowds",
        summary=(
            "The conservancies bordering the Mara are leased from Maasai landowners and run on "
            "rules the national reserve cannot offer: off-road tracking when a cat is working, "
            "night drives, and walking safaris with an armed guide. Wildlife density is comparable, "
            "vehicle numbers are far lower, and the fees go directly to the landowner communities."
        ),
        card="Off-road tracking, night drives and walking in a community-run Mara conservancy.",
        hero="maasai-mara-card.jpg",
        gallery=[
            ("maasai-mara-card.jpg", "Savannah inside a Mara conservancy"),
            ("maasai-mara.jpg", "Lion pride on the Mara plains"),
            ("maasai-mara-balloon.jpg", "First light over the Mara"),
        ],
        highlights=[
            "Off-road game tracking, which the national reserve does not allow",
            "Night drives for leopard, serval and hunting lion",
            "Guided walking safaris with an armed conservancy ranger",
            "A fraction of the vehicles at every sighting",
            "Conservancy fees that support landowner communities directly",
        ],
        itinerary=[
            ("Nairobi to the conservancy",
             "Drive or fly to the conservancy boundary, arriving for lunch. Afternoon game drive, "
             "then a night drive after dinner."),
            ("Full conservancy day",
             "Dawn drive with off-road tracking, a bush breakfast, then a guided walk in the late "
             "morning. Afternoon drive and a second night drive."),
            ("Walking and departure",
             "Early walk with a ranger, breakfast, then the transfer back to Nairobi or the "
             "airstrip."),
        ],
        accommodation=[
            ("Luxury", "Conservancy tented suites with private decks and full board."),
            ("Luxury family", "Family tents with a shared living tent and flexible meal times."),
            ("Boutique", "Small camps with six to eight tents and hosted dining."),
        ],
        activities=[
            "Off-road game tracking",
            "Night drives in the conservancy",
            "Guided walking safari",
            "Bush breakfast and sundowners",
            "Community and landowner visit arranged locally",
            "Optional balloon safari at extra cost",
        ],
        best_for="Photographers and travellers who want a quieter Mara with walking and night drives",
    ),
    # 20 -----------------------------------------------------------------
    pkg(
        slug="nairobi-national-park-day-safari",
        title="Nairobi National Park Day Safari",
        short="Nairobi Day Safari",
        group="Kenya Safaris",
        country="Kenya",
        destination="Nairobi National Park",
        destination_slug="nairobi-national-park",
        days=1,
        duration="1 Day",
        safari_type="Day Safari",
        luxury="Comfort",
        tagline="Rhino against the skyline, back in the city by dinner",
        summary=(
            "The only national park inside a capital city, and a genuinely good half day: black rhino, "
            "lion, buffalo and giraffe on open plains with Nairobi's towers on the horizon. It works "
            "as a long layover, a first morning in Kenya, or a rest day before a wedding. The park is "
            "small, so it is a game drive rather than a wilderness day, and we say so."
        ),
        card="A morning of rhino, lion and giraffe inside Nairobi, back by early afternoon.",
        hero="nairobi-national-park.jpg",
        gallery=[
            ("nairobi-national-park.jpg", "Giraffe in Nairobi National Park"),
            ("maasai-mara-card.jpg", "Open savannah on the park's eastern boundary"),
        ],
        highlights=[
            "Black rhino in the park's eastern sector",
            "Lion and buffalo on the Athi plains, with the city skyline behind",
            "Giraffe, zebra and eland close to the main gate",
            "Optional visit to the elephant orphanage or the Giraffe Centre nearby",
            "Half-day format that fits a layover or a business trip",
        ],
        itinerary=[
            ("Nairobi National Park, morning to early afternoon",
             "Collected from your hotel or the airport at first light, then into the park through "
             "the main gate. The morning covers the rhino sanctuary, the Athi basin and the "
             "viewpoints above the Mbagathi river. Picnic breakfast or lunch in the park, then a "
             "return transfer by early afternoon. Optional add-on: the elephant orphanage or the "
             "Giraffe Centre, both a short drive away."),
        ],
        accommodation=[
            ("No overnight", "This is a day safari. We can add a Nairobi hotel night before or after if you need one."),
        ],
        activities=[
            "Morning game drive in Nairobi National Park",
            "Rhino sanctuary and Athi basin drives",
            "Picnic breakfast or lunch in the park",
            "Optional elephant orphanage visit",
            "Optional Giraffe Centre visit",
            "Hotel or airport transfers",
        ],
        best_for="Layovers, first or last days in Kenya, and short business trips",
        style="Private half-day game drive",
        inclusions=[
            "Private safari vehicle with professional driver-guide",
            "Nairobi National Park entry fees for the day",
            "Picnic breakfast or lunch in the park",
            "Bottled drinking water in the vehicle",
            "Hotel or airport pickup and return transfer",
            "24/7 WhatsApp support from your Horizon Legacy consultant",
        ],
        exclusions=[
            "Any overnight accommodation unless added",
            "Elephant orphanage or Giraffe Centre entry fees",
            "Alcoholic drinks and personal expenses",
            "Gratuities for your guide",
            "Travel insurance",
            "Any item not listed under inclusions",
        ],
        travel_info=[
            "A single morning covers the park comfortably. Afternoon departures can also be arranged.",
            "Nairobi National Park is fenced and close to the city, so this is a game drive rather than a wilderness day.",
            "Park fees are quoted at the official rate current at the time of booking.",
            "Wildlife sightings are never guaranteed; the park is small and the morning is the best window.",
        ],
    ),
]
