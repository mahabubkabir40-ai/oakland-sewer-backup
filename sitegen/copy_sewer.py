"""Conservative sewer-backup pages. Titles and H1s stay on the ranking phrase.

Local risk paragraphs are the ones already published for these URLs, with contractor-voice
lines removed. They still need an owner fact-check (see the PR description).
"""
from site_config import PHONE_DISPLAY, PHONE_TEL

from sitegen.render import a, callout, h2, h3, nearby_section, note, ol, p, ul

WHY = {
    "royal-oak": (
        "If the house is pre-1960s, in Vinsetta Park, Northwood, or near downtown along Woodward Avenue, "
        "the sewer lateral is often clay tile or cast iron. Those pipes take roots, open at the joints, "
        "and collapse over decades more readily than modern PVC. Royal Oak's older storm and sanitary "
        "mains can also fill in a heavy spring rain or a fast summer storm and push sewage back up the "
        "basement floor drain."
    ),
    "troy": (
        "A 1960s or 1970s split-level near Big Beaver Road, or a house in a subdivision such as "
        "Northfield Hills, often still has its original clay or cast-iron lateral. Scale builds up "
        "inside those pipes, the joints get brittle, and tree roots on a mature street find the opening. "
        "Residents also describe a high water table near the Big Beaver corridor, so spring thaw and a "
        "hard summer storm both raise the chance that the lower level takes water."
    ),
    "birmingham": (
        "Houses from the 1920s through the 1950s, in Poppleton Park and around Quarton Lake, commonly "
        "still have cast-iron plumbing and clay sewer laterals from before PVC. The mature trees that "
        "make those streets look the way they do also send roots into the joints. Low ground near "
        "Quarton Lake is where that shows up most often as a backup."
    ),
    "berkley": (
        "Most Berkley houses are 1940s and 1950s bungalows on original clay or cast-iron laterals that "
        "are near the end of a long service life. The city is flat, so a hard rain has few places to go. "
        "Older municipal lines have been described as combined, and in a storm that shared pipe can push "
        "wastewater back up the basement floor drain. Confirm the pipe on your block with the city."
    ),
    "clawson": (
        "Clawson is mostly mid-century brick bungalows and ranches from the 1940s to the 1960s, on "
        "compact lots. The lateral is often original clay or cast iron. After decades, roots enter at "
        "the joints and corrosion narrows the pipe. A heavy regional storm then loads those older sanitary "
        "lines, and sewage can come up inside the house."
    ),
}

TRIGGERS = {
    "royal-oak": [
        "Sudden basement backups following heavy summer thunderstorms",
        "Slow-draining or gurgling floor drains that precede a full backup by hours or days",
        "Backups tied to aging sump pump systems that cannot keep pace during storm surges",
        "Root intrusion in older sewer laterals, especially on tree-lined streets near downtown",
    ],
    "troy": [
        "Backups following spring thaw as frozen ground releases and shifts around aging pipe joints",
        "Storm surges near the Big Beaver Road corridor overwhelming aging storm drainage",
        "Root intrusion in older clay laterals throughout established subdivisions",
        "Sump pump failures during high-water-table conditions on lower-lying lots",
    ],
    "birmingham": [
        "Backups in older homes tied to original clay or cast-iron laterals",
        "Root intrusion from mature trees along Birmingham's older residential streets",
        "Heavy spring and fall rain overwhelming aging storm and sanitary lines",
        "Basement flooding near Quarton Lake and other low-lying residential sections",
    ],
    "berkley": [
        "Backups tied to older sections that still carry storm and sanitary flow together during heavy rain",
        "Root intrusion in clay sewer laterals common to 1940s–50s bungalow construction",
        "Sump pump overload during downpours on Berkley's flat, slow-draining lots",
        "Water reaching original hardwood floors and framing in older homes",
    ],
    "clawson": [
        "Root intrusion through clay pipe joints common to mid-century bungalow construction",
        "Internal corrosion in older cast-iron lines reducing the pipe's usable diameter",
        "Backups following heavy regional rain that overwhelms aging sanitary lines",
        "Tight lots where equipment has to be staged from a short driveway or the street",
    ],
}

