"""Conservative sewer-backup pages. Titles and H1s stay on the ranking phrase.

Local risk paragraphs are the ones already published for these URLs, with contractor-voice
lines removed. They still need an owner fact-check (see the PR description).
"""
from site_config import PHONE_DISPLAY, PHONE_TEL

from sitegen.render import a, callout, h2, h3, nearby_section, note, ol, p, ul

WHY = {
    "royal-oak": (
        "Royal Oak's housing stock is largely pre-1960s, concentrated in established neighborhoods "
        "like Vinsetta Park, Northwood, and the areas surrounding downtown near Woodward Avenue. "
        "Homes of this era were commonly built with clay tile or cast-iron sewer laterals — materials "
        "that are far more prone to root intrusion, joint separation, and collapse over decades than "
        "modern PVC piping. Combined with Royal Oak's aging municipal storm and sanitary infrastructure, "
        "heavy spring rainfall or rapid summer storm surges can push more wastewater into the system "
        "than it can handle, forcing sewage back up through basement floor drains."
    ),
    "troy": (
        "Troy's neighborhoods span a wide range of housing ages, from 1960s–70s split-levels near "
        "Big Beaver Road to established subdivisions in areas like Northfield Hills. Many homes from "
        "this era still run on original clay tile or cast-iron sewer laterals — materials that develop "
        "interior scale and brittle joints over decades, giving tree roots an easy entry point. Troy's "
        "mature, tree-lined subdivisions compound this, while high water table conditions near the Big "
        "Beaver corridor increase flood risk during spring thaw and heavy summer storms."
    ),
    "birmingham": (
        "Birmingham's housing stock includes a significant share of homes from the 1920s through the "
        "1950s, in neighborhoods like Poppleton Park and the "
        "areas around Quarton Lake. These older homes commonly carry original cast-iron plumbing and sit "
        "on clay sewer laterals installed decades before modern PVC became standard. Birmingham's mature "
        "tree canopy means root intrusion is a frequent contributor to backups, especially in low-lying "
        "sections near Quarton Lake."
    ),
    "berkley": (
        "Berkley's housing stock is largely bungalow-style construction from the 1940s and 1950s, built "
        "with original clay or cast-iron sewer laterals that are reaching the end of their service life. "
        "Berkley's relatively flat topography means heavy "
        "rain has limited places to drain quickly. Combined with older municipal combined sewer lines, "
        "heavy rain events push extra wastewater volume back up through basement floor drains in older homes."
    ),
    "clawson": (
        "Clawson's housing stock is predominantly mid-century brick bungalows and ranches built between the 1940s and 1960s on "
        "compact city lots. Homes of this era commonly run on original clay or cast-iron sewer laterals, "
        "which after decades of use are prone to root intrusion at pipe joints and internal corrosion "
        "that narrows usable pipe diameter. Heavy regional storm events in southeast Oakland County put "
        "extra strain on older sanitary infrastructure, contributing to Category 3 sewer-backup exposure "
        "during rainstorms."
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
        f"This referral line covers Royal Oak neighborhoods along the {a('https://en.wikipedia.org/wiki/Woodward_Avenue', 'Woodward Avenue corridor')}, "
        f"near the Royal Oak Music Theatre, and toward the {a('https://en.wikipedia.org/wiki/Detroit_Zoo', 'Detroit Zoo')}. "
        "It is not a staffed office at those landmarks."
    ),
    "troy": (
        "This referral line covers Troy neighborhoods along Big Beaver Road, near Somerset Collection, "
        "and out toward Troy Historic Village. It is not a staffed office at those places."
    ),
    "birmingham": (
        "This referral line covers Birmingham homes around downtown, Shain Park, Poppleton Park, and the Quarton area. "
        "It is not a staffed office in the city."
    ),
    "berkley": (
        "This referral line covers Berkley bungalow blocks and the 12 Mile Road corridor. "
        "It is not a staffed office in the city."
    ),
    "clawson": (
        "This referral line covers Clawson's brick-bungalow blocks and the 14 Mile Road downtown strip. "
        "It is not a staffed office in the city."
    ),
}

