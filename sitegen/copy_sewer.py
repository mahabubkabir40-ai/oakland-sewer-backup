"""Conservative sewer-backup pages. Titles and H1s stay on the ranking phrase.

Local risk paragraphs are the ones already published for these URLs, with contractor-voice
lines removed. They still need an owner fact-check (see the PR description).
"""
from site_config import PHONE_DISPLAY, PHONE_TEL

from sitegen.citations import (
    BHAM,
    BERK_CLAIM,
    BERK_TIPS,
    CLAW_SEWER,
    MCL1419,
    RO_CLEAN,
    RO_FLOOD,
    RO_SEWER,
    TROY_AGENDA,
    TROY_CLAIMS,
    WRC_GWK,
    cite,
)
from sitegen.render import a, callout, h2, h3, nearby_section, note, ol, p, ul

WHY = {
    "royal-oak": (
        "Royal Oak's Sewer Division maintains about 300 miles of sanitary and storm sewers, and the city "
        "is part of the former Twelve Towns program, now the George W. Kuhn basin. In a hard storm those "
        "mains fill, and sewage can come back up the lowest opening in the house, usually the basement "
        "floor drain. The George W. Kuhn basin sits under the I-75 overpass at 12 Mile Road in Madison Heights, "
        "was expanded in 2006, and can hold and treat 150 million gallons. None of that storage can stop a blocked "
        "private lateral from backing up, and in Royal Oak the lateral is the homeowner's pipe up to and including "
        "the connection. A camera inspection shows whether yours is the problem. The city is responsible for the main; the lateral up to and including the connection is yours."
    ),
    "troy": (
        "Census estimates for 2019 to 2023 date about 49 percent of Troy's housing units to the 1960s and 1970s; "
        "in a finished lower level, carpet, pad, and drywall sit close to the floor drain. The city's wastewater leaves through three "
        "districts, so the pipe behind one street is not the pipe behind the next. Ask the Water Division which district serves your address."
    ),
    "birmingham": (
        "Much of Birmingham was built in the early and middle 1900s. The city's own FAQ says older "
        "communities have combined sewer and storm systems, historically designed for about 2 inches of "
        "rain in one hour, and that the system is all gravity with no city pump or lift stations. A heavier "
        "storm can push sewage back up a basement floor drain, and plaster, trim, and finished floors soak it up first."
    ),
    "berkley": (
        "Berkley's sewer is a single combined pipe for stormwater and sewage, entirely gravity, with no "
        "pumps or valves. The city designs its streets to hold water so flow enters that pipe more slowly. "
        "In a hard rain the shared pipe can still push wastewater back up a bungalow's basement floor drain, "
        "and in a short basement it reaches the furnace and the laundry fast."
    ),
    "clawson": (
        "Clawson's sewer page points to the George W. Kuhn Retention Treatment Basin and the Oakland County "
        "Water Resources Commissioner, and links to an explainer on combined sewers, where sanitary flow "
        "and stormwater share pipes. When a heavy regional storm loads that system, sewage can come up a "
        "basement floor drain. Compact lots also mean hoses and equipment may have to be staged from a short driveway or the street."
    ),
}

TRIGGERS = {
    "royal-oak": [
        "A slow or gurgling floor drain before a storm",
        "Heavy rain that fills the public sewer faster than it drains",
        "Roots or a cracked joint in the private lateral",
        "A sump that stops while the floor drain is also backing up",
    ],
    "troy": [
        "A floor drain that gurgles before sewage appears",
        "Rain that loads one of the three wastewater districts",
        "A blockage in the private lateral under the yard",
        "A sump that quits in the same storm that backs up a drain",
    ],
    "birmingham": [
        "A gurgling floor drain in an older lower level",
        "Rain heavier than the roughly 2 inches in one hour the city says its older sewers were designed for",
        "Roots or a cracked joint in the private lateral",
        "A sump that stops while sewage is also coming up a drain",
    ],
    "berkley": [
        "Ponding at the curb, which the city designs its streets to do",
        "Heavy rain in the combined pipe that carries stormwater and sewage together",
        "Roots or a cracked joint in the private lateral",
        "A sump that stops while the floor drain is also backing up",
    ],
    "clawson": [
        "A slow or gurgling floor drain before a storm",
        "Heavy regional rain that loads the public sewer",
        "Roots or a cracked joint in the private lateral",
        "A short driveway that changes how hoses and equipment can be staged",
    ],
}

