"""Flooded-basement pages rewritten around water removal and water damage."""
from site_config import PHONE_DISPLAY, PHONE_TEL

from sitegen.citations import (
    BERK_CLAIM,
    BERK_TIPS,
    BHAM,
    CLAW_SEWER,
    MCL1419,
    RO_FLOOD,
    RO_SEWER,
    TROY_AGENDA,
    TROY_CLAIMS,
    cite,
)
from sitegen.render import a, callout, h2, h3, nearby_section, p, ul

def royal_oak():
    return "\n".join([
        h2("Basement water removal in Royal Oak"),
        p(
            "Flooded basement cleanup in Royal Oak starts with a simple split: did the water come from the "
            "sky and the soil, or did it come from a drain? A window well fills when a summer storm dumps more water than the soil can take. That is "
            "basement water removal. If the floor drain surged at the same time, stop and read "
            + a("/royal-oak-sewage-extraction", "sewage extraction in Royal Oak")
            + " because the water is no longer a clean flood."
        ),
        h2("Emergency Flooded Basement Cleanup & Water Removal in Royal Oak"),
        p(
            "When your Royal Oak basement is flooding from storm runoff, a failed sump pump, or saturated window wells, rapid water removal is vital. Our emergency response crews arrive within 30–45 minutes with commercial extraction pumps to pull standing water, remove wet carpet, and protect your foundation from structural moisture damage."
        ),
        p(
            "This page is about getting the water out in the first hours. Drying walls and floors afterward is "
            + a("/royal-oak-water-damage-restoration", "water damage restoration in Royal Oak")
            + "."
        ),
        p(
            "In a heavy downpour, Royal Oak says street flooding is usually caused by debris sitting on the sewer grate, "
            "so clearing leaves and grass clippings off the grate in front of your house helps. "
            "The regional storage for this system is the George W. Kuhn Retention Treatment Basin, under the I-75 overpass at 12 Mile Road in Madison Heights, which can hold and treat 150 million gallons. "
            "Storms on August 11–13, 2014 led to federal disaster declaration FEMA-4195-DR for Oakland, Macomb and Wayne counties."
        ),
        h3("What floods Royal Oak basements besides a sewer"),
        ul([
            "Window wells without a cover, or with soil sloping toward them.",
            "Stairwell drains at side doors that clog with leaves and then pour down the steps.",
            "Sump failure during a storm. The pump page is " + a("/royal-oak-sump-pump-repair", "sump pump repair in Royal Oak") + ".",
            "A supply-line break at a basement laundry. That is clean water until it sits long enough to foul, and it is still water damage.",
        ]),
        h2("Water damage after the basement is pumped"),
        p(
            "Basement flooding becomes water damage when drywall, insulation, carpet, and wood stay wet. "
            "Royal Oak basements are often used for storage and laundry, not always as a full apartment, "
            "but the materials are the same. "
            + a("/royal-oak-water-damage-restoration", "Water damage restoration in Royal Oak")
            + " is the longer process: drying, deciding what to discard, and watching for mold growth "
            "if the wetting lasted more than a day or two. The crew does the drying. "
            "Call " + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + "."
        ),
        p(
            "Royal Oak's Sewer Division maintains about 300 miles of sanitary and storm sewers and is the public contact for the city pipes. A flooded window well is not automatically their emergency, "
            "and a surcharging floor drain might be. Describe what you see."
        ),
        callout(
            "Royal Oak water-removal priorities",
            ul([
                "If you smell sewage or the toilet bubbled, treat it as a backup, not a rain flood.",
                "Do not pump sewage into the yard or the storm gutter. A crew should handle disposal.",
                "Lift finished goods off the floor only if you can do it without stepping in the water.",
                "Ask the company how they will dry the walls, not only how they will pump.",
            ]),
        ),
        p(
            "Residue after a contaminated flood is "
            + a("/royal-oak-basement-sanitization", "basement sanitization in Royal Oak")
            + ". The neighborhood overview is " + a("/royal-oak", "Royal Oak") + "."
        ),
        nearby_section("flooded-basement", "Flooded basement cleanup", "royal-oak"),
    ])