OWNER = {
    "royal-oak": (
        "This URL is sewage cleanup in Royal Oak, MI and the sewer backup cleanup page for the same older "
        "houses. The pumping step, once wastewater is on the floor, is a different page so the two do not "
        f"compete: {a('/royal-oak-sewage-extraction', 'sewage extraction in Royal Oak')}. Oakland Sewer Pros "
        "does not send a truck. Ask the company you reach for a written scope and for the license and "
        "insurance the job requires."
    ),
    "troy": (
        "People looking up sewage cleanup in Troy, MI should stay on this page. It is also the sewer backup "
        "cleanup page for split-levels and subdivision basements. Pumping the water out is "
        f"{a('/troy-sewage-extraction', 'sewage extraction in Troy')}, written separately so the extraction "
        "page does not try to rank for the cleanup phrase. We do not quote a Troy price or promise a crew."
    ),
    "birmingham": (
        "Sewage cleanup in Birmingham, MI and sewer backup cleanup are the same visit for these older houses, "
        "and this is the page for both. If you already know the lower level is wet and you only need the "
        f"water removed, use {a('/birmingham-sewage-extraction', 'sewage extraction in Birmingham')} instead. "
        "The company you hire sets the methods. This site does not."
    ),
    "berkley": (
        "Sewage cleanup in Berkley, MI belongs here, with the bungalow floor-drain backups. Sewer backup "
        "cleanup is the same topic on this URL. "
        f"{a('/berkley-sewage-extraction', 'Sewage extraction in Berkley')} is only the removal step, and "
        "that page should not be used as a second copy of this one. Call to reach an independent provider "
        "when one is participating."
    ),
    "clawson": (
        "Sewage cleanup in Clawson, MI is this page, including sewer backup cleanup in the brick bungalows "
        "on short lots. The extraction URL is "
        f"{a('/clawson-sewage-extraction', 'sewage extraction in Clawson')}, for the pump-out itself. "
        "Keep the two straight: cleanup and causes here, hoses and access there. We do not stage equipment "
        "on 14 Mile."
    ),
}