AREA_LINE = {
    "royal-oak": (
        f"The same phone number covers Royal Oak neighborhoods along the {a('https://en.wikipedia.org/wiki/Woodward_Avenue', 'Woodward Avenue corridor')}, "
        f"near the Royal Oak Music Theatre, and toward the {a('https://en.wikipedia.org/wiki/Detroit_Zoo', 'Detroit Zoo')}. "
    ),
    "troy": (
        "The same phone number covers neighborhoods along Big Beaver Road, near Somerset Collection, "
        "and out toward Troy Historic Village."
    ),
    "birmingham": (
        "The same phone number covers Birmingham homes around downtown, Shain Park, Poppleton Park, and the Quarton area."
    ),
    "berkley": (
        "The same phone number covers Berkley bungalow blocks and the 12 Mile Road corridor."
    ),
    "clawson": (
        "The same phone number covers Clawson's brick-bungalow blocks and the 14 Mile Road downtown strip."
    ),
}

OWNER = {
    "royal-oak": (
        "Once wastewater is on the floor, the pumping step is "
        f"{a('/royal-oak-sewage-extraction', 'sewage extraction in Royal Oak')}. Keep people and pets "
        "out of that water until it is gone. A local crew does that pumping. "
        "Ask them for a written scope and for the license and insurance the job requires."
    ),
    "troy": (
        "Pumping the water out of a split-level or a subdivision basement is "
        f"its own job: {a('/troy-sewage-extraction', 'sewage extraction')}. Ask for a written scope before anyone starts."
    ),
    "birmingham": (
        "If the lower level is already wet and you only need the water removed, use "
        f"{a('/birmingham-sewage-extraction', 'sewage extraction in Birmingham')}. "
        "Ask the crew how they will protect plaster and trim before they cut anything."
    ),
    "berkley": (
        "If the bungalow floor drain already overflowed, pumping the water out is "
        f"{a('/berkley-sewage-extraction', 'sewage extraction in Berkley')}. A local crew handles the pump-out. "
        "Keep people off the short stair until that water is gone. Tell the crew whether the laundry tub or the floor drain overflowed first."
    ),
    "clawson": (
        "The pump-out, once sewage is on the floor of a brick bungalow, is "
        f"{a('/clawson-sewage-extraction', 'sewage extraction in Clawson')}. A local crew handles that visit, including where the hoses go."
    ),
}

SEWAGE_H2 = {
    "royal-oak": (
        "Sewage cleanup in Royal Oak starts with the water that came out of a floor drain, "
        "a laundry standpipe, or a basement toilet. Treat it as heavily soiled. A crew that only pumps the "
        f"visible puddle can leave residue in the pad and the wall base. If the backup also soaked finishes, see {a('/royal-oak-water-damage-restoration', 'water damage restoration in Royal Oak')} "
        f"and {a('/royal-oak-flooded-basement', 'flooded basement cleanup and water removal in Royal Oak')}."
    ),
    "troy": (
        "Sewage cleanup in Troy deals with water that left the sanitary line, not a clean rain leak. Split-level "
        "lower floors near Big Beaver often hold carpet and storage right where a backup surfaces. Ask the crew "
        f"how they will separate that water from the rest of the house. Related pages: {a('/troy-water-damage-restoration', 'water damage restoration')} "
        f"and {a('/troy-flooded-basement', 'flooded basement cleanup')}."
    ),
    "birmingham": (
        "Sewage cleanup in Birmingham is hard on older houses, because plaster, wood trim, and finished lower "
        "levels sit close to the floor drain. Pumping is only the start. The company on site should say what has to be discarded "
        f"because it soaked up sewage. Continue with {a('/birmingham-water-damage-restoration', 'water damage restoration in Birmingham')} "
        f"or {a('/birmingham-flooded-basement', 'basement water removal in Birmingham')}."
    ),
    "berkley": (
        "Sewage cleanup in Berkley usually happens in a small bungalow basement, not a wide commercial room. A shop vac on "
        "sewage water spreads droplets onto stairs and joists. Hire a company that treats the water as contaminated and can "
        f"work on a tight stair. If the basement is simply full of storm water, start at {a('/berkley-flooded-basement', 'flooded basement cleanup in Berkley')} "
        f"or {a('/berkley-water-damage-restoration', 'water damage restoration in Berkley')}."
    ),
    "clawson": (
        "Sewage cleanup in Clawson often starts at a floor drain in a brick bungalow. Compact lots limit where "
        "hoses and drying gear can sit, so ask how the crew will stage the job before you book. When the loss is broader "
        f"than the drain itself, use {a('/clawson-water-damage-restoration', 'water damage restoration in Clawson')} and "
        f"{a('/clawson-flooded-basement', 'flooded basement water removal in Clawson')}."
    ),
}


