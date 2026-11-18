# -*- coding: utf-8 -*-
"""
Horizon Legacy Safaris - Comprehensive Destination Database
Contains structured data for 52 world-class destinations across Kenya,
East Africa, Africa, Asia, Europe, Middle East, Americas, Oceania, and Antarctica.
"""

DESTINATIONS = [
    # =========================================================================
    # KENYA (14 Destinations)
    # =========================================================================
    {
        "id": "maasai-mara",
        "slug": "maasai-mara",
        "name": "Maasai Mara National Reserve",
        "country": "Kenya",
        "region": "Kenya",
        "regions": ["Kenya", "East Africa", "Africa"],
        "categories": ["Wildlife Safaris", "Luxury Getaways", "Family Holidays", "Adventure Travel"],
        "tagline": "The Crown Jewel of African Wildlife & the Great Migration",
        "shortDescription": "Witness the spectacle of the Great Wildebeest Migration, abundant Big Five predators, and hot air balloon flights over iconic golden savannah plains.",
        "overview": (
            "Maasai Mara National Reserve is globally celebrated as one of Africa's greatest wildlife reserves. "
            "Bordering Tanzania's Serengeti, the Mara encompasses over 1,500 square kilometers of pristine savannah, "
            "rolling hills, and acacia-dotted grasslands. It is home to an extraordinary concentration of big cats, "
            "including prides of lions, elusive leopards, and swift cheetahs.\n\n"
            "Between July and October, the reserve hosts the world-famous Great Wildebeest Migration, where over two "
            "million wildebeest, zebras, and gazelles brave predator-infested Mara River crossings in search of lush pastures. "
            "Beyond the migration, the Mara offers breathtaking year-round safari game drives, sunrise hot air balloon safaris, "
            "and enriching cultural encounters with the traditional Maasai pastoralist communities."
        ),
        "heroImage": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1534177616072-ef7dc120449d?auto=format&fit=crop&w=1000&q=80", "caption": "Lions resting in the golden grasses of Maasai Mara"},
            {"url": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=1000&q=80", "caption": "Dawn hot air balloon safari over the Mara plains"},
            {"url": "https://images.unsplash.com/photo-1575550959106-5a7defe28b56?auto=format&fit=crop&w=1000&q=80", "caption": "Cheetah perched scanning for prey"},
            {"url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1000&q=80", "caption": "Elephant family marching towards the Mara River"}
        ],
        "coordinates": [-1.4889, 35.1439],
        "highlights": [
            "World-famous Great Wildebeest Migration & dramatic river crossings",
            "Highest density of lions, cheetahs, and leopards in East Africa",
            "Spectacular sunrise hot air balloon safaris followed by bush champagne breakfasts",
            "Authentic cultural visits to indigenous Maasai Manyattas and villages",
            "Exclusive private conservancy night game drives and bushwalking safaris"
        ],
        "activities": [
            "Early morning & sunset 4x4 game drives",
            "Hot air balloon safaris over the plains",
            "Maasai cultural boma visits & traditional dances",
            "Guided bushwalking safaris with Maasai naturalists",
            "Bush dinners under the African starlit sky",
            "Photographic safaris led by wildlife photography guides"
        ],
        "bestTimeToVisit": "July to October is ideal for the Great Migration. January to March offers clear skies, excellent cat tracking, and fewer vehicles.",
        "quickFacts": {
            "bestTime": "July – October & Jan – Mar",
            "idealDuration": "3 – 5 Days",
            "language": "English, Swahili, Maa",
            "currency": "Kenyan Shilling (KES) & USD",
            "visa": "Kenya eTA required online",
            "climate": "Pleasant warm days (25-28°C), cool evenings (12-15°C)"
        },
        "accommodations": [
            {"name": "Angama Mara", "tier": "Ultra-Luxury", "location": "Oloololo Escarpment", "description": "High above the Mara plains with panoramic glass-front tented suites."},
            {"name": "Governors' Camp", "tier": "Luxury Tented", "location": "Mara Riverbanks", "description": "Classic safari elegance nestled in lush forest along the winding Mara River."},
            {"name": "Mara Serena Safari Lodge", "tier": "Premium Lodge", "location": "Mara Triangle", "description": "Inspired by traditional Maasai Manyattas, offering sweeping savannah panoramas."},
            {"name": "Cottar's 1920s Safari Camp", "tier": "Luxury Heritage", "location": "Olderkesi Conservancy", "description": "Timeless vintage glamour with private guides and immaculate wilderness access."}
        ],
        "packageIds": [],
        "relatedSlugs": ["amboseli", "lake-nakuru", "serengeti", "samburu"],
        "faqs": [
            {
                "q": "When can I see the Great Migration river crossing?",
                "a": "The migration river crossings typically occur between late July and October, with peak activity across August and September as herds cross between the Serengeti and Maasai Mara."
            },
            {
                "q": "How do I get to Maasai Mara from Nairobi?",
                "a": "You can take a scenic 45-minute scheduled flight from Wilson Airport (Nairobi) directly to one of the Mara airstrips, or travel by road in a luxury 4x4 Land Cruiser (approx. 5 to 6 hours)."
            },
            {
                "q": "Is the Maasai Mara suitable for family holidays?",
                "a": "Yes! Many luxury lodges offer family suites, junior ranger programs, bushcraft lessons, and Maasai warrior training that children find unforgettable."
            }
        ]
    },
    {
        "id": "amboseli",
        "slug": "amboseli",
        "name": "Amboseli National Park",
        "country": "Kenya",
        "region": "Kenya",
        "regions": ["Kenya", "East Africa", "Africa"],
        "categories": ["Wildlife Safaris", "Luxury Getaways", "Family Holidays"],
        "tagline": "Land of Giants Beneath the Majestic Mount Kilimanjaro",
        "shortDescription": "Marvel at free-roaming giant elephant herds framed by the snow-capped summit of Mount Kilimanjaro, Africa's highest mountain.",
        "overview": (
            "Amboseli National Park is world-renowned for offering the iconic African safari postcard: massive herds of elephants "
            "grazing gracefully with the snow-capped volcanic peak of Mount Kilimanjaro rising dramatically in the background. "
            "Covering nearly 400 square kilometers near the Tanzanian border, Amboseli combines dry savannah plains with "
            "verdant marshes fed by underground springs from Kilimanjaro.\n\n"
            "This unique hydrology draws an astonishing variety of wildlife, from big tuskers and lions to cheetahs, hippos, "
            "and over 400 species of birds. Observation Hill provides panoramic 360-degree vistas across the entire park, "
            "where swamp elephants bathe and dust-devil whirlwinds dance across the dried Lake Amboseli bed."
        ),
        "heroImage": "https://images.unsplash.com/photo-1589556264800-08ae9e129a8c?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1589556264800-08ae9e129a8c?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1581852017103-68ac6550407b?auto=format&fit=crop&w=1000&q=80", "caption": "Elephant family with Kilimanjaro in the backdrop"},
            {"url": "https://images.unsplash.com/photo-1534567153574-2b12153a87f0?auto=format&fit=crop&w=1000&q=80", "caption": "Lioness on morning prowl in Amboseli"},
            {"url": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=1000&q=80", "caption": "Zebras drinking at Amboseli swamp"},
            {"url": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=1000&q=80", "caption": "Golden sunrise over Observation Hill"}
        ],
        "coordinates": [-2.6527, 37.2606],
        "highlights": [
            "Incredible close encounters with Africa's famous long-tusked elephants",
            "Unrivalled photography backdrop of snow-capped Mount Kilimanjaro",
            "Panoramic viewing from Observation Hill overlooking Enkongo Narok swamp",
            "Over 400 species of resident and migratory birds",
            "Rich cultural exchanges with local Maasai communities"
        ],
        "activities": [
            "Photographic morning game drives beneath Kilimanjaro",
            "Climbing Observation Hill for swamp birdwatching",
            "Sunset sundowners with views of the mountain peak",
            "Maasai cultural community visits",
            "Night drives in adjacent private wildlife conservancies"
        ],
        "bestTimeToVisit": "June to October and January to February offer dry conditions with clear mountain views and animals congregating around the central swamps.",
        "quickFacts": {
            "bestTime": "June – October & Jan – Feb",
            "idealDuration": "2 – 3 Days",
            "language": "English, Swahili, Maa",
            "currency": "Kenyan Shilling (KES) & USD",
            "visa": "Kenya eTA required online",
            "climate": "Warm and dry (27-30°C daytime, 14-16°C night)"
        },
        "accommodations": [
            {"name": "Tortilis Camp", "tier": "Eco-Luxury Tented", "location": "Kitirua Conservancy", "description": "Under thatch tents with uninterrupted views of Mount Kilimanjaro."},
            {"name": "Ol Tukai Lodge", "tier": "Luxury Safari Lodge", "location": "Heart of Amboseli", "description": "Set inside the park with lush gardens and prime elephant viewing."},
            {"name": "Amboseli Serena Safari Lodge", "tier": "Premium Lodge", "location": "Amboseli Swamps", "description": "Maasai-inspired architecture shaded by giant acacia trees."}
        ],
        "packageIds": [],
        "relatedSlugs": ["tsavo-national-parks", "maasai-mara", "kilimanjaro", "lake-naivasha"],
        "faqs": [
            {
                "q": "What is the best time of day to see Mount Kilimanjaro clearly?",
                "a": "Early morning right after sunrise and late afternoon before sunset offer the clearest views, as cloud cover typically gathers over the summit during mid-day."
            },
            {
                "q": "How far is Amboseli from Nairobi?",
                "a": "It takes approximately 4 hours by road via Namanga or Emali, or a quick 35-minute scheduled flight from Wilson Airport to Amboseli Airstrip."
            }
        ]
    },
    {
        "id": "lake-nakuru",
        "slug": "lake-nakuru",
        "name": "Lake Nakuru National Park",
        "country": "Kenya",
        "region": "Kenya",
        "regions": ["Kenya", "East Africa", "Africa"],
        "categories": ["Wildlife Safaris", "Luxury Getaways", "Family Holidays"],
        "tagline": "Rift Valley Haven for Rhinos, Waterfalls & Flamingos",
        "shortDescription": "Discover Kenya's sanctuary for endangered black and white rhinos, pink flamingo-fringed shores, and picturesque Great Rift Valley lookouts.",
        "overview": (
            "Nestled on the floor of the Great Rift Valley, Lake Nakuru National Park is one of Kenya's most accessible "
            "and rewarding wildlife sanctuaries. Famous worldwide for the kaleidoscopic spectacle of flamingos gathering "
            "along its alkaline shores, the park is also Kenya's premier sanctuary for both endangered black and white rhinos.\n\n"
            "Enclosed within picturesque yellow-barked fever tree woodlands and volcanic cliffs, visitors enjoy sightings "
            "of rare Rothschild's giraffes, tree-climbing lions, leopards, waterbucks, and African buffalos. "
            "Viewpoints like Baboon Cliff and Lion Hill afford breathtaking panoramas across the sparkling lake, "
            "while Makalia Falls cascades gracefully in the southern woodland basin."
        ),
        "heroImage": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1000&q=80", "caption": "The Encore Hotel Nakuru luxury pool and grounds"},
            {"url": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=1000&q=80", "caption": "White rhino grazing peacefully along Lake Nakuru shore"},
            {"url": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=1000&q=80", "caption": "Flock of flamingos feeding along the alkaline shallows"},
            {"url": "https://images.unsplash.com/photo-1589556264800-08ae9e129a8c?auto=format&fit=crop&w=1000&q=80", "caption": "Panoramic Rift Valley view from Baboon Cliff"}
        ],
        "coordinates": [-0.3667, 36.0833],
        "highlights": [
            "Kenya's premier sanctuary for endangered Black & White Rhinoceros",
            "Flamingo and pelican birdwatching along the Great Rift Valley alkaline shores",
            "Sensational cliffside views from Baboon Cliff, Out of Africa, and Lion Hill",
            "Makalia Falls waterfall nature walks",
            "Home to rare Rothschild's giraffes and tree-climbing lions"
        ],
        "activities": [
            "Rhino tracking game drives with experienced safari guides",
            "Scenic Great Rift Valley escarpment viewpoints",
            "Birdwatching along the lakeshore with 450+ avian species",
            "Luxury weekend staycations & fine dining in Nakuru City",
            "Visiting Hyrax Hill prehistoric site and Menengai Crater"
        ],
        "bestTimeToVisit": "Year-round destination. November to April is spectacular for migratory birdwatching; July to October offers dry game tracking.",
        "quickFacts": {
            "bestTime": "All Year Round (Peak: Jun – Mar)",
            "idealDuration": "2 – 3 Days",
            "language": "English, Swahili",
            "currency": "Kenyan Shilling (KES) & USD",
            "visa": "Kenya eTA required online",
            "climate": "Temperate Rift Valley climate (22-26°C)"
        },
        "accommodations": [
            {"name": "The Encore Hotel Nakuru", "tier": "Featured Luxury Partner", "location": "Nakuru City / Lake Nakuru View", "description": "Modern luxury hotel with lavish executive suites, gourmet dining, and outdoor swimming pool."},
            {"name": "Sarova Lion Hill Game Lodge", "tier": "Luxury Lodge", "location": "Lion Hill Inside Park", "description": "Classic safari lodge with panoramic lake vistas and traditional dance performances."},
            {"name": "Lake Nakuru Sopa Lodge", "tier": "Premium Lodge", "location": "Western Escarpment", "description": "Perched on a ridge with sweeping views across the lake and flamingo shores."}
        ],
        "packageIds": ["encore-hotel-nakuru-2d1n"],
        "relatedSlugs": ["lake-naivasha", "hells-gate", "aberdare-national-park", "maasai-mara"],
        "faqs": [
            {
                "q": "Is Lake Nakuru easy to reach from Nairobi?",
                "a": "Yes! Lake Nakuru is only 160 km northwest of Nairobi, an easy 2.5 to 3 hour drive along the scenic Great Rift Valley Highway with viewpoints overlooking Mount Longonot."
            },
            {
                "q": "Can I see rhinos in Lake Nakuru National Park?",
                "a": "Absolutely. Lake Nakuru is one of the highest-density rhino sanctuaries in Africa, making sightings of both black and white rhinos almost guaranteed."
            }
        ]
    },
    {
        "id": "lake-naivasha",
        "slug": "lake-naivasha",
        "name": "Lake Naivasha & Crescent Island",
        "country": "Kenya",
        "region": "Kenya",
        "regions": ["Kenya", "East Africa", "Africa"],
        "categories": ["Luxury Getaways", "Family Holidays", "Adventure Travel"],
        "tagline": "Freshwater Serenity, Crescent Island Walks & Hippos",
        "shortDescription": "Glide across freshwater waters dotted with hippos, walk among giraffes and zebras on Crescent Island, and relax in lakeside luxury resorts.",
        "overview": (
            "Lake Naivasha is the highest of the Great Rift Valley lakes, lying at 1,884 meters above sea level. "
            "A freshwater oasis fringed by papyrus reeds and magnificent fever trees, Naivasha is a beloved weekend escape "
            "for residents and international travelers seeking tranquility and outdoor adventure.\n\n"
            "A boat safari on Lake Naivasha brings you up close to basking pods of hippos and swooping African fish eagles. "
            "On Crescent Island Game Sanctuary, visitors experience one of Kenya's few walking safaris without predators, "
            "strolling freely amidst herds of giraffes, zebras, wildebeests, waterbucks, and gazelles."
        ),
        "heroImage": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=1000&q=80", "caption": "Giraffes roaming peacefully on Crescent Island"},
            {"url": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=1000&q=80", "caption": "Boat cruise approaching hippos at Lake Naivasha"},
            {"url": "https://images.unsplash.com/photo-1589556264800-08ae9e129a8c?auto=format&fit=crop&w=1000&q=80", "caption": "African Fish Eagle resting on submerged acacia tree"},
            {"url": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1000&q=80", "caption": "Sunset tranquility over Lake Naivasha waters"}
        ],
        "coordinates": [-0.7667, 36.4333],
        "highlights": [
            "Walking safaris among giraffes and zebras on Crescent Island",
            "Motorized boat safaris watching pods of hippos and fish eagles",
            "Proximity to Hell's Gate National Park & Mount Longonot volcano",
            "World-class spa resorts and championship 18-hole golf courses",
            "Highland climate perfect for romantic weekend retreats"
        ],
        "activities": [
            "Guided walking safari on Crescent Island",
            "Boat cruise across the lake with fish eagle feeding",
            "Biking and gorge exploration at nearby Hell's Gate",
            "Hiking the crater rim of Mount Longonot",
            "Relaxing at luxury geothermal natural spas"
        ],
        "bestTimeToVisit": "Pleasant all year round. Dry months from June to October and December to March are best for hiking and outdoor walking.",
        "quickFacts": {
            "bestTime": "All Year Round (Dry: Jun – Oct)",
            "idealDuration": "2 – 3 Days",
            "language": "English, Swahili",
            "currency": "Kenyan Shilling (KES) & USD",
            "visa": "Kenya eTA required online",
            "climate": "Cool temperate highland (20-25°C daytime, 11-13°C nights)"
        },
        "accommodations": [
            {"name": "Enashipai Resort & Spa", "tier": "5-Star Luxury Resort", "location": "Moi South Lake Road", "description": "Lakeside luxury featuring Siyara Spa, swimming pools, and manicured tropical gardens."},
            {"name": "Chui Lodge", "tier": "Exclusive Boutique", "location": "Oserengoni Wildlife Sanctuary", "description": "Private wildlife conservancy lodge built with local stone and olive wood."},
            {"name": "Great Rift Valley Lodge & Golf Resort", "tier": "Luxury Golf Resort", "location": "Eburru Hills", "description": "Perched high on the escarpment with an 18-hole golf course and lake views."}
        ],
        "packageIds": [],
        "relatedSlugs": ["lake-nakuru", "hells-gate", "aberdare-national-park", "maasai-mara"],
        "faqs": [
            {
                "q": "Can I walk safely on Crescent Island?",
                "a": "Yes! There are no large carnivores (lions, leopards) on Crescent Island, making it one of the safest places in Africa to walk right alongside giraffes, zebras, and impalas."
            }
        ]
    },
    {
        "id": "diani-beach",
        "slug": "diani-beach",
        "name": "Diani Beach",
        "country": "Kenya",
        "region": "Kenya",
        "regions": ["Kenya", "East Africa", "Africa"],
        "categories": ["Beach Escapes", "Luxury Getaways", "Honeymoon Destinations", "Family Holidays"],
        "tagline": "Voted Africa's Leading Beach Destination on the Indian Ocean",
        "shortDescription": "Relax on pristine powdery white sands, dive vibrant coral reefs, and experience luxury beachfront boutiques on Kenya's South Coast.",
        "overview": (
            "Diani Beach, situated on Kenya's South Coast south of Mombasa, has repeatedly earned the title of Africa's "
            "Leading Beach Destination at the World Travel Awards. Stretching over 17 kilometers of dazzling white sand "
            "kissed by the warm turquoise waves of the Indian Ocean, Diani is the quintessential tropical paradise.\n\n"
            "An offshore coral barrier reef protects the shoreline from rough waters, creating calm, crystal-clear lagoons "
            "ideal for swimming, windsurfing, and snorkeling. Beyond the beach, travelers can explore ancient sacred Kaya coastal "
            "forests, encounter colobus monkeys in the canopy, swim with whale sharks, or take a dhow safari to Kisite Mpunguti Marine Park."
        ),
        "heroImage": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1000&q=80", "caption": "Powdery white sand shores of Diani Beach"},
            {"url": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=1000&q=80", "caption": "Snorkeling with sea turtles at Kisite Marine Park"},
            {"url": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=1000&q=80", "caption": "Luxury private beachfront villa at sunset"},
            {"url": "https://images.unsplash.com/photo-1510414842594-a61782153f5b?auto=format&fit=crop&w=1000&q=80", "caption": "Traditional wooden dhow sailing the turquoise lagoon"}
        ],
        "coordinates": [-4.2788, 39.5936],
        "highlights": [
            "17 km of unspoilt powdery white sands and swaying coconut palms",
            "Marine safaris to Kisite Mpunguti Marine Park with dolphins and sea turtles",
            "World-renowned kitesurfing and stand-up paddleboarding conditions",
            "Shimba Hills National Reserve day safari tracking rare sable antelopes",
            "Romantic sunset dhow dinners and beachfront candlelit dining"
        ],
        "activities": [
            "Kitesurfing, windsurfing, and jet skiing",
            "Traditional dhow excursions to Wasini Island",
            "Scuba diving and snorkeling on the outer barrier reef",
            "Deep-sea game fishing for marlin and sailfish",
            "Skydiving directly over Diani's white beach sands"
        ],
        "bestTimeToVisit": "December to March and July to October bring sunny tropical weather with calm, crystal-clear ocean waters.",
        "quickFacts": {
            "bestTime": "Dec – Mar & Jul – Oct",
            "idealDuration": "4 – 7 Days",
            "language": "English, Swahili",
            "currency": "Kenyan Shilling (KES) & USD",
            "visa": "Kenya eTA required online",
            "climate": "Warm tropical climate (28-32°C year-round)"
        },
        "accommodations": [
            {"name": "The Sands at Nomad", "tier": "Eco-Chic Luxury", "location": "Diani Beachfront", "description": "Boutique luxury set within an indigenous coastal forest with fine Italian dining."},
            {"name": "Alfajiri Villas", "tier": "Exclusive Private Villa", "location": "Cliffside Diani", "description": "Considered by Conde Nast one of the world's most luxurious private villas with private butler service."},
            {"name": "Swahili Beach Resort", "tier": "5-Star Architectural", "location": "Diani Beach", "description": "Spectacular cascading eight-tier pool blending Arabic, Indian, and Swahili architecture."}
        ],
        "packageIds": [],
        "relatedSlugs": ["watamu", "mombasa", "lamu", "zanzibar"],
        "faqs": [
            {
                "q": "How do I get to Diani Beach?",
                "a": "You can fly directly from Nairobi (Wilson or JKIA) to Ukunda Airstrip (Diani), landing just 10 minutes from your beach resort, or fly to Mombasa Airport and take the scenic Diani bypass."
            }
        ]
    },
    {
        "id": "watamu",
        "slug": "watamu",
        "name": "Watamu & Malindi",
        "country": "Kenya",
        "region": "Kenya",
        "regions": ["Kenya", "East Africa", "Africa"],
        "categories": ["Beach Escapes", "Luxury Getaways", "Honeymoon Destinations", "Adventure Travel"],
        "tagline": "Crystalline Marine Lagoons, Sandbanks & Ancient Swahili Ruins",
        "shortDescription": "Immerse yourself in Watamu Marine National Park, explore 13th-century Gedi Ruins, and relax on secluded golden sandbanks.",
        "overview": (
            "Watamu is a peaceful coastal village situated approximately 105 km north of Mombasa and 15 km south of Malindi. "
            "Renowned for its natural beauty, Watamu boasts a series of picturesque bays, coral islands, and the UNESCO-protected "
            "Watamu Marine National Park, which protects sea turtles, coral gardens, and vibrant marine life.\n\n"
            "Just inland lies the Arabuko-Sokoke Forest, the largest remaining tract of coastal indigenous forest in East Africa, "
            "sheltering rare golden-rumped elephant shrews and Clarke's weavers. Nearby, the mysterious 13th-century Swahili ruins of Gedi "
            "offer a fascinating archaeological journey through ancient mosques, palaces, and coral stone gateways hidden beneath giant baobabs."
        ),
        "heroImage": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=1000&q=80", "caption": "Crystalline sandbank exposed at low tide in Watamu"},
            {"url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1000&q=80", "caption": "Sailing dhow near the coral islands of Watamu Bay"},
            {"url": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=1000&q=80", "caption": "Relaxed seaside dining overlooking the lagoon"}
        ],
        "coordinates": [-3.3500, 40.0167],
        "highlights": [
            "Watamu Marine National Park & sea turtle rehabilitation center",
            "Sardinia 2 sandbank day trips with fresh seafood grilled on sandbanks",
            "UNESCO Gedi Ruins 13th-century lost Swahili city",
            "Mida Creek mangrove boardwalk and sunset canoeing",
            "Arabuko Sokoke Forest birdwatching and butterfly tracking"
        ],
        "activities": [
            "Snorkeling and scuba diving with dolphins and sea turtles",
            "Paddleboarding across the tranquil Mida Creek mangroves",
            "Exploring the ancient Gedi ruins and Kipepeo butterfly project",
            "Big game deep-sea fishing in the Malindi-Watamu trench",
            "Sunset cocktail cruises aboard traditional Swahili dhows"
        ],
        "bestTimeToVisit": "October to April offers crystal-clear water visibility for diving and calm sunny skies.",
        "quickFacts": {
            "bestTime": "Oct – Apr",
            "idealDuration": "3 – 5 Days",
            "language": "English, Swahili, Italian",
            "currency": "Kenyan Shilling (KES) & USD",
            "visa": "Kenya eTA required online",
            "climate": "Warm tropical coastal weather (28-31°C)"
        },
        "accommodations": [
            {"name": "Medina Palms", "tier": "5-Star Luxury Suites", "location": "Watamu Beachfront", "description": "Moroccan-inspired luxury villas, rooftop penthouses, and private plunge pools."},
            {"name": "Hemingways Watamu", "tier": "Luxury Icon", "location": "Watamu Marine Park", "description": "World-class beachfront hotel renowned for big game fishing, fine dining, and marine views."}
        ],
        "packageIds": [],
        "relatedSlugs": ["diani-beach", "lamu", "mombasa", "zanzibar"],
        "faqs": [
            {
                "q": "What is the closest airport to Watamu?",
                "a": "Malindi Airport is only 20 minutes from Watamu, with daily scheduled flights from Nairobi Wilson and JKIA."
            }
        ]
    },
    {
        "id": "mombasa",
        "slug": "mombasa",
        "name": "Mombasa Coastal Island",
        "country": "Kenya",
        "region": "Kenya",
        "regions": ["Kenya", "East Africa", "Africa"],
        "categories": ["Beach Escapes", "Cultural Experiences", "City Breaks", "Family Holidays"],
        "tagline": "Historic Swahili Gateway, Fort Jesus & North Coast Resorts",
        "shortDescription": "Step back through centuries of spice trade history in Old Town, visit UNESCO Fort Jesus, and relax at sun-kissed North Coast beach resorts.",
        "overview": (
            "Mombasa is Kenya's second-largest city and its historic maritime soul. Located on an island connected to the mainland "
            "by bridges and ferries, Mombasa has been a bustling trading crossroads between Arabia, Persia, India, and Europe "
            "for over a millennium.\n\n"
            "Its UNESCO World Heritage site, Fort Jesus, built by the Portuguese in 1593, guards the entrance to the Old Port. "
            "Strolling through Mombasa's Old Town reveals narrow cobbled alleyways lined with intricately carved wooden doors, "
            "vibrant spice bazaars, and traditional Swahili coffee houses. Just north of the island lie the idyllic golden beaches "
            "of Nyali, Bamburi, and Shanzu, brimming with luxury beach hotels and oceanfront dining."
        ),
        "heroImage": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=1000&q=80", "caption": "Sunbed by the pool at Mombasa beach resort"},
            {"url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1000&q=80", "caption": "Old Port Mombasa overlooking the Indian Ocean"}
        ],
        "coordinates": [-4.0435, 39.6682],
        "highlights": [
            "UNESCO World Heritage Fort Jesus & multimedia sound and light show",
            "Mombasa Old Town historical walking tour and antique spice markets",
            "Haller Park reclaimed limestone quarry wildlife sanctuary",
            "Famous Tamarind Dhow romantic seafood dinner cruise",
            "Pristine North Coast beaches of Nyali, Bamburi, and Shanzu"
        ],
        "activities": [
            "Heritage walking tours through Mombasa Old Town",
            "Dinner cruise aboard the historic Tamarind Dhow",
            "Feeding giraffes and seeing giant tortoises at Haller Park",
            "Water sports, glass-bottom boat trips, and beach lounging",
            "Shopping for authentic Swahili spices, kikoys, and hand-carved art"
        ],
        "bestTimeToVisit": "July to October and December to March offer warm, sunny weather and vibrant coastal culture.",
        "quickFacts": {
            "bestTime": "Jul – Oct & Dec – Mar",
            "idealDuration": "2 – 4 Days",
            "language": "English, Swahili",
            "currency": "Kenyan Shilling (KES) & USD",
            "visa": "Kenya eTA required online",
            "climate": "Tropical maritime (28-33°C)"
        },
        "accommodations": [
            {"name": "Serena Beach Resort & Spa", "tier": "5-Star Swahili Heritage", "location": "Shanzu Beach", "description": "Modeled after an authentic 13th-century Swahili town with lush bougainvillea gardens."},
            {"name": "Sarova Whitesands Beach Resort & Spa", "tier": "Luxury Beach Resort", "location": "Bamburi Beach", "description": "Set over 22 acres of palm-fringed grounds with five outdoor swimming pools."}
        ],
        "packageIds": [],
        "relatedSlugs": ["diani-beach", "watamu", "lamu", "tsavo-national-parks"],
        "faqs": [
            {
                "q": "Can I take the SGR train from Nairobi to Mombasa?",
                "a": "Yes! The modern Madaraka Express SGR train connects Nairobi to Mombasa in just 4.5 hours, traversing scenic Tsavo wilderness where you can spot elephants from your window."
            }
        ]
    },
    {
        "id": "tsavo-national-parks",
        "slug": "tsavo-national-parks",
        "name": "Tsavo National Parks (East & West)",
        "country": "Kenya",
        "region": "Kenya",
        "regions": ["Kenya", "East Africa", "Africa"],
        "categories": ["Wildlife Safaris", "Adventure Travel", "Luxury Getaways"],
        "tagline": "Legendary Red Elephants, Mzima Springs & Rugged Wilderness",
        "shortDescription": "Traverse Kenya's largest wilderness, famous for dust-red elephants, crystal-clear Mzima Springs hippo chambers, and Shetani lava flows.",
        "overview": (
            "Together, Tsavo East and Tsavo West form one of the largest protected wildlife sanctuaries on the planet, "
            "spanning nearly 22,000 square kilometers between Nairobi and the Kenyan coast. Divided by the railway and highway, "
            "the two parks offer starkly distinct yet complementary safari landscapes.\n\n"
            "Tsavo East is celebrated for its vast, rolling semi-arid plains, the 300-km-long Yatta Plateau (the world's longest lava flow), "
            "Lugard Falls, and the iconic 'Red Elephants of Tsavo'—magnificent herds stained ochre-red from the volcanic soil. "
            "Tsavo West features dramatic volcanic topography, including the jagged Shetani Lava Flow, Roaring Rocks, and Mzima Springs, "
            "where fifty million gallons of crystal-clear spring water gush daily into pools with an underwater glass viewing chamber for hippos and fish."
        ),
        "heroImage": "https://images.unsplash.com/photo-1534177616072-ef7dc120449d?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1534177616072-ef7dc120449d?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1534177616072-ef7dc120449d?auto=format&fit=crop&w=1000&q=80", "caption": "Red-dusted elephants marching through Tsavo savannah"},
            {"url": "https://images.unsplash.com/photo-1589556264800-08ae9e129a8c?auto=format&fit=crop&w=1000&q=80", "caption": "Mzima Springs crystal-clear water pools"}
        ],
        "coordinates": [-2.9833, 38.4667],
        "highlights": [
            "Legendary Tsavo 'Red Elephants' dust-bathing in volcanic soil",
            "Underwater hippo and fish observation chamber at Mzima Springs",
            "World's longest lava flow: The 300 km Yatta Plateau",
            "Black Rhino sanctuary in the Ngulia Valley",
            "Lugard Falls and Mudanda Rock natural water catchment"
        ],
        "activities": [
            "Extensive wilderness game drives across raw landscapes",
            "Visiting Mzima Springs nature trail with armed rangers",
            "Exploring the Shetani Lava Flow and volcanic caves",
            "Sundowners atop Poacher's Lookout with views of Kilimanjaro",
            "Birdwatching for over 500 species in Ngulia"
        ],
        "bestTimeToVisit": "June to October and January to February offer dry conditions and excellent visibility around waterholes.",
        "quickFacts": {
            "bestTime": "Jun – Oct & Jan – Feb",
            "idealDuration": "2 – 4 Days",
            "language": "English, Swahili",
            "currency": "Kenyan Shilling (KES) & USD",
            "visa": "Kenya eTA required online",
            "climate": "Warm and semi-arid (27-32°C daytime)"
        },
        "accommodations": [
            {"name": "Finch Hattons Luxury Tented Camp", "tier": "Ultra-Luxury Tented", "location": "Tsavo West", "description": "Aristocratic tented luxury with private plunge pools overlooking natural hippo pools."},
            {"name": "Kilaguni Serena Safari Lodge", "tier": "Classic Safari Lodge", "location": "Tsavo West", "description": "Kenya's first safari lodge, set directly in front of a busy natural waterhole."},
            {"name": "Salt Lick Safari Lodge", "tier": "Unique Architecture", "location": "Taita Hills Wildlife Sanctuary", "description": "Iconic stilted round-rooms connected by elevated walkways directly above animal waterholes."}
        ],
        "packageIds": [],
        "relatedSlugs": ["amboseli", "mombasa", "diani-beach", "maasai-mara"],
        "faqs": [
            {
                "q": "Why are the elephants in Tsavo red?",
                "a": "Tsavo's elephants are regular African savannah elephants, but they dust-bathe and wallow in the rich red volcanic laterite soil, giving them their iconic, radiant red hue."
            }
        ]
    },
    {
        "id": "mount-kenya",
        "slug": "mount-kenya",
        "name": "Mount Kenya & Laikipia Plateau",
        "country": "Kenya",
        "region": "Kenya",
        "regions": ["Kenya", "East Africa", "Africa"],
        "categories": ["Mountain Adventures", "Adventure Travel", "Luxury Getaways"],
        "tagline": "Africa's Second-Highest Peak & Premier Private Conservancies",
        "shortDescription": "Trek glacial alpine valleys on Mount Kenya (5,199m) or experience exclusive rhino and wild dog conservation on the Laikipia Plateau.",
        "overview": (
            "Mount Kenya is Africa's second-highest mountain at 5,199 meters and a revered UNESCO World Heritage Site. "
            "An extinct stratovolcano that once rivalled Kilimanjaro in height, Mount Kenya features jagged glaciated peaks "
            "(Batian, Nelion, and Point Lenana), afro-alpine moorlands, giant lobelias, and emerald tarn lakes.\n\n"
            "Stretching northwest from the slopes of the mountain lies the magnificent Laikipia Plateau. A visionary model "
            "for community-led conservation, Laikipia is home to Kenya's highest concentration of endangered black rhinos, "
            "reintroduced African wild dogs, and Grevy's zebras, protected across exclusive private ranches and luxury eco-lodges."
        ),
        "heroImage": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1000&q=80", "caption": "Mount Kenya peaks rising above alpine moorlands"},
            {"url": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=1000&q=80", "caption": "Rhino sanctuary in Laikipia conservancy"}
        ],
        "coordinates": [-0.1521, 37.3084],
        "highlights": [
            "Point Lenana summit trekking (4,985m) accessible to regular hikers",
            "UNESCO afro-alpine flora featuring giant groundsels and lobelias",
            "Premier private conservancies of Laikipia with Black Rhinos and Wild Dogs",
            "Scenic high-altitude fly-fishing in alpine glacial tarns",
            "Fairmont Mount Kenya Safari Club historic equator-straddling grounds"
        ],
        "activities": [
            "Multi-day trekking expeditions (Sirimon & Chogoria routes)",
            "Helicopter scenic flights to Mount Kenya's peaks and alpine lakes",
            "Horseback and camel safaris across Laikipia plains",
            "Tracking wild dogs and rhinos with dedicated conservation rangers",
            "Fly-fishing for rainbow and brown trout in mountain streams"
        ],
        "bestTimeToVisit": "December to March and July to October offer the clearest mountain weather and safest trekking conditions.",
        "quickFacts": {
            "bestTime": "Dec – Mar & Jul – Oct",
            "idealDuration": "3 – 6 Days",
            "language": "English, Swahili, Kikuyu",
            "currency": "Kenyan Shilling (KES) & USD",
            "visa": "Kenya eTA required online",
            "climate": "Alpine mountain climate (sub-zero on peaks, 15-22°C on plateau)"
        },
        "accommodations": [
            {"name": "Fairmont Mount Kenya Safari Club", "tier": "5-Star Luxury Heritage", "location": "Nanyuki Slopes", "description": "Historic estate founded by actor William Holden, straddling the equator with mountain views."},
            {"name": "Segera Retreat", "tier": "Eco-Luxury Oasis", "location": "Laikipia Plateau", "description": "Exquisite private villa retreat surrounded by botanical gardens and contemporary African art."}
        ],
        "packageIds": [],
        "relatedSlugs": ["nanyuki", "samburu", "aberdare-national-park", "kilimanjaro"],
        "faqs": [
            {
                "q": "Do I need technical mountaineering skills to climb Mount Kenya?",
                "a": "No, Point Lenana (4,985m) is a trekking peak achievable by fit hikers with proper acclimatization. The higher technical summits of Batian (5,199m) and Nelion (5,188m) require technical rock climbing."
            }
        ]
    },
    {
        "id": "samburu",
        "slug": "samburu",
        "name": "Samburu National Reserve",
        "country": "Kenya",
        "region": "Kenya",
        "regions": ["Kenya", "East Africa", "Africa"],
        "categories": ["Wildlife Safaris", "Cultural Experiences", "Adventure Travel"],
        "tagline": "Home of the 'Samburu Special Five' & the Ewaso Ng'iro River",
        "shortDescription": "Discover rare northern wildlife species, doum palm-fringed riverbanks, and authentic Samburu warrior cultural traditions.",
        "overview": (
            "Located in Kenya's rugged northern frontier district, Samburu National Reserve is a stark, sun-baked landscape "
            "of breathtaking beauty. Framed by Mount Ololokwe and nourished by the life-giving waters of the brown Ewaso Ng'iro River, "
            "Samburu is famous for its distinct arid-adapted wildlife species known as the 'Samburu Special Five': "
            "the Grevy's zebra, reticulated giraffe, Beisa oryx, Somali ostrich, and the long-necked gerenuk.\n\n"
            "The reserve boasts healthy populations of predators, including leopards, lions, and African wild dogs. "
            "Culturally, the Samburu people—close relatives of the Maasai—retain deeply authentic nomadic traditions, "
            "welcoming respectful visitors to learn about their pastoral heritage, traditional beadwork, and sacred mountain lore."
        ),
        "heroImage": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=1000&q=80", "caption": "Reticulated giraffe roaming Samburu acacia woodlands"},
            {"url": "https://images.unsplash.com/photo-1534177616072-ef7dc120449d?auto=format&fit=crop&w=1000&q=80", "caption": "Leopard relaxing in doum palm tree near Ewaso Ng'iro river"}
        ],
        "coordinates": [0.6167, 37.5333],
        "highlights": [
            "The Samburu Special Five: Grevy's zebra, reticulated giraffe, gerenuk, Beisa oryx, Somali ostrich",
            "High concentration of leopards frequently sighted along riverbanks",
            "Stunning volcanic backdrop of Mount Ololokwe sacred flat-top mountain",
            "Rich authentic Samburu warrior culture and traditional community visits",
            "Picturesque doum palm trees lining the Ewaso Ng'iro river"
        ],
        "activities": [
            "Morning & evening game drives along the riverbanks",
            "Guided bushwalks with Samburu morans (warriors)",
            "Birdwatching for over 450 arid-zone species",
            "Sundowners atop granite inselbergs with panoramic views",
            "Star-gazing in unpolluted African night skies"
        ],
        "bestTimeToVisit": "June to October and December to March offer optimal dry season wildlife viewing along the river.",
        "quickFacts": {
            "bestTime": "Jun – Oct & Dec – Mar",
            "idealDuration": "3 – 4 Days",
            "language": "English, Swahili, Samburu",
            "currency": "Kenyan Shilling (KES) & USD",
            "visa": "Kenya eTA required online",
            "climate": "Warm arid climate (30-34°C daytime, 18-20°C night)"
        },
        "accommodations": [
            {"name": "Saruni Samburu", "tier": "Ultra-Luxury Eco", "location": "Kalama Conservancy", "description": "Villas built into a giant volcanic rock face with jaw-dropping panoramic views."},
            {"name": "Elephant Bedroom Camp", "tier": "Luxury Tented", "location": "Riverbanks Inside Park", "description": "Intimate luxury tents on raised decks where wild elephants regularly stroll through camp."}
        ],
        "packageIds": [],
        "relatedSlugs": ["nanyuki", "mount-kenya", "maasai-mara", "tsavo-national-parks"],
        "faqs": [
            {
                "q": "What makes Samburu different from the Maasai Mara?",
                "a": "Samburu features dramatic semi-arid landscapes, unique northern animal species (the Special Five) found nowhere else in southern Kenya, and far fewer visitor vehicles."
            }
        ]
    },
    {
        "id": "nanyuki",
        "slug": "nanyuki",
        "name": "Nanyuki & Ol Pejeta Conservancy",
        "country": "Kenya",
        "region": "Kenya",
        "regions": ["Kenya", "East Africa", "Africa"],
        "categories": ["Wildlife Safaris", "Luxury Getaways", "Family Holidays"],
        "tagline": "Equator Gateway & Sanctuary of the Last Northern White Rhinos",
        "shortDescription": "Stand on the equator, visit the world's last two Northern White Rhinos, and see chimpanzees at Sweetwaters Sanctuary in Ol Pejeta.",
        "overview": (
            "Nanyuki is a vibrant safari hub nestled directly on the Equator on the northwestern foot slopes of Mount Kenya. "
            "Renowned as the gateway to the world-celebrated Ol Pejeta Conservancy, Nanyuki combines frontier ranching charm "
            "with pioneering global wildlife conservation.\n\n"
            "Ol Pejeta spans 90,000 acres and is the largest black rhino sanctuary in East Africa. Most famously, it is home "
            "to Najin and Fatu—the world's last two remaining Northern White Rhinos—guarded 24/7 by armed rangers. "
            "Ol Pejeta also hosts the Jane Goodall Sweetwaters Chimpanzee Sanctuary and high densities of lions, leopards, "
            "cheetahs, and elephants with Mount Kenya's snowy peaks as an ever-present backdrop."
        ),
        "heroImage": "https://images.unsplash.com/photo-1589556264800-08ae9e129a8c?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1589556264800-08ae9e129a8c?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1589556264800-08ae9e129a8c?auto=format&fit=crop&w=1000&q=80", "caption": "Northern White Rhino under conservation care at Ol Pejeta"},
            {"url": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=1000&q=80", "caption": "Equator crossing demonstration in Nanyuki"}
        ],
        "coordinates": [0.0167, 37.0722],
        "highlights": [
            "Meeting Najin and Fatu—the world's last two Northern White Rhinos",
            "Sweetwaters Chimpanzee Sanctuary established with Dr. Jane Goodall",
            "Largest Black Rhino sanctuary in East and Central Africa",
            "Official Equator crossing landmark and Coriolis effect demonstrations",
            "Lion tracking with conservation researchers using radio telemetry"
        ],
        "activities": [
            "Behind-the-scenes rhino sanctuary visit & keeper talks",
            "Chimpanzee sanctuary educational tours",
            "Night game drives to spot aardvarks, zorillas, and hunting lions",
            "Coriolis effect demonstrations at the official Equator marker",
            "Horse riding with non-predator wildlife"
        ],
        "bestTimeToVisit": "Year-round due to the moderate highland climate. June to October and December to March offer dry game tracks.",
        "quickFacts": {
            "bestTime": "All Year Round (Peak: Jun – Mar)",
            "idealDuration": "2 – 4 Days",
            "language": "English, Swahili",
            "currency": "Kenyan Shilling (KES) & USD",
            "visa": "Kenya eTA required online",
            "climate": "Highland plateau climate (22-26°C daytime, 10-12°C nights)"
        },
        "accommodations": [
            {"name": "Sweetwaters Serena Camp", "tier": "Luxury Tented", "location": "Ol Pejeta Conservancy", "description": "Comfortable tents overlooking a floodlit waterhole visited day and night by rhinos and elephants."},
            {"name": "Ol Pejeta Bush Camp", "tier": "Eco-Safari Camp", "location": "Ewaso Nyiro Riverbank", "description": "Authentic canvas safari camp focusing on deep conservation experiences."}
        ],
        "packageIds": [],
        "relatedSlugs": ["mount-kenya", "samburu", "aberdare-national-park", "lake-nakuru"],
        "faqs": [
            {
                "q": "Can I visit the last two Northern White Rhinos?",
                "a": "Yes! Guided visits to their predator-proof enclosure can be arranged through Horizon Legacy Safaris, accompanied by their personal armed caretakers."
            }
        ]
    },
    {
        "id": "lamu",
        "slug": "lamu",
        "name": "Lamu Island Archipelago",
        "country": "Kenya",
        "region": "Kenya",
        "regions": ["Kenya", "East Africa", "Africa"],
        "categories": ["Cultural Experiences", "Beach Escapes", "Honeymoon Destinations", "Luxury Getaways"],
        "tagline": "Untouched Swahili Heritage, Donkeys & Dhow Sailing",
        "shortDescription": "Step into a car-free UNESCO Swahili sanctuary with carved coral doors, serene Shela beaches, and tranquil Indian Ocean dhow cruises.",
        "overview": (
            "Lamu Island is a tranquil tropical enclave off the northern coast of Kenya and the oldest continuously inhabited "
            "Swahili settlement in East Africa. A UNESCO World Heritage Site, Lamu Old Town has changed little over the centuries, "
            "with narrow winding streets built for donkeys and pedestrians rather than automobiles.\n\n"
            "Built with coral rag stone and mangrove timber, Lamu's historic mansions feature inner courtyards, carved wooden "
            "doors, and intricately stuccoed walls. A short boat ride or stroll down the beach leads to the sophisticated village "
            "of Shela, where miles of pristine, uncrowded sand dunes meet the turquoise sea, creating an unmatched retreat for artists, "
            "romantic getaways, and luxury relaxation."
        ),
        "heroImage": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1000&q=80", "caption": "Traditional wooden dhow sailing past Shela beach dunes"},
            {"url": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=1000&q=80", "caption": "Hand-carved Swahili coral door in Lamu Old Town"}
        ],
        "coordinates": [-2.2696, 40.9006],
        "highlights": [
            "UNESCO World Heritage Lamu Old Town with preserved 14th-century architecture",
            "Completely car-free island where donkeys and traditional dhows are the only transport",
            "Miles of golden sand dunes along tranquil Shela beach",
            "Sunset sailing aboard handcrafted wooden Mozambique dhows",
            "Lamu Fort, Swahili museums, and traditional silversmith workshops"
        ],
        "activities": [
            "Sunset dhow sailing and private island beach picnics",
            "Exploring Lamu Old Town with architectural historians",
            "Yoga retreats and holistic wellness on Shela beach",
            "Deep-sea fishing and mangrove channel snorkeling",
            "Tasting fresh mangrove crab and Swahili coconut fish curries"
        ],
        "bestTimeToVisit": "November to April brings calm waters, warm sunshine, and gentle ocean breezes.",
        "quickFacts": {
            "bestTime": "Nov – Apr",
            "idealDuration": "3 – 6 Days",
            "language": "English, Swahili, Bajuni",
            "currency": "Kenyan Shilling (KES) & USD",
            "visa": "Kenya eTA required online",
            "climate": "Warm tropical coastal (28-32°C)"
        },
        "accommodations": [
            {"name": "The Majlis Resort", "tier": "5-Star Boutique Luxury", "location": "Manda Island Across Shela", "description": "Exquisite luxury resort blending traditional Swahili culture and modern Italian design."},
            {"name": "Peponi Hotel", "tier": "Historic Chic", "location": "Shela Beach Waterfront", "description": "Legendary family-run boutique hotel famous for its waterfront bar and personalized dhow safaris."}
        ],
        "packageIds": [],
        "relatedSlugs": ["watamu", "diani-beach", "zanzibar", "mombasa"],
        "faqs": [
            {
                "q": "Are there any cars on Lamu Island?",
                "a": "No! There are no cars on Lamu Island (aside from an ambulance and police vehicle). Everyone walks, rides donkeys, or travels between villages and islands by boat."
            }
        ]
    },
    {
        "id": "hells-gate",
        "slug": "hells-gate",
        "name": "Hell's Gate National Park",
        "country": "Kenya",
        "region": "Kenya",
        "regions": ["Kenya", "East Africa", "Africa"],
        "categories": ["Adventure Travel", "Mountain Adventures", "Family Holidays"],
        "tagline": "Cycle Among Wildlife, Towering Cliffs & Geothermal Springs",
        "shortDescription": "Ride bicycles past grazing zebras, hike deep sandstone gorges, and soak in Africa's largest natural geothermal spa pool.",
        "overview": (
            "Named for a narrow break in the sheer red cliffs once carved by a prehistoric tributary of Lake Naivasha, "
            "Hell's Gate National Park is one of Kenya's most exhilarating adventure destinations. It is one of the only national parks "
            "in Africa where visitors are encouraged to explore on foot or by bicycle alongside herds of zebras, buffalos, "
            "gazelles, and giraffes.\n\n"
            "Towering volcanic plug formations like Fischer's Tower and Central Tower provide world-class rock climbing. "
            "Deep inside the park, the Ol Njorowa Gorge winds through dramatic water-sculpted sandstone canyon walls with natural hot springs. "
            "Nearby, the Olkaria Geothermal Spa offers a relaxing swim in massive, naturally heated mineral pools."
        ),
        "heroImage": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=1000&q=80", "caption": "Dramatic sandstone cliffs of Hell's Gate canyon"},
            {"url": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=1000&q=80", "caption": "Cycling along the main park trail with grazing wildlife"}
        ],
        "coordinates": [-0.9167, 36.3167],
        "highlights": [
            "Bicycle safaris riding directly among zebras, giraffes, and warthogs",
            "Hiking through the dramatic water-sculpted Ol Njorowa Gorge",
            "Rock climbing Fischer's Tower volcanic plug with certified guides",
            "Swimming in Africa's largest natural geothermal heated spa at Olkaria",
            "Inspirational setting that helped animate Disney's The Lion King"
        ],
        "activities": [
            "Mountain biking through the savannah valleys",
            "Guided gorge hiking and hot spring wading",
            "Rock climbing on Fischer's Tower",
            "Thermal spa swimming at Olkaria Geothermal complex",
            "Scenic picnic lunches overlooking volcanic cliffs"
        ],
        "bestTimeToVisit": "Year-round. Dry seasons (June to October and December to March) are ideal for gorge hiking.",
        "quickFacts": {
            "bestTime": "All Year Round (Dry: Jun – Oct)",
            "idealDuration": "1 – 2 Days",
            "language": "English, Swahili",
            "currency": "Kenyan Shilling (KES) & USD",
            "visa": "Kenya eTA required online",
            "climate": "Temperate Rift Valley climate (22-27°C)"
        },
        "accommodations": [
            {"name": "Enashipai Resort & Spa", "tier": "5-Star Luxury Resort", "location": "Lake Naivasha", "description": "Top-rated resort providing convenient proximity to Hell's Gate adventures."},
            {"name": "Kiboko Luxury Camp", "tier": "Luxury Tented", "location": "Lake Naivasha Shore", "description": "Tented suites right on the hippo-dotted lakefront."}
        ],
        "packageIds": [],
        "relatedSlugs": ["lake-naivasha", "lake-nakuru", "aberdare-national-park"],
        "faqs": [
            {
                "q": "Is it safe to cycle in Hell's Gate without a vehicle?",
                "a": "Yes! The park has no large predators like lions, making cycling and hiking among plains game safe and thrilling."
            }
        ]
    },
    {
        "id": "aberdare-national-park",
        "slug": "aberdare-national-park",
        "name": "Aberdare National Park",
        "country": "Kenya",
        "region": "Kenya",
        "regions": ["Kenya", "East Africa", "Africa"],
        "categories": ["Wildlife Safaris", "Mountain Adventures", "Luxury Getaways"],
        "tagline": "Misty Moorlands, Cascading Waterfalls & Rare Bongos",
        "shortDescription": "Explore misty cloud forests, plunge waterfalls, and night wildlife viewing from famous forest lodges in the Aberdare Mountains.",
        "overview": (
            "Aberdare National Park covers the higher reaches of the Aberdare Mountain Range in central Kenya. "
            "Characterized by misty afro-alpine moorlands, deep v-shaped valleys, and dense bamboo forests, "
            "it is a dramatically different safari experience from Kenya's open savannahs.\n\n"
            "The park is famed for majestic waterfalls such as Karuru Falls (which plunges 273 meters in three tiers), "
            "Gura Falls, and Chania Falls. Aberdare shelters rare and elusive wildlife including the endangered bongo antelope, "
            "black rhinos, giant forest hogs, and black panthers. Historically, it is where Princess Elizabeth stayed at Treetops Lodge "
            "in 1952 and ascended to the British throne upon her father's death."
        ),
        "heroImage": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1000&q=80", "caption": "Karuru Falls cascading through indigenous forest"},
            {"url": "https://images.unsplash.com/photo-1534177616072-ef7dc120449d?auto=format&fit=crop&w=1000&q=80", "caption": "Elephants at floodlit waterhole viewed from The Ark Lodge"}
        ],
        "coordinates": [-0.4667, 36.7000],
        "highlights": [
            "Karuru Falls plunging 273 meters in three spectacular cascades",
            "All-night floodlit wildlife viewing at The Ark waterhole",
            "Sanctuary for the critically endangered Mountain Bongo antelope",
            "Historic royal heritage where Princess Elizabeth became Queen",
            "Trout fly-fishing in sparkling mountain streams"
        ],
        "activities": [
            "Night game viewing from glass bunker hides at The Ark",
            "Waterfall nature walks and scenic lookout drives",
            "Fly-fishing for trout in moorland streams",
            "Birdwatching for mountain endemics like the Aberdare cisticola",
            "Forest walking safaris with Kenya Wildlife Service rangers"
        ],
        "bestTimeToVisit": "January to March and June to September offer the driest tracks for vehicle exploration.",
        "quickFacts": {
            "bestTime": "Jan – Mar & Jun – Sep",
            "idealDuration": "2 – 3 Days",
            "language": "English, Swahili, Kikuyu",
            "currency": "Kenyan Shilling (KES) & USD",
            "visa": "Kenya eTA required online",
            "climate": "Cool montane forest climate (15-20°C daytime, 6-10°C nights)"
        },
        "accommodations": [
            {"name": "The Ark Lodge", "tier": "Iconic Forest Lodge", "location": "Heart of Aberdares", "description": "Shaped like Noah's Ark with four viewing decks overlooking a floodlit waterhole and salt lick."},
            {"name": "Aberdare Country Club", "tier": "Colonial Heritage Resort", "location": "Mweiga Slopes", "description": "Set in a 1,300-acre wildlife sanctuary with golf course, tennis courts, and peacock gardens."}
        ],
        "packageIds": [],
        "relatedSlugs": ["mount-kenya", "lake-nakuru", "nanyuki", "lake-naivasha"],
        "faqs": [
            {
                "q": "What should I pack for the Aberdare Mountains?",
                "a": "Pack warm layers, fleece jackets, and rain gear, as mountain evenings and early mornings can become very chilly (dropping down to 6°C)."
            }
        ]
    },

    # =========================================================================
    # EAST AFRICA (8 Destinations)
    # =========================================================================
    {
        "id": "zanzibar",
        "slug": "zanzibar",
        "name": "Zanzibar Archipelago, Tanzania",
        "country": "Tanzania",
        "region": "East Africa",
        "regions": ["East Africa", "Africa"],
        "categories": ["Beach Escapes", "Honeymoon Destinations", "Cultural Experiences", "Luxury Getaways"],
        "tagline": "The Spice Island of Stone Town & Turquoise Atolls",
        "shortDescription": "Wander labyrinthine UNESCO Stone Town alleys, taste exotic spices, and unwind at luxury beach resorts along azure Indian Ocean shallows.",
        "overview": (
            "Zanzibar, also known as Unguja, is an idyllic semi-autonomous archipelago situated 35 km off the coast of mainland Tanzania. "
            "For centuries a pivotal trading hub between Arabia, India, and Africa, Zanzibar is rich in sensory wonders—from fragrant cloves "
            "and nutmeg to intricately carved teakwood doorways.\n\n"
            "Stone Town, Zanzibar's cultural heart, is a UNESCO World Heritage Site with winding cobbled streets, the House of Wonders, "
            "and bustling Forodhani night food market. Along the island's coastline, powdery white beaches like Nungwi and Kendwa "
            "offer tide-free swimming in glowing turquoise lagoons, while Mnemba Atoll is East Africa's premier marine sanctuary."
        ),
        "heroImage": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=1000&q=80", "caption": "Nungwi beach crystal turquoise waters"},
            {"url": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=1000&q=80", "caption": "Historic carved door in UNESCO Stone Town"}
        ],
        "coordinates": [-6.1659, 39.2026],
        "highlights": [
            "UNESCO World Heritage Stone Town walking & spice market tours",
            "Mnemba Atoll world-class coral reef snorkeling and scuba diving",
            "Jozani Chwaka Bay National Park home to endemic Red Colobus monkeys",
            "Sunset dhow sailing cruises with live Taarab music",
            "Famous The Rock Restaurant dining perched on an ocean coral rock"
        ],
        "activities": [
            "Spice farm sensory tasting tours",
            "Snorkeling with wild dolphins at Kizimkazi",
            "Dining at The Rock restaurant at high tide",
            "Forodhani Gardens seaside night street food tasting",
            "Luxury spa treatments with Zanzibar cloves and coconut oils"
        ],
        "bestTimeToVisit": "June to October and December to February offer dry, sunny days and gentle sea breezes.",
        "quickFacts": {
            "bestTime": "Jun – Oct & Dec – Feb",
            "idealDuration": "4 – 7 Days",
            "language": "Swahili, English, Arabic",
            "currency": "Tanzanian Shilling (TZS) & USD",
            "visa": "Tanzania eVisa required",
            "climate": "Warm tropical maritime (27-32°C year-round)"
        },
        "accommodations": [
            {"name": "The Residence Zanzibar", "tier": "5-Star Luxury Resort", "location": "Kizimkazi Coast", "description": "Luxurious private pool villas nestled amidst 32 hectares of tropical gardens."},
            {"name": "Baraza Resort & Spa", "tier": "All-Inclusive Luxury", "location": "Bwejuu-Paje Beach", "description": "Voted among the world's best beach resorts, blending Arabic, Swahili, and Indian palace decor."},
            {"name": "Park Hyatt Zanzibar", "tier": "Luxury Heritage", "location": "Stone Town Waterfront", "description": "Historic beachfront haven in the heart of UNESCO Stone Town."}
        ],
        "packageIds": [],
        "relatedSlugs": ["diani-beach", "serengeti", "watamu", "lamu"],
        "faqs": [
            {
                "q": "Can I combine a safari in Kenya or Tanzania with Zanzibar?",
                "a": "Yes! The classic 'Bush and Beach' safari combines game viewing in the Maasai Mara or Serengeti with direct flights to Zanzibar for beach relaxation."
            }
        ]
    },
    {
        "id": "serengeti",
        "slug": "serengeti",
        "name": "Serengeti National Park, Tanzania",
        "country": "Tanzania",
        "region": "East Africa",
        "regions": ["East Africa", "Africa"],
        "categories": ["Wildlife Safaris", "Luxury Getaways", "Adventure Travel"],
        "tagline": "Endless Plains & the Legendary Great Migration",
        "shortDescription": "Experience the world's most dramatic wildlife theater across endless plains holding over two million migrating wildebeest and predators.",
        "overview": (
            "Derived from the Maasai word 'Siringet' meaning 'endless plains', Serengeti National Park is a UNESCO World Heritage Site "
            "spanning nearly 15,000 square kilometers of golden grassland in northern Tanzania. It forms the southern portion "
            "of the greater Serengeti-Mara ecosystem.\n\n"
            "The Serengeti hosts the Great Migration year-round, following an ancient cyclical rhythm from the southern calving grounds "
            "in Ndutu through the central Seronera predator territory and across the crocodile-filled Grumeti and Mara rivers. "
            "With over 3,000 resident lions, the Serengeti boasts the largest lion population in Africa."
        ),
        "heroImage": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=1000&q=80", "caption": "Endless grasslands of Serengeti with wildebeest herds"},
            {"url": "https://images.unsplash.com/photo-1534177616072-ef7dc120449d?auto=format&fit=crop&w=1000&q=80", "caption": "Lion pride resting on Serengeti granite kopjes"}
        ],
        "coordinates": [-2.3333, 34.8333],
        "highlights": [
            "Year-round presence of the Great Wildebeest Migration",
            "Highest concentration of big cats in Africa (lions, leopards, cheetahs)",
            "Moru Kopjes rock islands sheltering endangered Black Rhinos",
            "Hot air balloon flights over the Seronera River valley at dawn",
            "Calving season in southern Serengeti with 8,000 wildebeest born daily"
        ],
        "activities": [
            "Full-day migration tracking game drives with picnic lunches",
            "Sunrise hot air balloon safari and bush champagne breakfast",
            "Photographic safaris focusing on big cat predator hunting behavior",
            "Stargazing under the crystal-clear equatorial night sky"
        ],
        "bestTimeToVisit": "Late June to October for northern river crossings; January to March for the southern calving season in Ndutu.",
        "quickFacts": {
            "bestTime": "Jun – Oct & Jan – Mar",
            "idealDuration": "3 – 5 Days",
            "language": "English, Swahili",
            "currency": "Tanzanian Shilling (TZS) & USD",
            "visa": "Tanzania eVisa required",
            "climate": "Warm savannah climate (25-28°C daytime, 13-15°C night)"
        },
        "accommodations": [
            {"name": "Four Seasons Safari Lodge Serengeti", "tier": "Ultra-Luxury Lodge", "location": "Central Seronera", "description": "Features an elevated infinity pool looking directly onto an active elephant waterhole."},
            {"name": "Singita Sasakwa Lodge", "tier": "Edwardian Luxury", "location": "Grumeti Reserves", "description": "Magnificent manor home with private plunge pools overlooking 350,000 acres of private wilderness."}
        ],
        "packageIds": [],
        "relatedSlugs": ["maasai-mara", "ngorongoro", "zanzibar", "kilimanjaro"],
        "faqs": [
            {
                "q": "How does the Serengeti connect with the Maasai Mara?",
                "a": "They are the same contiguous ecosystem separated by the Kenya-Tanzania border. Animals move freely between them following pasture and rain."
            }
        ]
    },
    {
        "id": "ngorongoro",
        "slug": "ngorongoro",
        "name": "Ngorongoro Crater, Tanzania",
        "country": "Tanzania",
        "region": "East Africa",
        "regions": ["East Africa", "Africa"],
        "categories": ["Wildlife Safaris", "Luxury Getaways", "Mountain Adventures"],
        "tagline": "The World's Largest Intact Volcanic Caldera & Eden of Wildlife",
        "shortDescription": "Descend 600 meters into a volcanic caldera teeming with 25,000 large mammals, black rhinos, and vibrant pink flamingo lakes.",
        "overview": (
            "The Ngorongoro Crater is a geological and biological marvel often referred to as the 'Eighth Wonder of the World'. "
            "Formed three million years ago when a massive volcano collapsed upon itself, the crater is the world's largest intact, "
            "unfilled caldera, measuring 20 kilometers across and 600 meters deep.\n\n"
            "Inside this self-contained natural amphitheater thrives an astonishing density of over 25,000 large mammals. "
            "It is one of the few places in East Africa where visitors can easily witness the Big Five in a single morning, "
            "including critically endangered black rhinos, giant tuskers, and dense prides of dark-maned lions."
        ),
        "heroImage": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=1000&q=80", "caption": "Panoramic view from the rim looking into Ngorongoro Crater"},
            {"url": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=1000&q=80", "caption": "Black rhino grazing on the crater floor"}
        ],
        "coordinates": [-3.1667, 35.5833],
        "highlights": [
            "World's largest intact volcanic caldera (260 sq km floor)",
            "Exceptionally high wildlife density of over 25,000 large animals",
            "Highest probability of seeing the endangered Black Rhino in Tanzania",
            "Lake Magadi alkaline lake with thousands of lesser flamingos",
            "Lerai Forest haven for giant bull elephants and leopards"
        ],
        "activities": [
            "Crater floor safari game drives",
            "Crater rim walking safaris guided by armed rangers",
            "Picnic lunches beside the hippo pool at Ngoitokitok Spring",
            "Visiting Olduvai Gorge 'Cradle of Humankind' archaeological site",
            "Meeting Maasai pastoralists in the conservation area"
        ],
        "bestTimeToVisit": "Exceptional year-round due to non-migratory permanent resident wildlife.",
        "quickFacts": {
            "bestTime": "All Year Round (Peak: Jun – Oct)",
            "idealDuration": "2 – 3 Days",
            "language": "English, Swahili",
            "currency": "Tanzanian Shilling (TZS) & USD",
            "visa": "Tanzania eVisa required",
            "climate": "Cool crater rim (10-18°C), warm crater floor (24-28°C)"
        },
        "accommodations": [
            {"name": "Ngorongoro Crater Lodge (andBeyond)", "tier": "Ultra-Luxury", "location": "Crater Rim", "description": "Versailles-meets-Maasai architecture with stilted suites offering dramatic crater floor panoramas."},
            {"name": "Ngorongoro Serena Safari Lodge", "tier": "Luxury Eco-Lodge", "location": "Western Rim", "description": "Built from local river stone and camouflaged seamlessly into the volcanic rim."}
        ],
        "packageIds": [],
        "relatedSlugs": ["serengeti", "kilimanjaro", "amboseli", "maasai-mara"],
        "faqs": [
            {
                "q": "Can animals leave the Ngorongoro Crater?",
                "a": "Yes, animals can physically ascend and descend the 600m walls, but most species remain inside because food and fresh water are abundant year-round."
            }
        ]
    },
    {
        "id": "kilimanjaro",
        "slug": "kilimanjaro",
        "name": "Mount Kilimanjaro, Tanzania",
        "country": "Tanzania",
        "region": "East Africa",
        "regions": ["East Africa", "Africa"],
        "categories": ["Mountain Adventures", "Adventure Travel"],
        "tagline": "The Roof of Africa & Highest Free-Standing Mountain on Earth",
        "shortDescription": "Summit Africa's iconic 5,895-meter glaciated stratovolcano across five distinct climate zones on a once-in-a-lifetime expedition.",
        "overview": (
            "Mount Kilimanjaro is the highest peak in Africa and the tallest free-standing mountain on Earth, rising majestically "
            "to 5,895 meters (19,341 feet) above the golden plains of northern Tanzania. An awe-inspiring dormant stratovolcano, "
            "Kilimanjaro is crowned with shimmering glaciers just three degrees south of the equator.\n\n"
            "Trekking Kilimanjaro is often described as walking from the Equator to the North Pole in just a few days. "
            "Trekkers journey through five distinct ecological climate zones: lush rainforest, heather moorland, alpine desert, "
            "and an arctic summit zone of glaciers and ice walls. Standing on Uhuru Peak at sunrise as the curvature of the Earth "
            "is revealed is one of life's supreme travel milestones."
        ),
        "heroImage": "https://images.unsplash.com/photo-1589556264800-08ae9e129a8c?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1589556264800-08ae9e129a8c?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1589556264800-08ae9e129a8c?auto=format&fit=crop&w=1000&q=80", "caption": "Snow-capped summit of Kilimanjaro above the clouds"},
            {"url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1000&q=80", "caption": "Trekkers ascending the alpine desert zone towards Kibo crater"}
        ],
        "coordinates": [-3.0674, 37.3556],
        "highlights": [
            "Uhuru Peak at 5,895m — the Highest Point in Africa",
            "Journey through five distinct climate zones from rainforest to arctic glaciers",
            "Non-technical trek accessible to determined hikers with proper conditioning",
            "Spectacular sunrise over the African continent from the crater rim",
            "Chagga cultural coffee tours on the fertile lower mountain foothills"
        ],
        "activities": [
            "Multi-day summit trekking via Machame, Lemosho, or Marangu routes",
            "Day hikes to Mandara Hut through lush montane rainforest",
            "Materuni Waterfalls hike and organic Chagga coffee-making experience",
            "Helicopter scenic flights around Kibo and Mawenzi volcanic cones"
        ],
        "bestTimeToVisit": "January to mid-March and June to October offer dry conditions, clear skies, and safe summit passes.",
        "quickFacts": {
            "bestTime": "Jan – Mar & Jun – Oct",
            "idealDuration": "6 – 8 Days",
            "language": "English, Swahili",
            "currency": "Tanzanian Shilling (TZS) & USD",
            "visa": "Tanzania eVisa required",
            "climate": "Rainforest (20°C) to Summit Arctic (-10°C to -15°C)"
        },
        "accommodations": [
            {"name": "Kilimanjaro Mountain Resort", "tier": "Pre/Post-Trek Hotel", "location": "Marangu Foothills", "description": "Comfortable garden lodge designed for climber preparation and post-summit recovery."},
            {"name": "Kaliwa Lodge", "tier": "Eco-Boutique Lodge", "location": "Machame Foothills", "description": "Minimalist eco-lodge nestled in lush forest overlooking the Kibo summit."}
        ],
        "packageIds": [],
        "relatedSlugs": ["amboseli", "serengeti", "mount-kenya", "ngorongoro"],
        "faqs": [
            {
                "q": "Which is the best route to climb Kilimanjaro?",
                "a": "The 7 or 8-day Lemosho and Machame routes are widely considered the best because they offer scenic beauty and excellent 'climb high, sleep low' acclimatization profiles with summit success rates over 90%."
            }
        ]
    },
    {
        "id": "uganda",
        "slug": "uganda",
        "name": "Uganda - Pearl of Africa",
        "country": "Uganda",
        "region": "East Africa",
        "regions": ["East Africa", "Africa"],
        "categories": ["Wildlife Safaris", "Adventure Travel", "Cultural Experiences"],
        "tagline": "Source of the Nile, Murchison Falls & Chimpanzee Havens",
        "shortDescription": "Discover the roar of Murchison Falls, track habituated chimpanzees in Kibale Forest, and raft the source of the River Nile.",
        "overview": (
            "Dubbed the 'Pearl of Africa' by Winston Churchill in 1908, Uganda is an astonishingly fertile, green, "
            "and biodiversity-rich jewel in East Africa. Dominated by Lake Victoria, snow-capped Rwenzori 'Mountains of the Moon', "
            "and the birthplace of the mighty River Nile at Jinja, Uganda offers unmatched safari diversity.\n\n"
            "At Murchison Falls National Park, the entire Nile River explodes through a tiny seven-meter cleft in the Rift Valley "
            "escarpment with unimaginable force before flowing calmly into Lake Albert. In Kibale Forest National Park, travelers track "
            "some of the world's highest concentrations of primates, including over 1,500 habituated wild chimpanzees."
        ),
        "heroImage": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1000&q=80", "caption": "The Nile River roaring through Murchison Falls gorge"},
            {"url": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=1000&q=80", "caption": "Wild chimpanzee resting in Kibale Forest canopy"}
        ],
        "coordinates": [1.3733, 32.2903],
        "highlights": [
            "Murchison Falls — the world's most powerful surge of water",
            "Chimpanzee habituation & tracking in Kibale Forest National Park",
            "Source of the Nile River at Jinja and world-class white water rafting",
            "Tree-climbing lions of Ishasha in Queen Elizabeth National Park",
            "Kazinga Channel boat cruise with thousands of hippos and buffalos"
        ],
        "activities": [
            "Boat cruise to the thunderous base of Murchison Falls",
            "Chimpanzee tracking with Uganda Wildlife Authority naturalists",
            "Grade 5 white-water rafting on the Nile River in Jinja",
            "Game drives in Queen Elizabeth National Park",
            "Birdwatching for the rare prehistoric Shoebill Stork in Mabamba Swamp"
        ],
        "bestTimeToVisit": "June to August and December to February are the driest periods, ideal for primate tracking and game drives.",
        "quickFacts": {
            "bestTime": "Jun – Aug & Dec – Feb",
            "idealDuration": "5 – 8 Days",
            "language": "English, Luganda, Swahili",
            "currency": "Ugandan Shilling (UGX) & USD",
            "visa": "East Africa Tourist Visa / Uganda eVisa",
            "climate": "Lush tropical climate (24-29°C year-round)"
        },
        "accommodations": [
            {"name": "Chobe Safari Lodge", "tier": "5-Star River Lodge", "location": "Murchison Falls", "description": "Perched directly above the swirling rapids of the River Nile."},
            {"name": "Ndali Lodge", "tier": "Eco-Luxury Lodge", "location": "Kibale Crater Lakes", "description": "Overlooking an extinct volcanic crater lake within reach of chimpanzee trekking."}
        ],
        "packageIds": [],
        "relatedSlugs": ["bwindi-impenetrable-forest", "rwanda", "volcanoes-national-park", "maasai-mara"],
        "faqs": [
            {
                "q": "Can I combine chimpanzee tracking with gorilla trekking in Uganda?",
                "a": "Yes! A classic Uganda itinerary combines chimpanzee tracking in Kibale Forest with mountain gorilla trekking in nearby Bwindi Impenetrable Forest."
            }
        ]
    },
    {
        "id": "bwindi-impenetrable-forest",
        "slug": "bwindi-impenetrable-forest",
        "name": "Bwindi Impenetrable Forest, Uganda",
        "country": "Uganda",
        "region": "East Africa",
        "regions": ["East Africa", "Africa"],
        "categories": ["Wildlife Safaris", "Adventure Travel", "Luxury Getaways"],
        "tagline": "Sanctuary of the Endangered Mountain Gorillas",
        "shortDescription": "Trek deep into a 25,000-year-old primeval rainforest for life-changing face-to-face encounters with gentle wild Mountain Gorillas.",
        "overview": (
            "Bwindi Impenetrable National Park is a biological masterpiece and UNESCO World Heritage Site in southwestern Uganda. "
            "Covering 321 square kilometers of rugged, tangled ancient montane and lowland rainforest, Bwindi is one of Africa's "
            "oldest and most diverse ecosystems, surviving through the last Ice Age.\n\n"
            "Bwindi's greatest treasure is that it shelters nearly half of the world's surviving endangered Mountain Gorillas. "
            "Trekking through steep, misty valleys draped in moss and giant ferns to spend an unforgettable hour sitting quietly "
            "with a habituated gorilla family—watching massive silverbacks, playful infants, and tender mothers—is universally "
            "recognized as one of humanity's most profound wildlife encounters."
        ),
        "heroImage": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=1000&q=80", "caption": "Silverback mountain gorilla in Bwindi dense rainforest"},
            {"url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1000&q=80", "caption": "Misty rainforest canopy of Bwindi Impenetrable Forest"}
        ],
        "coordinates": [-1.0500, 29.6833],
        "highlights": [
            "Home to nearly half of the world's remaining endangered Mountain Gorillas",
            "Exclusive Gorilla Habituation Experience allowing 4 hours with wild gorillas",
            "Primeval 25,000-year-old rainforest with 350+ bird species and 200+ butterflies",
            "Munyaga Waterfall nature walks and river canyon trails",
            "Cultural interaction with indigenous Batwa pygmy forest communities"
        ],
        "activities": [
            "Mountain Gorilla trekking with Uganda Wildlife Authority rangers",
            "Gorilla Habituation Experience in Rushaga sector",
            "Guided rainforest birdwatching and botanical walks",
            "Batwa cultural heritage forest demonstrations",
            "Community tea plantation and local craft cooperative visits"
        ],
        "bestTimeToVisit": "June to August and December to February are the driest months, providing firmer trail footing for rainforest treks.",
        "quickFacts": {
            "bestTime": "Jun – Aug & Dec – Feb",
            "idealDuration": "3 – 4 Days",
            "language": "English, Rukiga, Luganda",
            "currency": "Ugandan Shilling (UGX) & USD",
            "visa": "East Africa Tourist Visa / Uganda eVisa",
            "climate": "Rainforest climate (cool mornings 12-14°C, mild days 20-24°C)"
        },
        "accommodations": [
            {"name": "Sanctuary Gorilla Forest Camp", "tier": "Eco-Luxury Tented", "location": "Inside Bwindi Park", "description": "Exclusive luxury camp inside park boundaries where gorilla families occasionally wander through."},
            {"name": "Clouds Mountain Gorilla Lodge", "tier": "Boutique Stone Lodge", "location": "Nkuringo Ridge", "description": "Uganda's highest lodge with stone cottages and views extending to the Virunga volcanoes."}
        ],
        "packageIds": [],
        "relatedSlugs": ["volcanoes-national-park", "uganda", "rwanda", "serengeti"],
        "faqs": [
            {
                "q": "How difficult is gorilla trekking in Bwindi?",
                "a": "Trekking can take between 2 to 7 hours over steep, muddy, and densely vegetated terrain. A moderate level of physical fitness and good walking boots are recommended."
            },
            {
                "q": "Do I need a permit in advance?",
                "a": "Yes! Gorilla permits are strictly limited by the wildlife authority to protect gorillas and must be booked several months in advance through Horizon Legacy Safaris."
            }
        ]
    },
    {
        "id": "rwanda",
        "slug": "rwanda",
        "name": "Rwanda - Land of a Thousand Hills",
        "country": "Rwanda",
        "region": "East Africa",
        "regions": ["East Africa", "Africa"],
        "categories": ["Luxury Getaways", "Cultural Experiences", "City Breaks"],
        "tagline": "Clean, Visionary, Modern & Scenic East African Jewel",
        "shortDescription": "Discover Africa's cleanest and safest capital in Kigali, boat across picturesque Lake Kivu, and explore Akagera's Big Five savannah.",
        "overview": (
            "Rwanda, famously known as the 'Land of a Thousand Hills', is one of Africa's most extraordinary success stories. "
            "Celebrated for its sparkling cleanliness, progressive governance, and peaceful atmosphere, Rwanda offers visitors "
            "an ultra-modern travel infrastructure framed by dramatic verdant hills.\n\n"
            "The capital city, Kigali, is vibrant and sophisticated, home to modern art galleries, world-class coffee cafes, "
            "and the deeply moving Kigali Genocide Memorial. In eastern Rwanda, Akagera National Park provides a classic Big Five "
            "savannah safari around Lake Ihema, while the western borders feature tranquil Lake Kivu and ancient Nyungwe cloud forest."
        ),
        "heroImage": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=1000&q=80", "caption": "Lush rolling green hills of the Rwandan countryside"},
            {"url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1000&q=80", "caption": "Modern architecture and clean boulevards of Kigali"}
        ],
        "coordinates": [-1.9403, 29.8739],
        "highlights": [
            "Kigali — widely ranked the cleanest, safest, and most modern city in Africa",
            "Kigali Genocide Memorial center of peace, education, and reflection",
            "Akagera National Park Big Five safari overlooking scenic lakes",
            "Nyungwe National Park 70-meter-high rainforest canopy suspension bridge",
            "Lakeside relaxation, kayaking, and boat tours on Lake Kivu"
        ],
        "activities": [
            "Kigali contemporary art and barista coffee tour",
            "Big Five morning and sunset game drives in Akagera",
            "Canopy walking safari suspended 70m above Nyungwe rainforest",
            "Sunset catamaran and speed boat cruising on Lake Kivu",
            "Traditional Inyambo sacred horned cattle cultural visits"
        ],
        "bestTimeToVisit": "June to September and December to February are optimal for dry exploration across Rwanda's hills and parks.",
        "quickFacts": {
            "bestTime": "Jun – Sep & Dec – Feb",
            "idealDuration": "4 – 7 Days",
            "language": "Kinyarwanda, English, French",
            "currency": "Rwandan Franc (RWF) & USD",
            "visa": "Visa on arrival / East Africa Tourist Visa",
            "climate": "Mild spring-like highland climate (22-26°C year-round)"
        },
        "accommodations": [
            {"name": "The Retreat by Heaven", "tier": "5-Star Eco-Luxury", "location": "Kigali City Center", "description": "Solar-powered luxury boutique hotel with gourmet organic restaurant and heated saltwater pool."},
            {"name": "Magashi Camp (Wilderness Safaris)", "tier": "Ultra-Luxury Tented", "location": "Akagera National Park", "description": "Set on Lake Rwanyakazinga with exclusive access to prime private wilderness."}
        ],
        "packageIds": [],
        "relatedSlugs": ["volcanoes-national-park", "uganda", "bwindi-impenetrable-forest", "maasai-mara"],
        "faqs": [
            {
                "q": "Is Rwanda safe for international solo travelers and families?",
                "a": "Rwanda is officially ranked among the safest countries in the world with virtually zero street crime and exceptionally welcoming local hospitality."
            }
        ]
    },
    {
        "id": "volcanoes-national-park",
        "slug": "volcanoes-national-park",
        "name": "Volcanoes National Park, Rwanda",
        "country": "Rwanda",
        "region": "East Africa",
        "regions": ["East Africa", "Africa"],
        "categories": ["Wildlife Safaris", "Mountain Adventures", "Luxury Getaways"],
        "tagline": "Gorillas in the Mist Beneath the Virunga Volcanoes",
        "shortDescription": "Follow in Dian Fossey's footsteps for luxury mountain gorilla and golden monkey trekking across dramatic volcanic slopes.",
        "overview": (
            "Volcanoes National Park (Parc National des Volcans) covers 160 square kilometers of dramatic montane ecosystem "
            "in northwestern Rwanda. It encompasses five of the eight magnificent volcanoes in the Virunga chain: Karisimbi, "
            "Bisoke, Muhabura, Gahinga, and Sabyinyo, cloaked in bamboo and rainforest.\n\n"
            "This was the legendary base of zoologist Dian Fossey, who devoted twenty years of her life to studying and protecting "
            "mountain gorillas. Today, Rwanda is the world's premier luxury gorilla trekking destination, where travelers stay "
            "at world-class eco-lodges and trek through misty bamboo slopes to encounter wild gorilla families and playful golden monkeys."
        ),
        "heroImage": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=1000&q=80", "caption": "Mountain gorilla family in Volcanoes National Park bamboo"},
            {"url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1000&q=80", "caption": "The dramatic peaks of the Virunga volcanic mountain chain"}
        ],
        "coordinates": [-1.4833, 29.5000],
        "highlights": [
            "Ultra-luxury mountain gorilla trekking with expert national park trackers",
            "Trekking playful endangered Golden Monkeys in the bamboo zone",
            "Dramatic vistas of five majestic Virunga volcanoes (Karisimbi up to 4,507m)",
            "Hiking to Dian Fossey's historic Karisoke Research Center and grave",
            "Ascending Mount Bisoke to witness its sparkling crater summit lake"
        ],
        "activities": [
            "Gorilla trekking encounters (1 hour with family)",
            "Golden monkey habituation tracking",
            "Hiking to Dian Fossey's tomb and mountain gorilla graveyard",
            "Climbing Mount Bisoke crater lake (3,711m)",
            "Cultural tours of Iby'Iwacu Cultural Village"
        ],
        "bestTimeToVisit": "June to September and December to February are optimal for dry mountain trails.",
        "quickFacts": {
            "bestTime": "Jun – Sep & Dec – Feb",
            "idealDuration": "2 – 4 Days",
            "language": "Kinyarwanda, English, French",
            "currency": "Rwandan Franc (RWF) & USD",
            "visa": "Rwanda eVisa / Visa on arrival",
            "climate": "Cool mountain bamboo climate (10-18°C, can drop to 6°C at night)"
        },
        "accommodations": [
            {"name": "Bisate Lodge (Wilderness Safaris)", "tier": "Ultra-Luxury Eco", "location": "Volcanoes Foothills", "description": "Acclaimed spherical thatched pods set inside an eroded volcanic cone with views of Mount Bisoke."},
            {"name": "Singita Kwitonda Lodge", "tier": "Ultra-Luxury", "location": "Park Border", "description": "Set right on the park boundary with private heated plunge pools and indoor fireplaces."},
            {"name": "One&Only Gorilla's Nest", "tier": "5-Star Resort", "location": "Eucalyptus Forest", "description": "Stilted suites nestled among fragrant eucalyptus trees with private spa bathtubs."}
        ],
        "packageIds": [],
        "relatedSlugs": ["bwindi-impenetrable-forest", "rwanda", "uganda", "serengeti"],
        "faqs": [
            {
                "q": "How far is Volcanoes National Park from Kigali?",
                "a": "It is an easy, scenic 2.5-hour drive on smooth paved tarmac roads from Kigali Airport to Musanze (the park base)."
            }
        ]
    },

    # =========================================================================
    # AFRICA (9 Destinations)
    # =========================================================================
    {
        "id": "botswana",
        "slug": "botswana",
        "name": "Botswana & Okavango Delta",
        "country": "Botswana",
        "region": "Africa",
        "regions": ["Africa"],
        "categories": ["Wildlife Safaris", "Luxury Getaways", "Adventure Travel"],
        "tagline": "The Okavango Water Oasis & Chobe Elephant Kingdom",
        "shortDescription": "Glide through tranquil delta lily-pads on a mokoro canoe and encounter immense elephant herds in Africa's premier low-impact safari wilderness.",
        "overview": (
            "Botswana is globally acknowledged as the gold standard of luxury, low-impact eco-safaris. "
            "At its heart lies the UNESCO-inscribed Okavango Delta, the world's largest inland delta, where seasonal floodwaters "
            "originating in the Angolan highlands spill into the Kalahari Desert, transforming dry sands into an extraordinary water labyrinth.\n\n"
            "Here, travelers explore palm-fringed islands by traditional wooden mokoro dugout canoes, gliding silently within feet "
            "of drinking elephants, red lechwe antelopes, and rare Pel's fishing owls. Further north, Chobe National Park hosts "
            "Africa's highest concentration of elephants, offering world-class wildlife river boat safaris."
        ),
        "heroImage": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=1000&q=80", "caption": "Mokoro canoe gliding through Okavango Delta waterways"},
            {"url": "https://images.unsplash.com/photo-1589556264800-08ae9e129a8c?auto=format&fit=crop&w=1000&q=80", "caption": "Elephant herds crossing Chobe River shallows"}
        ],
        "coordinates": [-19.2833, 22.9000],
        "highlights": [
            "UNESCO Okavango Delta — Earth's premier inland wetland wilderness",
            "Traditional poler-guided mokoro dugout canoe excursions",
            "Chobe River boat safaris watching hundreds of bathing elephants",
            "Moremi Game Reserve predator tracking (wild dogs, lions, cheetahs)",
            "Quad biking across the surreal white expanse of Makgadikgadi Salt Pans"
        ],
        "activities": [
            "Mokoro boat safaris through water-lily lagoons",
            "Open-vehicle day and night game drives in private concessions",
            "Scenic fly-in helicopter safaris without doors for photography",
            "Horseback safaris across delta floodplains",
            "Stargazing sleep-outs on elevated skybeds"
        ],
        "bestTimeToVisit": "May to October offers optimal dry season game viewing as floodwaters fill the delta and wildlife concentrates along waterways.",
        "quickFacts": {
            "bestTime": "May – Oct",
            "idealDuration": "4 – 7 Days",
            "language": "English, Setswana",
            "currency": "Botswana Pula (BWP) & USD",
            "visa": "Visa-free for many nationalities",
            "climate": "Sunny dry winters (24-28°C daytime, cool 6-10°C night)"
        },
        "accommodations": [
            {"name": "Mombo Camp (Wilderness Safaris)", "tier": "Ultra-Luxury", "location": "Chief's Island", "description": "Widely known as 'The Place of Plenty', set in the heart of Moremi Game Reserve."},
            {"name": "Belmond Eagle Island Lodge", "tier": "Luxury Water Camp", "location": "Okavango Delta", "description": "Dedicated water-focused safari camp featuring private plunge pools and dedicated helicopter flights."}
        ],
        "packageIds": [],
        "relatedSlugs": ["south-africa", "namibia", "zambia", "zimbabwe"],
        "faqs": [
            {
                "q": "How do you travel between safari camps in Botswana?",
                "a": "Because most of the Okavango Delta is roadless wilderness, travelers travel between remote camps on scenic light aircraft bush flights."
            }
        ]
    },
    {
        "id": "south-africa",
        "slug": "south-africa",
        "name": "South Africa (Cape Town & Kruger)",
        "country": "South Africa",
        "region": "Africa",
        "regions": ["Africa"],
        "categories": ["Luxury Getaways", "City Breaks", "Wildlife Safaris", "Honeymoon Destinations"],
        "tagline": "A World in One Country: Table Mountain, Winelands & Greater Kruger",
        "shortDescription": "Ascend Table Mountain, taste vintage wines in Stellenbosch, watch penguins at Boulders Beach, and track the Big Five in Sabi Sands.",
        "overview": (
            "South Africa richly earns its title as 'A World in One Country'. Offering an unparalleled blend of first-world "
            "cosmopolitan elegance and raw African wilderness, South Africa is the ideal destination for travelers who want "
            "sophisticated wine tasting, world-class dining, dramatic coastlines, and premier Big Five safaris.\n\n"
            "Cape Town is framed by Table Mountain and two oceans, featuring the Victoria & Alfred Waterfront, colorful Bo-Kaap, "
            "and penguin colonies at Boulders Beach. A short drive into the Cape Winelands reveals historic Dutch estates in Stellenbosch "
            "and Franschhoek. In the north, Greater Kruger and private reserves like Sabi Sands provide Africa's finest luxury safari lodges "
            "and close-up leopard sightings."
        ),
        "heroImage": "https://images.unsplash.com/photo-1580618672591-eb180b1a973f?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1580618672591-eb180b1a973f?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1580618672591-eb180b1a973f?auto=format&fit=crop&w=1000&q=80", "caption": "Table Mountain overlooking the Atlantic Ocean and Cape Town"},
            {"url": "https://images.unsplash.com/photo-1534177616072-ef7dc120449d?auto=format&fit=crop&w=1000&q=80", "caption": "Leopard in Sabi Sands Game Reserve Kruger"}
        ],
        "coordinates": [-33.9249, 18.4241],
        "highlights": [
            "Table Mountain aerial cableway & Cape of Good Hope scenic drive",
            "African penguin colony at Boulders Beach Simon's Town",
            "World-renowned wine tasting in Stellenbosch and Franschhoek",
            "Big Five safaris with unmatched leopard sightings in Sabi Sands",
            "Scenic Garden Route coastal road trip and whale watching in Hermanus"
        ],
        "activities": [
            "Helicopter flights over the Twelve Apostles mountain range",
            "Wine tram tours through Franschhoek historic vineyards",
            "Open-top 4x4 game drives in private Kruger reserves",
            "Great White shark cage diving in Gansbaai",
            "Dining at world top-50 restaurants in Cape Town and Winelands"
        ],
        "bestTimeToVisit": "November to March for Cape Town beaches and Winelands; May to September for premier Kruger wildlife viewing.",
        "quickFacts": {
            "bestTime": "Cape: Nov – Mar | Safari: May – Sep",
            "idealDuration": "7 – 12 Days",
            "language": "English, Afrikaans, Zulu, Xhosa",
            "currency": "South African Rand (ZAR)",
            "visa": "Visa-free for many countries up to 90 days",
            "climate": "Mediterranean in Cape Town (22-28°C), subtropical in Kruger"
        },
        "accommodations": [
            {"name": "The Silo Hotel", "tier": "Ultra-Luxury Boutique", "location": "V&A Waterfront Cape Town", "description": "Set above the Zeitz MOCAA museum with pillowing pillowed-glass windows."},
            {"name": "Singita Boulders Lodge", "tier": "Ultra-Luxury Safari", "location": "Sabi Sand Reserve", "description": "Perched along the Sand River, widely acclaimed as one of the world's finest lodges."}
        ],
        "packageIds": [],
        "relatedSlugs": ["botswana", "namibia", "zimbabwe", "mauritius"],
        "faqs": [
            {
                "q": "Can I visit Cape Town and Kruger on the same vacation?",
                "a": "Yes! Direct 2-hour domestic flights link Cape Town directly to Kruger safari airports like Skukuza and Hoedspruit."
            }
        ]
    },
    {
        "id": "namibia",
        "slug": "namibia",
        "name": "Namibia - Sossusvlei & Skeleton Coast",
        "country": "Namibia",
        "region": "Africa",
        "regions": ["Africa"],
        "categories": ["Adventure Travel", "Luxury Getaways", "Mountain Adventures"],
        "tagline": "Ancient Red Dunes, Deadvlei & Desolate Shipwreck Coasts",
        "shortDescription": "Climb towering red desert dunes at Sossusvlei, walk among 900-year-old dead trees at Deadvlei, and explore the haunting Skeleton Coast.",
        "overview": (
            "Namibia is a land of dramatic, otherworldly landscapes where the oldest desert on Earth meets the crashing waves "
            "of the Atlantic Ocean. Renowned for its vast open spaces, unpolluted dark night skies, and surreal photography, "
            "Namibia is unlike anywhere else on the continent.\n\n"
            "At Sossusvlei in the Namib-Naukluft National Park, towering ochre dunes like Big Daddy and Dune 45 rise over 300 meters "
            "above bleached white clay pans. Deadvlei is an iconic photography wonder, where 900-year-old blackened camelthorn trees "
            "stand preserved against glowing orange dunes. Along the remote Skeleton Coast, rusting shipwrecks and seal colonies "
            "lie stranded between desert sand dunes and icy Atlantic surf."
        ),
        "heroImage": "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=1000&q=80", "caption": "Ancient camelthorn trees in Deadvlei white clay pan"},
            {"url": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=1000&q=80", "caption": "Desert-adapted elephants roaming dry Damaraland riverbed"}
        ],
        "coordinates": [-24.7275, 15.3400],
        "highlights": [
            "Sossusvlei giant red dunes (Big Daddy & Dune 45)",
            "Deadvlei surreal 900-year-old blackened trees preserved in white clay",
            "Skeleton Coast shipwreck fly-ins and Cape Cross fur seal colony",
            "Tracking desert-adapted elephants and black rhinos in Damaraland",
            "Dark Sky Reserve stargazing with crystal-clear southern hemisphere skies"
        ],
        "activities": [
            "Sunrise dune climbing and sandboarding",
            "Hot air balloon flights over the Namib Desert at dawn",
            "Fly-in safaris over the Skeleton Coast shipwrecks and dunes",
            "Stargazing with on-site lodge astronomers",
            "Tracking desert-adapted lions and black rhinos"
        ],
        "bestTimeToVisit": "May to October offers cool desert temperatures, clear skies, and comfortable travel weather.",
        "quickFacts": {
            "bestTime": "May – Oct",
            "idealDuration": "5 – 9 Days",
            "language": "English, Afrikaans, German",
            "currency": "Namibian Dollar (NAD) & South African Rand",
            "visa": "Visa-free for many nationalities",
            "climate": "Arid desert climate (warm days 24-28°C, cold nights 5-10°C)"
        },
        "accommodations": [
            {"name": "andBeyond Sossusvlei Desert Lodge", "tier": "Ultra-Luxury Eco", "location": "Sossusvlei Reserve", "description": "Architectural glass-and-stone suites with private plunge pools and skylights over beds for stargazing."},
            {"name": "Shipwreck Lodge", "tier": "Unique Architecture", "location": "Skeleton Coast", "description": "Innovative luxury cabins shaped like stranded shipwrecks nestled in coastal sand dunes."}
        ],
        "packageIds": [],
        "relatedSlugs": ["botswana", "south-africa", "zambia", "zimbabwe"],
        "faqs": [
            {
                "q": "How old are the trees in Deadvlei?",
                "a": "The dead camelthorn trees in Deadvlei died approximately 900 years ago when sand dunes cut off the river. The climate is so dry that the wood cannot decompose, leaving them standing as natural sculptures."
            }
        ]
    },
    {
        "id": "zambia",
        "slug": "zambia",
        "name": "Zambia & South Luangwa",
        "country": "Zambia",
        "region": "Africa",
        "regions": ["Africa"],
        "categories": ["Wildlife Safaris", "Adventure Travel"],
        "tagline": "The Birthplace of Walking Safaris & Leopard Capital",
        "shortDescription": "Embark on legendary walking safaris in South Luangwa, canoe the Lower Zambezi, and experience the thunder of Victoria Falls.",
        "overview": (
            "Zambia is widely celebrated by discerning safari connoisseurs as Africa's greatest authentic bush destination. "
            "It is the historic birthplace of the walking safari, pioneered in the legendary South Luangwa National Park by conservationist Norman Carr.\n\n"
            "South Luangwa is celebrated as the 'Valley of the Leopard' due to its unrivaled density of leopards, best observed on night game drives. "
            "To the south, the Lower Zambezi National Park offers tranquil canoeing past pods of hippos and riverbank elephants, "
            "while Livingstone provides access to the majestic Victoria Falls and adrenaline activities."
        ),
        "heroImage": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=1000&q=80", "caption": "Bush walking safari in South Luangwa National Park"},
            {"url": "https://images.unsplash.com/photo-1534177616072-ef7dc120449d?auto=format&fit=crop&w=1000&q=80", "caption": "Leopard hunting along Luangwa river lagoon"}
        ],
        "coordinates": [-13.0833, 31.7833],
        "highlights": [
            "Pioneering authentic walking safaris guided by top safari experts",
            "South Luangwa — Africa's premier leopard tracking destination",
            "Canoe safaris along the scenic channels of the Lower Zambezi",
            "Access to Victoria Falls (Mosi-oa-Tunya) in Livingstone",
            "Spectacular nocturnal spotlight game drives"
        ],
        "activities": [
            "Multi-day walking safaris between wilderness bush camps",
            "Canoeing along the Zambezi River with elephants and hippos",
            "Nocturnal game drives tracking leopards and genets",
            "Swimming in Devil's Pool at the lip of Victoria Falls (seasonal)",
            "Tiger fishing in the Zambezi River"
        ],
        "bestTimeToVisit": "June to October is peak dry season with animals concentrating in massive numbers along riverbanks.",
        "quickFacts": {
            "bestTime": "Jun – Oct",
            "idealDuration": "4 – 7 Days",
            "language": "English, Bemba, Nyanja",
            "currency": "Zambian Kwacha (ZMW) & USD",
            "visa": "KAZA UniVisa available online",
            "climate": "Warm dry winters (25-30°C daytime, cool nights)"
        },
        "accommodations": [
            {"name": "Time + Tide Chinzombo", "tier": "Ultra-Luxury Bush Camp", "location": "South Luangwa", "description": "Award-winning design camp on a sweeping bend of the Luangwa River."},
            {"name": "Royal Zambezi Lodge", "tier": "5-Star River Lodge", "location": "Lower Zambezi", "description": "Overlooking the Zambezi with private plunge pools and copper bathtubs."}
        ],
        "packageIds": [],
        "relatedSlugs": ["zimbabwe", "botswana", "south-africa", "namibia"],
        "faqs": [
            {
                "q": "What makes a walking safari in Zambia so special?",
                "a": "Zambia's walking safari guides are among the most rigorously trained on the planet, allowing you to track footprints, study plants, and encounter big game safely on foot."
            }
        ]
    },
    {
        "id": "zimbabwe",
        "slug": "zimbabwe",
        "name": "Zimbabwe & Victoria Falls",
        "country": "Zimbabwe",
        "region": "Africa",
        "regions": ["Africa"],
        "categories": ["Adventure Travel", "Wildlife Safaris", "Luxury Getaways"],
        "tagline": "The Smoke that Thunders & Hwange Elephant Sanctuaries",
        "shortDescription": "Witness the thunderous spray of Victoria Falls, track massive elephant herds in Hwange, and explore the ancient Great Zimbabwe stone ruins.",
        "overview": (
            "Zimbabwe is home to warm-hearted hospitality, exceptionally knowledgeable safari guides, and some of Southern Africa's "
            "most iconic natural wonders. At its border with Zambia lies Victoria Falls (known locally as Mosi-oa-Tunya—'The Smoke That Thunders'), "
            "one of the Seven Natural Wonders of the World, where the Zambezi River plunges over a 100-meter chasm creating clouds of mist visible 30 miles away.\n\n"
            "Just two hours south of the falls lies Hwange National Park, Zimbabwe's largest game reserve, home to over 40,000 elephants "
            "and packs of African wild dogs. In the north, Mana Pools National Park offers UNESCO-protected walking safaris beneath albida trees "
            "where elephants famously stand on their hind legs to reach upper branches."
        ),
        "heroImage": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1000&q=80", "caption": "The thunderous curtain of Victoria Falls with rainbow"},
            {"url": "https://images.unsplash.com/photo-1589556264800-08ae9e129a8c?auto=format&fit=crop&w=1000&q=80", "caption": "Elephant herd drinking at Hwange National Park waterhole"}
        ],
        "coordinates": [-17.9244, 25.8572],
        "highlights": [
            "Victoria Falls — world's largest sheet of falling water",
            "Helicopter 'Flight of Angels' over Victoria Falls and Batoka Gorge",
            "Hwange National Park with over 40,000 elephants and wild dog packs",
            "UNESCO Mana Pools walking safaris with legendary standing elephants",
            "Sunset luxury riverboat cruises along the upper Zambezi River"
        ],
        "activities": [
            "Guided walking tour of Victoria Falls rainforest trails",
            "Helicopter flights over the falls chasm",
            "Zambezi sunset luxury cocktail cruises",
            "Walking safaris in Hwange and Mana Pools with professional guides",
            "White-water rafting the rapids of the Zambezi River"
        ],
        "bestTimeToVisit": "May to October is ideal for wildlife viewing; February to May offers peak water flow and roaring spray at the falls.",
        "quickFacts": {
            "bestTime": "May – Oct (Wildlife) | Mar – May (Falls)",
            "idealDuration": "4 – 7 Days",
            "language": "English, Shona, Ndebele",
            "currency": "USD widely accepted",
            "visa": "KAZA UniVisa available on arrival",
            "climate": "Warm temperate (25-30°C daytime)"
        },
        "accommodations": [
            {"name": "The Victoria Falls Hotel", "tier": "Historic Edwardian Luxury", "location": "Victoria Falls", "description": "The Grand Old Lady of the Falls founded in 1904, with private pathway to the falls."},
            {"name": "Matetsi Victoria Falls", "tier": "Ultra-Luxury Safari Lodge", "location": "Private Zambezi Concession", "description": "Combines private Zambezi riverfront luxury villas with private Big Five game drives."}
        ],
        "packageIds": [],
        "relatedSlugs": ["zambia", "botswana", "south-africa", "namibia"],
        "faqs": [
            {
                "q": "Can I visit Victoria Falls from both Zimbabwe and Zambia?",
                "a": "Yes! The KAZA UniVisa covers both countries, allowing you to cross the historic Victoria Falls Bridge easily to view both sides."
            }
        ]
    },
    {
        "id": "mauritius",
        "slug": "mauritius",
        "name": "Mauritius Island",
        "country": "Mauritius",
        "region": "Africa",
        "regions": ["Africa"],
        "categories": ["Beach Escapes", "Honeymoon Destinations", "Luxury Getaways", "Family Holidays"],
        "tagline": "Sapphire Lagoons, Chamarel Earths & Coral Coastlines",
        "shortDescription": "Bask along tranquil turquoise coral lagoons, play championship golf, and marvel at Chamarel's Seven Coloured Earths on this Indian Ocean paradise.",
        "overview": (
            "Mauritius is a glittering jewel in the southwest Indian Ocean, celebrated worldwide for its idyllic sapphire waters, "
            "luxurious beach resorts, and harmonious blend of Creole, French, Indian, and Chinese cultures.\n\n"
            "Encircled almost entirely by a coral barrier reef, Mauritius offers calm, safe swimming in clear lagoons. "
            "Beyond the white beaches, visitors discover the dramatic UNESCO-protected mountain peninsula of Le Morne Brabant, "
            "the optical illusion of the underwater waterfall, the Seven Coloured Earths of Chamarel, and world-class luxury golf resorts."
        ),
        "heroImage": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1000&q=80", "caption": "Le Morne Brabant mountain rising above turquoise lagoon"},
            {"url": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=1000&q=80", "caption": "Luxury beachfront resort pool overlooking Indian Ocean"}
        ],
        "coordinates": [-20.3484, 57.5522],
        "highlights": [
            "Le Morne Brabant UNESCO mountain peninsula and turquoise lagoon",
            "Chamarel Seven Coloured Earths geological formation and waterfall",
            "Catamaran day cruises to idyllic offshore islets like Île aux Cerfs",
            "Swimming with wild spinner dolphins in Tamarin Bay",
            "Championship 18-hole golf courses designed by Ernie Els and Bernhard Langer"
        ],
        "activities": [
            "Catamaran sailing and snorkeling on coral reefs",
            "Swimming with wild dolphins in Tamarin Bay",
            "Helicopter scenic flights over the 'Underwater Waterfall'",
            "Hiking Le Morne mountain with panoramic ocean views",
            "Rum tasting tours at historic rhumeries in Chamarel"
        ],
        "bestTimeToVisit": "May to December brings pleasant, sunny, dry tropical weather with cooling trade winds.",
        "quickFacts": {
            "bestTime": "May – Dec",
            "idealDuration": "5 – 8 Days",
            "language": "English, French, Mauritian Creole",
            "currency": "Mauritian Rupee (MUR) & USD",
            "visa": "Visa-free for most international visitors",
            "climate": "Subtropical maritime (25-30°C year-round)"
        },
        "accommodations": [
            {"name": "The Oberoi Beach Resort Mauritius", "tier": "5-Star Ultra-Luxury", "location": "Turtle Bay", "description": "Set in 20 acres of sub-tropical gardens with private pavilion villas and sunken marble baths."},
            {"name": "Royal Palm Beachcomber Luxury", "tier": "Iconic Grand Luxury", "location": "Grand Baie", "description": "Prestigious address on the vibrant north coast, favored by royalty and celebrities."}
        ],
        "packageIds": [],
        "relatedSlugs": ["seychelles", "zanzibar", "diani-beach", "maldives"],
        "faqs": [
            {
                "q": "What is the 'Underwater Waterfall' in Mauritius?",
                "a": "It is a spectacular optical illusion off the coast of Le Morne where sand and silt runoff into the ocean trench creates the visual appearance of a roaring underwater waterfall when viewed from a helicopter."
            }
        ]
    },
    {
        "id": "seychelles",
        "slug": "seychelles",
        "name": "Seychelles Archipelago",
        "country": "Seychelles",
        "region": "Africa",
        "regions": ["Africa"],
        "categories": ["Beach Escapes", "Honeymoon Destinations", "Luxury Getaways"],
        "tagline": "Granite Boulders, Anse Source d'Argent & Giant Tortoises",
        "shortDescription": "Discover the Garden of Eden on Earth with sculpted pink granite boulders, Coco de Mer palms, and private island sanctuaries.",
        "overview": (
            "The Republic of Seychelles is an archipelago of 115 granite and coral islands scattered across the western Indian Ocean. "
            "Renowned as one of the most exclusive and pristine romantic hideaways in the world, Seychelles features postcard-perfect "
            "beaches defined by dramatic polished granite boulders, powdery white sand, and lush tropical jungles.\n\n"
            "On La Digue island, Anse Source d'Argent is frequently voted the world's most photographed beach. On Praslin, "
            "the UNESCO-protected Vallée de Mai nature reserve is home to the legendary Coco de Mer palm tree, producing the largest "
            "seed in the plant kingdom. On Curieuse Island, hundreds of giant Aldabra tortoises roam freely in the wild."
        ),
        "heroImage": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=1000&q=80", "caption": "Anse Source d'Argent granite boulders on La Digue"},
            {"url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1000&q=80", "caption": "Giant Aldabra tortoise on pristine Seychelles beach"}
        ],
        "coordinates": [-4.6796, 55.4920],
        "highlights": [
            "Anse Source d'Argent — the world's most photographed beach on La Digue",
            "UNESCO Vallée de Mai home to the endemic giant Coco de Mer palm",
            "Encountering giant Aldabra tortoises in the wild on Curieuse Island",
            "Pristine coral atoll scuba diving with manta rays and whale sharks",
            "Private island hopping via helicopter and luxury catamarans"
        ],
        "activities": [
            "Island hopping between Mahé, Praslin, and La Digue",
            "Bicycling around car-free La Digue island",
            "Snorkeling at Sainte Anne Marine National Park",
            "Private beachfront candlelight dinners with Creole seafood",
            "Scuba diving along outer granite drop-offs"
        ],
        "bestTimeToVisit": "April to May and October to November provide calm waters, high underwater visibility (up to 30m), and gentle breezes.",
        "quickFacts": {
            "bestTime": "Apr – May & Oct – Nov",
            "idealDuration": "5 – 9 Days",
            "language": "Seychellois Creole, English, French",
            "currency": "Seychellois Rupee (SCR) & EUR/USD",
            "visa": "Visa-free entry for all nationalities with valid passport",
            "climate": "Tropical maritime (26-31°C year-round)"
        },
        "accommodations": [
            {"name": "Six Senses Zil Pasyon", "tier": "Ultra-Luxury Private Island", "location": "Félicité Island", "description": "Private oceanfront pool villas nestled dramatically among towering granite boulders."},
            {"name": "Four Seasons Resort Seychelles", "tier": "5-Star Luxury", "location": "Petite Anse Mahé", "description": "Treehouse villas with private infinity pools overlooking one of Mahé's most secluded bays."}
        ],
        "packageIds": [],
        "relatedSlugs": ["mauritius", "maldives", "zanzibar", "diani-beach"],
        "faqs": [
            {
                "q": "How do you travel between islands in Seychelles?",
                "a": "High-speed modern catamarans (Cat Cocos) run daily between Mahé, Praslin, and La Digue. Scenic 15-minute inter-island flights and private helicopter transfers are also widely available."
            }
        ]
    },
    {
        "id": "egypt",
        "slug": "egypt",
        "name": "Egypt - Land of the Pharaohs",
        "country": "Egypt",
        "region": "Africa",
        "regions": ["Africa", "Middle East"],
        "categories": ["Cultural Experiences", "Adventure Travel", "Luxury Getaways"],
        "tagline": "The Pyramids of Giza, Valley of the Kings & Nile Cruises",
        "shortDescription": "Stand before the Great Pyramids, cruise the timeless Nile River aboard luxury dahabiyas, and explore ancient pharaonic temples.",
        "overview": (
            "Egypt is the cradle of human civilization, where five thousand years of monumental history line the life-giving waters "
            "of the River Nile. From the towering Great Pyramids of Giza and the enigmatic Sphinx to the colossal temples of Luxor "
            "and Karnak, Egypt is an unparalleled journey through antiquity.\n\n"
            "A luxury cruise along the Nile between Luxor and Aswan carries travelers past palm-lined riverbanks, timeless mudbrick villages, "
            "and rock-cut pharaonic tombs. In the Valley of the Kings, the underground burial chambers of Tutankhamun and Ramesses "
            "gleam with radiant hieroglyphic colors preserved for millennia."
        ),
        "heroImage": "https://images.unsplash.com/photo-1503177119275-0aa32b3a9368?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1503177119275-0aa32b3a9368?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1503177119275-0aa32b3a9368?auto=format&fit=crop&w=1000&q=80", "caption": "The Great Pyramids of Giza and Sphinx at sunset"},
            {"url": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=1000&q=80", "caption": "Luxury cruise vessel sailing along the Nile in Luxor"}
        ],
        "coordinates": [29.9792, 31.1342],
        "highlights": [
            "The Great Pyramids of Giza & Great Sphinx (the last surviving Ancient Wonder)",
            "Grand Egyptian Museum (GEM) world's largest archaeological museum",
            "Valley of the Kings and Valley of the Queens in Luxor",
            "Luxury Nile River cruise between Luxor and Aswan",
            "Colossal temples of Abu Simbel carved into sandstone cliffs by Ramesses II"
        ],
        "activities": [
            "Private Egyptologist-guided exploration of the Pyramids and Sphinx",
            "Hot air balloon flight over Luxor's West Bank at sunrise",
            "Multi-day luxury Nile River cruise aboard a private dahabiya",
            "Traditional felucca sailboat cruise around Elephantine Island in Aswan",
            "Exploring the Khan el-Khalili bazaar in historic Cairo"
        ],
        "bestTimeToVisit": "October to April brings pleasant, mild daytime weather ideal for exploring desert tombs and temple complexes.",
        "quickFacts": {
            "bestTime": "Oct – Apr",
            "idealDuration": "6 – 10 Days",
            "language": "Arabic, English",
            "currency": "Egyptian Pound (EGP) & USD",
            "visa": "Egypt eVisa / Visa on arrival",
            "climate": "Desert climate (mild winters 20-25°C, hot summers)"
        },
        "accommodations": [
            {"name": "Marriott Mena House Cairo", "tier": "Historic 5-Star Luxury", "location": "Giza Pyramids View", "description": "Historic palace hotel where private garden balconies look directly onto the Great Pyramids."},
            {"name": "Sofitel Legend Old Cataract Aswan", "tier": "Iconic Heritage Palace", "location": "Aswan Nile Riverbank", "description": "19th-century Victorian palace on pink granite rocks overlooking Elephantine Island, where Agatha Christie wrote."}
        ],
        "packageIds": [],
        "relatedSlugs": ["dubai", "morocco", "greece", "italy"],
        "faqs": [
            {
                "q": "What is the best way to travel between Cairo, Luxor, and Aswan?",
                "a": "Daily 1-hour domestic flights link Cairo to Luxor and Aswan, followed by a multi-day luxury Nile River cruise between Luxor and Aswan."
            }
        ]
    },
    {
        "id": "morocco",
        "slug": "morocco",
        "name": "Morocco - Imperial Cities & Sahara",
        "country": "Morocco",
        "region": "Africa",
        "regions": ["Africa"],
        "categories": ["Cultural Experiences", "Luxury Getaways", "Adventure Travel", "City Breaks"],
        "tagline": "Vibrant Souks, Majestic Riads & Sahara Golden Dunes",
        "shortDescription": "Wander colorful medinas in Marrakech, relax in palatial riads, hike High Atlas peaks, and sleep under desert stars in the Sahara.",
        "overview": (
            "Morocco is a sensory tapestry of colors, aromas, and ancient architectural splendor where Europe, the Mediterranean, "
            "and Africa converge. From the bustling labyrinthine souks and snake-charmers of Marrakech's Jemaa el-Fnaa square "
            "to the blue-washed walls of Chefchaouen, Morocco enchants at every turn.\n\n"
            "Restored palatial riads offer tranquil courtyards scented with orange blossoms and cooling fountains. "
            "Crossing the snow-capped High Atlas Mountains leads into the golden ocean of Sahara dunes at Erg Chebbi, "
            "where camel caravans journey to luxury glamping encampments under star-studded desert skies."
        ),
        "heroImage": "https://images.unsplash.com/photo-1548013146-72479768bada?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1548013146-72479768bada?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1548013146-72479768bada?auto=format&fit=crop&w=1000&q=80", "caption": "Lush courtyard and zellij tilework of a luxury Moroccan riad"},
            {"url": "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=1000&q=80", "caption": "Camel caravan traversing golden Erg Chebbi dunes in the Sahara"}
        ],
        "coordinates": [31.6295, -7.9811],
        "highlights": [
            "Marrakech vibrant Medina, Majorelle Garden, and Bahia Palace",
            "Erg Chebbi luxury Sahara desert glamping under Milky Way stars",
            "UNESCO Fes el-Bali — the world's largest preserved medieval car-free city",
            "High Atlas Mountains Berber villages and panoramic mountain passes",
            "Authentic Moroccan Hammam wellness and steam rituals"
        ],
        "activities": [
            "Private guided cultural walking tours through historic souks",
            "Camel trekking across the towering Sahara sand dunes",
            "Authentic Moroccan culinary masterclass cooking tagines and pastillas",
            "Traditional Hammam steam bath and argan oil massage treatments",
            "Exploring the ancient mudbrick ksar of Aït Benhaddou"
        ],
        "bestTimeToVisit": "March to May (Spring) and September to November (Autumn) offer warm pleasant temperatures across cities and the desert.",
        "quickFacts": {
            "bestTime": "Mar – May & Sep – Nov",
            "idealDuration": "6 – 10 Days",
            "language": "Arabic, Berber, French, English",
            "currency": "Moroccan Dirham (MAD)",
            "visa": "Visa-free for many nationalities up to 90 days",
            "climate": "Mediterranean on coast, continental in interior, desert in south"
        },
        "accommodations": [
            {"name": "Royal Mansour Marrakech", "tier": "Palatial Ultra-Luxury", "location": "Marrakech", "description": "Commissioned by the King of Morocco, an exquisite private medina of luxury multi-story riads."},
            {"name": "La Mamounia", "tier": "Iconic Historic Palace", "location": "Marrakech", "description": "Legendary hotel surrounded by 17-acre royal gardens, beloved by Winston Churchill and Yves Saint Laurent."}
        ],
        "packageIds": [],
        "relatedSlugs": ["egypt", "dubai", "spain", "italy"],
        "faqs": [
            {
                "q": "What is a riad?",
                "a": "A riad is a traditional Moroccan townhouse or palace designed around a central open-air courtyard with gardens and fountains, offering serene privacy away from bustling medina streets."
            }
        ]
    },

    # =========================================================================
    # ASIA & MIDDLE EAST (7 Destinations)
    # =========================================================================
    {
        "id": "dubai",
        "slug": "dubai",
        "name": "Dubai & UAE",
        "country": "United Arab Emirates",
        "region": "Middle East",
        "regions": ["Middle East", "Asia"],
        "categories": ["Luxury Getaways", "City Breaks", "Family Holidays", "Honeymoon Destinations"],
        "tagline": "Futuristic Skyline, Golden Deserts & World-Class Luxury",
        "shortDescription": "Marvel at the world's tallest skyscraper, stay on iconic Palm Jumeirah, shop luxury malls, and experience sunset desert dune safaris.",
        "overview": (
            "Dubai is a dazzling desert metropolis where bold futuristic architectural ambition meets deep Arabian heritage. "
            "Rising dramatically from the sands of the Arabian Gulf, Dubai is world-renowned for its superlative landmarks, "
            "including the world's tallest building (Burj Khalifa), the man-made Palm Jumeirah archipelago, and palatial shopping complexes.\n\n"
            "Travelers can experience afternoon tea atop the Burj Al Arab, explore the cutting-edge Museum of the Future, "
            "cruise Dubai Marina on luxury yachts, and head into the Dubai Desert Conservation Reserve for thrilling red dune bashing "
            "and starlit Bedouin feasts."
        ),
        "heroImage": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=1000&q=80", "caption": "Burj Khalifa and Downtown Dubai skyline illuminated at dusk"},
            {"url": "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=1000&q=80", "caption": "Red desert dune bashing safari in Dubai desert"}
        ],
        "coordinates": [25.2048, 55.2708],
        "highlights": [
            "Burj Khalifa — standing atop the world's tallest building at 828m",
            "The Palm Jumeirah iconic artificial island and Aquaventure waterpark",
            "Museum of the Future — architectural and technological masterpiece",
            "Dubai Desert Conservation Reserve luxury glamping and dune bashing",
            "Dubai Mall, gold souks, and dancing fountain spectacular"
        ],
        "activities": [
            "Viewing Dubai from the 148th-floor Burj Khalifa observation deck",
            "Luxury red dune desert safari with falconry and Bedouin dinner",
            "Private yacht charter cruising Dubai Marina and around the Palm",
            "Shopping in traditional Gold and Spice Souks in Deira",
            "Michelin-starred fine dining and rooftop lounges"
        ],
        "bestTimeToVisit": "November to March offers sunny, temperate winter weather with temperatures between 24°C and 28°C.",
        "quickFacts": {
            "bestTime": "Nov – Mar",
            "idealDuration": "4 – 6 Days",
            "language": "Arabic, English widely spoken",
            "currency": "UAE Dirham (AED) & USD",
            "visa": "Visa on arrival for most passports",
            "climate": "Arid subtropical (warm winters 24-28°C, hot summers)"
        },
        "accommodations": [
            {"name": "Burj Al Arab Jumeirah", "tier": "World's Only '7-Star' Luxury", "location": "Private Island Waterfront", "description": "Sail-shaped icon offering duplex suites with private butler service and helicopter pad."},
            {"name": "Atlantis The Royal", "tier": "Ultra-Luxury Landmark", "location": "Palm Jumeirah", "description": "Next-generation luxury icon featuring cloud pools, celebrity chef restaurants, and private beach."}
        ],
        "packageIds": [],
        "relatedSlugs": ["singapore", "maldives", "egypt", "thailand"],
        "faqs": [
            {
                "q": "What is the dress code in Dubai?",
                "a": "Dubai is modern and cosmopolitan. Standard resort wear and swimwear are completely normal at hotels, pools, and private beaches. Modest attire covering shoulders and knees is appreciated in shopping malls and mosques."
            }
        ]
    },
    {
        "id": "maldives",
        "slug": "maldives",
        "name": "Maldives Archipelago",
        "country": "Maldives",
        "region": "Asia",
        "regions": ["Asia"],
        "categories": ["Honeymoon Destinations", "Luxury Getaways", "Beach Escapes"],
        "tagline": "Private Overwater Bungalows & Bioluminescent Lagoons",
        "shortDescription": "Stay in dreamlike villas suspended over turquoise lagoons, dine underwater, and swim with manta rays across 1,200 coral atolls.",
        "overview": (
            "The Maldives is the quintessential paradise of luxury island escapism. A nation of over 1,200 coral islands grouped "
            "into 26 natural atolls in the heart of the Indian Ocean, the Maldives pioneered the iconic overwater villa concept, "
            "where guests wake up to stairs leading directly into warm, translucent lagoons.\n\n"
            "Each luxury resort occupies its own private island, ensuring unmatched exclusivity, privacy, and seclusion. "
            "Visitors can dine five meters below the sea in glass-enclosed underwater restaurants, snorkel with whale sharks and manta rays "
            "in the UNESCO Biosphere Reserve of Baa Atoll, or enjoy private sandbank champagne picnics."
        ),
        "heroImage": "https://images.unsplash.com/photo-1514282401047-d79a71a590e8?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1514282401047-d79a71a590e8?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1514282401047-d79a71a590e8?auto=format&fit=crop&w=1000&q=80", "caption": "Overwater villa boardwalk across turquoise lagoon"},
            {"url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1000&q=80", "caption": "Private sandbank breakfast surrounded by open ocean"}
        ],
        "coordinates": [3.2028, 73.2207],
        "highlights": [
            "Private overwater villas with glass floor panels and infinity plunge pools",
            "Underwater dining experiences surrounded by vibrant marine coral reefs",
            "Baa Atoll UNESCO Biosphere Reserve home to hundreds of feeding manta rays",
            "Spectacular seaplane flights over atolls and turquoise sandbars",
            "Bioluminescent beaches glowing neon blue under night skies"
        ],
        "activities": [
            "Snorkeling and scuba diving with whale sharks and sea turtles",
            "Seaplane flightseeing over the atolls",
            "Sunset dolphin cruises aboard traditional Maldivian dhonis",
            "Private chef candlelit dinners on deserted sandbanks",
            "Overwater spa treatments listening to the lapping waves"
        ],
        "bestTimeToVisit": "November to April offers the dry northeast monsoon with endless sunny days, calm seas, and brilliant visibility.",
        "quickFacts": {
            "bestTime": "Nov – Apr",
            "idealDuration": "4 – 7 Days",
            "language": "Dhivehi, English widely spoken",
            "currency": "Maldivian Rufiyaa (MVR) & USD widely used",
            "visa": "Free 30-day tourist visa on arrival for all nationalities",
            "climate": "Tropical year-round (28-31°C)"
        },
        "accommodations": [
            {"name": "Soneva Jani", "tier": "Ultra-Luxury Icon", "location": "Noonu Atoll", "description": "Palatial overwater villas with waterslides directly into the lagoon and retractable roofs for stargazing."},
            {"name": "Gili Lankanfushi", "tier": "Eco-Luxury Barefoot", "location": "North Malé Atoll", "description": "Barefoot luxury with private Mr./Ms. Friday butler service and private ocean hamlets."}
        ],
        "packageIds": [],
        "relatedSlugs": ["seychelles", "mauritius", "bali", "dubai"],
        "faqs": [
            {
                "q": "How do you reach resorts from Malé Airport?",
                "a": "Depending on the distance of your resort island, transfers are operated via scenic seaplanes (15 to 45 mins) or luxury private speedboats."
            }
        ]
    },
    {
        "id": "bali",
        "slug": "bali",
        "name": "Bali, Indonesia",
        "country": "Indonesia",
        "region": "Asia",
        "regions": ["Asia"],
        "categories": ["Cultural Experiences", "Beach Escapes", "Honeymoon Destinations", "Luxury Getaways"],
        "tagline": "Island of the Gods, Emerald Terraces & Sacred Temples",
        "shortDescription": "Immerse yourself in Ubud's emerald rice terraces, clifftop Uluwatu temples, holistic wellness spas, and vibrant beach sunsets.",
        "overview": (
            "Bali, the famed 'Island of the Gods', is a tropical Indonesian paradise revered for its rich spiritual heritage, "
            "vibrant artistic culture, and lush volcanic landscapes. Deeply rooted in Balinese Hinduism, daily offerings of fragrant flowers "
            "and incense grace temple stone steps and village lanes.\n\n"
            "In Ubud, the cultural heart of the island, verdant Tegallalang rice terraces cascade down jungle river gorges alongside "
            "holistic yoga retreats and royal palaces. Along the southern coasts, Uluwatu features dramatic cliffside temples perched "
            "above crashing Indian Ocean waves where traditional Kecak fire dances are performed at sunset."
        ),
        "heroImage": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=1000&q=80", "caption": "Tegallalang emerald green rice terraces near Ubud"},
            {"url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1000&q=80", "caption": "Uluwatu sea temple perched on dramatic sea cliff"}
        ],
        "coordinates": [-8.3405, 115.0920],
        "highlights": [
            "Tegallalang UNESCO terraced rice paddies and jungle river valleys",
            "Uluwatu Clifftop Temple and sunset Kecak Fire Dance performance",
            "Sacred Monkey Forest Sanctuary in Ubud",
            "Sunrise trek to the summit crater of Mount Batur active volcano",
            "World-renowned Balinese holistic massage and botanical wellness spas"
        ],
        "activities": [
            "Sunrise hike atop Mount Batur followed by hot spring soak",
            "Traditional Balinese cooking class using organic spices",
            "Surfing the world-famous breaks of Canggu and Uluwatu",
            "Purification water blessings at Tirta Empul water temple",
            "Browsing artisan silver, wood carving, and batik workshops"
        ],
        "bestTimeToVisit": "April to October offers the dry season with lower humidity, sunny skies, and pleasant evenings.",
        "quickFacts": {
            "bestTime": "Apr – Oct",
            "idealDuration": "5 – 9 Days",
            "language": "Indonesian, Balinese, English",
            "currency": "Indonesian Rupiah (IDR)",
            "visa": "Visa on arrival available for 90+ countries",
            "climate": "Tropical monsoon (27-31°C year-round)"
        },
        "accommodations": [
            {"name": "Mandapa, a Ritz-Carlton Reserve", "tier": "Ultra-Luxury Sanctuary", "location": "Ayung River Ubud", "description": "Hidden private reserve nestled in lush rainforest along the sacred Ayung River."},
            {"name": "Bulgari Resort Bali", "tier": "Exclusive Clifftop Luxury", "location": "Uluwatu Cliffs", "description": "Combines traditional Balinese design with high Italian luxury 150m above the Indian Ocean."}
        ],
        "packageIds": [],
        "relatedSlugs": ["thailand", "maldives", "singapore", "indonesia"],
        "faqs": [
            {
                "q": "Should I stay in Ubud or on the beach?",
                "a": "We recommend splitting your stay: 3 nights in Ubud for jungle, culture, and wellness, followed by 3-4 nights on the coast (Seminyak or Uluwatu) for beaches and sunsets."
            }
        ]
    },
    {
        "id": "thailand",
        "slug": "thailand",
        "name": "Thailand (Bangkok & Phuket)",
        "country": "Thailand",
        "region": "Asia",
        "regions": ["Asia"],
        "categories": ["Beach Escapes", "Cultural Experiences", "City Breaks", "Family Holidays"],
        "tagline": "Golden Temples, Limestone Karsts & World-Class Hospitality",
        "shortDescription": "Tour Bangkok's ornate Grand Palace, cruise Phang Nga Bay's limestone towers, and savor Michelin-starred street food in the Land of Smiles.",
        "overview": (
            "Thailand, affectionately known as the 'Land of Smiles', offers an exhilarating travel feast of gilded Buddhist temples, "
            "vibrant river canals, world-renowned culinary genius, and limestone island seascapes.\n\n"
            "In Bangkok, the Grand Palace and Wat Pho's giant Reclining Buddha contrast with sleek skytrains and bustling floating markets. "
            "Down south along the Andaman Sea, Phuket and Krabi provide gateways to Phang Nga Bay's dramatic limestone karst pillars "
            "rising out of emerald-green waters, vibrant night markets, and ultra-luxurious beachfront pool villas."
        ),
        "heroImage": "https://images.unsplash.com/photo-1528181304800-259b08848526?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1528181304800-259b08848526?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1528181304800-259b08848526?auto=format&fit=crop&w=1000&q=80", "caption": "Limestone karst islands of Phang Nga Bay in Phuket"},
            {"url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1000&q=80", "caption": "Gilded spires of Bangkok's Grand Palace and Wat Phra Kaew"}
        ],
        "coordinates": [7.8804, 98.3923],
        "highlights": [
            "Bangkok Grand Palace and Temple of the Emerald Buddha",
            "Phang Nga Bay & Phi Phi Islands limestone karst sea kayaking",
            "Chao Phraya River longtail boat canal cruises",
            "World-famous Thai street food markets and Michelin-starred dining",
            "Ethical elephant sanctuary visits in Chiang Mai and Phuket"
        ],
        "activities": [
            "Private longtail boat tour through Phang Nga Bay",
            "Bangkok street food tasting tour via tuk-tuk",
            "Traditional Thai herbal massage and spa rituals",
            "Thai culinary cooking masterclass",
            "Island-hopping snorkeling cruise to Phi Phi Islands"
        ],
        "bestTimeToVisit": "November to April offers sunny skies, calm waters, and comfortable humidity across both Bangkok and Andaman beaches.",
        "quickFacts": {
            "bestTime": "Nov – Apr",
            "idealDuration": "6 – 10 Days",
            "language": "Thai, English widely spoken in tourism",
            "currency": "Thai Baht (THB)",
            "visa": "Visa exemption for 60+ countries",
            "climate": "Tropical monsoon (28-33°C daytime)"
        },
        "accommodations": [
            {"name": "Amanpuri Phuket", "tier": "Ultra-Luxury Sanctuary", "location": "Pansea Beach Phuket", "description": "Aman's flagship resort set in a private coconut grove with private white sand beach."},
            {"name": "The Siam Hotel Bangkok", "tier": "Luxury Urban Resort", "location": "Chao Phraya River", "description": "Art Deco riverside retreat featuring private pool villas and private boat transfers."}
        ],
        "packageIds": [],
        "relatedSlugs": ["bali", "singapore", "malaysia", "dubai"],
        "faqs": [
            {
                "q": "Is street food in Thailand safe to eat?",
                "a": "Yes! Thai street food is famously delicious, freshly cooked in front of you over high heat, and heavily regulated. Stick to busy stalls with long local queues."
            }
        ]
    },
    {
        "id": "singapore",
        "slug": "singapore",
        "name": "Singapore",
        "country": "Singapore",
        "region": "Asia",
        "regions": ["Asia"],
        "categories": ["City Breaks", "Luxury Getaways", "Family Holidays"],
        "tagline": "The City in Nature: Supertrees, Marina Bay & Michelin Dining",
        "shortDescription": "Stroll beneath futuristic Supertrees at Gardens by the Bay, swim atop Marina Bay Sands, and savor street food alongside Michelin gastronomy.",
        "overview": (
            "Singapore is a futuristic island city-state where lush tropical gardens merge seamlessly with gleaming modern skyscrapers. "
            "Known as the 'City in Nature', Singapore is internationally acclaimed for its safety, pristine green spaces, and vibrant multicultural tapestry.\n\n"
            "At Gardens by the Bay, towering solar-powered Supertrees and the misty indoor waterfall of the Cloud Forest greenhouse dazzle visitors. "
            "From the iconic rooftop infinity pool of Marina Bay Sands to historic shophouses in Chinatown, Kampong Glam, and Little India, "
            "Singapore is a feast of sights, flavors, and luxury lifestyle."
        ),
        "heroImage": "https://images.unsplash.com/photo-1525625293386-3f8f99389edd?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1525625293386-3f8f99389edd?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1525625293386-3f8f99389edd?auto=format&fit=crop&w=1000&q=80", "caption": "Futuristic Supertree Grove illuminated at night in Gardens by the Bay"},
            {"url": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=1000&q=80", "caption": "Marina Bay Sands skyline and waterfront promenade"}
        ],
        "coordinates": [1.3521, 103.8198],
        "highlights": [
            "Gardens by the Bay Supertrees & Cloud Forest indoor 35m waterfall",
            "Marina Bay Sands SkyPark and 57th-floor infinity pool",
            "World-renowned Singapore Night Safari — world's first nocturnal zoo",
            "UNESCO-listed Singapore Botanic Gardens and National Orchid Garden",
            "Michelin-starred street food hawker centers (Chilli Crab, Hainanese Chicken Rice)"
        ],
        "activities": [
            "Evening garden light and sound show at Supertree Grove",
            "Dining at historic hawker centers (Maxwell, Lau Pa Sat)",
            "Cocktails at the historic Long Bar at Raffles Hotel (birthplace of the Singapore Sling)",
            "Cable car ride to Sentosa Island attractions and beaches",
            "High-end luxury shopping along Orchard Road"
        ],
        "bestTimeToVisit": "November to January and June to August offer vibrant festivals and great weather.",
        "quickFacts": {
            "bestTime": "All Year Round (Peak: Nov – Jan)",
            "idealDuration": "3 – 5 Days",
            "language": "English, Mandarin, Malay, Tamil",
            "currency": "Singapore Dollar (SGD)",
            "visa": "Visa-free for many nationalities up to 90 days",
            "climate": "Equatorial tropical (26-32°C year-round)"
        },
        "accommodations": [
            {"name": "Marina Bay Sands", "tier": "Iconic Luxury", "location": "Marina Bay", "description": "The world's most iconic integrated resort with the legendary 57th-floor rooftop infinity pool."},
            {"name": "Raffles Hotel Singapore", "tier": "Legendary Heritage Luxury", "location": "Colonial District", "description": "Founded in 1887, pure colonial elegance with private butler service and historic gardens."}
        ],
        "packageIds": [],
        "relatedSlugs": ["malaysia", "dubai", "thailand", "bali"],
        "faqs": [
            {
                "q": "Can I easily walk around Singapore?",
                "a": "Yes! Singapore is exceptionally pedestrian-friendly, with covered walkways, lush garden connectors, and an ultra-modern air-conditioned MRT subway system."
            }
        ]
    },
    {
        "id": "malaysia",
        "slug": "malaysia",
        "name": "Malaysia (Kuala Lumpur & Langkawi)",
        "country": "Malaysia",
        "region": "Asia",
        "regions": ["Asia"],
        "categories": ["Beach Escapes", "City Breaks", "Cultural Experiences", "Family Holidays"],
        "tagline": "Petronas Twin Towers, Batu Caves & Langkawi Geoparks",
        "shortDescription": "Gaze up at the glittering Petronas Twin Towers, climb rainbow stairs at Batu Caves, and unwind in rainforest luxury on Langkawi island.",
        "overview": (
            "Malaysia is a captivating Southeast Asian destination celebrated for its rich cultural harmony, futuristic cityscapes, "
            "and 10-million-year-old virgin rainforests.\n\n"
            "In the capital city of Kuala Lumpur, the steel-and-glass Petronas Twin Towers dominate a skyline steeped in Malay, Chinese, "
            "and Indian heritage, just minutes from the colorful 272 steps of the Batu Caves limestone temple. "
            "To the northwest, the 99-island archipelago of Langkawi is a UNESCO Global Geopark boasting pristine sandy coves, "
            "mangrove boat safaris with wild sea eagles, and world-class luxury eco-resorts."
        ),
        "heroImage": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1000&q=80", "caption": "Langkawi turquoise bay framed by ancient rainforest"},
            {"url": "https://images.unsplash.com/photo-1525625293386-3f8f99389edd?auto=format&fit=crop&w=1000&q=80", "caption": "Petronas Twin Towers rising above Kuala Lumpur night skyline"}
        ],
        "coordinates": [3.1390, 101.6869],
        "highlights": [
            "Petronas Twin Towers Skybridge and 86th-floor observation deck",
            "Batu Caves giant golden Murugan statue and 272 rainbow steps",
            "UNESCO Langkawi Global Geopark mangroves and limestone sea stacks",
            "Langkawi SkyCab cable car and curved Sky Bridge suspended over the abyss",
            "Culinary tasting tours of Penang street food and Jalan Alor night markets"
        ],
        "activities": [
            "Walking across the Langkawi Sky Bridge suspended 660m above sea level",
            "Mangrove boat safari spotting Brahminy kites and white-bellied sea eagles",
            "Climbing the colorful steps into the cathedral cavern of Batu Caves",
            "Shopping in luxury malls of Bukit Bintang in Kuala Lumpur",
            "Sunset catamaran cocktail sailing in the Andaman Sea"
        ],
        "bestTimeToVisit": "December to April offers dry sunny conditions ideal for Langkawi beaches and city exploration.",
        "quickFacts": {
            "bestTime": "Dec – Apr",
            "idealDuration": "5 – 8 Days",
            "language": "Bahasa Malaysia, English widely spoken",
            "currency": "Malaysian Ringgit (MYR)",
            "visa": "Visa-free for 90 days for most Western and African passports",
            "climate": "Equatorial tropical (28-32°C year-round)"
        },
        "accommodations": [
            {"name": "The Datai Langkawi", "tier": "Eco-Luxury Icon", "location": "Datai Bay Langkawi", "description": "Set inside a 10-million-year-old virgin rainforest on a private white sand bay."},
            {"name": "Four Seasons Resort Langkawi", "tier": "5-Star Beach Resort", "location": "Tanjung Rhu Beach", "description": "Moorish-inspired beach villas bordering the Kilim Karst Geopark."}
        ],
        "packageIds": [],
        "relatedSlugs": ["singapore", "thailand", "bali", "indonesia"],
        "faqs": [
            {
                "q": "Is Langkawi duty-free?",
                "a": "Yes! Langkawi is a designated duty-free island, making shopping for chocolates, perfumes, and dining exceptional value."
            }
        ]
    },
    {
        "id": "indonesia",
        "slug": "indonesia",
        "name": "Indonesia (Komodo & Raja Ampat)",
        "country": "Indonesia",
        "region": "Asia",
        "regions": ["Asia"],
        "categories": ["Adventure Travel", "Beach Escapes", "Wildlife Safaris", "Luxury Getaways"],
        "tagline": "Prehistoric Komodo Dragons & Earth's Richest Coral Reefs",
        "shortDescription": "Encounter prehistoric Komodo dragons on wild islands, walk pink sand beaches, and dive the unmatched marine wonderland of Raja Ampat.",
        "overview": (
            "Beyond Bali, the Indonesian archipelago spans over 17,000 islands of untamed natural wonders. "
            "Komodo National Park, a UNESCO World Heritage Site, is the only place on Earth where you can observe wild Komodo dragons—"
            "the world's largest living lizards, reaching three meters in length.\n\n"
            "The park is also celebrated for Padar Island's iconic tri-colored beach vista, glowing Pink Beach, and manta ray cleaning stations. "
            "Further east lies Raja Ampat, universally acknowledged by marine biologists as the epicenter of marine biodiversity on Earth, "
            "sheltering 75% of all known coral species and over 1,500 species of reef fish amidst emerald jungle-topped karst islands."
        ),
        "heroImage": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=1000&q=80", "caption": "Iconic Padar Island viewpoint overlooking three colored bays"},
            {"url": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=1000&q=80", "caption": "Wild Komodo dragon prowling on Komodo Island"}
        ],
        "coordinates": [-8.5583, 119.4894],
        "highlights": [
            "Encountering wild Komodo Dragons with expert park rangers",
            "Padar Island viewpoint overlooking pink, white, and black sand beaches",
            "Swimming along famous Pink Beach formed by crushed red coral",
            "Raja Ampat — the world's highest marine biodiversity coral reef",
            "Snorkeling with oceanic manta rays at Manta Point"
        ],
        "activities": [
            "Island-hopping liveaboard luxury yacht cruise through Komodo",
            "Trekking with rangers to track Komodo dragons on Rinca Island",
            "Scuba diving world-class current dives in Raja Ampat",
            "Snorkeling in crystal-clear lagoons of Misool",
            "Watching thousands of flying foxes take flight at Kalong Island sunset"
        ],
        "bestTimeToVisit": "May to October offers calm seas and clear skies for Komodo; October to April brings ideal diving conditions in Raja Ampat.",
        "quickFacts": {
            "bestTime": "Komodo: May – Oct | Raja Ampat: Oct – Apr",
            "idealDuration": "5 – 8 Days",
            "language": "Indonesian, English in tourism",
            "currency": "Indonesian Rupiah (IDR)",
            "visa": "Visa on arrival available",
            "climate": "Tropical maritime (28-32°C year-round)"
        },
        "accommodations": [
            {"name": "AYANA Komodo Waecicu Beach", "tier": "5-Star Luxury Resort", "location": "Labuan Bajo", "description": "Waterfront resort featuring private pier, glass-bottom phinisi boat, and ocean-facing suites."},
            {"name": "Misool Eco Resort", "tier": "Private Island Conservation", "location": "Raja Ampat", "description": "Exclusive private island dive resort inside a 300,000-acre marine protected reserve."}
        ],
        "packageIds": [],
        "relatedSlugs": ["bali", "thailand", "australia", "maldives"],
        "faqs": [
            {
                "q": "Are Komodo dragons dangerous?",
                "a": "Komodo dragons are powerful predators, which is why all treks are strictly conducted under the escort of experienced national park rangers carrying traditional wooden forked poles."
            }
        ]
    },

    # =========================================================================
    # EUROPE (6 Destinations)
    # =========================================================================
    {
        "id": "france",
        "slug": "france",
        "name": "France (Paris & French Riviera)",
        "country": "France",
        "region": "Europe",
        "regions": ["Europe"],
        "categories": ["City Breaks", "Luxury Getaways", "Cultural Experiences", "Honeymoon Destinations"],
        "tagline": "City of Light, Haute Couture & Côte d'Azur Glamour",
        "shortDescription": "Gaze at the sparkling Eiffel Tower, admire masterpieces in the Louvre, and cruise the glamorous blue waters of the French Riviera.",
        "overview": (
            "France represents the pinnacle of art, culture, gastronomy, and romantic elegance. "
            "Paris, the timeless 'City of Light', enchants with architectural landmarks like the Eiffel Tower, "
            "Notre-Dame Cathedral, the Louvre Museum, and tree-lined boulevards bustling with sidewalk cafes.\n\n"
            "To the south lies the sun-drenched French Riviera (Côte d'Azur), where the sapphire Mediterranean Sea kisses "
            "glamorous coastal towns like Nice, Cannes, Saint-Tropez, and the cliffside principality of Monaco. "
            "Inland, Provence offers lavender fields, rolling vineyards, and Michelin-starred culinary excellence."
        ),
        "heroImage": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=1000&q=80", "caption": "The Eiffel Tower viewed across the Seine River in Paris"},
            {"url": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=1000&q=80", "caption": "Pastel harbor and luxury yachts in Nice on the French Riviera"}
        ],
        "coordinates": [48.8566, 2.3522],
        "highlights": [
            "Eiffel Tower sparkling light show and summit observation views",
            "The Louvre Museum — home to the Mona Lisa and Venus de Milo",
            "Palace of Versailles magnificent Hall of Mirrors and royal fountains",
            "French Riviera glamour across Nice, Cannes, Saint-Tropez, and Monaco",
            "World-leading Michelin-starred fine dining and Champagne tasting"
        ],
        "activities": [
            "Private evening Seine River champagne cruise past illuminated monuments",
            "Guided VIP art tour through the Louvre and Musée d'Orsay",
            "High fashion shopping along Avenue Montaigne and Champs-Élysées",
            "Coastal yacht cruise along the capes of the French Riviera",
            "Day trip to the lavender fields and medieval villages of Provence"
        ],
        "bestTimeToVisit": "April to October offers warm, sunny weather for sidewalk cafes, garden strolls, and Riviera beach clubs.",
        "quickFacts": {
            "bestTime": "Apr – Oct",
            "idealDuration": "5 – 8 Days",
            "language": "French, English widely spoken in hotels",
            "currency": "Euro (€)",
            "visa": "Schengen Visa required for non-exempt visitors",
            "climate": "Temperate (Paris 18-25°C summer; Riviera 26-30°C sunny)"
        },
        "accommodations": [
            {"name": "Hôtel de Crillon (Rosewood)", "tier": "Palace Hotel", "location": "Place de la Concorde Paris", "description": "18th-century French architectural palace offering the epitome of Parisian luxury."},
            {"name": "Grand-Hôtel du Cap-Ferrat (Four Seasons)", "tier": "Iconic Riviera Luxury", "location": "Saint-Jean-Cap-Ferrat", "description": "Legendary Mediterranean palace set in 17 acres of gardens overlooking the sea."}
        ],
        "packageIds": [],
        "relatedSlugs": ["italy", "switzerland", "united-kingdom", "greece"],
        "faqs": [
            {
                "q": "How do you travel between Paris and the French Riviera?",
                "a": "The modern TGV high-speed train whisks travelers from central Paris to Nice in just 5.5 hours, or a quick 1-hour domestic flight."
            }
        ]
    },
    {
        "id": "italy",
        "slug": "italy",
        "name": "Italy (Rome, Florence & Amalfi Coast)",
        "country": "Italy",
        "region": "Europe",
        "regions": ["Europe"],
        "categories": ["Cultural Experiences", "Honeymoon Destinations", "Luxury Getaways", "City Breaks"],
        "tagline": "Colosseum, Renaissance Treasures & Cliffside Amalfi Glamour",
        "shortDescription": "Step inside Rome's ancient Colosseum, gaze at Michelangelo's David in Florence, and cruise pastel cliffs along the breathtaking Amalfi Coast.",
        "overview": (
            "Italy is a living open-air museum where thousands of years of art, architectural genius, and culinary passion "
            "interweave into the world's most romantic destination. In Rome, the ancient heart of the Roman Empire, "
            "monuments like the Colosseum, the Pantheon, and the Vatican's Sistine Chapel awe millions of visitors.\n\n"
            "In Florence, the birthplace of the Renaissance, masterpieces by Michelangelo and Botticelli fill world-class galleries "
            "set amidst the rolling vineyards of Tuscany. Along the southern Sorrentine Peninsula, the pastel-colored fishing villages "
            "of the Amalfi Coast—Positano, Amalfi, and Ravello—cling dramatically to towering cliffs plunging into azure Mediterranean waters."
        ),
        "heroImage": "https://images.unsplash.com/photo-1529260830199-42c24126f198?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1529260830199-42c24126f198?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1529260830199-42c24126f198?auto=format&fit=crop&w=1000&q=80", "caption": "The ancient Roman Colosseum illuminated at twilight"},
            {"url": "https://images.unsplash.com/photo-1533105079780-92b9be482077?auto=format&fit=crop&w=1000&q=80", "caption": "Pastel cliffside villas cascading into the sea in Positano Amalfi"}
        ],
        "coordinates": [41.9028, 12.4964],
        "highlights": [
            "The Colosseum, Roman Forum, and Vatican Museums (Sistine Chapel) in Rome",
            "Florence Duomo, Uffizi Gallery, and Michelangelo's David",
            "Amalfi Coast clifftop pastel villages of Positano, Amalfi, and Ravello",
            "Tuscan wine estates in Chianti producing Chianti Classico and Brunello",
            "Private wooden gozzo boat cruises around the Isle of Capri"
        ],
        "activities": [
            "Skip-the-line VIP tour of the Colosseum and Vatican City",
            "Private wine tasting and truffle hunting in the Tuscan hills",
            "Cruising the Amalfi Coast by private Riva speedboat with stop at Capri Blue Grotto",
            "Handmade pasta and gelato culinary workshop with an Italian chef",
            "Gondola ride through the secret canals of Venice"
        ],
        "bestTimeToVisit": "April to June and September to October offer sunny, pleasant weather and fewer crowds than midsummer.",
        "quickFacts": {
            "bestTime": "Apr – Jun & Sep – Oct",
            "idealDuration": "7 – 12 Days",
            "language": "Italian, English in tourism",
            "currency": "Euro (€)",
            "visa": "Schengen Visa required for non-exempt visitors",
            "climate": "Mediterranean climate (warm dry summers 26-32°C, mild winters)"
        },
        "accommodations": [
            {"name": "Le Sirenuse", "tier": "Iconic Clifftop Luxury", "location": "Positano Amalfi Coast", "description": "Legendary cliffside boutique hotel with sweeping views over Positano bay and champagne bar."},
            {"name": "Hotel de Russie (Rocco Forte)", "tier": "5-Star Luxury", "location": "Piazza del Popolo Rome", "description": "Historic luxury near the Spanish Steps featuring a secret terraced garden."}
        ],
        "packageIds": [],
        "relatedSlugs": ["france", "greece", "spain", "switzerland"],
        "faqs": [
            {
                "q": "How do you travel between cities in Italy?",
                "a": "Italy's high-speed rail network (Frecciarossa and Italo) connects Rome to Florence in just 1 hour 15 minutes, and Florence to Venice in 2 hours."
            }
        ]
    },
    {
        "id": "switzerland",
        "slug": "switzerland",
        "name": "Switzerland & the Swiss Alps",
        "country": "Switzerland",
        "region": "Europe",
        "regions": ["Europe"],
        "categories": ["Mountain Adventures", "Luxury Getaways", "Adventure Travel", "Family Holidays"],
        "tagline": "The Matterhorn, Glacier Express & Alpine Luxury",
        "shortDescription": "Ride panoramic glass trains through dramatic alpine valleys, admire the pyramid peak of the Matterhorn, and sail crystal lakes.",
        "overview": (
            "Switzerland is a pristine alpine wonderland of soaring snow-draped peaks, turquoise glacial lakes, "
            "and storybook villages. Synonymous with precision, luxury, and unmatched natural beauty, Switzerland offers "
            "travelers Europe's finest mountain experiences.\n\n"
            "In Zermatt, the iconic pyramid peak of the Matterhorn towers above a car-free alpine village. "
            "The world-famous Glacier Express panoramic train weaves through deep mountain gorges and across soaring stone viaducts, "
            "connecting Zermatt with glamorous St. Moritz. Across the lakes of Geneva, Lucerne, and Zurich, travelers enjoy "
            "lakeside castle cruises, world-class watchmaking ateliers, and artisanal chocolate houses."
        ),
        "heroImage": "https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99?auto=format&fit=crop&w=1000&q=80", "caption": "The iconic pyramid peak of the Matterhorn reflected in alpine lake"},
            {"url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1000&q=80", "caption": "Glacier Express train crossing stone viaduct in Swiss Alps"}
        ],
        "coordinates": [46.8182, 8.2275],
        "highlights": [
            "The iconic Matterhorn (4,478m) in the car-free mountain village of Zermatt",
            "Glacier Express 'World's Slowest Express Train' panoramic journey",
            "Jungfraujoch — 'Top of Europe' railway station at 3,454m altitude",
            "Steamboat cruises across crystal-clear Lake Lucerne and Lake Geneva",
            "Swiss artisan chocolate tasting and luxury Swiss horology ateliers"
        ],
        "activities": [
            "Riding the Gornergrat cogwheel train for Matterhorn viewpoints",
            "Panoramic train journeys aboard the Glacier Express and Bernina Express",
            "Alpine skiing and snowboarding in Zermatt and St. Moritz",
            "Hiking flower-filled alpine trails with cowbell melodies",
            "Thermal spa soaking in alpine mineral waters overlooking snow peaks"
        ],
        "bestTimeToVisit": "June to September for summer alpine hiking and lake cruises; December to March for world-class winter skiing.",
        "quickFacts": {
            "bestTime": "Jun – Sep (Hiking) | Dec – Mar (Ski)",
            "idealDuration": "5 – 8 Days",
            "language": "German, French, Italian, English widely spoken",
            "currency": "Swiss Franc (CHF)",
            "visa": "Schengen Visa required for non-exempt visitors",
            "climate": "Alpine temperate (summer 18-24°C, winter snow -5°C to 5°C)"
        },
        "accommodations": [
            {"name": "The Chedi Andermatt", "tier": "5-Star Alpine Luxury", "location": "Swiss Alps", "description": "Harmonious blend of Alpine chic and Asian zen featuring a 2,400 sq m wellness spa."},
            {"name": "Badrutt's Palace Hotel", "tier": "Historic Legend", "location": "St. Moritz", "description": "The cradle of winter tourism since 1896, host to European royalty and celebrities."}
        ],
        "packageIds": [],
        "relatedSlugs": ["france", "italy", "canada", "new-zealand"],
        "faqs": [
            {
                "q": "How does public transportation work in Switzerland?",
                "a": "The Swiss Travel Pass provides seamless, unlimited travel on all Swiss trains, panoramic alpine railways, lake steamboats, buses, and city trams across the country with legendary punctuality."
            }
        ]
    },
    {
        "id": "greece",
        "slug": "greece",
        "name": "Greece (Santorini & Athens)",
        "country": "Greece",
        "region": "Europe",
        "regions": ["Europe"],
        "categories": ["Beach Escapes", "Honeymoon Destinations", "Cultural Experiences", "Luxury Getaways"],
        "tagline": "Whitewashed Calderas, Blue Domes & the Acropolis",
        "shortDescription": "Gaze over Santorini's famous volcanic caldera, watch golden sunsets from whitewashed Oia cliff villas, and explore the ancient Acropolis in Athens.",
        "overview": (
            "Greece is the sun-kissed cradle of Western philosophy, democracy, and classical mythology. "
            "In Athens, the ancient Parthenon stands majestically atop the Acropolis, surveying three thousand years of history "
            "above modern open-air tavernas.\n\n"
            "Across the sparkling Aegean Sea lie the Cyclades islands, crowned by the world-famous volcanic island of Santorini. "
            "Here, dazzling white cubic villas and blue-domed churches cling to sheer 300-meter cliffs overlooking a submerged volcanic caldera. "
            "Santorini's sunsets from Oia, private catamaran cruises, volcanic vineyards, and luxury cave pool suites make it the world's "
            "most iconic romantic island escape."
        ),
        "heroImage": "https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?auto=format&fit=crop&w=1000&q=80", "caption": "Whitewashed blue-domed churches overlooking the Santorini caldera"},
            {"url": "https://images.unsplash.com/photo-1529260830199-42c24126f198?auto=format&fit=crop&w=1000&q=80", "caption": "The Parthenon temple atop the Acropolis in Athens"}
        ],
        "coordinates": [36.3932, 25.4615],
        "highlights": [
            "Santorini breathtaking volcanic caldera views and world-famous Oia sunsets",
            "The Acropolis of Athens and world-class Acropolis Museum",
            "Private luxury catamaran sunset cruises around the volcanic hot springs",
            "Volcanic wine tasting Assyrtiko grapes in ancient cliffside wineries",
            "Red Beach, White Beach, and black volcanic sand shores"
        ],
        "activities": [
            "Private sunset catamaran cruise around the caldera with Greek barbecue",
            "Exploring the Acropolis and ancient Plaka neighborhood with an archaeologist",
            "Wine tasting at volcanic vineyards overlooking the Aegean",
            "Hiking the scenic cliffside trail between Fira and Oia",
            "Dining at cliffside seafood tavernas with views of the caldera lights"
        ],
        "bestTimeToVisit": "May to October offers warm, dry Mediterranean sunshine, calm seas for sailing, and vibrant island life.",
        "quickFacts": {
            "bestTime": "May – Oct",
            "idealDuration": "5 – 8 Days",
            "language": "Greek, English widely spoken",
            "currency": "Euro (€)",
            "visa": "Schengen Visa required for non-exempt visitors",
            "climate": "Mediterranean sunny (25-32°C summer)"
        },
        "accommodations": [
            {"name": "Canaves Oia Suites", "tier": "Ultra-Luxury Cliffside", "location": "Oia Santorini", "description": "Carved into the volcanic cliffside with private plunge pools overlooking the caldera."},
            {"name": "Hotel Grande Bretagne", "tier": "5-Star Historic Luxury", "location": "Syntagma Square Athens", "description": "Historic landmark hotel with rooftop restaurant directly facing the illuminated Acropolis."}
        ],
        "packageIds": [],
        "relatedSlugs": ["italy", "france", "spain", "egypt"],
        "faqs": [
            {
                "q": "How do you travel from Athens to Santorini?",
                "a": "You can take a quick 45-minute flight from Athens Airport directly to Santorini, or enjoy a scenic 4.5-hour high-speed ferry across the Aegean Sea."
            }
        ]
    },
    {
        "id": "spain",
        "slug": "spain",
        "name": "Spain (Barcelona, Madrid & Costa del Sol)",
        "country": "Spain",
        "region": "Europe",
        "regions": ["Europe"],
        "categories": ["Cultural Experiences", "City Breaks", "Beach Escapes", "Family Holidays"],
        "tagline": "Gaudí Masterpieces, Flamenco Passions & Tapas Trails",
        "shortDescription": "Admire the soaring Sagrada Família in Barcelona, explore royal palaces in Madrid, and soak in sunshine on the Costa del Sol.",
        "overview": (
            "Spain is a vibrant, passionate country overflowing with artistic genius, sun-drenched beaches, "
            "and a zest for life celebrated around communal tables of tapas and wine. "
            "In Barcelona, the capital of Catalonia, the visionary modernist architecture of Antoni Gaudí—including the breathtaking "
            "Sagrada Família and whimsical Park Güell—creates an open-air wonderland alongside Mediterranean beaches.\n\n"
            "Madrid, Spain's stately capital, boasts the golden triangle of art museums (El Prado, Reina Sofía, Thyssen), "
            "majestic royal palaces, and vibrant tapas bars in La Latina. To the south, Andalusia enchants with the Moorish palace "
            "of the Alhambra in Granada, soul-stirring flamenco in Seville, and the golden beaches of Marbella on the Costa del Sol."
        ),
        "heroImage": "https://images.unsplash.com/photo-1583422409516-2895a77efded?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1583422409516-2895a77efded?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1583422409516-2895a77efded?auto=format&fit=crop&w=1000&q=80", "caption": "Antoni Gaudí's Sagrada Família soaring above Barcelona"},
            {"url": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=1000&q=80", "caption": "Royal Palace of Madrid and manicured gardens"}
        ],
        "coordinates": [41.3879, 2.1699],
        "highlights": [
            "Antoni Gaudí's Sagrada Família basilica and Park Güell in Barcelona",
            "The Prado Museum and Royal Palace in Madrid",
            "The Alhambra Moorish fortress palace in Granada",
            "Authentic Flamenco performances in intimate Andalusian tablaos",
            "Mediterranean beach luxury along the Costa del Sol and Marbella"
        ],
        "activities": [
            "Skip-the-line architectural tour of Gaudí's Sagrada Família",
            "Evening tapas and wine tasting tour through historic Gothic Quarter",
            "Attending an authentic Flamenco performance in Seville",
            "Day trip to historic Toledo or the wine region of La Rioja",
            "Beach relaxation and yachting on the Costa del Sol"
        ],
        "bestTimeToVisit": "April to June and September to October offer sunny, pleasant weather ideal for city sightseeing and beach relaxation.",
        "quickFacts": {
            "bestTime": "Apr – Jun & Sep – Oct",
            "idealDuration": "6 – 10 Days",
            "language": "Spanish, Catalan, English in hotels",
            "currency": "Euro (€)",
            "visa": "Schengen Visa required for non-exempt visitors",
            "climate": "Mediterranean (sunny warm summers 27-32°C, mild winters)"
        },
        "accommodations": [
            {"name": "Hotel Arts Barcelona", "tier": "5-Star Beachfront Luxury", "location": "Barcelona Beachfront", "description": "Overlooking the Mediterranean with panoramic suites, two-star Michelin dining, and infinity pool."},
            {"name": "Mandarin Oriental Ritz Madrid", "tier": "Belle Époque Palace", "location": "Retiro District", "description": "Iconic luxury palace originally opened by King Alfonso XIII in 1910."}
        ],
        "packageIds": [],
        "relatedSlugs": ["france", "italy", "morocco", "greece"],
        "faqs": [
            {
                "q": "What is the best way to travel between Madrid and Barcelona?",
                "a": "The modern AVE high-speed train connects Madrid and Barcelona in just 2.5 hours, running seamlessly from city center to city center."
            }
        ]
    },
    {
        "id": "united-kingdom",
        "slug": "united-kingdom",
        "name": "United Kingdom (London & Scottish Highlands)",
        "country": "United Kingdom",
        "region": "Europe",
        "regions": ["Europe"],
        "categories": ["City Breaks", "Cultural Experiences", "Mountain Adventures", "Family Holidays"],
        "tagline": "Royal Palaces, West End Shows & Dramatic Scottish Glens",
        "shortDescription": "Tour Buckingham Palace, watch West End theater, explore Edinburgh Castle, and drive through majestic glens in the Scottish Highlands.",
        "overview": (
            "The United Kingdom blends two millennia of royal heritage, world-defining literature, and cutting-edge culture "
            "with dramatic island wilderness. London, one of the world's great global capitals, dazzles with royal palaces "
            "(Buckingham Palace and the Tower of London), world-class free national museums, West End theaters, and Michelin-starred dining.\n\n"
            "To the north, Scotland enchants with the historic cobblestone Royal Mile and castle of Edinburgh, leading into the raw, "
            "mountainous beauty of the Scottish Highlands. Here, dramatic glens like Glen Coe, the mystical waters of Loch Ness, "
            "and single-malt whisky distilleries create an evocative journey through Celtic history and legend."
        ),
        "heroImage": "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?auto=format&fit=crop&w=1000&q=80", "caption": "Big Ben and the Houses of Parliament on the River Thames in London"},
            {"url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1000&q=80", "caption": "Dramatic mountain peaks and valley of Glen Coe in Scotland"}
        ],
        "coordinates": [51.5074, -0.1278],
        "highlights": [
            "Tower of London, Crown Jewels, and Changing of the Guard at Buckingham Palace",
            "World-famous West End musical and dramatic theater productions",
            "Edinburgh Castle perched atop an extinct volcanic crag",
            "Scenic Scottish Highlands, Isle of Skye, and Glenfinnan Viaduct steam train",
            "Traditional British Afternoon Tea at The Ritz or Claridge's"
        ],
        "activities": [
            "Private VIP tour of the Tower of London and Crown Jewels",
            "Attending an award-winning West End musical theater show",
            "Whisky tasting tour through historic Speyside and Islay distilleries",
            "Riding the Jacobite Steam Train ('Hogwarts Express') across the Highlands",
            "Day trip to historic Windsor Castle and the Roman baths of Bath"
        ],
        "bestTimeToVisit": "May to September offers long daylight hours (up to 17 hours of light in Scotland) and pleasant temperatures.",
        "quickFacts": {
            "bestTime": "May – Sep",
            "idealDuration": "6 – 10 Days",
            "language": "English",
            "currency": "British Pound Sterling (£ / GBP)",
            "visa": "UK Standard Visitor Visa required for non-exempt passports",
            "climate": "Temperate maritime (summer 18-24°C, mild variable weather)"
        },
        "accommodations": [
            {"name": "The Savoy London", "tier": "Historic Luxury Icon", "location": "The Strand London", "description": "Legendary Edwardian luxury hotel on the River Thames with world-famous American Bar."},
            {"name": "The Balmoral Hotel", "tier": "5-Star Landmark", "location": "Princes Street Edinburgh", "description": "Prestigious clocktower hotel at the gateway to Edinburgh's Old Town."}
        ],
        "packageIds": [],
        "relatedSlugs": ["france", "switzerland", "italy", "canada"],
        "faqs": [
            {
                "q": "How do you travel from London to Scotland?",
                "a": "You can take the scenic LNER high-speed train from London Kings Cross to Edinburgh in just 4.5 hours, or fly in 1 hour."
            }
        ]
    },

    # =========================================================================
    # AMERICAS (4 Destinations)
    # =========================================================================
    {
        "id": "united-states",
        "slug": "united-states",
        "name": "United States (National Parks & New York)",
        "country": "United States",
        "region": "Americas",
        "regions": ["Americas"],
        "categories": ["City Breaks", "Mountain Adventures", "Adventure Travel", "Family Holidays"],
        "tagline": "Manhattan Skylines, Grand Canyon Chasm & Geysers",
        "shortDescription": "Take in dazzling Broadway lights in New York City, gaze into the mile-deep Grand Canyon, and watch wildlife in Yellowstone.",
        "overview": (
            "The United States is a nation of staggering scale and dramatic geographical contrasts. "
            "New York City, the iconic financial and cultural capital, dazzles with the Manhattan skyline, Broadway theaters, "
            "Central Park, the Statue of Liberty, and diverse world-class gastronomy across five boroughs.\n\n"
            "Out west, America's National Parks preserve Earth's greatest natural spectacles: the mile-deep rock chasm of the Grand Canyon, "
            "Yellowstone's geothermal geysers and grizzly bear wilderness, and Yosemite's sheer granite monoliths like El Capitan. "
            "Whether cruising California's Pacific Coast Highway or exploring red rock canyons, the USA offers limitless epic journeys."
        ),
        "heroImage": "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?auto=format&fit=crop&w=1000&q=80", "caption": "Manhattan skyline and Central Park in New York City"},
            {"url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1000&q=80", "caption": "Vast carved canyon chasm of the Grand Canyon Arizona"}
        ],
        "coordinates": [40.7128, -74.0060],
        "highlights": [
            "New York City: Manhattan skyline, Broadway shows, Central Park & MET Museum",
            "Grand Canyon National Park — mile-deep natural wonder of the world",
            "Yellowstone National Park Old Faithful geyser and wild bison herds",
            "Yosemite Valley iconic granite monoliths (El Capitan & Half Dome)",
            "Pacific Coast Highway scenic California ocean drive"
        ],
        "activities": [
            "Helicopter flight over Manhattan skyline and the Grand Canyon",
            "Attending a hit Broadway musical in New York's Theater District",
            "Wildlife safari spotting grizzly bears and wolves in Yellowstone",
            "Hiking scenic trails in Yosemite or Zion National Park",
            "Fine dining at three-star Michelin restaurants in New York"
        ],
        "bestTimeToVisit": "May to October for National Parks; September to November (autumn) and spring for New York City.",
        "quickFacts": {
            "bestTime": "May – Oct (Parks) | Sep – Nov (NYC)",
            "idealDuration": "7 – 14 Days",
            "language": "English",
            "currency": "US Dollar (USD)",
            "visa": "US B1/B2 Tourist Visa or ESTA required",
            "climate": "Continental temperate across regions"
        },
        "accommodations": [
            {"name": "The Plaza New York", "tier": "Historic 5-Star Icon", "location": "Fifth Avenue NYC", "description": "The legendary castle on Central Park South, defining luxury hospitality for over a century."},
            {"name": "Amangiri", "tier": "Ultra-Luxury Desert Sanctuary", "location": "Canyon Point Utah", "description": "Architectural masterpiece blended seamlessly into the dramatic red rock desert landscape."}
        ],
        "packageIds": [],
        "relatedSlugs": ["canada", "brazil", "mexico", "united-kingdom"],
        "faqs": [
            {
                "q": "Can you combine New York City with Western National Parks?",
                "a": "Yes! A classic 10-12 day itinerary pairs 3-4 days in New York City with a direct domestic flight to Las Vegas or Salt Lake City to explore the Grand Canyon or Yellowstone."
            }
        ]
    },
    {
        "id": "canada",
        "slug": "canada",
        "name": "Canada & the Canadian Rockies",
        "country": "Canada",
        "region": "Americas",
        "regions": ["Americas"],
        "categories": ["Mountain Adventures", "Adventure Travel", "Family Holidays", "Luxury Getaways"],
        "tagline": "Glacial Turquoise Lakes, Jagged Peaks & Rocky Mountaineer",
        "shortDescription": "Admire emerald waters of Lake Louise and Moraine Lake, ride the luxury Rocky Mountaineer train, and spot grizzly bears in the Rockies.",
        "overview": (
            "Canada is a vast, pristine northern wilderness of breathtaking alpine majesty, friendly multicultural cities, "
            "and untouched nature. At its scenic pinnacle stand the Canadian Rocky Mountains in Alberta and British Columbia, "
            "encompassing Banff, Jasper, and Yoho National Parks.\n\n"
            "Here, glacial waters of Lake Louise and Moraine Lake glow an otherworldly turquoise blue, fed by melting glaciers "
            "and framed by towering snow-capped peaks. Aboard the world-famous Rocky Mountaineer glass-domed train, travelers enjoy "
            "gourmet dining while gliding through canyon rivers and mountain passes where grizzly bears, elk, and bighorn sheep roam free."
        ),
        "heroImage": "https://images.unsplash.com/photo-1503614472-8c93d56e92ce?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1503614472-8c93d56e92ce?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1503614472-8c93d56e92ce?auto=format&fit=crop&w=1000&q=80", "caption": "Glacial turquoise waters of Moraine Lake in Banff National Park"},
            {"url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1000&q=80", "caption": "Columbia Icefield and Athabasca Glacier in Jasper"}
        ],
        "coordinates": [51.1784, -115.5708],
        "highlights": [
            "Lake Louise & Moraine Lake — world's most photogenic turquoise glacial lakes",
            "Rocky Mountaineer luxury glass-domed train through the Rockies",
            "Icefields Parkway — rated one of the world's most spectacular scenic drives",
            "Walking onto the Athabasca Glacier aboard an all-terrain Ice Explorer",
            "Wildlife viewing for grizzly bears, black bears, moose, and elk"
        ],
        "activities": [
            "Canoeing across the turquoise waters of Lake Louise",
            "Luxury rail journey aboard the Rocky Mountaineer",
            "Walking the Columbia Icefield Skywalk glass-bottom observation deck",
            "Soaking in natural outdoor Banff Upper Hot Springs",
            "Helicopter flight over snow-capped Rocky Mountain peaks"
        ],
        "bestTimeToVisit": "Mid-June to mid-September for turquoise lake waters and hiking; December to March for world-class skiing at Whistler and Banff.",
        "quickFacts": {
            "bestTime": "Jun – Sep (Summer) | Dec – Mar (Ski)",
            "idealDuration": "6 – 10 Days",
            "language": "English, French",
            "currency": "Canadian Dollar (CAD)",
            "visa": "Canada eTA or Visitor Visa required",
            "climate": "Alpine temperate (pleasant summer 20-25°C, snowy winters)"
        },
        "accommodations": [
            {"name": "Fairmont Chateau Lake Louise", "tier": "5-Star Heritage Palace", "location": "Lake Louise Shore", "description": "Iconic luxury resort perched directly on the shores of Lake Louise facing Victoria Glacier."},
            {"name": "Fairmont Banff Springs", "tier": "Castle in the Rockies", "location": "Banff National Park", "description": "Magnificent Scottish baronial castle hotel nestled in pine forests beneath Mount Rundle."}
        ],
        "packageIds": [],
        "relatedSlugs": ["switzerland", "united-states", "new-zealand", "united-kingdom"],
        "faqs": [
            {
                "q": "Why are the lakes in the Canadian Rockies so turquoise?",
                "a": "The intense turquoise color is caused by 'rock flour'—extremely fine silt ground by glaciers that remains suspended in the water and reflects bright blue-green sunlight."
            }
        ]
    },
    {
        "id": "brazil",
        "slug": "brazil",
        "name": "Brazil (Rio de Janeiro & the Amazon)",
        "country": "Brazil",
        "region": "Americas",
        "regions": ["Americas"],
        "categories": ["Adventure Travel", "City Breaks", "Beach Escapes", "Cultural Experiences"],
        "tagline": "Christ the Redeemer, Copacabana & the Amazon Rainforest",
        "shortDescription": "Gaze over Rio from Christ the Redeemer, feel the thunder of Iguazu Falls, and cruise deep into the biodiversity of the Amazon basin.",
        "overview": (
            "Brazil is South America's colossal powerhouse of infectious joy, tropical nature, and vibrant cultural soul. "
            "Rio de Janeiro, the 'Cidade Maravilhosa' (Marvelous City), sits dramatically between green jungle mountains "
            "and golden Atlantic beaches, guarded by the open arms of the iconic Christ the Redeemer statue atop Corcovado.\n\n"
            "At the border with Argentina, the thunderous cascades of Iguazu Falls roar through subtropical rainforest with 275 separate waterfalls. "
            "Further north, the mighty Amazon River drains the world's largest rainforest, where luxury river cruise boats navigate tributaries "
            "teeming with pink river dolphins, jaguar tracks, and indigenous river communities."
        ),
        "heroImage": "https://images.unsplash.com/photo-1483729558449-99ef09a8c325?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1483729558449-99ef09a8c325?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1483729558449-99ef09a8c325?auto=format&fit=crop&w=1000&q=80", "caption": "Christ the Redeemer statue overlooking Rio de Janeiro and Sugarloaf"},
            {"url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1000&q=80", "caption": "Iguazu Falls roaring through lush subtropical rainforest"}
        ],
        "coordinates": [-22.9068, -43.1729],
        "highlights": [
            "Christ the Redeemer statue on Corcovado (New Wonder of the World)",
            "Sugarloaf Mountain cable car ride overlooking Guanabara Bay",
            "Copacabana and Ipanema world-famous golden beach culture",
            "Iguazu Falls — the world's most spectacular waterfall system",
            "Amazon Rainforest biodiversity expeditions and pink river dolphin spotting"
        ],
        "activities": [
            "Cogwheel train ride up Corcovado to Christ the Redeemer",
            "Speedboat safari directly beneath the roaring cascades of Iguazu Falls",
            "Piranha fishing and pink river dolphin swimming in the Amazon",
            "Samba dancing night tour in Rio's historic Lapa district",
            "Helicopter flight over Rio de Janeiro's beaches and peaks"
        ],
        "bestTimeToVisit": "December to March for summer beach vitality and Carnival; May to September for dry Amazon expeditions and cooler Rio touring.",
        "quickFacts": {
            "bestTime": "Dec – Mar (Beaches) | May – Sep (Amazon)",
            "idealDuration": "7 – 11 Days",
            "language": "Portuguese, English in luxury tourism",
            "currency": "Brazilian Real (BRL)",
            "visa": "eVisa / Visa-free depending on nationality",
            "climate": "Tropical and subtropical (25-33°C)"
        },
        "accommodations": [
            {"name": "Copacabana Palace (A Belmond Hotel)", "tier": "Iconic Art Deco Palace", "location": "Copacabana Beach Rio", "description": "Legendary beachfront hotel that has hosted royalty, rockstars, and film icons since 1923."},
            {"name": "Hotel das Cataratas (A Belmond Hotel)", "tier": "Exclusive Wonder", "location": "Inside Iguazu National Park", "description": "The only hotel inside the Brazilian national park, granting exclusive access to the falls after gates close."}
        ],
        "packageIds": [],
        "relatedSlugs": ["mexico", "united-states", "south-africa", "thailand"],
        "faqs": [
            {
                "q": "Is Iguazu Falls better viewed from Brazil or Argentina?",
                "a": "Both complement each other perfectly: Brazil offers the breathtaking panoramic wide-angle view, while Argentina lets you walk right across catwalks directly above the Devil's Throat."
            }
        ]
    },
    {
        "id": "mexico",
        "slug": "mexico",
        "name": "Mexico (Cancun, Riviera Maya & Oaxaca)",
        "country": "Mexico",
        "region": "Americas",
        "regions": ["Americas"],
        "categories": ["Beach Escapes", "Cultural Experiences", "Luxury Getaways", "Family Holidays"],
        "tagline": "Mayan Pyramids, Turquoise Cenotes & Caribbean Luxury",
        "shortDescription": "Discover Chichen Itza Mayan ruins, swim in crystal-clear jungle cenotes, relax on Riviera Maya beaches, and savor authentic Oaxacan cuisine.",
        "overview": (
            "Mexico is a vibrant land rich in Mesoamerican history, warm Caribbean waters, and UNESCO-recognized gastronomy. "
            "On the Yucatan Peninsula, the Riviera Maya borders the turquoise Caribbean Sea with powdery white beaches "
            "backed by lush jungles and secret underground freshwater cenotes.\n\n"
            "At Chichen Itza, the imposing Kukulkan pyramid stands as a New Wonder of the World, demonstrating astronomical genius "
            "engineered by the ancient Maya. Inland, the colonial city of Oaxaca enchants with cobblestone plazas, vibrant textile weavers, "
            "and world-celebrated culinary traditions featuring complex moles and artisanal mezcal."
        ),
        "heroImage": "https://images.unsplash.com/photo-1518638150340-f706e86654de?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1518638150340-f706e86654de?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1518638150340-f706e86654de?auto=format&fit=crop&w=1000&q=80", "caption": "Chichen Itza ancient Mayan Kukulkan pyramid"},
            {"url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1000&q=80", "caption": "Swimming in turquoise underground freshwater cenote"}
        ],
        "coordinates": [20.6296, -87.0739],
        "highlights": [
            "Chichen Itza UNESCO Mayan pyramid and archaeological wonder",
            "Swimming in crystal-clear freshwater jungle cenotes",
            "Tulum clifftop Mayan ruins overlooking Caribbean turquoise waters",
            "Luxury eco-resorts of Riviera Maya and tranquil Isla Holbox",
            "Oaxaca culinary capital tasting authentic moles and artisanal mezcals"
        ],
        "activities": [
            "Private morning tour of Chichen Itza before public crowds",
            "Snorkeling in underground cenote river caves with stalactites",
            "Private catamaran charter to Isla Mujeres with reef snorkeling",
            "Oaxaca culinary market tour and mezcal tasting",
            "Sea turtle swimming at Akumal Bay"
        ],
        "bestTimeToVisit": "December to April offers dry, sunny Caribbean weather with minimal rainfall and comfortable humidity.",
        "quickFacts": {
            "bestTime": "Dec – Apr",
            "idealDuration": "5 – 9 Days",
            "language": "Spanish, English widely spoken in resorts",
            "currency": "Mexican Peso (MXN) & USD widely accepted",
            "visa": "Visa-free for US, UK, Schengen, and Canadian visa holders",
            "climate": "Tropical Caribbean climate (26-31°C year-round)"
        },
        "accommodations": [
            {"name": "Rosewood Mayakoba", "tier": "5-Star Ultra-Luxury", "location": "Riviera Maya", "description": "Private lagoon villas accessed by electric boats with plunge pools and private butler service."},
            {"name": "Hotel Esencia", "tier": "Boutique Estate Luxury", "location": "Xpu-Ha Beach", "description": "Originally built as a private hideaway for an Italian duchess on a secluded white Caribbean beach."}
        ],
        "packageIds": [],
        "relatedSlugs": ["brazil", "united-states", "fiji", "maldives"],
        "faqs": [
            {
                "q": "What is a cenote in Mexico?",
                "a": "A cenote is a natural limestone sinkhole exposing groundwater, revered by the ancient Maya as sacred portals to the underworld and now offering crystal-clear swimming."
            }
        ]
    },

    # =========================================================================
    # AUSTRALIA & OCEANIA (3 Destinations)
    # =========================================================================
    {
        "id": "australia",
        "slug": "australia",
        "name": "Australia (Sydney & the Great Barrier Reef)",
        "country": "Australia",
        "region": "Australia and Oceania",
        "regions": ["Australia and Oceania"],
        "categories": ["Beach Escapes", "City Breaks", "Adventure Travel", "Wildlife Safaris"],
        "tagline": "Sydney Harbour, the Great Barrier Reef & Outback Uluru",
        "shortDescription": "Sail past the iconic Sydney Opera House, dive the world's largest living coral reef, and watch kangaroos and koalas in the wild.",
        "overview": (
            "Australia is a dynamic continent of sun-soaked coastal cities, ancient Indigenous heritage, and jaw-dropping natural wonders. "
            "Sydney, framed by its world-famous natural harbor, sparkles with the architectural sail roofs of the Sydney Opera House, "
            "the Harbour Bridge, and golden surf beaches like Bondi and Manly.\n\n"
            "Up in tropical Queensland, the UNESCO-listed Great Barrier Reef stretches over 2,300 kilometers—the largest living structure "
            "on Earth, visible from space and teeming with neon corals, sea turtles, and clownfish. Deep in the spiritual Red Centre Outback, "
            "the ancient sandstone monolith of Uluru (Ayers Rock) glows fiery red at sunset."
        ),
        "heroImage": "https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?auto=format&fit=crop&w=1000&q=80", "caption": "Sydney Opera House and Harbour Bridge at golden sunset"},
            {"url": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=1000&q=80", "caption": "Scuba diving among vibrant corals of the Great Barrier Reef"}
        ],
        "coordinates": [-33.8688, 151.2093],
        "highlights": [
            "Sydney Opera House and Sydney Harbour Bridge climb",
            "Great Barrier Reef world's largest coral reef diving and snorkeling",
            "Uluru (Ayers Rock) sacred monolith in the heart of the Red Centre",
            "Wildlife encounters with wild kangaroos, koalas, and quokkas",
            "Scenic helicopter flights over the iconic Heart Reef and Whitehaven Beach"
        ],
        "activities": [
            "Private yacht charter cruising Sydney Harbour",
            "Outer Great Barrier Reef catamaran luxury dive day trip",
            "Indigenous Anangu cultural storytelling tour at Uluru base",
            "Coastal walk from Bondi to Coogee along Sydney cliffs",
            "Helicopter flight over Whitehaven Beach pure silica sands"
        ],
        "bestTimeToVisit": "September to November and March to May for Sydney; June to October for dry sunny weather at the Great Barrier Reef.",
        "quickFacts": {
            "bestTime": "Sep – Nov & Mar – May",
            "idealDuration": "8 – 14 Days",
            "language": "English",
            "currency": "Australian Dollar (AUD)",
            "visa": "Australia eVisitor / ETA required online",
            "climate": "Temperate in South, Tropical in North, Arid in Outback"
        },
        "accommodations": [
            {"name": "Park Hyatt Sydney", "tier": "5-Star Waterfront Luxury", "location": "The Rocks Sydney", "description": "Unrivaled waterfront luxury with direct private balcony views of the Sydney Opera House."},
            {"name": "Qualia Resort", "tier": "Ultra-Luxury Island Resort", "location": "Hamilton Island Great Barrier Reef", "description": "World-class private pavilions nestled in tropical bushland on the doorstep of the reef."}
        ],
        "packageIds": [],
        "relatedSlugs": ["new-zealand", "fiji", "singapore", "indonesia"],
        "faqs": [
            {
                "q": "Can you see the Great Barrier Reef from Sydney?",
                "a": "No, the Great Barrier Reef is in Queensland (Cairns / Hamilton Island), a comfortable 3-hour domestic flight north of Sydney."
            }
        ]
    },
    {
        "id": "new-zealand",
        "slug": "new-zealand",
        "name": "New Zealand (Queenstown & South Island)",
        "country": "New Zealand",
        "region": "Australia and Oceania",
        "regions": ["Australia and Oceania"],
        "categories": ["Mountain Adventures", "Adventure Travel", "Honeymoon Destinations", "Luxury Getaways"],
        "tagline": "Milford Sound Fjords, Southern Alps & Adventure Capital",
        "shortDescription": "Cruise dramatic glacial fjords in Milford Sound, heli-hike ancient glaciers, and sip world-class Pinot Noir in Queenstown.",
        "overview": (
            "New Zealand (Aotearoa) is a pure, cinematic paradise of dramatic glacial fjords, towering snow-capped Southern Alps, "
            "and lush ancient beech forests. Located on the South Island, Queenstown is celebrated as the 'Adventure Capital of the World', "
            "perched beside the crystal waters of Lake Wakatipu beneath The Remarkables mountain range.\n\n"
            "A short scenic flight leads into Fiordland National Park to behold Milford Sound, described by Rudyard Kipling "
            "as the 'Eighth Wonder of the World', where waterfalls plunge thousands of feet directly into dark glacial waters. "
            "Travelers can heli-hike atop Fox and Franz Josef glaciers, tour Lord of the Rings film locations, and stay at world-class luxury lodges."
        ),
        "heroImage": "https://images.unsplash.com/photo-1507699622108-4be3abd695ad?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1507699622108-4be3abd695ad?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1507699622108-4be3abd695ad?auto=format&fit=crop&w=1000&q=80", "caption": "Mitre Peak rising dramatically out of Milford Sound fjord"},
            {"url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1000&q=80", "caption": "Queenstown waterfront beneath snow-capped Southern Alps"}
        ],
        "coordinates": [-45.0312, 168.6626],
        "highlights": [
            "Milford Sound & Doubtful Sound breathtaking glacial fjords",
            "Queenstown adventure capital & Central Otago Pinot Noir wineries",
            "Helicopter glacier landings on Franz Josef and Tasman Glaciers",
            "Scenic steamship cruise aboard the historic TSS Earnslaw on Lake Wakatipu",
            "Lord of the Rings epic cinematic landscape exploration"
        ],
        "activities": [
            "Scenic flight and luxury nature cruise in Milford Sound",
            "Helicopter flight with snow landing in the Southern Alps",
            "Boutique wine tasting tour through Gibbston Valley Pinot Noir vineyards",
            "Shotover River thrilling jet boat ride through narrow canyons",
            "Stargazing inside the Aoraki Mackenzie International Dark Sky Reserve"
        ],
        "bestTimeToVisit": "December to March (Southern Hemisphere summer) offers warm pleasant hiking weather, long daylight, and blooming lupins.",
        "quickFacts": {
            "bestTime": "Dec – Mar",
            "idealDuration": "7 – 12 Days",
            "language": "English, Māori",
            "currency": "New Zealand Dollar (NZD)",
            "visa": "NZeTA required online before departure",
            "climate": "Temperate maritime (pleasant summer 20-25°C, cool winters)"
        },
        "accommodations": [
            {"name": "Matakauri Lodge", "tier": "Ultra-Luxury Alpine Lodge", "location": "Lake Wakatipu Queenstown", "description": "Spectacular luxury suites with floor-to-ceiling glass windows facing The Remarkables peaks."},
            {"name": "Blanket Bay", "tier": "World-Class Wilderness Lodge", "location": "Glenorchy", "description": "Consistently voted among the world's best luxury lodges, nestled on the northern shores of Lake Wakatipu."}
        ],
        "packageIds": [],
        "relatedSlugs": ["australia", "switzerland", "canada", "fiji"],
        "faqs": [
            {
                "q": "How far is Milford Sound from Queenstown?",
                "a": "By road it takes 4 hours through scenic Fiordland, but we highly recommend a 40-minute scenic flight from Queenstown directly to Milford Sound airstrip over snow peaks and glaciers."
            }
        ]
    },
    {
        "id": "fiji",
        "slug": "fiji",
        "name": "Fiji Islands",
        "country": "Fiji",
        "region": "Australia and Oceania",
        "regions": ["Australia and Oceania"],
        "categories": ["Beach Escapes", "Honeymoon Destinations", "Luxury Getaways", "Family Holidays"],
        "tagline": "330 Tropical South Pacific Isles, Manta Rays & Warm 'Bula' Smiles",
        "shortDescription": "Unwind in luxury overwater bures, snorkel with manta rays in crystal lagoons, and experience authentic Fijian 'Bula' hospitality.",
        "overview": (
            "Fiji is the idyllic crown of the South Pacific, an archipelago of 330 tropical volcanic islands blessed with turquoise lagoons, "
            "swaying coconut palms, and world-famous soft coral reefs. Revered for having the friendliest people on Earth, "
            "the warm greeting of 'Bula!' welcomes travelers into an oasis of pure relaxation.\n\n"
            "From the luxurious private island resorts of the Mamanuca and Yasawa chains to lush rainforest waterfalls on Vanua Levu, "
            "Fiji offers supreme tropical pampering. Guests stay in traditional thatched beachfront 'bures', snorkel alongside gentle manta rays, "
            "participate in traditional kava welcoming ceremonies, and dine on fresh kokoda (marinated fish) beside torchlit beaches."
        ),
        "heroImage": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1000&q=80", "caption": "Traditional thatched beach bure in the Mamanuca Islands"},
            {"url": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=1000&q=80", "caption": "Manta ray swimming gracefully across soft coral garden"}
        ],
        "coordinates": [-17.7134, 178.0650],
        "highlights": [
            "Private island resorts with direct lagoon access and thatched luxury bures",
            "World-capital of soft coral scuba diving and snorkeling",
            "Swimming with gentle oceanic manta rays in the Yasawa Islands",
            "Traditional Fijian Kava ceremonies, meke dances, and lovo earth-oven banquets",
            "Cloudbreak — legendary world-class surfing reef break"
        ],
        "activities": [
            "Snorkeling and diving on the Great Astrolabe Reef",
            "Private boat charter to deserted sandspits for champagne picnics",
            "Participating in authentic village kava welcoming rituals",
            "Stand-up paddleboarding and sea kayaking across tranquil lagoons",
            "Luxury outdoor massages infused with coconut and frangipani oils"
        ],
        "bestTimeToVisit": "May to October brings the dry, sun-drenched winter season with low humidity, gentle trade winds, and calm turquoise waters.",
        "quickFacts": {
            "bestTime": "May – Oct",
            "idealDuration": "5 – 9 Days",
            "language": "English, Fijian",
            "currency": "Fijian Dollar (FJD)",
            "visa": "Visa-free entry for up to 4 months for most nationalities",
            "climate": "Warm tropical climate (26-30°C year-round)"
        },
        "accommodations": [
            {"name": "Kokomo Private Island Fiji", "tier": "Ultra-Luxury Private Island", "location": "Yaukuve Levu Island", "description": "Exclusive private island luxury with private infinity pool villas, organic farm, and direct reef access."},
            {"name": "Likuliku Lagoon Resort", "tier": "Adults-Only Luxury", "location": "Mamanuca Islands", "description": "Fiji's first and only resort with authentic traditional overwater bures suspended over coral reefs."}
        ],
        "packageIds": [],
        "relatedSlugs": ["australia", "new-zealand", "maldives", "seychelles"],
        "faqs": [
            {
                "q": "How do you get to Fiji's outer island resorts?",
                "a": "From Nadi International Airport on the main island of Viti Levu, transfers to outer resorts operate via scenic 15-minute helicopters, seaplanes, or comfortable high-speed South Sea Cruises catamarans."
            }
        ]
    },

    # =========================================================================
    # ANTARCTICA (1 Destination)
    # =========================================================================
    {
        "id": "antarctica",
        "slug": "antarctica",
        "name": "Antarctica - The White Continent",
        "country": "Antarctica",
        "region": "Antarctica",
        "regions": ["Antarctica"],
        "categories": ["Adventure Travel", "Wildlife Safaris", "Luxury Getaways"],
        "tagline": "The Earth's Final Frontier of Colossal Icebergs & Penguins",
        "shortDescription": "Voyage to the end of the Earth aboard luxury polar expedition vessels among tabular icebergs, breaching whales, and vast penguin colonies.",
        "overview": (
            "Antarctica is the Earth's final and most pristine frontier. A frozen wilderness of monumental scale and silence, "
            "the White Continent holds 90% of all the ice on the planet and remains untouched by commercial civilization. "
            "Traveling to Antarctica is a profound, transformative voyage into pure nature.\n\n"
            "Aboard modern, luxury polar expedition vessels with ice-strengthened hulls, travelers cruise past colossal sapphire-blue "
            "tabular icebergs, navigate the breathtaking Lemaire Channel, and step ashore in Zodiac boats into the midst of thousands "
            "of gentoo, chinstrap, and Adélie penguins. Breaching humpback whales, sleek leopard seals, and soaring albatrosses accompany "
            "this once-in-a-lifetime expedition."
        ),
        "heroImage": "https://images.unsplash.com/photo-1517411032315-54ef2cb783bb?auto=format&fit=crop&w=1600&q=85",
        "cardImage": "https://images.unsplash.com/photo-1517411032315-54ef2cb783bb?auto=format&fit=crop&w=800&q=80",
        "gallery": [
            {"url": "https://images.unsplash.com/photo-1517411032315-54ef2cb783bb?auto=format&fit=crop&w=1000&q=80", "caption": "Penguins gathered on ice floe beneath colossal Antarctic glacier"},
            {"url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1000&q=80", "caption": "Expedition Zodiac cruising past blue tabular icebergs in Antarctica"}
        ],
        "coordinates": [-65.0000, -64.0000],
        "highlights": [
            "Stepping onto the Seventh Continent — the world's most remote wilderness",
            "Encounters with hundreds of thousands of Gentoo, Chinstrap, and Adélie penguins",
            "Zodiac boat cruising through towering sapphire icebergs and sea arches",
            "Spectacular whale watching (Humpbacks, Minkes, and Orcas breaching beside ships)",
            "The daring Polar Plunge into freezing Antarctic waters (optional & thrilling)"
        ],
        "activities": [
            "Zodiac shore landings among penguin rookeries and seal colonies",
            "Sea kayaking in calm polar bays surrounded by floating brash ice",
            "Lectures by world-renowned polar marine biologists, geologists, and historians",
            "Snowshoeing on Antarctic glaciers",
            "The unforgettable Antarctic Polar Plunge"
        ],
        "bestTimeToVisit": "November to March (the Austral summer) brings 24 hours of daylight, melting pack ice, and active penguin nesting and whale arrivals.",
        "quickFacts": {
            "bestTime": "Nov – Mar (Austral Summer)",
            "idealDuration": "10 – 14 Days",
            "language": "English on expedition vessels",
            "currency": "USD on board vessels",
            "visa": "No visa needed for Antarctica, but transit visa for Argentina/Chile",
            "climate": "Polar summer (-2°C to +5°C on Antarctic Peninsula)"
        },
        "accommodations": [
            {"name": "Silversea Silver Endeavour", "tier": "Ultra-Luxury Polar Expedition", "location": "Antarctic Peninsula", "description": "PC6 ice-class luxury expedition ship with private butler service, Michelin gastronomy, and observation lounges."},
            {"name": "Ponant Le Commandant Charcot", "tier": "Luxury Hybrid Electric", "location": "Weddell & Ross Seas", "description": "High luxury polar exploration vessel equipped with scientific laboratories and indoor heated pool."}
        ],
        "packageIds": [],
        "relatedSlugs": ["new-zealand", "canada", "norway"],
        "faqs": [
            {
                "q": "How cold is Antarctica during tourist season?",
                "a": "During the Antarctic summer (Nov to Mar), temperatures along the Antarctic Peninsula are surprisingly mild, typically hovering around 0°C to +4°C—comparable to winter in New York or Paris."
            },
            {
                "q": "How do you get to Antarctica?",
                "a": "Most expeditions depart from Ushuaia, Argentina, sailing across the Drake Passage (approx. 48 hours), or you can take a 'fly-and-cruise' flight from Punta Arenas (Chile) directly to King George Island."
            }
        ]
    }
]

# Packages Database
PACKAGES = [
    {
        "id": "encore-hotel-nakuru-2d1n",
        "title": "2 Days 1 Night Luxury Getaway - The Encore Hotel Nakuru",
        "destinationId": "lake-nakuru",
        "duration": "2 Days / 1 Night",
        "price": "From Ksh 20,900 PPS",
        "badge": "Bestseller Package",
        "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=800&q=80",
        "url": "../../../index.html#overview",
        "description": "Escape to Nakuru for an unforgettable luxury getaway at The Encore Hotel with gourmet dining, deluxe rooms, and thrilling Lake Nakuru rhino and flamingo game drives."
    }
]