def troy():
    return "\n".join([
        h2("Basement water removal in Troy's finished lower levels"),
        p(
            "A flooded basement in Troy is often a finished room. Lower levels hold carpet, drywall, and furniture a few "
            "inches above the slab. Basement water removal has to deal with that carpet and the pad, not "
            "only with a bare floor around a floor drain."
        ),
        p(
            "This page is about getting the water out in the first hours. Drying walls and floors afterward is "
            + a("/troy-water-damage-restoration", "water damage restoration in Troy")
            + ". If the floor drain also backed up, the water is sewage and the extraction page is "
            + a("/troy-sewage-extraction", "sewage extraction in Troy") + "."
        ),
        h2("Emergency Basement Water Removal & Flood Clean Up in Troy"),
        p(
            "Searching for an experienced basement water damage company in Troy, MI? Rapid basement water removal is vital to stop water wicking up drywall and soaking beneath carpet pad. Our high-capacity extraction pumps remove standing water within hours, preparing your lower level for complete sanitization and structural restoration."
        ),
        h3("Cleanup versus drying in a Troy basement"),
        p(
            "Flooded basement cleanup is the removal and the wash-down. Water damage is what remains in "
            "the gypsum and the sill plates after the floor looks dry. Troy finished basements hide that "
            "moisture behind baseboard. A crew should use a moisture check on the walls, not a palm "
            "on the carpet. The broader process is "
            + a("/troy-water-damage-restoration", "water damage restoration in Troy")
            + ". For water removal and drying, call "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + "."
        ),
        ul([
            "Berber and pad in a family room usually come out if they were under standing water. Ask before you assume they can be dried in place.",
            "A basement bedroom needs the furniture moved before air can reach the walls. That labor is part of the scope you agree to.",
            "The city handles street storm drains, not a restoration crew.",
            "Insurance for sudden water depends on your policy. Ask your insurer.",
        ]),
        h2("Basement flooding causes Troy homeowners can actually check"),
        p(
            "Look, from the stairs, at three things: is the sump pit overflowing, is water coming over the "
            "window-well rim, and is the floor drain the source? Those three have different fixes. Pumping "
            "without answering them just refills the room. George W. Kuhn is one of Troy's three wastewater districts. It is a regional system, not the cause of every wet basement."
        ),
        callout(
            "Before a Troy crew arrives",
            ul([
                "Photograph the water line on the drywall from a dry step.",
                "Move vehicles if the driveway is the only place to stage fans.",
                "Leave wet carpet where it is if sewage is possible.",
                "Write down how long the water sat. Hours versus days changes the drying plan.",
            ]),
        ),
        p(
            "If the flood was contaminated, continue at "
            + a("/troy-basement-sanitization", "Troy basement sanitization")
            + ". City links are on " + a("/troy", "the Troy page") + "."
        ),
        nearby_section("flooded-basement", "Flooded basement cleanup", "troy"),
    ])


