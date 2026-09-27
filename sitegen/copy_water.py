"""Water damage restoration pages. County hub is in copy_hubs.py."""
from site_config import PHONE_DISPLAY, PHONE_TEL

from sitegen.render import a, callout, h2, h3, nearby_section, p, ul

def royal_oak():
    return "\n".join([
        h2("Water extraction in Royal Oak houses"),
        p(
            "Water damage restoration in Royal Oak begins with where the water entered. On the Woodward "
            "corridor, in Northwood, in Vinsetta, and in the blocks between downtown Main Street and the "
            "Detroit Zoo on West Ten Mile, the usual paths are a basement floor drain, a window well, a "
            "failed sump, or a supply line at the laundry. Extraction is the removal of standing water "
            "and the soaked layers you can already see. It is not the whole restoration."
        ),
        p(
            "A Royal Oak basement from before the 1960s often has a thin slab, a cove that was poured "
            "against clay-tile or cast-iron plumbing, and storage pushed against the walls. Extraction "
            "that stops at the open floor leaves the bottom of every box and the lower drywall wet. Ask "
            "the independent provider, before they start, how far up they will open walls. Oakland Sewer "
            "Pros does not extract water. Call "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " to be connected if a participating company can take the call."
        ),
        h2("Structural drying after the pump-out"),
        p(
            "Structural drying is the unglamorous middle of water damage repair. Air has to move across "
            "wet masonry and any wood that took on water, and someone has to recheck it on later days. "
            "Royal Oak owners sometimes expect a single afternoon because the floor looks dry by evening. "
            "The slab edge and the sill can still be wet. The provider should explain how they will "
            "measure that. This website will not tell you the job takes a fixed number of days."
        ),
        p(
            "If the loss is mostly a flooded basement from storm water or a sump, read "
            + a("/royal-oak-flooded-basement", "flooded basement cleanup and water removal in Royal Oak")
            + " beside this page. If a drain discharged sewage, drying alone is the wrong first step. "
            "Use " + a("/royal-oak-sewage-extraction", "sewage extraction")
            + " and " + a("/royal-oak-sewer-cleanup", "sewer backup cleanup") + "."
        ),
        h2("Sewage and other heavily contaminated water"),
        p(
            "The restoration trade calls sewage, and water that has mixed with it, Category 3 or black "
            "water. The label matters because porous materials that absorbed it are usually removed, not "
            "dried and kept. Royal Oak backups through floor drains fall in that group. A clean supply-line "
            "break does not, unless the water sat long enough to become foul. "
            + a("/royal-oak-basement-sanitization", "Sanitizing after the backup")
            + " is the residue step, done by the company you hire. We do not claim those companies hold "
            "any particular certificate. You ask them."
        ),
        h3("Basement flooding causes that show up in Royal Oak"),
        ul([
            "Older laterals under tree-lined streets near downtown, which root up and then surcharge into the basement in a storm.",
            "Window wells below grade on Woodward-side lots when the well cover is gone and the soil is already saturated.",
            "Sump failure. See " + a("/royal-oak-sump-pump-repair", "sump pump repair in Royal Oak") + ".",
            "Sections of the city built before storm and sanitary sewers were separated. "
            + a("https://www.romi.gov/384/Sewer-Division", "Royal Oak's Sewer Division")
            + " can speak to the public main. We cannot.",
        ]),
        h2("Insurance conversations we will not have for you"),
        p(
            "Water damage and sewer backup are often treated differently on a homeowners policy. A sudden "
            "pipe break and a sewer backup are not the same endorsement. Groundwater is frequently limited "
            "or excluded. Oakland Sewer Pros does not read your policy, file a claim, or bill an insurer. "
            "The provider you hire may photograph and record moisture. Ask them whether documentation is "
            "included. Ask your insurer what your form actually says. Do not rely on a contractor, or on "
            "this page, for a coverage opinion."
        ),
        p(
            "Parts of Royal Oak lie in the southern Oakland County drainage area associated with the "
            "Oakland County Water Resources Commissioner and the George W. Kuhn district, formerly the "
            "Twelve Towns Drain. That is background for how regional storm water is handled. It is not "
            "a finding about your lateral. Confirm anything you intend to put in a complaint or a claim."
        ),
        callout(
            "What to tell the provider on a Royal Oak water-damage call",
            ul([
                "Which room, and whether the floor drain or a supply line was the source.",
                "How high the water got on the wall, from a photo taken on the stairs.",
                "Whether the panel or the furnace is in the water.",
                "That you want a written scope and proof of license and insurance before work starts.",
            ]),
        ),
        p("The Royal Oak map of these services is " + a("/royal-oak", "the city page") + "."),
        nearby_section("water-damage-restoration", "Water damage restoration", "royal-oak"),
    ])


