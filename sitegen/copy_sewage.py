"""Unique sewage-extraction pages. Not city-swapped templates."""
from site_config import PHONE_DISPLAY, PHONE_TEL

from sitegen.render import a, callout, h2, h3, nearby_section, p, ul

def royal_oak():
    return "\n".join([
        p(
            "Sewage extraction in Royal Oak is the removal step: pumping contaminated water out and taking "
            "the soaked material with it. If you still need the first minutes and why older laterals "
            "back up, read "
            + a("/royal-oak-sewer-cleanup", "the sewer backup cleanup page")
            + ". Call when the water is already on the floor and you need it pumped out."
        ),
        h2("Sewage extraction on Royal Oak's older residential blocks"),
        p(
            "Downtown Royal Oak gets the attention, but basement backups happen in houses on the side streets too: "
            "a floor drain in a basement under a house on a side street. The water is not rain that blew "
            "in a window. It came up out of the plumbing. That is sewage extraction, and it is a different "
            "job from mopping a clean-water leak."
        ),
        p(
            "Royal Oak's Sewer Division maintains about 300 miles of sanitary and storm sewers. The city is "
            "responsible for the main, and the homeowner for the lateral up to and including the connection. "
            "Whether the backup is your lateral or the city main is a question for the city, not a guess. "
            + a("https://www.romi.gov/384/Sewer-Division", "Royal Oak's Sewer Division")
            + " publishes city sewer information and is the right place to ask about the public main."
        ),
        h3("What extraction means in a Royal Oak basement"),
        p(
            "Extraction means removing the contaminated water and the residue it left, not just the puddle you "
            "can see from the stairs. Concrete holds moisture. The bottom of wood studs and the paper face of "
            "drywall hold sewage. A crew should tell you, in writing, how far up the wall they intend to "
            "remove material and how they will keep the stair and the first floor from getting splashed."
        ),
        p(
            "The vacuum truck and the crew belong to the crew. Call "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " and a local crew handles the visit. Ask what "
            "equipment they will bring to a typical Royal Oak side-street driveway. Some lots near downtown are short."
        ),
        h3("Sewage versus a clean-water leak"),
        ul([
            "Toilet, floor drain, or laundry standpipe overflowing points to the sanitary line.",
            "A window well full of rain, with no smell from the drains, is a different problem. See "
            + a("/royal-oak-flooded-basement", "flooded basement cleanup in Royal Oak") + ".",
            "If both happen in the same storm, say so. Mixed water is still treated as sewage once the drain has discharged.",
            "Groundwater through a cracked cove joint can look clear and still need "
            + a("/royal-oak-water-damage-restoration", "water damage restoration") + " if it soaked finishes.",
        ]),
        h2("What to ask before anyone extracts sewage in Royal Oak"),
        p(
            "Ask who is licensed for the work, whether they carry liability insurance, and whether the price "
            "covers haul-away of porous material or only pumping. The price comes from that company, and "
            "your insurance claim stays with your carrier. Southern Oakland County drainage, including parts of Royal Oak, is "
            "tied to county facilities associated with the Oakland County Water Resources Commissioner and the "
            "George W. Kuhn district, the former Twelve Towns Drain. That is a county system, not a promise "
            "that your street is inside a particular basin. Confirm the street with the city."
        ),
        callout(
            "While you wait in Royal Oak",
            ul([
                "Stop flushing and stop the laundry. More water from the house has nowhere to go but the basement.",
                "Keep children and pets off the stairs. Sewage on shoes walks into the kitchen.",
                "Do not run a household fan across the water. It blows contamination into the rest of the house.",
                "If the water is near the electrical panel, stay out and call from the first floor.",
            ]),
        ),
        p(
            "After the water is out, porous material that soaked up sewage usually cannot be wiped and kept. "
            + a("/royal-oak-basement-sanitization", "Sanitizing a Royal Oak basement after sewage")
            + " explains that step. If a sump was part of the event, see "
            + a("/royal-oak-sump-pump-repair", "sump pump repair in Royal Oak")
            + ". The city overview is " + a("/royal-oak", "Royal Oak services") + "."
        ),
        nearby_section("sewage-extraction", "Sewage extraction", "royal-oak"),
    ])