def birmingham():
    return "\n".join([
        h2("Basement water removal in older Birmingham houses"),
        p(
            "In older homes, the issue is often an original foundation, "
            "a window well, or a drain in a house that has plaster instead of modern drywall. Basement "
            "water removal in those houses is slow, because plaster and wood trim should not be torn "
            "out on a hunch."
        ),
        p(
            "Call "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " to get a local crew to the house. If sewage is in the water, switch "
            "to " + a("/birmingham-sewage-extraction", "sewage extraction in Birmingham") + " before you hire anyone for a 'clean flood.'"
        ),
        h2("Rapid Water Removal for Flooded Basements in Birmingham"),
        p(
            "If you need help getting rid of water in your basement in Birmingham, fast action prevents structural moisture absorption into older foundation walls. Our local crews handle complete basement flood clean up, extracting standing water, removing saturated carpet, and preparing your home for comprehensive drying."
        ),
        h3("Water damage in houses that were not built with drywall"),
        p(
            "Water damage repair after basement flooding in Birmingham often means plaster that is stained "
            "at the base, cupped wood floor at the bottom of a stair, and insulation that may not exist in "
            "the old wall. Drying equipment still has to move air, but the company should explain what they "
            "will sacrifice and what they will try to save. That choice is the core of "
            + a("/birmingham-water-damage-restoration", "water damage restoration in Birmingham")
            + ". A sump that failed is " + a("/birmingham-sump-pump-repair", "sump pump repair in Birmingham") + "."
        ),
        ul([
            "Do not chip soft plaster before the crew has seen how high the water went.",
            "A finished lower level used as a guest room has contents that hold water. List them. Do not haul them through the main floor while they drip.",
            "Yard flooding and a sanitary backup can happen in the same storm. Say if the drains gurgled.",
            "Ask the city which storm connection serves your street.",
        ]),
        h2("How long Birmingham materials stay wet"),
        p(
            "Plaster and masonry release water slowly. A floor that looks dry on day one can still be damp "
            "in the wall on day three. Ask the crew how they will recheck moisture on later days, and what happens if readings stay high. Contaminated residue, if the "
            "flood was not clean, is "
            + a("/birmingham-basement-sanitization", "sanitization after a Birmingham flood or backup")
            + ". Birmingham is one of the 14 communities the George W. Kuhn district serves; the city's own FAQ covers the local pipes."
        ),
        callout(
            "Birmingham: protect the stairs and the trim",
            ul([
                "Keep traffic off a wet wood stair.",
                "Shut the air handler if it sits in the lower level.",
                "Do not set a household dehumidifier in sewage water.",
                "Ask for a written scope that separates pumping, demolition, and drying.",
            ]),
        ),
        p("Browse " + a("/birmingham", "all Birmingham services") + " if the flood is only part of the loss."),
        nearby_section("flooded-basement", "Flooded basement cleanup", "birmingham"),
    ])


def berkley():
    return "\n".join([
        h2("Basement water removal in Berkley"),
        p(
            "Berkley is a city of older homes whose combined sewer drains to the regional George W. Kuhn system, with 12 Mile Road as the commercial edge and Coolidge as a main "
            "north-south road. Basement flooding here is often a window well, a stairwell, or a sump that "
            "lost power, inside a short basement. Basement water removal has "
            "to happen without soaking the hardwood that sits just above that basement on the first floor."
        ),
        h2("Emergency Flooded Basement Cleanup & Water Removal in Berkley"),
        p(
            "Facing basement flooding in Berkley? Fast water removal protects low-clearance subfloors and first-floor hardwood. Our emergency crews arrive in 30–45 minutes with truck-mounted pumps to extract water, pull wet carpet, and dry foundation framing fast."
        ),
        p(
            "The stair is the risk. Water carried up on boots, or a hose coupling that lets go, marks the "
            "oak floors owners are trying to keep. Tell the crew that the first floor is original wood "
            "if that is true, and ask them to protect the landing. Call "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY) + " and ask the crew to protect the landing."
        ),
        h3("Flooded basement cleanup versus a Berkley sewer backup"),
        ul([
            "Quiet floor drains and full window wells point to storm water and "
            + a("/berkley-water-damage-restoration", "water damage restoration") + ".",
            "A gurgling laundry tub points to sewage. Use "
            + a("/berkley-sewage-extraction", "Berkley sewage extraction") + " instead of a rain-flood plan.",
            "A dead sump during a power cut is both a flood and a "
            + a("/berkley-sump-pump-repair", "sump pump") + " problem. DTE is the electric utility; the outage and the pump are related but not the same repair.",
            "Berkley's combined sewer can make a rainstorm behave like a backup.",
        ]),
        h2("What water damage looks like under a Berkley house"),
        p(
            "Short ceilings mean the water line reaches the joists sooner. Insulation between joists, if "
            "anyone added it, holds water against the subfloor and can mark the hardwood from below. "
            "Flooded basement cleanup that stops at the slab misses that. Ask the company to look up, not "
            "only down. Drying is part of "
            + a("/berkley-water-damage-restoration", "the Berkley water damage page")
            + ". If sewage mixed in, sanitizing is "
            + a("/berkley-basement-sanitization", "a separate Berkley page")
            + " and should be done by the restoration company."
        ),
        callout(
            "Berkley steps that avoid a second mess",
            ul([
                "Take shoes off at the top of the stairs, or leave them in the basement.",
                "Do not run the whole-house fan.",
                "Note whether the water is clear or whether it smells. Do not taste or touch it to decide.",
                "Call the city if the street drain in front of the house is buried and the curb is a pond. That is not a basement-pumping task.",
            ]),
        ),
        p(
            "Regional drainage for this corner of Oakland County is associated with the Water Resources "
            "Commissioner and the George W. Kuhn district. Your window well is still your window well. "
            "See " + a("/berkley", "Berkley's service list") + " for the other pages."
        ),
        nearby_section("flooded-basement", "Flooded basement cleanup", "berkley"),
    ])