def troy():
    return "\n".join([
        h2("Water extraction in Troy lower levels"),
        p(
            "Water damage restoration in Troy is usually about a finished lower level. Split-levels along "
            "Big Beaver Road, houses in subdivisions such as Northfield Hills, and basements near the "
            "Coolidge and Rochester corridors often have carpeted rooms, not a bare cellar. Extraction "
            "means lifting that carpet, getting the pad out if it is saturated, and removing water from "
            "the gypsum behind the baseboard. Somerset Collection is the landmark people use for the Big "
            "Beaver and Coolidge corner. The wet rooms are in the subdivisions around it, not in the mall."
        ),
        p(
            "Call " + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " and Oakland Sewer Pros may connect you with an independent restoration provider. We do "
            "not bring air movers, we do not quote a Troy price, and we do not promise a crew the same day. "
            "Availability depends on the companies, the address, and how busy they are."
        ),
        h2("Structural drying where the basement is living space"),
        p(
            "Drying a Troy family room in the basement fails if the furniture stays on the wet floor and "
            "the doors stay closed. The provider should say what has to be moved and whether contents "
            "manipulation is in the price. Structural drying also includes the cavity behind the wall if "
            "the water climbed. A palm test on the paint is not a measurement. Ask what instrument they "
            "use and when they will come back."
        ),
        p(
            "Pair this page with "
            + a("/troy-flooded-basement", "flooded basement cleanup and basement water removal in Troy")
            + ". A sanitary backup is "
            + a("/troy-sewer-cleanup", "sewer backup cleanup")
            + " and " + a("/troy-sewage-extraction", "sewage extraction")
            + ". A pump that quit is " + a("/troy-sump-pump-repair", "sump pump repair") + "."
        ),
        h2("When Troy water is sewage"),
        p(
            "If a basement bath or floor drain overflowed, treat the loss as sewage, which restorers call "
            "Category 3 water. Carpet and pad in a finished Troy basement that sat in that water are "
            "typically discarded. Kids' furniture and cloth bins in the same room usually are too. "
            + a("/troy-basement-sanitization", "Sanitizing")
            + " comes after removal, not before. A clear sump overflow with no drain involvement is a "
            "different, often smaller, water damage repair. Do not let anyone dry sewage-soaked pad in place."
        ),
        h3("Basement flooding causes in Troy"),
        ul([
            "Sump pumps that lose power in a storm. DTE serves these neighborhoods. The outage and the flood are linked, and the pump may still need service after the lights return.",
            "Older clay or cast-iron laterals in 1950s and 1960s houses, especially where mature trees line the subdivision streets.",
            "Storm drainage along Big Beaver that the city's Streets and Drains Division maintains. Street water and a basement backup are not automatically the same pipe.",
            "High water around lower lots. People describe a high water table near parts of the Big Beaver corridor. Treat that as a local pattern to ask about, not as a survey of your parcel.",
        ]),
        h2("Insurance, without a coverage promise"),
        p(
            "Troy water losses get denied or reduced when the policy excludes sewer backup, excludes "
            "groundwater, or requires the water to be sudden. We will not predict your outcome. The "
            "provider can document moisture if you ask them to. You call the insurer. Parts of Troy are "
            "in the regional drainage area of the George W. Kuhn facility and the Oakland County Water "
            "Resources Commissioner. Cite that only after you confirm it applies to your question, and "
            "not as the cause of a private lateral failure."
        ),
        callout(
            "Troy call details that change the scope",
            ul([
                "Finished room or bare utility space.",
                "Carpet still down, or already pulled up.",
                "Whether anyone is living or sleeping on that level.",
                "Power status, and whether the sump is underwater.",
            ]),
        ),
        h2("Water damage repair after a Troy extraction"),
        p(
            "Water damage repair is the later half of the same loss: what stays, what comes out, and "
            "what gets rebuilt. In Troy that often means a carpeted family room in a split-level, a "
            "bedroom in the basement of a 1950s or 1960s house, or a utility corner that shares a wall "
            "with living space. Along the I-75 side of the city and near the Troy Historic Village, the "
            "lower level may still be the original unfinished room. Near Big Beaver and the subdivisions "
            "around Somerset Collection it is more often finished. The repair path is not the same. "
            "Unfinished concrete can be cleaned and dried. Carpet pad that sat in water usually cannot."
        ),
        p(
            "Ask the independent provider to separate extraction, drying, and any rebuild in writing. "
            "Oakland Sewer Pros will not schedule the rebuild, choose materials, or tell you the "
            "Somerset-area houses are a different risk class from Northfield Hills. Those are place "
            "names so you can describe the house. The company's written scope is what you hire. If the "
            "drains never backed up and the water came from a window well or a supply line, say so. "
            "Calling it a sewer backup when it was a burst hose changes both the cleanup and the "
            "conversation with your insurer. Start at "
            + a("/troy", "Troy services")
            + " if you need the sewer page instead."
        ),
        nearby_section("water-damage-restoration", "Water damage restoration", "troy"),
    ])


