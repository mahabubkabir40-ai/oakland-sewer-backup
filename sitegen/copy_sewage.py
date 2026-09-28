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
            "Downtown Royal Oak gets the attention, but the backups we hear about from callers are usually "
            "a block or two off the commercial strip: a floor drain in a basement under a house on a side "
            "street near Main Street, Washington, or the Woodward frontage. The water is not rain that blew "
            "in a window. It came up out of the plumbing. That is sewage extraction, and it is a different "
            "job from mopping a clean-water leak."
        ),
        p(
            "A lot of those houses went up before the 1960s. Vinsetta and Northwood are the names residents "
            "use for two of the established areas. Laterals from that era were often clay tile or cast iron. "
            "Roots at a joint, or a belly in the pipe under the yard, are ordinary explanations. Whether that "
            "is your lateral or the city main is not something this website can know. "
            + a("https://www.romi.gov/384/Sewer-Division", "Royal Oak's Sewer Division")
            + " publishes city sewer information and is the right place to ask about the public main."
        ),
        h3("What extraction means in a Royal Oak basement"),
        p(
            "Extraction means removing the contaminated water and the residue it left, not just the puddle you "
            "can see from the stairs. Concrete holds moisture. The bottom of wood studs and the paper face of "
            "drywall hold sewage. A provider should tell you, in writing, how far up the wall they intend to "
            "remove material and how they will keep the stair and the first floor from getting splashed."
        ),
        p(
            "Oakland Sewer Pros does not own vacuum trucks and does not employ the people who run them. Call "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " to be connected with an independent company when one is participating. Ask that company what "
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
            "covers haul-away of porous material or only pumping. This site does not quote those prices and "
            "does not bill your insurer. Southern Oakland County drainage, including parts of Royal Oak, is "
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
            "slab. The independent provider you hire should list what they will move, what they will bag, and "
            "what they will not touch."
        ),
        p(
            "Oakland Sewer Pros is the phone introduction, not the contractor. We do not station a truck at "
            "Somerset or anywhere else in Troy. "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " connects you when a participating company can take the call. Availability is not promised."
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
            "to remove what already entered the house. Those are three different jobs, and this website only helps you reach the third."
        ),
        callout(
            "Troy: keep the lower level closed off",
            ul([
                "Shut the door at the top of the split-level stair if you have one, and stop the furnace if the return is in the wet room.",
                "Do not carry wet bins up into the hallway. They drip on treads.",
                "Write down what you smelled and which fixture backed up. That helps the provider and, later, your insurer if you choose to call them.",
                "We do not file the insurance claim and we do not know if your policy has a sewer-backup endorsement.",
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
            + ". If the lower level is wet and the drains were the source, call to reach an independent provider."
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
            "issue from a sanitary backup and sometimes happens the same night. Tell the provider which fixtures "
            "overflowed so they do not treat a window-well flood as sewage, or the reverse."
        ),
        h3("How a careful extraction is described"),
        p(
            "Ask the company to explain containment: how they will keep sewage off the stair, whether they "
            "will protect remaining wood floors above, and which porous items they expect to throw away. "
            "Oakland Sewer Pros will not be on site to supervise that conversation. We are a referral line. "
            "Dial " + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " and you may be connected with an independent provider. You still have to check their license "
            "and insurance for the work you want done."
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
            "lateral under the yard. A restoration company removes what entered the house. Calling this site "
            "only starts the third conversation, and only when a provider is taking calls. Parts of Birmingham "
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
                "Insurance coverage for sewage is a question for your policy, not for a referral line.",
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
            "did not run a faucet. Confirm the pipe with Berkley's city offices. A website cannot tell you which pipe is in your street."
        ),
        h3("Why a household vac makes a Berkley backup worse"),
        p(
            "A shop vac in a low bungalow basement exhausts into a small volume of air and then up a short "
            "stair. Sewage droplets end up on the treads and the door trim. Extraction by a company set up "
            "for contaminated water is the point of the call. Oakland Sewer Pros does not arrive with that "
            "equipment. "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " is a matching number for independent providers, subject to who is actually available."
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
            "A company set up for Category 3 water should keep the mess in the basement. That means "
            "containment at the stair, removal of standing sewage, and bagging of pad, drywall, and "
            "other porous material that soaked it up. Health-wise, the risk in a Berkley bungalow is "
            "the short path upstairs: droplets on the treads, a furnace return that was left running, "
            "and wet shoes carried into the kitchen. Keep people and pets out until that path is clean."
        ),
        p(
            "Insurance is a separate conversation. Many homeowners policies do not cover a sewer backup "
            "unless an endorsement is on the form. Ask your insurer. Oakland Sewer Pros does not read "
            "the policy or bill a carrier. Call "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " when the water is inside and you want an independent provider. Call the city as well "
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
            + " is the follow-up, done by the company you hire, not by a regular house cleaner. If the sump "
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
            "Tell the provider the truth about access: alley or no alley, street parking, gate width, and "
            "whether the basement stair turns. A company that cannot stage on your lot should say so before "
            "you hire them. Oakland Sewer Pros does not inspect the lot and does not send a crew. The call "
            "at " + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " is a referral. If no participating provider can take the call, you will need another way to reach a company."
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
                "Ask your insurer about a sewer-backup endorsement. This site will not call them for you.",
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
        ("Does Oakland Sewer Pros pump out Royal Oak basements?", "No. The company you are connected with does the extraction if you hire them. We do not own trucks or employ technicians."),
        ("Should I call Royal Oak's Sewer Division and a cleanup company?", "Yes, if you suspect the city main. The Sewer Division is the public-system contact. A cleanup company removes water from the house. They are not substitutes for each other."),
    ],
    "troy": [
        ("Is sewage extraction in Troy the same as draining a flooded window well?", "No. Window-well rain can be clean storm water. Water from a floor drain or basement bath is sewage. Tell the provider which one you have, especially in split-levels near Big Beaver."),
        ("Can this site send a crew to Northfield Hills or Somerset tonight?", "We cannot send a crew anywhere. A participating independent provider may be available. That is not a promise for a specific subdivision or a specific hour."),
        ("Who decides what carpet comes out of a Troy basement?", "The company you hire, based on what touched sewage. This website does not write that scope and does not set the price."),
    ],
    "birmingham": [
        ("Will sewage extraction save original Birmingham plaster?", "Sometimes the base is already ruined and has to be opened. Sometimes the wetting stopped below the trim. Only someone on site can say. Do not chip the plaster out before they look."),
        ("Are Poppleton Park and Quarton covered by this referral line?", "The line is for Birmingham homeowners, including those neighborhoods. Coverage by a provider still depends on who is participating when you call."),
        ("Does extraction include repairing the old cast-iron lateral?", "No. Removing water from the house does not dig up or replace the lateral. That is a separate plumbing hire."),
    ],
    "berkley": [
        ("Why mention combined sewers on a Berkley extraction page?", "Because older Berkley sections have been described as carrying storm and sanitary flow together, which can push sewage up floor drains in a storm. Confirm your street with the city before you treat it as fact for your house."),
        ("Is a bungalow stair a problem for extraction equipment?", "It can be. Say how narrow and how steep the stair is when you call so the provider can say whether they can work there."),
        ("Does this site sanitize the Berkley basement after pumping?", "No. Sanitizing is part of the restoration company's work. See the Berkley sanitization page for what to ask them. We do not do the cleaning."),
    ],
    "clawson": [
        ("Can extraction equipment fit a typical Clawson lot?", "Sometimes, from the street or a short drive. Ask the provider after you describe the lot. We do not visit the property first."),
        ("Is 14 Mile Road the only Clawson area you refer?", "No. 14 Mile is the downtown reference. The referral is for Clawson houses, including the bungalow blocks off that road."),
        ("What if several Clawson houses back up at once?", "Call the city about the main and call a cleanup company about the water in your basement. A neighborhood-wide surcharge and a single lateral failure are different problems."),
    ],
}

HERO = {
    "royal-oak": "Sewage extraction in Royal Oak means removing contaminated water that came out of the plumbing in an older house, then deciding what that water ruined. This line connects you with an independent provider. We do not pump the basement ourselves.",
    "troy": "Troy sewage extraction is usually a lower-level or split-level problem off corridors like Big Beaver, not a mall-parking-lot issue. Call to reach an independent company. Oakland Sewer Pros does not run the job.",
    "birmingham": "In Birmingham, sewage extraction has to respect plaster, trim, and finished lower levels in older houses. We connect you with an outside provider. We do not perform the extraction.",
    "berkley": "Sewage extraction in Berkley, MI means pumping contaminated water out of a short bungalow basement. A household vac is a poor substitute. We connect you with an independent provider and do not send a truck.",
    "clawson": "Clawson sewage extraction has to work on compact bungalow lots near 14 Mile. This is a referral to an independent company, not a city crew and not our own crew.",
}

ALT = {
    "royal-oak": "Contaminated water being removed from a basement, the extraction step Royal Oak sewer backups need",
    "troy": "Basement extraction equipment beside wet carpet, relevant to Troy lower-level sewage backups",
    "birmingham": "Sewage water removal in a finished lower level, a Birmingham extraction concern",
    "berkley": "Tight basement stairs and standing sewage water, a Berkley bungalow extraction problem",
    "clawson": "Sewage extraction hoses staged for a small house, a Clawson lot constraint",
}

DESCRIPTIONS = {
    "royal-oak": "Sewage extraction in Royal Oak, MI for basement backups. We connect you with independent providers. Call {PHONE_DISPLAY}.",
    "troy": "Sewage extraction in Troy, MI for lower-level backups. Independent providers via Oakland Sewer Pros. Call {PHONE_DISPLAY}.",
    "birmingham": "Sewage extraction in Birmingham, MI for older homes. A referral to independent providers. Call {PHONE_DISPLAY}.",
    "berkley": "Sewage extraction in Berkley, MI bungalows. Pumping contaminated water, not the sewage cleanup page. Call {PHONE_DISPLAY}.",
    "clawson": "Sewage extraction in Clawson, MI for bungalow backups. Independent local providers. Call {PHONE_DISPLAY} today.",
}
