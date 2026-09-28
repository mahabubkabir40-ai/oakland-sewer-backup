"""Flooded-basement pages rewritten around water removal and water damage."""
from site_config import PHONE_DISPLAY, PHONE_TEL

from sitegen.render import a, callout, h2, h3, nearby_section, p, ul

def royal_oak():
    return "\n".join([
        h2("Basement water removal in Royal Oak"),
        p(
            "Flooded basement cleanup in Royal Oak starts with a simple split: did the water come from the "
            "sky and the soil, or did it come from a drain? Houses along Woodward, around the Detroit Zoo "
            "on West Ten Mile, and in Vinsetta and Northwood all have basements. Window wells on those "
            "blocks fill when a summer storm dumps on the avenue and the soil cannot take it. That is "
            "basement water removal. If the floor drain surged at the same time, stop and read "
            + a("/royal-oak-sewage-extraction", "sewage extraction in Royal Oak")
            + " because the water is no longer a clean flood."
        ),
        p(
            "Water removal means getting standing water off the slab and out of the finishes it touched. "
            "A wet-vac pass that leaves the pad and the bottom of the drywall soaked is not finished. "
            "Concrete in these older foundations takes on water at the cove. The crew "
            "should say how they will check that, not just how fast they can empty the visible pool."
        ),
        h3("What floods Royal Oak basements besides a sewer"),
        ul([
            "Window wells that sit below the grade along older Woodward-side lots, especially where the well cover is missing.",
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
            "City storm drainage and the sanitary sewer are different systems in many newer separations, "
            "and older Royal Oak sections were built before that split was standard. "
            + a("https://www.romi.gov/384/Sewer-Division", "Royal Oak's Sewer Division")
            + " is the public contact for the city pipes. A flooded window well is not automatically their emergency, "
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
            "A flooded basement in Troy is often a finished room. Split-levels near Big Beaver and larger "
            "basements in subdivisions such as Northfield Hills hold carpet, drywall, and furniture a few "
            "inches above the slab. Basement water removal has to deal with that carpet and the pad, not "
            "only with a bare floor around a floor drain. Somerset Collection and the I-75 corridor tell "
            "you where the commercial traffic is. The water is in the houses behind those roads."
        ),
        p(
            "In a quick thaw or a summer downpour, a sump in a Troy lower level can run for hours and then quit. "
            "When the pump quits, the pit overflows and the lower level floods. That sequence is water "
            "removal first and "
            + a("/troy-sump-pump-repair", "sump pump repair in Troy")
            + " second. If the floor drain also backed up, the water is sewage and the extraction page is "
            + a("/troy-sewage-extraction", "sewage extraction in Troy") + "."
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
            "Storm-drain questions on the street go to Troy's Streets and Drains Division, not to a restoration crew.",
            "Insurance for sudden water depends on your policy. Ask your insurer. The claim stays with you and your carrier.",
        ]),
        h2("Basement flooding causes Troy homeowners can actually check"),
        p(
            "Look, from the stairs, at three things: is the sump pit overflowing, is water coming over the "
            "window-well rim, and is the floor drain the source? Those three have different fixes. Pumping "
            "without answering them just refills the room. Parts of Troy are associated with southern Oakland County's George W. Kuhn "
            "drainage district. That is a regional storm system, not the cause of every wet basement."
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
        h2("Basement water removal around Quarton, Poppleton, and downtown Birmingham"),
        p(
            "Birmingham flooded-basement calls split by neighborhood. Near Quarton Lake, residents talk "
            "about low yards and water that finds the lower level in a long rain. In Poppleton Park and "
            "on the older streets off Old Woodward and Maple, the issue is often an original foundation, "
            "a window well, or a drain in a house that has plaster instead of modern drywall. Basement "
            "water removal in that second group is slow, because plaster and wood trim should not be torn "
            "out on a hunch."
        ),
        p(
            "Shain Park is the downtown green, not a flood gauge. It is a landmark so you know which "
            "Birmingham we mean. The work is in the houses. Call "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + ". A local crew handles the visit. If sewage is in the water, switch "
            "to " + a("/birmingham-sewage-extraction", "sewage extraction in Birmingham") + " before you hire anyone for a 'clean flood.'"
        ),
        h3("Water damage in houses that were not built with drywall"),
        p(
            "Water damage repair after basement flooding in Birmingham often means plaster that is stained "
            "at the base, cupped wood floor at the bottom of a stair, and insulation that may not exist in "
            "the old wall. Drying equipment still has to move air, but the company should explain what they "
            "will sacrifice and what they will try to save. That conversation is the core of "
            + a("/birmingham-water-damage-restoration", "water damage restoration in Birmingham")
            + ". A sump that failed is " + a("/birmingham-sump-pump-repair", "sump pump repair in Birmingham") + "."
        ),
        ul([
            "Do not chip soft plaster before the crew has seen how high the water went.",
            "A finished lower level used as a guest room has contents that hold water. List them. Do not haul them through the main floor while they drip.",
            "Quarton-area yard flooding and a sanitary backup can happen together. Say if the drains gurgled.",
            "Ask the city which storm connection serves your street.",
        ]),
        h2("How long Birmingham materials stay wet"),
        p(
            "Plaster and masonry release water slowly. A floor that looks dry on day one can still be damp "
            "in the wall on day three. Ask the crew how they will recheck, and what happens if readings "
            "stay high. Ask the crew how they will recheck moisture on later days. Contaminated residue, if the "
            "flood was not clean, is "
            + a("/birmingham-basement-sanitization", "sanitization after a Birmingham flood or backup")
            + ". Southern Oakland County drainage context, including portions of Birmingham and the George "
            "W. Kuhn district, is a county matter. Confirm it before you cite it to anyone."
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
        h2("Basement water removal in Berkley's flat bungalow grid"),
        p(
            "Berkley does not have a ravine to send storm water downhill. The city is a flat bungalow grid "
            "whose combined sewers drain to the regional George W. Kuhn system, with 12 Mile Road as the commercial edge and Coolidge as a main "
            "north-south road. Basement flooding here is often a window well, a stairwell, or a sump that "
            "lost power, inside a short basement under a 1940s or 1950s house. Basement water removal has "
            "to happen without soaking the hardwood that sits just above that basement on the first floor."
        ),
        p(
            "The stair is the risk. Water carried up on boots, or a hose coupling that lets go, marks the "
            "oak floors owners are trying to keep. Tell the crew that the first floor is original wood "
            "if that is true, and ask them to protect the landing. The company on site lays that protection. "
            "Call "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY) + ". A local crew handles the visit."
        ),
        h3("Flooded basement cleanup versus a Berkley sewer backup"),
        ul([
            "Quiet floor drains and full window wells point to storm water and "
            + a("/berkley-water-damage-restoration", "water damage restoration") + ".",
            "A gurgling laundry tub points to sewage. Use "
            + a("/berkley-sewage-extraction", "Berkley sewage extraction") + " instead of a rain-flood plan.",
            "A dead sump during a power cut is both a flood and a "
            + a("/berkley-sump-pump-repair", "sump pump") + " problem. DTE is the electric utility; the outage and the pump are related but not the same repair.",
            "Older combined-sewer sections, if the city confirms them for your block, can make a rainstorm behave like a backup.",
        ]),
        h2("What water damage looks like under a Berkley bungalow"),
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
        h2("Basement water removal in Clawson brick bungalows"),
        p(
            "Clawson basement flooding shows up in small rooms under mid-century brick bungalows and "
            "ranches, mostly built from the 1940s to the 1960s. The downtown reference is 14 Mile Road. The houses are on tight lots between "
            "Royal Oak and Troy. There is often one basement room with the furnace, the water heater, and "
            "the floor drain together. Basement water removal starts by keeping that equipment from sitting "
            "in the water, which means staying out if the water is already at the burners or the panel."
        ),
        p(
            "A flood from a stairwell or a low window is not the same event as a sewer backup, even though "
            "both leave a wet floor. Clawson laterals are old enough that a storm and a backup can coincide. "
            "If the drain was the source, go to "
            + a("/clawson-sewage-extraction", "sewage extraction in Clawson")
            + " and do not pump that water into the alley. If the sump quit, include "
            + a("/clawson-sump-pump-repair", "sump pump repair")
            + " in the call. The call number is "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + ". The crew hauls the water."
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
            "Street flooding on 14 Mile is a city drainage question. Your basement is a separate hire.",
            "Contaminated floods need " + a("/clawson-basement-sanitization", "sanitizing after the Clawson flood") + ", not a mop and bleach from the grocery store as the whole plan.",
            "Ask your insurer what is covered. Sudden discharge and groundwater are often treated differently. The claim stays with you and your carrier.",
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
            "wade in, do not mop it up the stair, and do not restart equipment that was submerged."
        ),
        p(
            "A reasonable sequence, done by the crew, is: make the room safe, remove standing "
            "water, discard porous material that cannot be saved, then dry what remains. Drying is "
            + a("/clawson-water-damage-restoration", "water damage restoration in Clawson")
            + ". Insurance for a sudden pipe break, a sewer backup, and groundwater are often different "
            "parts of a policy. Ask your insurer which one matches what you saw. Your claim stays with you "
            "and your carrier. The city's 45-day notice is a separate letter. Call "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " when you want a local crew for the water that is already inside."
        ),
        h2("Causes that fit Clawson's lots"),
        p(
            "Compact lots put the downspout discharge close to the wall. A disconnected downspout dumps "
            "the roof onto the foundation and in through a low window. That is a maintenance fact you can "
            "see from outside without entering the water. Roots in an old lateral are not visible from the "
            "sidewalk; they need a camera. The George W. Kuhn drainage district is part of the regional "
            "story for Clawson and nearby southern Oakland County cities. It does not replace looking at "
            "your downspout and your pit."
        ),
        callout(
            "Clawson safety before water removal",
            ul([
                "If water reached the furnace or the panel, leave and call from upstairs.",
                "Do not restart a flooded water heater.",
                "Keep the basement door shut so humidity does not move into the bungalow's main floor.",
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
        ("Can I pump a Royal Oak basement into the street?", "Do not pump sewage or heavily soiled water into the street or storm inlet. A crew should handle disposal. Clean rainwater is still worth asking the city about before you discharge it."),
        ("Who does Royal Oak list for basement water, if this might be the city main?", "Weekdays 7:30 a.m. to 4:00 p.m., call (248) 246-3300. After hours, (248) 246-3500 dispatches sewer personnel. Royal Oak is in the former Twelve Towns program, now the George W. Kuhn basin. Call (248) 825-8312 when you need a local crew to remove water from the house."),
        ("Does a window-well flood in Royal Oak start a 45-day sewer claim?", "Only a sewage disposal event is in that statute. A quiet drain and rain in a window well is storm water. If the floor drain discharged, treat it as sewage and look at the 45-day written notice. The city is responsible for the main, and you are responsible for the lateral through the connection."),
    ],
    "troy": [
        ("Why are Troy finished basements a bigger water-removal job?", "Carpet, pad, and drywall in a split-level or subdivision basement hold more water than a bare utility floor. The visible puddle is the small part."),
        ("Does Troy's sewer district matter after a basement flood?", "It can matter for a claim. Troy discharges through three districts: Evergreen-Farmington, Oakland-Troy, and George W. Kuhn. Ask the Water Division (248-524-3370) which one serves your address before anyone blames the street."),
        ("Is basement flooding the same as water damage?", "Flooding is the water. Water damage is the harm to materials after it sits. The Troy water damage page covers drying and repair decisions."),
        ("If the Troy lower level smells like a drain, which city number is that?", "Water Division 248-524-3370 during business hours, and Troy Police 248-524-3477 after hours. Street water and a sanitary backup are not automatically the same pipe. Troy uses three wastewater districts. Ask the city which one serves the house."),
        ("What should I tell a crew about a flooded Troy basement?", "Whether the room is finished with carpet, and whether sewage came up a drain. If the public system is involved, a written claim to the City Attorney's Office is due within 45 days of discovery."),
    ],
    "birmingham": [
        ("Should flooded basement cleanup in Birmingham rip out plaster the first day?", "Not by default. Plaster and trim in older houses may be salvageable depending on how high the water went. The crew should look before anyone chisels."),
        ("Are Quarton-area floods usually sewage?", "Not always. Low ground and yard drainage are common explanations there. Sewage is indicated by drain activity and odor. Do not guess if you are unsure; keep people out and describe both possibilities on the call."),
        ("What did Birmingham publish about the August 24, 2023 storm?", "The city posted an engineer's presentation on the August 24, 2023 rain event on its Risk Management page. The city FAQ also says its older combined and storm sewers were designed for about 2 inches of rain in one hour."),
        ("Were Birmingham sewers built for a heavy one-hour rain?", "The city says combined and storm sewers were historically designed for about 2 inches of rain in one hour. The system is gravity, with no city pump stations. Downspouts extended about 6 feet and a backflow preventer are prevention. They do not pump out a lower level that is already wet."),
        ("Is Birmingham's water-event form the 45-day claim?", "The water-event form and (248) 530-1703 collect flooding data. They are not the claim. Use the city's sewer backup claim form. Claims questions are 248.530.1808, and the city says claims go through the Michigan Municipal League Liability and Property Pool and Meadowbrook Claims Service. Written notice is due within 45 days of discovery. A late-1990s bond financed relief sewers in part of the city, not on every street."),
    ],
    "berkley": [
        ("How does Berkley's flat layout affect a flooded basement?", "Storm water has little slope to leave. Window wells and stairwells fill, and a sump may be the only thing keeping the short basement dry. That is a site condition, not a promise about your house."),
        ("Can basement water removal stain first-floor hardwood?", "Yes, if dirty water is tracked up the short bungalow stair or if joist insulation stays wet against the subfloor. Ask the crew to protect the landing and to check the joists."),
        ("What if the Berkley flood smells like sewage?", "Stop treating it as rainwater. Berkley's sewer is one combined gravity pipe, so a storm can put wastewater on the floor. Keep people off the short stair and call (248) 825-8312 for a local crew, plus Public Works at 248-658-3490."),
        ("Why is the street ponding in Berkley during the same storm?", "The city says streets are designed to hold water so it enters the pipe more slowly, and catch basins use restrictor covers. Ponding at the curb is not, by itself, a forgotten pump. There is no city pump. Your basement sump is a separate machine."),
        ("Does flooded-basement cleanup in Berkley replace the claims form?", "No. The city posts a Sewer Backup Claims Form, and written notice is due within 45 days of discovery when you believe a sewage event caused the damage. A clean window-well flood is a different description. Tell your insurer which one you saw."),
    ],
    "clawson": [
        ("What makes Clawson basement water removal different?", "Small basements, furnaces in the same room as the water, and short driveways. Access and electrical safety drive the first decisions."),
        ("Is a disconnected downspout really enough to flood a bungalow basement?", "It can be. Roof water dumped at the foundation on a small lot has nowhere to go but down the wall and in at a low opening. Check that from outside."),
        ("Who sets the price for Clawson basement water removal?", "The cleanup company, in writing, before you agree. Tell them the driveway is short and whether the furnace is in the water."),
        ("Who do I call in Clawson if the flood might be the city sewer?", "The city line is (248) 435-4500, Monday through Thursday, 7:00 a.m. to 3:30 p.m. The department is closed on Fridays. After hours, dispatch is 248-524-3477, extension 1. The sewer page points to the George W. Kuhn basin. Confirm your street with the city."),
        ("How do I give Clawson written notice if the water was sewage?", "State law requires written notice within 45 days of discovering the damage, with your name, address, and phone, the property address, the discovery date, and a brief description. Ask the city in writing who receives sewer backup notices. Clawson's sewer calls go to (248) 435-4500. A quiet drain and rain at a downspout is a different description. The sewer page links Public Act 222."),
    ],
}

HERO = {
    "royal-oak": "The basement in your Royal Oak house is full of water, from a storm, a sump, or a drain. A local cleanup crew handles the visit for flooded basement cleanup in Royal Oak, and they'll tell you when they can be there.",
    "troy": "A finished Troy lower level or split-level is under water and the carpet is holding it. Call and a local cleanup crew handles the visit for flooded basement cleanup in Troy, and they'll tell you when they can be there.",
    "birmingham": "Water is in an older Birmingham lower level, around the plaster and trim. When you call, you reach a local cleanup crew for basement water removal in Birmingham, and they'll tell you when they can be there.",
    "berkley": "Water is in a short Berkley bungalow basement, and the stair runs straight up to the first floor. Your call puts you through to a local cleanup crew for flooded basement cleanup in Berkley, and they'll tell you when they can be there.",
    "clawson": "Water is in a small Clawson bungalow basement, close to the furnace, and you need flooded basement cleanup in Clawson. Call, and a local cleanup crew handles flooded basement cleanup in Clawson. They'll tell you when they can be there. If a drain caused it, say so.",
}

ALT = {
    "royal-oak": "Standing water covering a basement floor, a Royal Oak flooded-basement water removal situation",
    "troy": "Water across a finished basement floor, the cleanup Troy lower levels often need",
    "birmingham": "Floodwater in a lower level of an older house, a Birmingham water-removal concern",
    "berkley": "A flooded short basement under a bungalow, typical of Berkley water removal jobs",
    "clawson": "Basement floodwater near mechanical equipment, a safety issue in Clawson bungalows",
}

DESCRIPTIONS = {
    "royal-oak": "Flooded basement cleanup and water removal in Royal Oak, MI. A local crew handles it. Call {PHONE_DISPLAY}.",
    "troy": "Flooded basement cleanup and basement water removal in Troy, MI. Call a local crew at {PHONE_DISPLAY}.",
    "birmingham": "Basement water removal and flooded basement cleanup in Birmingham, MI. Call {PHONE_DISPLAY} for a crew.",
    "berkley": "Flooded basement cleanup and water removal in Berkley, MI. We refer local crews. Call {PHONE_DISPLAY}.",
    "clawson": "Flooded basement cleanup and water removal in Clawson, MI bungalows. Local crews. Call {PHONE_DISPLAY}.",
}