SEWAGE_H2 = {
    "royal-oak": (
        "Sewage cleanup in Royal Oak is the contaminated-water part of a sewer backup: water that came out of a floor drain, "
        "a laundry standpipe, or a basement toilet and should be treated as heavily soiled. A provider who only pumps the "
        f"visible puddle can leave residue in the pad and the wall base. If the backup also soaked finishes, see {a('/royal-oak-water-damage-restoration', 'water damage restoration in Royal Oak')} "
        f"and {a('/royal-oak-flooded-basement', 'flooded basement cleanup and water removal in Royal Oak')}."
    ),
    "troy": (
        "Sewage cleanup in Troy means dealing with water that left the sanitary line, not a clean rain leak. Split-level "
        "lower floors near Big Beaver often hold carpet and storage right where a backup surfaces. Ask the company you hire "
        f"how they will separate that water from the rest of the house. Related pages: {a('/troy-water-damage-restoration', 'water damage restoration in Troy')} "
        f"and {a('/troy-flooded-basement', 'flooded basement cleanup in Troy')}."
    ),
    "birmingham": (
        "Sewage cleanup in Birmingham is especially unforgiving in older houses where plaster, wood trim, and finished lower "
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
            "<strong>Call " + city + " help at the number above</strong> to be connected with an independent provider. How fast someone arrives depends on who is available. This site does not promise a response time.",
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
            "City public works can tell you whether a street has separate storm and sanitary sewers and how "
            f"to report a backup that looks like it is coming from the municipal main. For {city}, start with "
            "the city's own website rather than a third-party listing. A private lateral under the yard is "
            "usually the homeowner's pipe; the city main in the street is a different asset. The company you "
            "hire should not guess which one failed."
        ),
        h2(f"Sewer backup cleanup in {city}, MI"),
        p(
            f"{city} homeowners use this page after sewage comes up through a basement drain, a laundry "
            "standpipe, or a basement toilet. Treat that water as Category 3: keep people and pets out, "
            "do not mop it through the house, and do not run a household vac. The steps below are the "
            "first minutes. The cleanup itself is the independent provider's work."
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
            "Does Royal Oak have a combined sewer system that increases backup risk?",
            "Many older sections of Royal Oak were built before separated storm and sanitary sewers were standard. Where sewers are combined or simply old, a heavy summer storm can load the pipes and push sewage toward basement floor drains. Royal Oak's public works department can confirm what serves a specific street. Oakland Sewer Pros does not map the city system.",
        ),
        (
            "Who performs sewer backup cleanup in Royal Oak?",
            "An independent restoration or cleanup company does the work. Oakland Sewer Pros is a referral service. We do not employ technicians, own trucks, or guarantee the job. Confirm the company's license and insurance yourself.",
        ),
        (
            "How should a Royal Oak homeowner think about drying time?",
            "After sewage is removed, drying building materials often takes several days. The provider should explain how they will check moisture. This site does not set or promise that schedule.",
        ),
        (
            "Does homeowners insurance pay for a Royal Oak sewer backup?",
            "Not automatically. Many policies exclude sewer backup unless a separate endorsement is on the policy. Ask your insurer what your form covers. Oakland Sewer Pros does not file claims or bill insurance companies.",
        ),
    ],
    "troy": [
        (
            "Does Troy's storm drainage add to sewer backup risk?",
            "Troy's Streets and Drains Division maintains a large storm-drainage network. Older blocks can still load up faster in a hard rain than newer subdivisions built to later standards. Confirm your street with the city. This page is not a city record.",
        ),
        (
            "Who does the sewage cleanup work in Troy?",
            "A separate local company does the cleanup. Calling the number here connects you when a participating provider is available. Oakland Sewer Pros does not perform the cleanup and does not quote a price for it.",
        ),
        (
            "What should Troy homeowners do about a gurgling floor drain?",
            "Stop running water and treat a gurgling basement drain as a warning, especially in older split-levels near Big Beaver. Do not snake it yourself if you smell sewage. Call to be matched with a provider, and call the city if you believe the main in the street is surcharging.",
        ),
        (
            "Will insurance cover a Troy sewer backup?",
            "Coverage depends on your policy. Sewer backup is often excluded unless you bought an endorsement. Read your form or ask your agent. The provider you hire may document the loss; this website does not.",
        ),
    ],
    "birmingham": [
        (
            "Are older Birmingham houses more prone to sewer backups?",
            "Houses in Birmingham's older sections often still have clay or cast-iron laterals. Those materials crack, separate, and invite roots, which is why backups show up more often there than in newer construction. A camera inspection by a plumber or the city is how you confirm a specific lateral, not a page on this site.",
        ),
        (
            "Who cleans up sewage in a Birmingham home?",
            "An independent provider you hire. Oakland Sewer Pros only makes the connection. Ask that company how they will protect plaster and finished floors, and ask for license and insurance before they start.",
        ),
        (
            "Should I cut out wet drywall in Birmingham before anyone arrives?",
            "No. Sewage-soaked material is contaminated, and opening walls can spread it. Keep people out and let the company you hire decide what comes out, based on what got wet.",
        ),
        (
            "Does a standard Birmingham homeowners policy cover sewage backup?",
            "Many do not, unless a sewer-backup endorsement is listed. Check with your insurer. This site does not interpret policies or submit claims.",
        ),
    ],
    "berkley": [
        (
            "Does Berkley still have combined sewer sections?",
            "Berkley's own master plan describes the city's sewers as a combined system that carries storm and sanitary flow together to the regional George W. Kuhn Drain. During hard rain that shared capacity can push water back through basement drains. Confirm the pipe in front of your house with the city. Treat this as a reason to ask, not as a map.",
        ),
        (
            "Who does sewage cleanup in a Berkley bungalow?",
            "An independent company matched through this line, if a provider is participating. This page is that sewage cleanup. The pumping-only step is the Berkley sewage extraction page. Oakland Sewer Pros does not own equipment and does not station a crew in Berkley.",
        ),
        (
            "Why is a shop vac a poor idea for Berkley sewage water?",
            "A household vac aerosolizes contaminated water in a small basement and on a short stair. That is a health problem in a bungalow where the stairs open near living space. Wait for a company equipped for sewage.",
        ),
        (
            "Is sewer-backup damage covered on a Berkley homeowners policy?",
            "Only if your policy says so. Endorsements are common add-ons, not the default. Ask your insurer. We do not bill carriers.",
        ),
    ],
    "clawson": [
        (
            "Why do Clawson bungalows see sewer backups?",
            "A large share of Clawson is mid-century brick bungalows and ranches on small lots, often still on clay or cast-iron laterals. Roots and corrosion narrow those pipes. Heavy rain adds load. Whether your lateral or the city main failed is a fact for the city or a camera inspection, not a guess from this website.",
        ),
        (
            "Who shows up for sewer backup cleanup in Clawson?",
            "An independent provider, when one is available through this referral line. We do not guarantee arrival, price, or the outcome of the work.",
        ),
        (
            "What if the cleanup truck cannot fit a Clawson driveway?",
            "Say so when you call. Compact lots and short drives are common. A provider should tell you whether they can stage from the street before you agree to the job.",
        ),
        (
            "Does insurance automatically cover a Clawson sewage backup?",
            "No. Ask your insurer whether a sewer-backup endorsement is on the policy. Oakland Sewer Pros does not file the claim.",
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