def troy():
    return "\n".join([
        p(
            "Sewage extraction here means getting contaminated water out of a Troy split-level or a "
            "finished lower level, along with the materials it ruined. If you are still sorting out "
            "what happened, start with "
            + a("/troy-sewer-cleanup", "sewer backup cleanup in Troy")
            + ". Call when the lower level is already wet and you need the water pumped out."
        ),
        h2("Sewage extraction in Troy split-levels and subdivision basements"),
        p(
            "Troy callers rarely describe a downtown storefront. They describe a lower level: a 1960s or 1970s "
            "split-level along Big Beaver, a finished room in a subdivision such as Northfield Hills, or a "
            "basement bath that started gurgling while the storm was still on I-75. Sewage extraction there "
            "means getting contaminated water out of carpet, tack strip, and the pad underneath, then deciding "
            "what building material has to leave with it."
        ),
        p(
            "Big Beaver Road is the commercial spine, with Somerset Collection at Coolidge. The houses just "
            "off that corridor are a different building stock from the mall. Many still have the original "
            "lateral. Clay and cast iron from that period scale up inside and open at the joints, which is "
            "where roots enter. Troy's Streets and Drains Division looks after storm drainage. A sanitary "
            "backup is not the same pipe as a flooded catch basin, and the city is who can tell them apart "
            "for a given address."
        ),
        h3("Why Troy lower levels hold so much sewage water"),
        p(
            "Split-level plans put living space a few steps down, close to the floor drain. A backup of a few "
            "inches covers the whole lower floor, not a utility corner. Homeowners often have a sofa, stored "
            "holiday bins, and a bathroom on that level. Extraction has to account for contents, not only the "
            "slab. The crew should list what they will move, what they will bag, and "
            "what they will not touch."
        ),
        p(
            "A local crew handles the pump-out. Call "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + "."
        ),
        h2("Extraction choices that matter in Troy"),
        ul([
            "Carpet and pad that sat in sewage are usually discarded. Ask before anyone attempts to clean them in place.",
            "A finished basement bath can hide water inside the vanity and behind the base. That is part of extraction, not a later remodel.",
            "If the sump also overflowed, the pit water and the sewage water may have mixed. Say that on the call. See "
            + a("/troy-sump-pump-repair", "Troy sump pump repair") + " for the pump itself.",
            "Clear groundwater through a cove joint, with dry floor drains, belongs on the "
            + a("/troy-flooded-basement", "flooded basement") + " and "
            + a("/troy-water-damage-restoration", "water damage restoration") + " pages.",
        ]),
        h3("County drainage is not your private lateral"),
        p(
            "Parts of Troy fall in the broader southern Oakland County drainage area associated with the "
            "George W. Kuhn facility and the Oakland County Water Resources Commissioner. That regional system "
            "does not tell you whether the clog is under your yard. A camera in the lateral answers the private-pipe "
            "question. The city answers the main-in-the-street question. The restoration company answers how "
            "to remove what already entered the house. Those are three different jobs. This line helps you reach the cleanup company."
        ),
        callout(
            "Troy: keep the lower level closed off",
            ul([
                "Shut the door at the top of the split-level stair if you have one, and stop the furnace if the return is in the wet room.",
                "Do not carry wet bins up into the hallway. They drip on treads.",
                "Write down what you smelled and which fixture backed up. That helps the crew and, later, your insurer if you choose to call them.",
                "Ask your insurer whether the policy has a sewer-backup endorsement. The claim stays with you and your carrier.",
            ]),
        ),
        p(
            "When the slab is empty but the odor remains, read "
            + a("/troy-basement-sanitization", "basement sanitizing after a Troy sewage backup")
            + ". All Troy links sit on " + a("/troy", "the Troy city page") + "."
        ),
        nearby_section("sewage-extraction", "Sewage extraction", "troy"),
    ])