def first_ten(city, heading=None):
    return callout(
        heading or f"What to do in the first 10 minutes of a sewer backup in {city}",
        ol([
            "<strong>Stop using water.</strong> Do not run faucets, flush toilets, or run the washer or dishwasher.",
            "<strong>Keep people and pets out</strong> of the water. Sewage carries bacteria and other pathogens.",
            "<strong>Do not plunge or snake</strong> the drain. A household snake can push dirty water into the subfloor.",
            "<strong>Leave the basement if water is near outlets,</strong> the panel, or the furnace. Shut power off only from a dry location.",
            "<strong>Call (248) 825-8312.</strong> Say your city and that a floor drain backed up.",
        ]),
    )


_GUIDE = '<a href="/sewer-backup-claim-guide" class="text-red-400 hover:text-red-300 underline font-medium">sewer backup claim guide</a>'
_CHECK = '<a href="/basement-flood-checklist" class="text-red-400 hover:text-red-300 underline font-medium">printable basement flood checklist</a>'

# One claim sentence per city, drawn from each city's own published process (checked 28 Sep 2026).
CLAIM_LINE = {
    "royal-oak": (
        "Royal Oak asks residents to call the Department of Public Service while the water is coming in, so the city can "
        "check the main during the event. A claim against the city needs written notice within 45 days of discovery; "
        f"the {_GUIDE} explains the content and timeline. Keep the {_CHECK} for the next storm."
    ),
    "troy": (
        "The city takes written sewer backup claims through the City Attorney's Office, and state law sets a 45-day deadline "
        f"from discovery. The form, the contact, and what to photograph are in the {_GUIDE}. The {_CHECK} "
        "covers the steps before and during a storm."
    ),
    "birmingham": (
        "Birmingham posts a Sewer Backup Claim form on its Risk Management page and notes that its water event tracking "
        f"form is not a claim. The 45-day notice rule and a documentation list are in the {_GUIDE}; storm prep is on the {_CHECK}."
    ),
    "berkley": (
        "Berkley asks residents to report basement flooding to Public Works at 248-658-3490 and posts a Sewer Backup Claims Form. "
        f"Michigan law gives you 45 days from discovery to send written notice. Details are in the {_GUIDE}. Because Berkley's sewer is combined, the {_CHECK} "
        "is worth printing before spring storms."
    ),
    "clawson": (
        "The city line on Clawson's sewer page is (248) 435-4500. Ask the city in writing who should receive a claim notice. "
        f"The 45-day written notice rule is explained in the {_GUIDE}, and the {_CHECK} lists what to do during a storm."
    ),
}


CITY_SEWER_CALL = {
    "royal-oak": "the city at (248) 246-3300 (weekdays 7:30 a.m. to 4:00 p.m.) or (248) 246-3500 after hours",
    "troy": "Troy's Water Division at 248-524-3370, or the police at 248-524-3477 after hours",
    "birmingham": "the city's water event line, (248) 530-1703, so the city has a record of the flooding",
    "berkley": "Berkley Public Works at 248-658-3490",
    "clawson": "the city at (248) 435-4500 (public works Monday to Thursday, 7:00 a.m. to 3:30 p.m.), or Troy Police dispatch at 248-524-3477, extension 1, after hours",
}