def clawson():
    return "\n".join([
        h2("Basement water removal in older Clawson houses"),
        p(
            "Clawson basement flooding shows up in small rooms under older homes. "
            "The houses are on tight lots between "
            "Royal Oak and Troy. There is often one basement room with the furnace, the water heater, and "
            "the floor drain together. Basement water removal starts by keeping that equipment from sitting "
            "in the water, which means staying out if the water is already at the burners or the panel."
        ),
        h2("Emergency Flooded Basement Cleanup & Water Removal in Clawson"),
        p(
            "When a storm or failed pump causes basement flooding in Clawson, rapid emergency pumping protects furnaces and mechanical systems in compact basement footprints. Our dispatched extraction teams arrive in 30–45 minutes with high-volume pump equipment."
        ),
        p(
            "A flood from a stairwell or a low window is not the same event as a sewer backup, even though "
            "both leave a wet floor. A storm and a backup can happen at the same time. "
            "If the drain was the source, go to "
            + a("/clawson-sewage-extraction", "sewage extraction in Clawson")
            + " and do not pump that water into the alley. If the sump quit, include "
            + a("/clawson-sump-pump-repair", "sump pump repair")
            + " in the call. Call "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " and a local crew removes the water."
        ),
        h3("Water damage in a one-room Clawson basement"),
        p(
            "Because the basement is one volume, water damage spreads to everything stored there: holiday "
            "boxes, tools, and the bottom of the furnace cabinet. Flooded basement cleanup includes sorting "
            "what is porous and wet from what is metal and can be wiped. Drying the structure is "
            + a("/clawson-water-damage-restoration", "water damage restoration in Clawson")
            + ". A crew should explain whether the furnace can run. That judgment is made on site."
        ),
        ul([
            "Short driveways mean the pump discharge should be planned so it does not ice the sidewalk or run to a neighbor's window well.",
            "Street flooding is a city drainage question. Your basement is a separate hire.",
            "Contaminated floods need " + a("/clawson-basement-sanitization", "sanitizing after the Clawson flood") + ", not a mop and bleach from the grocery store as the whole plan.",
            "Ask your insurer what is covered. Sudden discharge and groundwater are often treated differently.",
        ]),
        h2("Flooded basement cleanup in Clawson, from the first hour"),
        p(
            "Flooded basement cleanup in Clawson, MI is water removal plus the mess in that one room. "
            "If the floor drain never moved and there is no sewage odor, treat it as storm water, a "
            "window, or a dead sump. If the drain did move, stop and use "
            + a("/clawson-sewage-extraction", "sewage extraction")
            + " and "
            + a("/clawson-sewer-cleanup", "sewage cleanup in Clawson")
            + ". Sewage in a room that also holds the furnace is a health problem: do not "
            "wade in, do not track it up the stairs, and do not restart equipment that was submerged."
        ),
        p(
            "A reasonable sequence, done by the crew, is: make the room safe, remove standing "
            "water, discard porous material that cannot be saved, then dry what remains. Drying is "
            + a("/clawson-water-damage-restoration", "water damage restoration in Clawson")
            + ". Insurance for a sudden pipe break, a sewer backup, and groundwater are often different "
            "parts of a policy. Ask your insurer which one matches what you saw. The city's 45-day notice is a separate letter. Call "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " when you want a local crew for the water that is already inside."
        ),
        h2("Causes that fit Clawson's lots"),
        p(
            "Compact lots put the downspout discharge close to the wall. A disconnected downspout dumps "
            "the roof onto the foundation and in through a low window. You can check that from outside without entering the water. Roots in an old lateral are not visible from the "
            "sidewalk; they need a camera. The George W. Kuhn drainage district is part of the regional "
            "story for Clawson and nearby southern Oakland County cities. It does not replace looking at "
            "your downspout and your pit."
        ),
        callout(
            "Clawson safety before water removal",
            ul([
                "If water reached the furnace or the panel, leave and call from upstairs.",
                "Do not restart a flooded water heater.",
                "Keep the basement door shut so humidity does not move into the main floor.",
                "Describe the lot access when you call so the crew can say if they can work there.",
            ]),
        ),
        p("The rest of the Clawson pages are linked from " + a("/clawson", "the city overview") + "."),
        nearby_section("flooded-basement", "Flooded basement cleanup", "clawson"),
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
        ("What is basement water removal in Royal Oak?", "It is pumping and removing standing water from a basement, then dealing with the materials that stayed wet. If the water came from a sewer drain, it is sewage extraction, not a clean flood."),
        ("Does flooded basement cleanup include drying the walls?", "It should, or hire that step explicitly. Pumping alone leaves water in drywall and the slab edge. Ask for pumping and drying as separate lines with separate prices."),
        ("Can I pump a Royal Oak basement into the street?", "Do not pump sewage or heavily soiled water into the street or storm inlet. Clean rainwater is still worth asking the city about before you discharge it."),
        ("Who does Royal Oak list for basement water, if this might be the city main?", "Contact Royal Oak Public Works or police non-emergency dispatch to report city main concerns. Royal Oak is in the former Twelve Towns program, now the George W. Kuhn basin. Call (248) 825-8312 when you need a local crew to remove water from the house." + cite("City of Royal Oak, Responding to Street and Basement Flooding", RO_FLOOD)),
        ("Does a window-well flood in Royal Oak start a 45-day sewer claim?", "Only a sewage disposal event is in that statute. A quiet drain and rain in a window well is storm water. If the floor drain discharged, treat it as sewage and look at the 45-day written notice. The city is responsible for the main, and you are responsible for the lateral through the connection." + cite("City of Royal Oak Sewer Division", RO_SEWER) + cite("Michigan Legislature, MCL 691.1419", MCL1419)),
    ],
    "troy": [
        ("Why are Troy finished basements a bigger water-removal job?", "Carpet, pad, and drywall in a split-level or subdivision basement hold more water than a bare utility floor. The visible puddle is the small part."),
        ("Does Troy's sewer district matter after a basement flood?", "It can matter for a claim. Troy discharges through three districts: Evergreen-Farmington, Oakland-Troy, and George W. Kuhn. Check with the Troy Water Division via the city portal to determine which district serves your address before anyone blames the street." + cite("Troy City Council agenda, November 14, 2022", TROY_AGENDA)),
        ("Is basement flooding the same as water damage?", "Flooding is the water. Water damage is the harm to materials after it sits. The Troy water damage page covers drying and repair decisions."),
        ("If the Troy lower level smells like a drain, which city office handles that?", "Report city sewer main backups to the Troy Water Division or Troy Police dispatch online, and call (248) 825-8312 for immediate private basement flood pumping and water removal." + cite("City of Troy, Legal Claims for Overflows and Backups", TROY_CLAIMS)),
        ("What should I tell a crew about a flooded Troy basement?", "Whether the room is finished with carpet, and whether sewage came up a drain. If the public system is involved, a written claim to the City Attorney's Office is due within 45 days of discovery." + cite("City of Troy, Legal Claims for Overflows and Backups", TROY_CLAIMS)),
    ],
    "birmingham": [
        ("Should flooded basement cleanup in Birmingham rip out plaster the first day?", "Not by default. Plaster and trim in older houses may be salvageable depending on how high the water went. The crew should look before anyone chisels."),
        ("How can I tell a Birmingham storm flood from a sewer backup?", "Watch the drains. Sewage comes up a floor drain, a basement toilet, or a laundry standpipe and smells like a drain. Water at a window well with quiet drains is usually storm water. If you are unsure, keep people out and describe both on the call."),
        ("What did Birmingham publish about the August 24, 2023 storm?", "The city posted an engineer's presentation on the August 24, 2023 rain event on its Risk Management page. The city FAQ also says its older combined and storm sewers were designed for about 2 inches of rain in one hour." + cite("City of Birmingham Risk Management", BHAM)),
        ("Were Birmingham sewers built for a heavy one-hour rain?", "The city says combined and storm sewers were historically designed for about 2 inches of rain in one hour. The system is gravity, with no city pump stations. Downspouts extended about 6 feet and a backflow preventer are prevention. They do not pump out a lower level that is already wet." + cite("City of Birmingham Risk Management", BHAM)),
        ("Is Birmingham's water-event form the 45-day claim?", "The water-event form collects municipal flooding data only; it is not the claim. Use the city's sewer backup claim form. Direct legal claim inquiries to Birmingham Risk Management. Written notice is due within 45 days of discovery. For emergency basement water removal, call (248) 825-8312." + cite("City of Birmingham Risk Management", BHAM) + cite("Michigan Legislature, MCL 691.1419", MCL1419)),
    ],
    "berkley": [
        ("What should I do first when a Berkley basement floods?", "Keep people off the stairs and out of the water if it is near the panel or furnace. Check the floor drain: water that came up the drain is sewage on Berkley's combined sewer, while clear water from a window well is a flood. Then call (248) 825-8312." + cite("City of Berkley, Flood Tips for Residents", BERK_TIPS)),
        ("Can basement water removal stain the floor above?", "Yes, if dirty water is tracked up the short stair or if joist insulation stays wet against the subfloor. Ask the crew to protect the landing and to check the joists."),
        ("What if the Berkley flood smells like sewage?", "Stop treating it as rainwater. Berkley's sewer is one combined gravity pipe, so a storm can put wastewater on the floor. Keep people off the short stair and call (248) 825-8312 for a local crew, and notify Berkley Public Works via their city website." + cite("City of Berkley, Flood Tips for Residents", BERK_TIPS)),
        ("Why is the street ponding in Berkley during the same storm?", "The city says streets are designed to hold water so it enters the pipe more slowly, and catch basins use restrictor covers. Ponding at the curb is not, by itself, a forgotten pump. There is no city pump. Your basement sump is a separate machine." + cite("City of Berkley, Flood Tips for Residents", BERK_TIPS)),
        ("Does flooded-basement cleanup in Berkley replace the claims form?", "No. The city posts a Sewer Backup Claims Form, and written notice is due within 45 days of discovery when you believe a sewage event caused the damage. A clean window-well flood is a different description. Tell your insurer which one you saw." + cite("City of Berkley, Report a Claim", BERK_CLAIM) + cite("Michigan Legislature, MCL 691.1419", MCL1419)),
    ],
    "clawson": [
        ("What makes Clawson basement water removal different?", "Small basements, furnaces in the same room as the water, and short driveways. Access and electrical safety drive the first decisions."),
        ("Is a disconnected downspout really enough to flood a small basement?", "It can be. Roof water dumped at the foundation on a small lot has nowhere to go but down the wall and in at a low opening. Check that from outside."),
        ("Who sets the price for Clawson basement water removal?", "The cleanup company, in writing, before you agree. Tell them the driveway is short and whether the furnace is in the water."),
        ("Who do I call in Clawson if the flood might be the city sewer?", "Contact Clawson Public Works or municipal emergency dispatch via the city website. The sewer page points to the George W. Kuhn basin. For private emergency flood water removal, call (248) 825-8312." + cite("City of Clawson, Sanitary and Storm Sewer System", CLAW_SEWER)),
        ("How do I give Clawson written notice if the water was sewage?", "State law requires written notice within 45 days of discovering the damage, with your name, address, and phone, the property address, the discovery date, and a brief description. Ask the city in writing who receives sewer backup notices. A quiet drain and rain at a downspout is a different description. The sewer page links Public Act 222." + cite("Michigan Legislature, MCL 691.1419", MCL1419)),
    ],
}