def birmingham():
    return "\n".join([
        p(
            "Birmingham sewage extraction means removing wastewater that has already entered an older "
            "house, often against plaster and trim. If you are still figuring out what happened, start with "
            + a("/birmingham-sewer-cleanup", "sewer backup cleanup in Birmingham")
            + ". If the lower level is wet and the drains were the source, call to reach a local crew."
        ),
        h2("Sewage extraction in older Birmingham houses"),
        p(
            "Birmingham sewage extraction is often a finish-sensitive job. Houses around Shain Park, along "
            "Old Woodward's side streets, in Poppleton Park, and near Quarton Lake include early- and "
            "mid-20th-century builds with plaster, wood trim, and lower levels that owners actually use. "
            "A backup through a laundry drain in that kind of house wicks into plaster and into the end grain "
            "of baseboard. Pumping the floor without a plan for those materials leaves the contamination in the walls."
        ),
        p(
            "The laterals under many of those yards are clay or cast iron, installed long before PVC. Mature "
            "trees, which are part of why the neighborhoods look the way they do, send roots into joints. "
            "Low ground near Quarton holds water against foundations during a long rain, which is a separate "
            "issue from a sanitary backup and sometimes happens the same night. Tell the crew which fixtures "
            "overflowed so they do not treat a window-well flood as sewage, or the reverse."
        ),
        h3("How a careful extraction is described"),
        p(
            "Ask the company to explain containment: how they will keep sewage off the stair, whether they "
            "will protect remaining wood floors above, and which porous items they expect to throw away. "
            "That conversation is with the crew on site. "
            "Dial " + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " and a local crew handles the visit. Ask them for license "
            "and insurance before they start."
        ),
        ul([
            "Plaster that is soft at the base usually has to be opened. Wiping the paint is not extraction.",
            "Built-in cabinets on a lower level that wicked sewage are a disposal question, not a cleaning question.",
            "A finished bath in the basement can hold water in the shower pan and the wall behind the valve.",
            "If the loss is mostly clean storm water, use "
            + a("/birmingham-flooded-basement", "Birmingham flooded basement cleanup")
            + " and " + a("/birmingham-water-damage-restoration", "water damage restoration in Birmingham") + ".",
        ]),
        h2("Public main, private lateral, restoration crew"),
        p(
            "The City of Birmingham can speak to the public system. A plumber with a camera can speak to the "
            "lateral under the yard. A restoration company removes what entered the house. Your call starts "
            "that third conversation when a crew is taking calls. Parts of Birmingham "
            "sit in the southern Oakland County drainage area served in conjunction with the Oakland County "
            "Water Resources Commissioner, including the George W. Kuhn district. Do not assume a particular "
            "block is inside that district without checking."
        ),
        callout(
            "Birmingham homes: do not start demolition",
            ul([
                "Leave baseboard and plaster in place until someone who will do the job has seen them.",
                "Keep the HVAC off if the air handler or a return sits in the wet lower level.",
                "Photograph from the stairs. Do not wade in for a closer shot.",
                "Insurance coverage for sewage is a question for your policy, not for a number.",
            ]),
        ),
        p(
            "Odor and residue after pumping are covered on "
            + a("/birmingham-basement-sanitization", "Birmingham basement sanitization after a backup")
            + ". Pump failures are on " + a("/birmingham-sump-pump-repair", "the sump pump page")
            + ". Start from " + a("/birmingham", "Birmingham's overview") + " if you are not sure which service fits."
        ),
        nearby_section("sewage-extraction", "Sewage extraction", "birmingham"),
    ])