def birmingham():
    return "\n".join([
        h2("Water extraction in Birmingham's older houses"),
        p(
            "Water damage restoration in Birmingham runs into original materials. Around Shain Park and "
            "Old Woodward, in Poppleton Park, and in the Quarton Lake area, lower levels may be plaster "
            "over wood lath, with trim that was milled for that house. Extraction is still the first "
            "physical step: get the standing water out without grinding debris into the wood stair. How "
            "aggressively to open walls is the second step, and it should be slower here than in a house "
            "built with replaceable drywall."
        ),
        p(
            "The referral line is " + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + ". Oakland Sewer Pros is not a Birmingham restoration company. We do not station anyone "
            "downtown. A participating independent provider may take the call. You still compare their "
            "license, insurance, and written scope."
        ),
        h2("Structural drying of plaster and masonry"),
        p(
            "Plaster releases water slowly and stains when it stays damp. Structural drying in these "
            "houses is as much about time and rechecks as about the number of fans. A provider who wants "
            "to demolish every soft spot on hour one may be right, or they may be skipping a drying "
            "attempt you would rather try on intact trim. Ask them to mark what is definitely coming out "
            "and what they will test again. Water damage repair, in the sense of putting finishes back, "
            "is a later trade. This page is about the water and the damaged materials, not a remodeling bid."
        ),
        p(
            "Storm flooding and sump overflow sit on "
            + a("/birmingham-flooded-basement", "the flooded basement page")
            + ". Sewage is on " + a("/birmingham-sewer-cleanup", "sewer backup cleanup")
            + " and " + a("/birmingham-sewage-extraction", "sewage extraction")
            + ". Pumps are " + a("/birmingham-sump-pump-repair", "sump pump repair") + "."
        ),
        h2("Category 3 sewage in a finished Birmingham lower level"),
        p(
            "Sewage in a guest room or a lower-level office is Category 3 water. Upholstery, rugs, and "
            "the back of built-in shelving that wicked it up are not a cleaning problem. "
            + a("/birmingham-basement-sanitization", "Sanitization")
            + " after removal is part of the same hire, not a separate maid appointment. Low ground near "
            "Quarton can also push clear water in through the foundation. If you did not see a drain "
            "overflow and there is no sewage odor, say that. Mislabeling a seepage flood as sewage, or "
            "the reverse, sends the job down the wrong path."
        ),
        h3("Basement flooding causes in Birmingham"),
        ul([
            "Clay and cast-iron laterals under mature trees in the older sections.",
            "Window wells and stairwells on houses that sit slightly below the sidewalk grade.",
            "Yard drainage toward Quarton-area low spots during a multi-day rain.",
            "Failed sumps during outages. The electric utility is DTE. Restoring power does not repair a burned pump.",
        ]),
        h2("What we will not say about your insurance"),
        p(
            "We will not say that Birmingham water damage is covered. Many policies handle a sudden "
            "plumbing discharge differently from sewer backup and from groundwater seepage. Ask your "
            "insurer. Ask the provider whether their documentation is itemized. Do not expect this "
            "website to talk to the carrier. Portions of Birmingham are discussed in connection with "
            "southern Oakland County drainage and the George W. Kuhn district. Verify that with the "
            "Oakland County Water Resources Commissioner before you treat it as true for your street."
        ),
        callout(
            "Birmingham details to have ready",
            ul([
                "Plaster or drywall, if you know.",
                "Whether trim and built-ins got wet.",
                "The water line, photographed from a dry step.",
                "Any gurgling from drains, separate from water at the windows.",
            ]),
        ),
        h2("Water damage repair when the finishes are original"),
        p(
            "Along Maple and in the older blocks off Old Woodward, water damage repair is not a drywall "
            "swap. Baseboards may be one piece of milled trim. Plaster patches show. A lower-level room "
            "used as a study or a guest room near Shain Park holds books, upholstered chairs, and built-in "
            "shelving that a bare cellar does not. Extraction gets the water out. Repair is the decision "
            "about which of those pieces can be saved after they have been wet, and that decision belongs "
            "to you and the company you hire, on site."
        ),
        p(
            "A newer finished room in the same city, with standard drywall and replaceable carpet, can "
            "follow a faster demolition plan. Do not let a provider use one plan for both houses. "
            "Photograph the water line before anything is moved, especially on plaster, because the stain "
            "line is the record. Oakland Sewer Pros does not inspect Birmingham houses and does not "
            "recommend a contractor by name. The city index is "
            + a("/birmingham", "Birmingham services")
            + "."
        ),
        nearby_section("water-damage-restoration", "Water damage restoration", "birmingham"),
    ])