AREA_LINE = {
    "royal-oak": (
        f"The same phone number covers Royal Oak neighborhoods along the {a('https://en.wikipedia.org/wiki/Woodward_Avenue', 'Woodward Avenue corridor')}, "
        f"near the Royal Oak Music Theatre, and toward the {a('https://en.wikipedia.org/wiki/Detroit_Zoo', 'Detroit Zoo')}. "
        "Your call is a referral for the house."
    ),
    "troy": (
        "The same phone number covers Troy neighborhoods along Big Beaver Road, near Somerset Collection, "
        "and out toward Troy Historic Village. Your call is a referral for the house."
    ),
    "birmingham": (
        "The same phone number covers Birmingham homes around downtown, Shain Park, Poppleton Park, and the Quarton area. "
        "Your call is a referral for the house."
    ),
    "berkley": (
        "The same phone number covers Berkley bungalow blocks and the 12 Mile Road corridor. "
        "Your call is a referral for the house."
    ),
    "clawson": (
        "The same phone number covers Clawson's brick-bungalow blocks and the 14 Mile Road downtown strip. "
        "Your call is a referral for the house."
    ),
}

OWNER = {
    "royal-oak": (
        "Once wastewater is on the floor, the pumping step is "
        f"{a('/royal-oak-sewage-extraction', 'sewage extraction in Royal Oak')}. Keep people and pets "
        "out of that water until it is gone. The company you reach is independent, and this line makes "
        "the introduction. Ask them for a written scope and for the license and insurance the job requires."
    ),
    "troy": (
        "Pumping the water out of a split-level or a subdivision basement is "
        f"{a('/troy-sewage-extraction', 'sewage extraction in Troy')}. The price and the crew come from "
        "that company. Ask them for a written scope before anyone starts."
    ),
    "birmingham": (
        "If the lower level is already wet and you only need the water removed, use "
        f"{a('/birmingham-sewage-extraction', 'sewage extraction in Birmingham')}. "
        "The company you hire sets the methods and does the work. Ask them how they will protect "
        "plaster and trim before they cut anything."
    ),
    "berkley": (
        "If the bungalow floor drain already overflowed, pumping the water out is "
        f"{a('/berkley-sewage-extraction', 'Sewage extraction in Berkley')}. Call to reach an independent "
        "provider when one is participating. Keep people off the short stair until that water is gone."
    ),
    "clawson": (
        "The pump-out, once sewage is on the floor of a brick bungalow, is "
        f"{a('/clawson-sewage-extraction', 'sewage extraction in Clawson')}. Hoses and access are part of "
        "that visit. The crew that comes is independent. This line makes the introduction."
    ),
}

SEWAGE_H2 = {
    "royal-oak": (
        "Sewage cleanup in Royal Oak is the water that came out of a floor drain, "
        "a laundry standpipe, or a basement toilet. Treat it as heavily soiled. A provider who only pumps the "
        f"visible puddle can leave residue in the pad and the wall base. If the backup also soaked finishes, see {a('/royal-oak-water-damage-restoration', 'water damage restoration in Royal Oak')} "
        f"and {a('/royal-oak-flooded-basement', 'flooded basement cleanup and water removal in Royal Oak')}."
    ),
    "troy": (
        "Sewage cleanup in Troy is water that left the sanitary line, not a clean rain leak. Split-level "
        "lower floors near Big Beaver often hold carpet and storage right where a backup surfaces. Ask the company you hire "
        f"how they will separate that water from the rest of the house. Related pages: {a('/troy-water-damage-restoration', 'water damage restoration in Troy')} "
        f"and {a('/troy-flooded-basement', 'flooded basement cleanup in Troy')}."
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
        "Sewage cleanup in Clawson often starts at a floor drain in a mid-century brick bungalow. Compact lots limit where "
        "hoses and drying gear can sit, so ask how the provider will stage the job before you book. When the loss is broader "
        f"than the drain itself, use {a('/clawson-water-damage-restoration', 'water damage restoration in Clawson')} and "
        f"{a('/clawson-flooded-basement', 'flooded basement water removal in Clawson')}."
    ),
}