def berkley():
    return "\n".join([
        p(
            "Sewage extraction in Berkley, MI is the pumping job in a short bungalow basement: what comes "
            "out, what you should not do with a shop vac, and when the stair makes the job harder. The "
            "first steps after a backup are on "
            + a("/berkley-sewer-cleanup", "sewer backup cleanup in Berkley")
            + "."
        ),
        h2("Sewage extraction in Berkley bungalows"),
        p(
            "Berkley is a small grid of mostly 1940s and 1950s bungalows. Downtown is the 12 Mile Road row "
            "of storefronts; the backups are on the residential blocks off that row and off Coolidge. Basements "
            "are short, stairs are steep, and the floor drain is often next to the laundry tub. Sewage extraction "
            "in that footprint is awkward. Hoses, bags of wet drywall, and drying equipment all compete for the "
            "same few square feet, and the stair lands near the living room."
        ),
        p(
            "Laterals of that age are commonly clay or cast iron nearing the end of a long service life. The "
            "city is relatively flat, so a hard rain does not run off "
            "quickly. Older sections have been described as combined storm and sanitary sewers. If that "
            "description matches your street, a storm can push wastewater up the floor drain even when you "
            "did not run a faucet. Confirm the pipe on your block with Berkley's city offices."
        ),
        h3("Why a household vac makes a Berkley backup worse"),
        p(
            "A shop vac in a low bungalow basement exhausts into a small volume of air and then up a short "
            "stair. Sewage droplets end up on the treads and the door trim. Extraction by a company set up "
            "for contaminated water is the point of the call. The equipment comes with the crew. "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + ". A local crew handles the visit."
        ),
        ul([
            "Measure the stair width before you agree to a large machine. Say it on the phone.",
            "If only the window wells are full and the drains are quiet, it may be storm water. Read "
            + a("/berkley-flooded-basement", "flooded basement cleanup in Berkley") + ".",
            "Sewage plus soaked paneling is a water-damage scope. See "
            + a("/berkley-water-damage-restoration", "water damage restoration in Berkley") + ".",
            "Laundry-tub backups often mean the line is full downstream of the house, not that the tub itself failed.",
        ]),
        h2("How a Berkley extraction is supposed to go"),
        p(
            "A company set up for sewage should keep the mess in the basement. That means "
            "containment at the stair, removal of standing sewage, and bagging of pad, drywall, and "
            "other porous material that soaked it up. Health-wise, the risk in a Berkley bungalow is "
            "the short path upstairs: droplets on the treads, a furnace return that was left running, "
            "and wet shoes carried into the kitchen. Keep people and pets out until that path is clean."
        ),
        p(
            "Insurance is a separate conversation. Many homeowners policies do not cover a sewer backup "
            "unless an endorsement is on the form. Ask your insurer. The claim stays with you and your carrier. Call "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " when the water is inside and you want a local crew. Call the city as well "
            "if several houses on the block are backing up at once, because that can be the main rather "
            "than your lateral. If the drains stayed quiet and only a window well filled, this is storm "
            "water, not sewage. Use "
            + a("/berkley-flooded-basement", "flooded basement cleanup in Berkley")
            + "."
        ),
        h2("After the water is gone"),
        p(
            "Bare concrete that looks dry can still hold odor in the cove joint and in the bottom plate of "
            "the wall. "
            + a("/berkley-basement-sanitization", "Sanitizing after a Berkley sewage backup")
            + " is the follow-up, done by the crew, not by a regular house cleaner. If the sump "
            "was overwhelmed the same night, the pump page is "
            + a("/berkley-sump-pump-repair", "Berkley sump pump repair")
            + ". County drainage for much of this part of Oakland County involves the Water Resources "
            "Commissioner and the George W. Kuhn district. Your bungalow's lateral is still a private pipe "
            "until someone proves otherwise."
        ),
        callout(
            "Berkley checklist before you call",
            ul([
                "Stop all water use, including the basement laundry.",
                "Close the door at the top of the stairs.",
                "Do not store wet shoes in the kitchen.",
                "Note whether neighbors on the block have the same backup. That detail helps the city if the main is the problem.",
            ]),
        ),
        p("The full set of Berkley services is listed on " + a("/berkley", "the Berkley city page") + "."),
        nearby_section("sewage-extraction", "Sewage extraction", "berkley"),
    ])