def berkley():
    return "\n".join([
        h2("Water extraction under Berkley bungalows"),
        p(
            "Water damage restoration in Berkley is shaped by a short basement and a first floor of "
            "original flooring. The city is a 1940s and 1950s bungalow grid, flat, in the Rouge River "
            "watershed, with shops along 12 Mile and traffic on Coolidge. Extraction has to remove water "
            "from the basement without tracking it onto the oak or maple at the top of a steep stair. "
            "Joist bays are close to that floor. Wet insulation in those bays is water damage to the "
            "house you live in, not only to the cellar."
        ),
        p(
            "Use " + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " to reach an independent provider through Oakland Sewer Pros. We are not the company with "
            "the truck. If nobody is available, the line cannot invent a crew."
        ),
        h2("Structural drying in a low basement"),
        p(
            "There is little headroom for equipment, and the stair limits what can be carried down. "
            "Structural drying still requires air at the wet surfaces and a later moisture check. A "
            "single dehumidifier in the middle of a cluttered bungalow basement dries the air and not "
            "the sill. Ask the provider what they will move. Water damage repair of the first-floor "
            "hardwood, if the subfloor swelled, is a different carpenter once the water is actually gone. "
            "Do not sand the floor while the basement is still wet."
        ),
        p(
            "See " + a("/berkley-flooded-basement", "flooded basement cleanup in Berkley")
            + " for water removal, "
            + a("/berkley-sewer-cleanup", "sewer backup cleanup")
            + " and " + a("/berkley-sewage-extraction", "sewage extraction")
            + " if the drains were involved, and "
            + a("/berkley-sump-pump-repair", "sump pump repair")
            + " if the pit overflowed."
        ),
        h2("Sewage in a house this small"),
        p(
            "Category 3 sewage in a Berkley basement does not stay downstairs. The stair, the door, and "
            "any return-air opening connect the rooms. Porous material comes out. Then someone sanitizes "
            "what remains. That sequence is "
            + a("/berkley-basement-sanitization", "basement sanitization after the backup")
            + ". Older sections of Berkley have been described as combined storm and sanitary sewers, "
            "which can put sewage in the basement during rain. The city can confirm your street. Until "
            "you know, do not treat a storm flood that smells like a drain as clean rainwater."
        ),
        h3("Basement flooding causes in Berkley"),
        ul([
            "Window wells and side-door stairwells on a flat lot with nowhere for rain to sheet away.",
            "Sump overload or a dead pump when the power drops.",
            "Clay laterals from the original build, rooted at the joints.",
            "Downspouts that discharge at the foundation because the side yard is only a few feet wide.",
        ]),
        h2("Insurance is your policy, not our script"),
        p(
            "We do not know whether a Berkley bungalow's policy includes sewer backup, sudden discharge, "
            "or groundwater. Homeowners should ask the insurer directly. A provider's photos are not a "
            "claim. The George W. Kuhn drainage district and the Oakland County Water Resources "
            "Commissioner are part of the regional system for this part of the county. They are not a "
            "substitute for reading your declaration page."
        ),
        callout(
            "Berkley facts that change the drying plan",
            ul([
                "Height of the basement and width of the stair.",
                "Whether the first floor is original hardwood.",
                "Whether the furnace return is in the wet room.",
                "How many hours the water stood.",
            ]),
        ),
        h2("Water damage repair above a Berkley basement"),
        p(
            "The rooms people live in are one short stair above the water. On the residential blocks off "
            "12 Mile Road and Coolidge, a bungalow's oak or maple floor sits on joists that can take on "
            "moisture from below even when the first floor never had standing water. Water damage repair "
            "here sometimes starts with cupped flooring days after the basement looks dry. Mention the "
            "first-floor material when you call. A provider who only plans for the cellar will miss it."
        ),
        p(
            "Laundry hookups in these original basements are a common clean-water source: a hose, a "
            "washer pan that was never there, a supply line at the back wall. That loss is still water "
            "damage, and it is not a sewer backup. Keep the two descriptions separate so the extraction "
            "and the insurer conversation match the house. The flat lots do not shed a heavy rain the "
            "way a sloped yard would, which is why window wells and side stairs show up in the same "
            "storm as a laundry leak. Every Berkley link is on "
            + a("/berkley", "the city overview")
            + "."
        ),
        nearby_section("water-damage-restoration", "Water damage restoration", "berkley"),
    ])