def article(slug, city):
    resources = {
        "royal-oak": (
            f"More Royal Oak pages: {a('/royal-oak-sewage-extraction', 'sewage extraction')}, "
            f"{a('/royal-oak-flooded-basement', 'flooded basement cleanup')}, "
            f"{a('/royal-oak-basement-sanitization', 'sanitizing after a backup')}, "
            f"{a('/royal-oak-sump-pump-repair', 'sump pump repair')}, and "
            f"{a('/royal-oak', 'the Royal Oak overview')}."
        ),
        "troy": (
            f"More local pages: {a('/troy-sewage-extraction', 'sewage extraction')}, "
            f"{a('/troy-flooded-basement', 'flooded basement cleanup')}, "
            f"{a('/troy-basement-sanitization', 'sanitizing after a backup')}, "
            f"{a('/troy-sump-pump-repair', 'sump pump repair')}, and "
            f"{a('/troy', 'the city overview')}."
        ),
        "birmingham": (
            f"More Birmingham pages: {a('/birmingham-sewage-extraction', 'sewage extraction')}, "
            f"{a('/birmingham-flooded-basement', 'flooded basement cleanup')}, "
            f"{a('/birmingham-basement-sanitization', 'sanitizing after a backup')}, "
            f"{a('/birmingham-sump-pump-repair', 'sump pump repair')}, and "
            f"{a('/birmingham', 'the Birmingham overview')}."
        ),
        "berkley": (
            f"More Berkley pages: {a('/berkley-sewage-extraction', 'sewage extraction')}, "
            f"{a('/berkley-flooded-basement', 'flooded basement cleanup')}, "
            f"{a('/berkley-basement-sanitization', 'sanitizing after a backup')}, "
            f"{a('/berkley-sump-pump-repair', 'sump pump repair')}, and "
            f"{a('/berkley', 'the Berkley overview')}."
        ),
        "clawson": (
            f"More Clawson pages: {a('/clawson-sewage-extraction', 'sewage extraction')}, "
            f"{a('/clawson-flooded-basement', 'flooded basement cleanup')}, "
            f"{a('/clawson-basement-sanitization', 'sanitizing after a backup')}, "
            f"{a('/clawson-sump-pump-repair', 'sump pump repair')}, and "
            f"{a('/clawson', 'the Clawson overview')}."
        ),
    }
    html_out = "\n".join([
        h2(f"Sewage Cleanup {city}, MI"),
        p(SEWAGE_H2[slug]),
        p(OWNER[slug]),
        p(
            f"If the backup looks like the city main, call {CITY_SEWER_CALL[slug]} while the water is still coming in. "
            "The lateral under the yard is usually your pipe. The main in the street is the city's. "
            "Ask the cleanup company not to guess which one failed."
        ),
        h2(f"Sewer backup cleanup in {city}, MI"),
        p(
            f"Sewage cleanup in {city} usually starts when sewage comes up a basement drain, a laundry "
            "standpipe, or a basement toilet. Keep people and pets out, do not mop it through the house, "
            "and do not run a household vac. The steps below are the first minutes. Then call, and a local "
            "cleanup crew takes it from there."
        ),
        h3(f"Why {city} homes are at higher risk"),
        p(WHY[slug]),
        h3("Common backup triggers" if slug == "troy" else f"Common backup triggers in {city}"),
        ul(TRIGGERS[slug]),
        first_ten(
            city,
            "What to do in the first 10 minutes of a sewer backup" if slug == "troy" else None,
        ),
        note(AREA_LINE[slug]),
        p(CLAIM_LINE[slug]),
        p(
            "A November 14, 2022 City Council agenda says the Oakland County Water Resources Commissioner "
            "is responsible for the district facilities the city discharges into: Evergreen-Farmington, Oakland-Troy, "
            "and George W. Kuhn. Do not treat one street as the pattern for the whole city, and do not describe the system as "
            "fully combined or fully separated."
        ) if slug == "troy" else "",
        p(resources[slug]),
        nearby_section("sewer-cleanup", "Sewer backup cleanup", slug),
    ])
    if slug == "troy":
        block = p(SEWAGE_H2[slug])
        extra = p(
            "Sewage and water cleanup in a finished lower level can mean two different jobs: sewage from a drain "
            "that backed up, or carpet soaked by a storm or a failed sump. The first is contaminated from the start, "
            "so say which one you have when you call."
        )
        html_out = html_out.replace(block, block + "\n" + extra, 1)
        return html_out
    return html_out