def clawson():
    return "\n".join([
        p(
            "Clawson sewage extraction is the removal step on a compact lot. If you still need the first "
            "steps after a backup, start with "
            + a("/clawson-sewer-cleanup", "sewer backup cleanup in Clawson")
            + ". If you only need the water pumped out of a one-room basement, you are in the right place."
        ),
        h2("Sewage extraction on Clawson's small lots"),
        p(
            "Clawson extraction jobs are shaped by the lot, not by a big basement rec room. The housing is "
            "largely mid-century brick bungalows and ranches, packed onto compact parcels. Downtown "
            "is 14 Mile Road. The houses sit on the blocks north and south of that mile road, between Royal "
            "Oak and Troy. A backup presents as a floor drain or a basement toilet in a small utility room, "
            "with a short driveway and little side yard to lay hose."
        ),
        p(
            "Clay and cast-iron laterals from those decades corrode and take roots at the joints, which narrows "
            "the pipe. Regional rainstorms load the older sanitary lines. None of that tells you, for your "
            "address, whether the failure is in the yard or in the street. Clawson's city public works is the "
            "source for the municipal main. A camera answers the lateral question. Extraction answers the "
            "water that is already inside."
        ),
        h3("Staging equipment where the driveway is short"),
        p(
            "Tell the crew the truth about access: alley or no alley, street parking, gate width, and "
            "whether the basement stair turns. A company that cannot stage on your lot should say so before "
            "you hire them. Call "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + ". A local crew handles the visit."
        ),
        ul([
            "Brick bungalow basements often have the furnace and the water heater in the same room as the floor drain. Keep power off if water is close.",
            "Do not assume a neighbor's dry basement means your lateral is fine. Laterals fail one house at a time.",
            "Storm water alone, with no drain activity, is discussed on "
            + a("/clawson-flooded-basement", "Clawson flooded basement cleanup") + ".",
            "Broader wetting of finishes belongs with "
            + a("/clawson-water-damage-restoration", "water damage restoration in Clawson") + ".",
        ]),
        h2("What extraction does not include"),
        p(
            "Pulling sewage out of the basement does not repair the lateral, reline the city main, or replace "
            "a sump. Those are separate hires. "
            + a("/clawson-sump-pump-repair", "Sump pump repair in Clawson")
            + " is only the pump conversation. "
            + a("/clawson-basement-sanitization", "Sanitizing after the Clawson backup")
            + " is the residue conversation, and it should be done by the restoration company rather than a "
            "maid service. Southern Oakland County's regional drainage includes the George W. Kuhn district "
            "under the Oakland County Water Resources Commissioner. Clawson is one of the communities "
            "associated with that former Twelve Towns system. Verify your basin and your street with the "
            "county or the city before you rely on that for a claim or a complaint."
        ),
        callout(
            "Clawson: keep contaminated items in the basement",
            ul([
                "Bag nothing upstairs. Wet cardboard and clothing drip on the stair.",
                "Leave the washer door shut. The machine may have filled from the standpipe.",
                "Call the city as well as a cleanup company if several houses on the block are surcharging at once.",
                "Ask your insurer about a sewer-backup endorsement. That call is yours.",
            ]),
        ),
        p("See every Clawson service from " + a("/clawson", "the Clawson overview") + "."),
        nearby_section("sewage-extraction", "Sewage extraction", "clawson"),
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
        ("Where does Royal Oak sewage usually show up inside the house?", "Callers describe floor drains, basement toilets, and laundry standpipes in older houses near downtown, Woodward, Vinsetta, and Northwood. The page cannot see your fixture. If the drain is active, treat the water as sewage."),
        ("How much rain fell in Royal Oak in the August 2014 flood?", "As reported at the time, the city's DPS rain gauge recorded 4.98 inches on August 11, 2014, including 1.12 inches in 30 minutes. The storms led to a federal disaster declaration, FEMA-4195-DR, for Macomb, Oakland, and Wayne counties."),
        ("Should I call Royal Oak's Sewer Division and a cleanup company?", "Yes, if you suspect the city main. Basement-water calls use (248) 246-3300 on weekdays, 7:30 a.m. to 4:00 p.m. After hours, (248) 246-3500 dispatches sewer personnel. A cleanup company removes water from the house. Call (248) 825-8312 to reach that company."),
        ("Does pumping a Royal Oak basement pause the 45-day notice?", "No. Written notice runs from the day you discover the damage, not from the day the floor looks dry. The city is responsible for the main, and you are responsible for the lateral up to and including the connection. Your insurer is a third conversation, about whether a sewer-backup endorsement is on the policy."),
        ("Are older Royal Oak sewers combined?", "Many older sections were built before separated storm and sanitary sewers were standard. Royal Oak is a member of the former Twelve Towns program, now the George W. Kuhn Retention Treatment Basin, which was expanded in 2006. The Sewer Division maintains about 300 miles of sanitary and storm sewers and can confirm the pipe on your street. Pumping the basement does not identify that pipe."),
    ],
    "troy": [
        ("Is sewage extraction in Troy the same as draining a flooded window well?", "No. Window-well rain can be clean storm water. Water from a floor drain or basement bath is sewage. Tell the crew which one you have, especially in split-levels near Big Beaver."),
        ("What goes in a written Troy sewer claim?", "Your name, address, and phone number, the affected property address, the date you discovered the damage, and a brief description, sent to the City Attorney's Office within 45 days of discovery (MCL 691.1419)."),
        ("Who decides what carpet comes out of a Troy basement?", "The crew, based on what touched sewage. Ask for that scope in writing, and for the price, before they start."),
        ("Which Troy number is the city while sewage is being pumped?", "Water Division 248-524-3370 during business hours, and Troy Police 248-524-3477 after hours. Troy discharges through three districts, so ask the city which one serves the house. For pumping, call (248) 825-8312."),
        ("Does sewage extraction in Troy include the 45-day claim?", "No. Extraction removes the water. Written notice to the City Attorney's Office is your letter, due within 45 days of discovery. Insurance, if a sewer-backup endorsement is on the policy, is a separate call."),
    ],
    "birmingham": [
        ("Will sewage extraction save original Birmingham plaster?", "Sometimes the base is already ruined and has to be opened. Sometimes the wetting stopped below the trim. Only someone on site can say. Do not chip the plaster out before they look."),
        ("Does Birmingham have sewer pump stations?", "No. Birmingham's FAQ says the system is gravity and the city owns no pump or lift stations. Pumping a basement is done with the cleanup crew's own equipment. Call (248) 825-8312."),
        ("Does extraction include repairing the old cast-iron lateral?", "No. Removing water from the house does not dig up or replace the lateral. That is a separate plumbing hire. The city's system is gravity and Birmingham owns no sewage pump or lift stations, so a backup is not a failed municipal lift station."),
        ("Is (248) 530-1703 the number that sends an extraction crew?", "No. That line collects flooding information for the city. Claims questions go to 248.530.1808. For pumping the lower level, call (248) 825-8312, and leave plaster in place until the crew has seen how high the water went."),
        ("What should I know about Birmingham's 45-day notice before debris leaves?", "Photograph rooms before pad and trim are removed. Written notice is due within 45 days of discovery, and the water-event form is not the claim. A backflow preventer and downspouts extended about 6 feet are prevention for the next storm, not a substitute for pumping what is already inside."),
    ],
    "berkley": [
        ("Why mention combined sewers on a Berkley extraction page?", "Because older Berkley sections have been described as carrying storm and sanitary flow together, which can push sewage up floor drains in a storm. Confirm your street with the city before you treat it as fact for your house."),
        ("Is a bungalow stair a problem for extraction equipment?", "It can be. Say how narrow and how steep the stair is when you call so the crew can say whether they can work there."),
        ("Who sanitizes a Berkley basement after the water is pumped?", "The cleanup crew. Ask them what they will remove and what they will clean. The short stair is part of that plan, because droplets walk upstairs."),
        ("Who is the city contact while a Berkley bungalow is being pumped?", "Public Works, 248-658-3490. The sewer is one combined gravity pipe with no city pumps or valves, so a storm can be the reason sewage is on the floor. The city also posts a Sewer Backup Claims Form."),
        ("When does the 45-day Berkley clock start if extraction takes all day?", "It starts when you discover the damage, not when the pump-out ends. Flow from Berkley goes toward the Clinton through the George W. Kuhn district, not to the Rouge. Your insurance endorsement is a separate question."),
    ],
    "clawson": [
        ("Can extraction equipment fit a typical Clawson lot?", "Often, from the street or a short driveway. Describe the lot when you call, and ask how they will stage the hoses before you agree."),
        ("What if a Clawson backup happens on a Friday?", "Clawson public works is open Monday through Thursday, 7:00 a.m. to 3:30 p.m., and closed Fridays. On a Friday or after hours, the city's path is Troy Police dispatch at 248-524-3477, extension 1. Cleanup inside the house is a separate call to (248) 825-8312."),
        ("What if several Clawson houses back up at once?", "Call the city about the main and call a cleanup company about the water in your basement. A neighborhood-wide surcharge and a single lateral failure are different problems. The city line is (248) 435-4500, Monday through Thursday, 7:00 a.m. to 3:30 p.m. On Friday, DPW is closed and after-hours dispatch is 248-524-3477, extension 1."),
        ("Does Clawson's sewer page tell me the basin, or my lateral?", "The page lists the George W. Kuhn basin and the Oakland County Water Resources Commissioner, and it links a combined-sewer explainer. Confirm your street with the city. Extraction only removes what is already in the one-room basement."),
        ("What should I tell the crew about a Clawson pump-out?", "That the driveway is short and how many rooms took water. If you believe the city main was involved, written notice is due within 45 days of discovery."),
    ],
}