def clawson():
    return "\n".join([
        h2("Water extraction on Clawson's compact lots"),
        p(
            "Water damage restoration in Clawson starts with access. Brick bungalows from the 1930s to "
            "the 1950s sit on small lots along 14 Mile Road and the blocks between Royal Oak and Troy. "
            "The basement is often one room. Extraction equipment, wet debris, and the family's cars "
            "are competing for a short driveway. A provider who has not heard that description may show "
            "up with a plan that does not fit. Tell them on the call."
        ),
        p(
            "Oakland Sewer Pros connects the call at "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " when an independent provider is participating. We do not extract water, dry buildings, "
            "or publish a Clawson price."
        ),
        h2("Structural drying next to the furnace"),
        p(
            "In a one-room basement the furnace and water heater are in the drying zone. Structural "
            "drying cannot ignore them. If water reached the burners or the controls, the provider and "
            "a heating contractor, not this website, decide whether the unit runs. Water damage repair "
            "of finishes comes after the structure is actually dry. Painting a stained brick-bungalow "
            "stair while the stringer is wet just seals the damage in."
        ),
        p(
            "Water removal details are on "
            + a("/clawson-flooded-basement", "flooded basement cleanup in Clawson")
            + ". Sewage paths are "
            + a("/clawson-sewer-cleanup", "sewer backup cleanup")
            + " and " + a("/clawson-sewage-extraction", "sewage extraction")
            + ". The pump is " + a("/clawson-sump-pump-repair", "sump pump repair") + "."
        ),
        h2("Sewage, Category 3, and a shared basement room"),
        p(
            "A floor-drain backup in that single room contaminates the mechanical equipment and the "
            "storage together. Restorers treat sewage as Category 3 water. Soft goods come out. Metal "
            "cabinets may be cleaned. The crock, if sewage entered it, is not clean because the floor "
            "was mopped. "
            + a("/clawson-basement-sanitization", "Sanitizing after the Clawson backup")
            + " belongs in the same scope as the extraction. A rain flood through a low window, with "
            "quiet drains and no odor, is a smaller and different water damage job. Describe which one you have."
        ),
        h3("Basement flooding causes in Clawson"),
        ul([
            "Downspouts discharging against the foundation on a lot with almost no side yard.",
            "Original clay or cast-iron laterals narrowed by roots and corrosion.",
            "Sump or power failure during a storm, with the pit in the same room as the furnace.",
            "Load on older sanitary lines in heavy regional rain. The city can discuss the main. The George W. Kuhn district is the regional drainage context for Clawson; confirm details with Oakland County before you rely on them.",
        ]),
        h2("No coverage opinion from this site"),
        p(
            "Ask your insurer whether sewer backup, sudden discharge, or groundwater is on your Clawson "
            "policy. We will not estimate what they will pay, and we will not bill them. A written scope "
            "from the provider is what you compare to that conversation. License and insurance for the "
            "work are documents you get from the provider, not from Oakland Sewer Pros."
        ),
        callout(
            "Say this when you call about Clawson water damage",
            ul([
                "Driveway length and whether the street is the only staging area.",
                "Whether the furnace sits in the water.",
                "Drain backup, window leak, or both.",
                "That you want license, insurance, and a written scope before demolition.",
            ]),
        ),
        h2("Water damage repair in a one-room Clawson basement"),
        p(
            "Clawson is not a finished Troy lower level and it is not a wide Royal Oak cellar. The "
            "typical loss is one room under a brick bungalow, with the furnace, the water heater, stored "
            "boxes, and sometimes the only sump all sharing the floor. Water damage repair means deciding "
            "what among those contents is porous and done, and whether the mechanical equipment can be "
            "put back in service. That decision is the heating contractor's and the restoration "
            "provider's. This website will not clear a furnace to run."
        ),
        p(
            "Staging is the other Clawson constraint. Downtown 14 Mile is a short commercial strip; the "
            "houses behind it have short drives. Wet carpet and drywall cannot sit in the street. Ask "
            "where debris will go before work starts. If the water came up the floor drain, treat it as "
            "sewage until someone who is on site says otherwise. If it came through a low window during "
            "rain and the drains stayed quiet, say that too. The hub for this city is "
            + a("/clawson", "Clawson services")
            + "."
        ),
        nearby_section("water-damage-restoration", "Water damage restoration", "clawson"),
    ])