def first_ten(city):
    return callout(
        f"What to do in the first 10 minutes of a sewer backup in {city}",
        ol([
            "<strong>Stop using water.</strong> Do not run faucets, flush toilets, or run the washer or dishwasher.",
            "<strong>Keep people and pets out</strong> of the water. Sewage carries bacteria and other pathogens.",
            "<strong>Do not plunge or snake</strong> the drain. A household snake can push dirty water into the subfloor.",
            "<strong>Leave the basement if water is near outlets,</strong> the panel, or the furnace. Shut power off only from a dry location.",
            "<strong>Call " + city + " help at the number above</strong> and you are connected with an independent provider, and they'll tell you when they can be there.",
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
        "Troy takes written sewer backup claims through the City Attorney's Office, and state law sets a 45-day deadline "
        f"from discovery. The form, the contact, and what to photograph are in the {_GUIDE}. The {_CHECK} "
        "covers the steps before and during a storm."
    ),
    "birmingham": (
        "Birmingham posts a Sewer Backup Claim form on its Risk Management page and notes that its water event tracking "
        f"form is not a claim. The 45-day notice rule and a documentation list are in the {_GUIDE}; storm prep is on the {_CHECK}."
    ),
    "berkley": (
        "Berkley's Notice of Claim form goes to the City Manager's Office, and Michigan law gives you 45 days from discovery "
        f"to send written notice. Details are in the {_GUIDE}. The city's master plan describes Berkley's sewers as combined, so the {_CHECK} "
        "is worth printing before spring storms."
    ),
    "clawson": (
        "Clawson's DPW handles sewer calls; we did not find a posted claim form, so ask the city in writing who receives "
        f"notices. The 45-day written notice rule is explained in the {_GUIDE}, and the {_CHECK} lists what to do during a storm."
    ),
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
            f"More Troy pages: {a('/troy-sewage-extraction', 'sewage extraction')}, "
            f"{a('/troy-flooded-basement', 'flooded basement cleanup')}, "
            f"{a('/troy-basement-sanitization', 'sanitizing after a backup')}, "
            f"{a('/troy-sump-pump-repair', 'sump pump repair')}, and "
            f"{a('/troy', 'the Troy overview')}."
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
    return "\n".join([
        h2(f"Sewage Cleanup {city}, MI"),
        p(SEWAGE_H2[slug]),
        p(OWNER[slug]),
        p(
            f"If the backup looks like the city main, call {city} public works while the water is still coming in "
            "and ask whether your street has separate storm and sanitary sewers. Use the city's own website "
            "for that number. The lateral under the yard is usually your pipe. The main in the street is the city's. "
            "Ask the cleanup company not to guess which one failed."
        ),
        h2(f"Sewer backup cleanup in {city}, MI"),
        p(
            f"Sewage cleanup in {city} usually starts when sewage comes up a basement drain, a laundry "
            "standpipe, or a basement toilet. Keep people and pets out, do not mop it through the house, "
            "and do not run a household vac. The steps below are the first minutes. After you call, an "
            "independent cleanup company does the work, and they'll tell you when they can be there."
        ),
        h3(f"Why {city} homes are at higher risk"),
        p(WHY[slug]),
        h3(f"Common backup triggers in {city}"),
        ul(TRIGGERS[slug]),
        first_ten(city),
        note(AREA_LINE[slug]),
        p(CLAIM_LINE[slug]),
        p(resources[slug]),
        nearby_section("sewer-cleanup", "Sewer backup cleanup", slug),
    ])


FAQS = {
    "royal-oak": [
        (
            "Who do I call at the City of Royal Oak during a sewer backup?",
            "For basement water, the city lists (248) 246-3300 on weekdays from 7:30 a.m. to 4:00 p.m. After hours, police non-emergency (248) 246-3500 dispatches sewer personnel. Call (248) 825-8312 when you need an independent cleanup company inside the house. That call connects you when a participating provider is available.",
        ),
        (
            "Who owns the sewer lateral in Royal Oak?",
            "The city says it is responsible for the main, and the homeowner for the lateral up to and including the connection. The Sewer Division maintains about 300 miles of sanitary and storm sewers. Ask them about the main. A camera inspection is how a plumber or the city checks a specific lateral.",
        ),
        (
            "How long do I have to send Royal Oak written notice?",
            "Michigan law requires written notice within 45 days of discovering the damage before compensation for a sewage disposal event is possible. Include your name, address, and phone, the property address, the date you discovered the damage, and a brief description. Confirm with the city who receives that letter. A sewer-backup endorsement on your homeowners policy is a separate question for your insurer.",
        ),
        (
            "Are Royal Oak sewers combined?",
            "Many older sections were built before separated storm and sanitary sewers were standard. Where pipes are combined or simply old, a heavy summer storm can push sewage toward a basement floor drain. Royal Oak is a member of the former Twelve Towns program, now the George W. Kuhn Retention Treatment Basin, which was expanded in 2006. The Sewer Division can confirm the pipe on your street.",
        ),
        (
            "What happens when I call (248) 825-8312 about a Royal Oak backup?",
            "When a participating independent cleanup company is available, the call is connected to them. They do the work in the house. Ask for a written scope and for the license and insurance the job requires. How soon they can come depends on that company. After the water is out, drying often takes several days. Ask them how they will check moisture. A sewer-backup endorsement, if you need one, is a question for your insurer, separate from the city letter.",
        ),
    ],
    "troy": [
        (
            "Who does Troy tell residents to call for a sewer backup?",
            "The Water Division number is 248-524-3370 during business hours. After hours, Troy Police is 248-524-3477. Call (248) 825-8312 to reach an independent cleanup company for the house when one is available. That line is not the Water Division.",
        ),
        (
            "Is Troy on one combined sewer?",
            "No single label fits. A November 14, 2022 City Council agenda item says Troy discharges wastewater through the Evergreen-Farmington, Oakland-Troy, and George W. Kuhn districts. The Oakland County Water Resources Commissioner is responsible for those district facilities. Ask the city which district serves your address before you assume the pipe in the street.",
        ),
        (
            "Where does a written Troy sewer claim go?",
            "Troy directs written claims to the City Attorney's Office. State law sets 45 days from the day you discover the damage. The notice needs your name, address, and phone, the property address, the discovery date, and a brief description. A sewer-backup rider, if you have one, is a separate call to your insurer.",
        ),
        (
            "Who is responsible for a Troy sewer lateral?",
            "The main in the street is a city question. The lateral under the yard is usually the homeowner's pipe. Confirm the split for your address with the city. A camera answers the private lateral. The cleanup company removes what already entered the lower level.",
        ),
        (
            "What should I do about a gurgling floor drain near Big Beaver?",
            "Stop running water. Treat a gurgling basement drain as a warning, especially in a 1960s or 1970s split-level. Do not snake it if you smell sewage. Call the city if you think the main is surcharging, and call (248) 825-8312 to reach an independent cleanup company. The price and the crew come from that company.",
        ),
    ],
    "birmingham": [
        (
            "Who do I call in Birmingham if sewage is in the lower level?",
            "The water event line, (248) 530-1703, collects flooding data. It is not a claim. Claims questions are 248.530.1808, and the city says claims go through the Michigan Municipal League Liability and Property Pool and Meadowbrook Claims Service. For cleanup inside the house, call (248) 825-8312. You are connected with an independent company when one is available.",
        ),
        (
            "Can a hard rain overload Birmingham's older sewers?",
            "The city's Risk Management FAQ says older communities have combined sewer and storm systems. Those sewers were historically designed for about 2 inches of rain in one hour, which the city calls a 10-year storm. The system is gravity, and Birmingham owns no sewage pump or lift stations. A late-1990s bond financed relief sewers in part of the city, not on every street.",
        ),
        (
            "What is the 45-day notice for a Birmingham sewer backup?",
            "Written notice is due within 45 days of discovering the damage. Include your name, address, and phone, the property address, the discovery date, and a brief description. Use the city's sewer backup claim form. The water-event tracking form is not that claim. Ask your insurer separately about a sewer-backup endorsement.",
        ),
        (
            "What does Birmingham suggest before the next storm?",
            "The city FAQ lists a backflow preventer, downspouts disconnected and extended about 6 feet from the foundation, and soil graded away from the house. Those steps do not remove sewage that is already on the floor. The company you hire does that cleanup. Leave plaster and trim in place until they have seen it.",
        ),
        (
            "Who owns the pipe under a Birmingham yard?",
            "The public system is the city's to explain. The private lateral under the yard is a homeowner pipe unless the city tells you otherwise for that address. A camera inspection confirms a lateral. Early- and mid-1900s houses often still have clay or cast iron, and roots at the joints are a common reason for a backup.",
        ),
    ],
    "berkley": [
        (
            "Is Berkley's sewer combined?",
            "Yes, as the city describes it: one pipe for stormwater and sewage, entirely gravity, with no pumps and no valves. Streets are designed to hold water so flow enters more slowly, and catch basins use restrictor covers. In a hard rain that shared pipe can push wastewater up a basement floor drain. Confirm your block with Public Works.",
        ),
        (
            "Who do I call in Berkley while the basement is wet?",
            "Public Works is 248-658-3490 for the city system, and the city posts a Sewer Backup Claims Form. Call (248) 825-8312 to reach an independent cleanup company for the bungalow when one is available. Say the stair is short so they know the equipment has to fit.",
        ),
        (
            "Where does Berkley's sewage go when it rains hard?",
            "Flow leaves toward the Clinton River side: the George W. Kuhn district, then the Red Run Drain, then the Clinton. It does not go to the Rouge. Berkley is one of 14 communities in that district. In wet weather the combined flow there is typically more than 93 percent stormwater, which is why a fast storm can fill the shared pipes.",
        ),
        (
            "How long do I have to send Berkley written notice?",
            "Written notice is due within 45 days of discovery. Include your name, address, and phone, the property address, the discovery date, and a brief description. The city's claims form is the city process. Whether your homeowners policy has a sewer-backup endorsement is a question for your insurer.",
        ),
        (
            "Why is a shop vac a poor idea in a Berkley bungalow?",
            "A household vac blows contaminated droplets through a small basement and up a short stair that opens near living space. Keep people and pets off that stair. Wait for a company equipped for sewage. Pumping is the extraction step. Cleaning what remains comes after the water is gone.",
        ),
    ],
    "clawson": [
        (
            "Who answers a Clawson sewer call?",
            "The city main line on the sewer page is (248) 435-4500. Public works is open Monday through Thursday, 7:00 a.m. to 3:30 p.m., and closed on Fridays. After hours, Clawson uses Troy Police dispatch at 248-524-3477, extension 1. That dispatch line is the city's path, not a cleanup crew. Call (248) 825-8312 to reach an independent company for the house when one is available.",
        ),
        (
            "Is every Clawson street a combined sewer?",
            "The city sewer page lists the George W. Kuhn Retention Treatment Basin and the Oakland County Water Resources Commissioner, and it links a combined-sewer explainer and Public Act 222. Confirm the pipe on your street with the city. Heavy rain can still load older lines and push sewage up a floor drain in a mid-century brick bungalow.",
        ),
        (
            "How do I give Clawson written notice within 45 days?",
            "State law requires written notice within 45 days of discovering the damage, with your name, address, and phone, the property address, the discovery date, and a brief description. Ask the city in writing who receives sewer backup notices. Your insurer is a separate call. A sewer-backup endorsement is not on every policy.",
        ),
        (
            "Who owns the lateral on a small Clawson lot?",
            "The main in the street is a question for the city. The lateral under the yard is usually the homeowner's pipe. A camera inspection tells them apart. The cleanup crew removes what is already in the one-room basement. They do not reline the city main.",
        ),
        (
            "What if the cleanup truck cannot fit a Clawson driveway?",
            "Say so when you call. Brick bungalows on tight lots often have to stage from the street. The provider should tell you whether they can work there before you agree. The crew, the arrival, and the price come from that company.",
        ),
    ],
}

HERO = {
    "royal-oak": "Sewage coming up a floor drain in your Royal Oak basement is a health hazard, so keep people and pets out of the water. Call now for sewage cleanup in Royal Oak. We connect you with an independent local company that handles sewer backup cleanup in Royal Oak, and they'll tell you when they can be there.",
    "troy": "Sewage backed up into your Troy basement or lower level? Don't try to mop it up yourself. One call gets you started on sewage cleanup in Troy. We connect you with an independent local company for sewer backup cleanup in Troy, and they'll tell you when they can be there.",
    "birmingham": "Sewage in the basement of an older Birmingham home can soak into plaster, trim and finished floors quickly. Call for sewage cleanup in Birmingham and we'll connect you with an independent local company that does sewer backup cleanup in Birmingham. They'll tell you when they can be there.",
    "berkley": "When the floor drain by the laundry backs up in a Berkley bungalow, the sewage needs to come out before it spreads. Call for sewage cleanup in Berkley. We connect you with an independent local company for sewer backup cleanup in Berkley, and they'll tell you when they can be there.",
    "clawson": "Sewage in your Clawson basement after a backup? Stay out of the water and call. We connect you with an independent local company for sewage cleanup in Clawson and sewer backup cleanup in Clawson, and they'll tell you when they can be there.",
}

ALT = {
    "royal-oak": "Basement floor with standing water from a sewer backup, the situation Royal Oak homeowners call about",
    "troy": "Wet basement floor after a sewer backup, the kind of loss Troy homeowners ask for help with",
    "birmingham": "Standing wastewater on a basement floor during sewer backup cleanup, relevant to older Birmingham homes",
    "berkley": "Sewage water on a basement floor in a small house, a common Berkley backup scene",
    "clawson": "Backup water on a bungalow basement floor, a Clawson sewer cleanup situation",
}

DESCRIPTIONS = {
    "royal-oak": "Sewage cleanup in Royal Oak, MI, and sewer backup cleanup for the same houses. Independent providers. Call {PHONE_DISPLAY}.",
    "troy": "Sewage cleanup in Troy, MI for lower levels and split-levels, plus sewer backup cleanup. Call {PHONE_DISPLAY}.",
    "birmingham": "Sewage cleanup in Birmingham, MI for older homes, and sewer backup cleanup. Independent providers. Call {PHONE_DISPLAY}.",
    "berkley": "Sewage cleanup in Berkley, MI bungalows, and sewer backup cleanup on this page. Call {PHONE_DISPLAY} to connect.",
    "clawson": "Sewage cleanup in Clawson, MI and sewer backup cleanup for brick bungalows. Independent providers. Call {PHONE_DISPLAY}.",
}