FAQS = {
    "royal-oak": [
        (
            "Who do I call at the City of Royal Oak during a sewer backup?",
            "For basement water, the city lists (248) 246-3300 on weekdays from 7:30 a.m. to 4:00 p.m. After hours, the police non-emergency line (248) 246-3500 dispatches sewer personnel. For sewage cleanup inside the house, call (248) 825-8312." + cite("City of Royal Oak, Responding to Street and Basement Flooding", RO_FLOOD),
        ),
        (
            "Who owns the sewer lateral in Royal Oak?",
            "The city says it is responsible for the main, and the homeowner for the lateral up to and including the connection. Ask the Sewer Division, (248) 246-3300, about the main. A camera inspection is how a plumber or the city checks a specific lateral." + cite("City of Royal Oak Sewer Division", RO_SEWER),
        ),
        (
            "How long do I have to send Royal Oak written notice?",
            "Michigan law requires written notice within 45 days of discovering the damage before compensation for a sewage disposal event is possible. Include your name, address, and phone, the property address, the date you discovered the damage, and a brief description. Confirm with the city who receives that letter. A sewer-backup endorsement on your homeowners policy is a separate question for your insurer." + cite("Michigan Legislature, MCL 691.1419", MCL1419),
        ),
        (
            "Are Royal Oak sewers combined?",
            "Royal Oak is in the George W. Kuhn district, where stormwater and sewage share pipes; in wet weather more than 93 percent of that flow is stormwater. The city is a member of the former Twelve Towns program. The Sewer Division can confirm the pipe on your street." + cite("Oakland County Water Resources Commissioner, George W. Kuhn Retention Treatment Basin", WRC_GWK),
        ),
        (
            "Does Royal Oak publish cleanup steps after basement flooding?",
            "Yes. The city publishes a page called Cleaning Up the Mess After Basement Flooding. Treat sewage as contaminated, keep people and pets out, and photograph the damage before anything is thrown away. For the city main, call the Sewer Division at (248) 246-3300 on weekdays or (248) 246-3500 after hours." + cite("City of Royal Oak, Cleaning Up the Mess After Basement Flooding", RO_CLEAN),
        ),
    ],
    "troy": [
        (
            "Who should residents call for a sewer backup?",
            "The city lists the Water Division at 248-524-3370 during business hours and the police at 248-524-3477 after hours. A written claim goes to the City Attorney's Office within 45 days of discovery. For sewage cleanup inside the house, call (248) 825-8312." + cite("City of Troy, Legal Claims for Overflows and Backups", TROY_CLAIMS),
        ),
        (
            "Is Troy on one combined sewer?",
            "No single label fits. A November 14, 2022 City Council agenda item says the city discharges wastewater through the Evergreen-Farmington, Oakland-Troy, and George W. Kuhn districts. The Oakland County Water Resources Commissioner is responsible for those district facilities. Ask which district serves your address before you assume the pipe in the street." + cite("City of Troy City Council agenda, November 14, 2022", TROY_AGENDA),
        ),
        ("Where does a written sewer claim go?", "To the City Attorney's Office. State law sets 45 days from discovery. The sewer backup claim guide lists what to include." + cite("City of Troy, Legal Claims for Overflows and Backups", TROY_CLAIMS) + cite("Michigan Legislature, MCL 691.1419", MCL1419)),
        (
            "Who is responsible for the sewer lateral?",
            "The main in the street is a city question. The lateral under the yard is usually the homeowner's pipe. Confirm the split for your address with the city. A camera answers the private lateral. The cleanup company removes what already entered the lower level.",
        ),
        (
            "What should I do about a gurgling floor drain in the basement?",
            "Stop running water. In a 1960s or 1970s house, treat a gurgling basement drain as a warning, and do not snake it if you smell sewage. If you think the main is backing up, call the Water Division (248-524-3370, or the police at 248-524-3477 after hours)." + cite("City of Troy, Legal Claims for Overflows and Backups", TROY_CLAIMS),
        ),
    ],
    "birmingham": [
        (
            "Who do I call in Birmingham if sewage is in the lower level?",
            "The water event line, (248) 530-1703, collects flooding information. It is not a claim. Claims questions are 248.530.1808, and the city says claims go through the Michigan Municipal League Liability and Property Pool and Meadowbrook Claims Service. For sewage cleanup inside the house, call (248) 825-8312." + cite("City of Birmingham Risk Management", BHAM),
        ),
        (
            "Can a hard rain overload Birmingham's older sewers?",
            "The city's Risk Management FAQ says older communities have combined sewer and storm systems. Those sewers were historically designed for about 2 inches of rain in one hour, which the city calls a 10-year storm. The system is gravity, and Birmingham owns no sewage pump or lift stations. A late-1990s bond financed relief sewers in part of the city, not on every street." + cite("City of Birmingham Risk Management", BHAM),
        ),
        (
            "What is the 45-day notice for a Birmingham sewer backup?",
            "Written notice is due within 45 days of discovering the damage. Include your name, address, and phone, the property address, the discovery date, and a brief description. Use the city's sewer backup claim form. The water-event tracking form is not that claim. Ask your insurer separately about a sewer-backup endorsement." + cite("City of Birmingham Risk Management", BHAM) + cite("Michigan Legislature, MCL 691.1419", MCL1419),
        ),
        (
            "What does Birmingham suggest before the next storm?",
            "The city FAQ lists a backflow preventer, downspouts disconnected and extended about 6 feet from the foundation, and soil graded away from the house. Those steps do not remove sewage that is already on the floor. The crew does that cleanup. Leave plaster and trim in place until they have seen it." + cite("City of Birmingham Risk Management", BHAM),
        ),
        (
            "Who owns the pipe under a Birmingham yard?",
            "The public system is the city's to explain. The private lateral under the yard is a homeowner pipe unless the city tells you otherwise for that address. A camera inspection confirms a lateral. Roots at a joint are a common reason for a backup.",
        ),
    ],
    "berkley": [
        (
            "Is Berkley's sewer combined?",
            "Yes, as the city describes it: one pipe for stormwater and sewage, entirely gravity, with no pumps and no valves. Streets are designed to hold water so flow enters more slowly, and catch basins use restrictor covers. In a hard rain that shared pipe can push wastewater up a basement floor drain. Confirm your block with Public Works." + cite("City of Berkley, Flood Tips for Residents", BERK_TIPS),
        ),
        (
            "Who do I call in Berkley while the basement is wet?",
            "Report basement flooding to Berkley Public Works at 248-658-3490, and use the city's Sewer Backup Claims Form if you plan to claim. For sewage cleanup in the house, call (248) 825-8312." + cite("City of Berkley, Flood Tips for Residents", BERK_TIPS),
        ),
        (
            "Where does Berkley's sewage go when it rains hard?",
            "Flow leaves toward the Clinton River side: the George W. Kuhn district, then the Red Run Drain, then the Clinton. It does not go to the Rouge. Berkley is one of 14 communities in that district. In wet weather the combined flow there is typically more than 93 percent stormwater, which is why a fast storm can fill the shared pipes." + cite("Oakland County Water Resources Commissioner, George W. Kuhn Retention Treatment Basin", WRC_GWK),
        ),
        (
            "How long do I have to send Berkley written notice?",
            "Written notice is due within 45 days of discovery. Include your name, address, and phone, the property address, the discovery date, and a brief description. The city's claims form is the city process. Whether your homeowners policy has a sewer-backup endorsement is a question for your insurer." + cite("City of Berkley, Report a Claim", BERK_CLAIM) + cite("Michigan Legislature, MCL 691.1419", MCL1419),
        ),
        (
            "Why is a shop vac a poor idea in a Berkley bungalow?",
            "A household vac blows contaminated droplets through a small basement and up a short stair that opens near living space. Keep people and pets off that stair. Wait for a company equipped for sewage. Pumping is the extraction step. Cleaning what remains comes after the water is gone.",
        ),
    ],
    "clawson": [
        (
            "Who answers a Clawson sewer call?",
            "The city's main line on the sewer page is (248) 435-4500. Public works is open Monday through Thursday, 7:00 a.m. to 3:30 p.m., and closed on Fridays. After hours, Clawson uses Troy Police dispatch at 248-524-3477, extension 1. For sewage cleanup inside the house, call (248) 825-8312." + cite("City of Clawson, Sanitary and Storm Sewer System", CLAW_SEWER),
        ),
        (
            "Is every Clawson street a combined sewer?",
            "The city sewer page lists the George W. Kuhn Retention Treatment Basin and the Oakland County Water Resources Commissioner, and it links a combined-sewer explainer and Public Act 222. Confirm the pipe on your street with the city. Heavy rain can still load older lines and push sewage up a basement floor drain." + cite("City of Clawson, Sanitary and Storm Sewer System", CLAW_SEWER),
        ),
        (
            "How do I give Clawson written notice within 45 days?",
            "State law requires written notice within 45 days of discovering the damage, with your name, address, and phone, the property address, the discovery date, and a brief description. Ask the city in writing who receives sewer backup notices. Your insurer is a separate call. A sewer-backup endorsement is not on every policy." + cite("Michigan Legislature, MCL 691.1419", MCL1419),
        ),
        (
            "Who owns the lateral on a small Clawson lot?",
            "The main in the street is a question for the city. The lateral under the yard is usually the homeowner's pipe. A camera inspection tells them apart. The cleanup crew removes what is already in the one-room basement. They do not reline the city main.",
        ),
        (
            "What if the cleanup truck cannot fit a Clawson driveway?",
            "Say so when you call. Brick bungalows on tight lots often have to stage from the street. The crew should tell you whether they can work there before you agree.",
        ),
    ],
}