ARTICLES = {
    "royal-oak": royal_oak,
    "troy": troy,
    "birmingham": birmingham,
    "berkley": berkley,
    "clawson": clawson,
}

FAQS = {
    "royal-oak": [
        ("What does water damage restoration include in Royal Oak?", "Extraction of standing water, removal of materials that cannot be saved, drying of what remains, and, if the water was sewage, sanitizing. The provider writes the actual scope. This site does not."),
        ("Is water damage repair the same phrase?", "People use water damage repair for the same loss, especially once finishes have to be replaced. Drying comes before rebuild. We do not perform either one."),
        ("Does Royal Oak water damage restoration cover sewage backups?", "The referral line can connect you with a provider for sewage water damage as well as cleaner floods. Say which one you have. Sewage is a stricter cleanup."),
    ],
    "troy": [
        ("Why is Troy water damage restoration often a finished-basement job?", "Many Troy lower levels are carpeted living space in split-levels and subdivisions. The pad and drywall hold more water than an empty utility cellar."),
        ("Will you send a dryer to a house near Somerset or Northfield Hills?", "No. We do not send equipment. An independent provider may be available. Neighborhood names do not create a guaranteed response."),
        ("How is basement flooding different from water damage?", "Flooding is water in the room. Water damage is the lasting effect on materials. Both pages exist so you can start with the one that matches what you see."),
    ],
    "birmingham": [
        ("Can water damage restoration save Birmingham plaster?", "Sometimes, if the wetting is shallow and someone monitors drying. Deeply soaked plaster and sewage-soaked trim often have to come out. The provider decides on site."),
        ("Do you restore the finishes yourselves?", "No. Oakland Sewer Pros is a referral service. Rebuild work, if you want it, is a separate agreement with a company you hire."),
        ("Are Quarton floods covered by this page?", "The page is for Birmingham water damage, including that area. Whether a provider accepts the job depends on availability, not on this sentence."),
    ],
    "berkley": [
        ("Can basement water reach Berkley hardwood floors?", "Yes, through a short stair and through wet joists under the subfloor. Mention original floors when you call so protection and joist checks are in the scope."),
        ("Is water damage restoration appropriate for a sewage backup?", "Yes, as the overall process, with extraction and sanitizing included because sewage is heavily contaminated water. Do not hire a dry-only visit for a backup."),
        ("Who dries the bungalow?", "The independent company you hire. We do not own drying equipment in Berkley or anywhere else."),
    ],
    "clawson": [
        ("What should a Clawson water damage company know about the lot?", "That driveways are short and the basement may be a single room containing the furnace. Access changes how they stage the job."),
        ("Does restoration include the sewer repair?", "No. Removing and drying water does not dig up a lateral or repair a city main. Those are separate."),
        ("Can Oakland Sewer Pros quote water damage repair in Clawson?", "No. We do not quote prices. The provider does, in writing, before you agree."),
    ],
}