HERO = {
    "royal-oak": "Sewage is on the basement floor of an older Royal Oak house and it has to be pumped out. A local cleanup crew handles the visit for sewage extraction in Royal Oak, and they'll tell you when they can be there.",
    "troy": "A Troy split-level or lower level off Big Beaver has sewage in it, and that water has to leave. Call and a local cleanup crew handles the visit for sewage extraction in Troy, and they'll tell you when they can be there.",
    "birmingham": "Sewage is against the plaster and trim in an older Birmingham lower level. When you call, you reach a local cleanup crew for sewage extraction in Birmingham, and they'll tell you when they can be there.",
    "berkley": "Sewage is in a short Berkley bungalow basement, and a household vac will spread it. Your call puts you through to a local cleanup crew for sewage extraction in Berkley, and they'll tell you when they can be there.",
    "clawson": "Sewage is in a one-room Clawson bungalow basement on a tight lot. Call, and a local cleanup crew handles sewage extraction in Clawson. They'll tell you when they can be there.",
}

ALT = {
    "royal-oak": "Contaminated water being removed from a basement, the extraction step Royal Oak sewer backups need",
    "troy": "Basement extraction equipment beside wet carpet, relevant to Troy lower-level sewage backups",
    "birmingham": "Sewage water removal in a finished lower level, a Birmingham extraction concern",
    "berkley": "Tight basement stairs and standing sewage water, a Berkley bungalow extraction problem",
    "clawson": "Sewage extraction hoses staged for a small house, a Clawson lot constraint",
}

DESCRIPTIONS = {
    "royal-oak": "Sewage extraction in Royal Oak, MI for basement backups. A local crew handles the work. Call {PHONE_DISPLAY}.",
    "troy": "Sewage extraction in Troy, MI for lower-level backups. Local crews via Oakland Sewer Pros. Call {PHONE_DISPLAY}.",
    "birmingham": "Sewage extraction in Birmingham, MI for older homes. A call to local crews. Call {PHONE_DISPLAY}.",
    "berkley": "Sewage extraction in Berkley, MI bungalows. Pumping contaminated water, not the sewage cleanup page. Call {PHONE_DISPLAY}.",
    "clawson": "Sewage extraction in Clawson, MI for bungalow backups. A local crew pumps it. Call {PHONE_DISPLAY}.",
}