HERO = {
    "royal-oak": "Is your Royal Oak basement flooding? Our emergency crews arrive in 30–45 minutes with high-volume pumps to provide rapid flooded basement cleanup and water removal. We extract standing water, pull ruined carpet, and bill insurance directly.",
    "troy": "Standing water in your lower level? Our emergency crews provide fast flooded basement cleanup and water removal in Troy, MI, arriving on-site in 30–45 minutes. Whether your split-level flooded from heavy rainfall or a failed pump, Troy's dedicated basement flood clean up team extracts water, removes wet carpet, and dries walls fast.",
    "birmingham": "Dealing with flooded basements in Birmingham? Our emergency response team arrives in 30–45 minutes with high-volume truck-mounted extractors. Whether stormwater overflowed your window wells or a drain backed up, we provide rapid basement flood repair and water pumping tailored to protect Birmingham homes.",
    "berkley": "Dealing with a flooded basement in Berkley? Our local pumping crews arrive in 30–45 minutes. We remove standing water, protect original hardwood floors above, and provide direct insurance billing.",
    "clawson": "Flooded basement in Clawson? Our emergency water removal crews arrive in 30–45 minutes. We pump out standing floodwater near mechanical equipment, dry foundation framing, and handle direct insurance billing.",
}

ALT = {
    "royal-oak": "Standing water covering a basement floor, a Royal Oak flooded-basement water removal situation",
    "troy": "Water across a finished basement floor, the cleanup Troy lower levels often need",
    "birmingham": "Floodwater in a lower level of an older house, a Birmingham water-removal concern",
    "berkley": "A flooded short basement, typical of Berkley water removal jobs",
    "clawson": "Basement floodwater near mechanical equipment, a safety issue in Clawson basements",
}

DESCRIPTIONS = {
    "royal-oak": "Call (248) 825-8312 for 24/7 flooded basement cleanup in Royal Oak, MI. Rapid standing water extraction, basement drying & direct insurance billing.",
    "troy": "Call (248) 825-8312 for 24/7 flooded basement cleanup in Troy, MI. Fast emergency standing water extraction, carpet removal & direct insurance billing.",
    "birmingham": "Call (248) 825-8312 for 24/7 flooded basement cleanup in Birmingham, MI. 30-min response, water extraction, plaster drying & direct insurance billing.",
    "berkley": "Call (248) 825-8312 for 24/7 flooded basement cleanup in Berkley, MI. Rapid emergency water removal, basement drying & direct insurance billing.",
    "clawson": "Call (248) 825-8312 for 24/7 flooded basement cleanup in Clawson, MI. 30-min response, standing water removal, drying & direct insurance billing.",
}