HERO = {
    "royal-oak": "Water damage restoration in Royal Oak covers extraction, drying, and, when the water is sewage, a stricter cleanup. This is a referral to independent providers. We do not restore the house ourselves.",
    "troy": "Troy water damage restoration usually means a finished lower level: extract the water, remove what cannot be saved, and dry the rest. Call to reach an independent provider. Oakland Sewer Pros does not do the work.",
    "birmingham": "Water damage restoration in Birmingham has to respect plaster and older trim as well as the water itself. We connect you with an independent provider and do not run the drying.",
    "berkley": "Berkley water damage restoration has to protect a short stair and the first floor above a bungalow basement. Use this page for a referral. We do not extract or dry the house.",
    "clawson": "Water damage restoration in Clawson is a small-basement, small-lot job. This line refers you to an independent provider for extraction and drying. We do not quote or perform the repair.",
}

ALT = {
    "royal-oak": "Wet basement materials after a leak or backup, the start of water damage restoration in Royal Oak",
    "troy": "A wet finished basement, a common Troy water damage restoration setting",
    "birmingham": "Water damage on lower-level finishes in an older house, relevant to Birmingham restoration",
    "berkley": "Water in a bungalow basement under living space, a Berkley water damage path",
    "clawson": "A small basement with standing water near mechanical equipment, a Clawson water damage scene",
}

DESCRIPTIONS = {
    "royal-oak": "Water damage restoration in Royal Oak, MI. We connect you with independent local providers. Call {PHONE_DISPLAY}.",
    "troy": "Water damage restoration in Troy, MI for basement floods and backups. Independent providers. Call {PHONE_DISPLAY}.",
    "birmingham": "Water damage restoration in Birmingham, MI. A referral to independent local providers. Call {PHONE_DISPLAY}.",
    "berkley": "Water damage restoration in Berkley, MI bungalows. Connect with independent providers. Call {PHONE_DISPLAY}.",
    "clawson": "Water damage restoration in Clawson, MI. Independent local providers through this line. Call {PHONE_DISPLAY}.",
}