HERO = {
    "royal-oak": "Sewage coming up a floor drain in your Royal Oak basement is a health hazard, so keep people and pets out of the water. Call now for sewage cleanup in Royal Oak. A local crew handles sewer backup cleanup in Royal Oak, and they'll tell you when they can be there.",
    "troy": "Sewage backed up into your Troy basement or lower level? Don't try to mop it up yourself. One call gets you started on sewage cleanup in Troy. A local crew handles sewer backup cleanup in Troy, and they'll tell you when they can be there.",
    "birmingham": "Sewage in the basement of an older Birmingham home can soak into plaster, trim and finished floors quickly. Call for sewage cleanup in Birmingham. A local crew handles sewer backup cleanup in Birmingham. They'll tell you when they can be there.",
    "berkley": "When the floor drain by the laundry backs up in a Berkley bungalow, the sewage needs to come out before it spreads. Call for sewage cleanup in Berkley. A local crew handles sewer backup cleanup in Berkley, and they'll tell you when they can be there.",
    "clawson": "Sewage in your Clawson basement after a backup? Stay out of the water and call. A local crew handles sewage cleanup in Clawson and sewer backup cleanup in Clawson, and they'll tell you when they can be there.",
}

ALT = {
    "royal-oak": "Basement floor with standing water from a sewer backup, the situation Royal Oak homeowners call about",
    "troy": "Wet basement floor after a sewer backup, the kind of loss Troy homeowners ask for help with",
    "birmingham": "Standing wastewater on a basement floor during sewer backup cleanup, relevant to older Birmingham homes",
    "berkley": "Sewage water on a basement floor in a small house, a common Berkley backup scene",
    "clawson": "Backup water on a bungalow basement floor, a Clawson sewer cleanup situation",
}

DESCRIPTIONS = {
    "royal-oak": "Sewer backup cleanup in Royal Oak, MI. Get a local crew for sewage cleanup: pump-out, disinfecting and drying your basement. Call (248) 825-8312 now.",
    "troy": "Sewer backup cleanup in Troy, MI. A local crew handles sewage cleanup in split-levels and finished lower levels: pump-out and drying. Call (248) 825-8312.",
    "birmingham": "Sewer backup cleanup in Birmingham, MI. A local crew handles sewage cleanup in older homes with plaster, trim and finished floors. Call (248) 825-8312.",
    "berkley": "Sewer backup cleanup in Berkley, MI. A local crew handles sewage cleanup in your bungalow basement: pump-out, disinfecting and drying. Call (248) 825-8312.",
    "clawson": "Sewer backup cleanup in Clawson, MI. A local crew handles sewage cleanup in bungalow basements: pump-out, disinfecting and drying. Call (248) 825-8312.",
}
