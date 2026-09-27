"""Basement sanitization reframed as cleanup after flood or sewage, not a maid service."""
from site_config import PHONE_DISPLAY, PHONE_TEL

from sitegen.render import a, callout, h2, h3, nearby_section, p, ul

def royal_oak():
    return "\n".join([
        h2("Sanitizing a Royal Oak basement after sewage or a flood"),
        p(
            "Basement sanitization in Royal Oak is the step after the water is gone, and only when that "
            "water was sewage or sat long enough to foul. It is not a recurring cleaning service for a "
            "dry storage room. Houses near Woodward, in Northwood, in Vinsetta, and on the blocks toward "
            "the Detroit Zoo get sewer backups through floor drains. Once the standing sewage is extracted, "
            "the film on the slab, the cove joint, and the bottom of the studs is still there. Wiping it "
            "with a kitchen sponge spreads it."
        ),
        p(
            "The company that did "
            + a("/royal-oak-sewage-extraction", "sewage extraction")
            + " should be the one that sanitizes, because they already know what got wet. Oakland Sewer "
            "Pros does not sell disinfectant and does not send a technician. "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " connects you with an independent provider when one is available. Ask what product they "
            "will use and whether the label allows it on sewage residue. You should not have to take "
            "their word that a bottle is appropriate."
        ),
        h3("What usually cannot be sanitized and kept"),
        ul([
            "Drywall and insulation that wicked sewage. The paper and the fibers hold contamination. They typically come out rather than get sprayed and left.",
            "Carpet pad. The top carpet may look rinseable. The pad underneath is not.",
            "Cardboard boxes and soft furnishings that sat in the water. Bag them in the basement, not in the kitchen.",
            "Open food, including anything on a basement shelf that was splashed.",
        ]),
        h2("How this differs from water damage drying"),
        p(
            "Sanitizing does not dry the structure. Drying is "
            + a("/royal-oak-water-damage-restoration", "water damage restoration in Royal Oak")
            + " and, for the pumping itself, "
            + a("/royal-oak-flooded-basement", "basement water removal")
            + ". A clean rain flood may need detergent and drying without a sewage protocol. A backup "
            "needs the stricter cleanup. If you are unsure which event you had, say so. Guessing wrong "
            "and using a light cleaner on sewage is the mistake this page is here to prevent."
        ),
        p(
            "Odor that remains after the floor looks clean usually means something porous was left in "
            "place, or the trap and the pit were not addressed. A sump pit that took sewage needs the "
            "same caution as the floor. See "
            + a("/royal-oak-sump-pump-repair", "sump pump repair")
            + " if the pump itself failed. Royal Oak's city sewer questions still go to the Sewer Division, not to a cleaning crew."
        ),
        callout(
            "Royal Oak: keep the dirty zone downstairs",
            ul([
                "Do not carry a mop bucket up to the kitchen sink.",
                "Clothes that got splashed go in bags. Do not wash them in the family machine with other laundry until you have asked the provider.",
                "Run no fan across a still-contaminated floor.",
                "Ask the provider what you must throw away before you pay for a 'sanitize in place' visit that cannot work.",
            ]),
        ),
        p("More context is on " + a("/royal-oak", "the Royal Oak overview") + " and " + a("/royal-oak-sewer-cleanup", "sewer backup cleanup") + "."),
        nearby_section("basement-sanitization", "Basement sanitization", "royal-oak"),
    ])


def troy():
    return "\n".join([
        h2("Sanitizing Troy finished basements after a backup or flood"),
        p(
            "Troy basement sanitization comes up after a lower level has already been used as living space. "
            "Split-levels near Big Beaver and finished rooms in places like Northfield Hills often have "
            "carpet, a sofa, a kids' corner, and a bath. If sewage touched those, sanitizing is not a "
            "spray over the top. The pad, the sofa bottom, and the bath base are reservoirs. A company "
            "has to remove the ruined layers before any disinfectant has a surface it can actually treat."
        ),
        p(
            "Oakland Sewer Pros does not certify cleaners and does not claim the providers we may reach "
            "hold any particular credential. Ask the company you hire what training and insurance they "
            "carry for sewage cleanup. The phone "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " is only the introduction. If the event was a clean sump overflow with no drain backup, "
            "say that. The scope is smaller than a sewage loss and may be handled under "
            + a("/troy-flooded-basement", "flooded basement cleanup")
            + " and " + a("/troy-water-damage-restoration", "water damage restoration") + "."
        ),
        h3("Contents versus structure in a Troy lower level"),
        ul([
            "Structure: studs, sill, drywall, and the slab. The provider decides what is cut out.",
            "Contents: toys, bins, and upholstered furniture. Soft items that soaked up sewage are generally discarded, not cleaned.",
            "The bathroom vanity and the hollow base of a built-in can hold water after the floor is dry.",
            "HVAC returns in the lower level can pull odor upstairs. Ask whether the system should stay off.",
        ]),
        h2("After sewage extraction, not instead of it"),
        p(
            "Sanitizing a room that still has standing sewage does nothing useful. "
            + a("/troy-sewage-extraction", "Sewage extraction in Troy")
            + " comes first. "
            + a("/troy-sewer-cleanup", "Sewer backup cleanup")
            + " is the overview of the backup itself. A failed pump that started the overflow is "
            + a("/troy-sump-pump-repair", "sump pump repair")
            + ". None of those pages is a price list. The provider quotes the work. We do not."
        ),
        callout(
            "Troy questions worth asking",
            ul([
                "Will you remove carpet and pad before you apply anything?",
                "What happens to a contaminated sofa? Do you haul it, or is haul-away my problem?",
                "How will you keep the split-level stair from becoming the path that dirties the upper floor?",
                "Will you recheck odor after the drying equipment has run, or is this a one-visit spray?",
            ]),
        ),
        p("Troy's other services are grouped on " + a("/troy", "the Troy city page") + "."),
        nearby_section("basement-sanitization", "Basement sanitization", "troy"),
    ])


def birmingham():
    return "\n".join([
        h2("Sanitizing after a flood or sewage backup in an older Birmingham house"),
        p(
            "Birmingham basement sanitization is mostly a materials problem. Plaster, wood base, and "
            "built-ins in houses around Poppleton Park, Quarton, and the streets off Old Woodward and "
            "Maple do not behave like modern painted drywall. Sewage that wicked into the bottom of "
            "plaster is inside the material. A surface wipe of the paint film leaves the contamination "
            "in place and can trap odor. The provider has to say whether that plaster comes off."
        ),
        p(
            "This is not a housekeeping visit and not a 'make the lower level smell better' product "
            "pitch. If you had a sewer backup, start from "
            + a("/birmingham-sewage-extraction", "sewage extraction")
            + " and " + a("/birmingham-sewer-cleanup", "sewer backup cleanup")
            + ". If the water was a flood without sewage, drying and selective cleaning sit under "
            + a("/birmingham-water-damage-restoration", "water damage restoration")
            + " and " + a("/birmingham-flooded-basement", "basement water removal")
            + ". Oakland Sewer Pros refers the call at "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " and does not apply chemicals."
        ),
        h3("Wood trim and what sanitizing cannot promise"),
        ul([
            "Unfinished end grain on baseboard that sat in sewage is a poor candidate for saving. Painted face grain may look fine and still be fouled at the cut ends.",
            "A closed-cell finish on a floor is different from a bare softwood stair. Ask for a specific answer, not a blanket 'we can save the wood.'",
            "Plaster keys that are already soft will not hold because someone sprayed them.",
            "No one on this website can promise the house will be odor-free on a date.",
        ]),
        h2("Who should do the work"),
        p(
            "Hire a restoration company that will put the scope in writing, including what is discarded. "
            "A janitorial service with a mop is the wrong trade once sewage is involved. Verify license "
            "and insurance for the work. We do not hold those documents for the companies who may answer "
            "the referral. If a sump pit was part of the contamination, include "
            + a("/birmingham-sump-pump-repair", "the pump")
            + " in the discussion so the crock is not the piece left dirty."
        ),
        callout(
            "Birmingham: do not fog the house and hope",
            ul([
                "Odor treatments that do not remove the wet material only cover the smell until the next humid day.",
                "Keep children out of a lower level that had sewage, even after it looks dry, until the company says the demolition is done.",
                "Do not mix random household chemicals in the same bucket.",
                "Photograph discarded materials if you plan to talk to your insurer. We do not submit the claim.",
            ]),
        ),
        p("See " + a("/birmingham", "Birmingham's overview") + " for the full local list."),
        nearby_section("basement-sanitization", "Basement sanitization", "birmingham"),
    ])


def berkley():
    return "\n".join([
        h2("Sanitizing a Berkley bungalow after sewage or floodwater"),
        p(
            "Berkley sanitization happens in a small volume of air. The basement is short, the stair is "
            "steep, and the door at the top often opens near the living room of a 1940s or 1950s bungalow "
            "off 12 Mile or Coolidge. Anything volatile you apply downstairs is in the main floor in "
            "minutes. That is why the product and the ventilation plan matter more here than they do in "
            "a wide commercial basement. It is also why sewage residue should be removed, not perfumed."
        ),
        p(
            "Older Berkley sections have been described as combined sewers. A storm can put wastewater "
            "on the floor even in a house that did not have a plumbing break. Confirm that with the city "
            "for your block. If it happened, treat the water as sewage. Sewage cleanup in Berkley, MI is "
            + a("/berkley-sewer-cleanup", "sewer backup cleanup in Berkley")
            + ". Pumping the water out is "
            + a("/berkley-sewage-extraction", "sewage extraction in Berkley")
            + ". This page starts after that water is out. Oakland Sewer Pros does not clean the house. Call "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " for a referral to an independent provider."
        ),
        h3("The stair and the first floor"),
        ul([
            "Dirty water on the treads will be walked into the room at the top. Clean the path only after the basement source is controlled, and bag the rags downstairs.",
            "A furnace return in a bungalow basement will distribute odor. Leave the system off until the provider advises.",
            "Panel doors and hollow closet bases on the first floor can wick if the humidity stayed high. Mention them.",
            "A clean flood still needs drying. That scope is " + a("/berkley-flooded-basement", "flooded basement cleanup") + " and " + a("/berkley-water-damage-restoration", "water damage restoration") + ".",
        ]),
        h2("What sanitizing covers after a Berkley backup"),
        p(
            "Basement sanitization in Berkley, MI is the residue step. It is not sewage extraction and "
            "it is not the sewage cleanup overview. Those are linked above. A sensible order is: stop "
            "water use, keep the stair closed, have contaminated water removed, throw out porous items "
            "that soaked it up, then clean what is left and dry the structure. Spraying a still-wet "
            "pad does none of those things. Category 3 water can carry bacteria up a short bungalow "
            "stair, so the living room is part of the safety plan even when the flood stayed downstairs."
        ),
        p(
            "Call " + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " when you need an independent provider for that cleaning. Ask what they will remove, "
            "what they will apply, and how they will keep the first floor from being the next dirty "
            "surface. Insurance questions go to your insurer. We do not say a policy will pay, and we "
            "do not quote a cleaning price."
        ),
        h2("Not a substitute for fixing the drain"),
        p(
            "Sanitizing does not clear a root-filled lateral or a city main. You can have a clean-looking "
            "slab and back up again on the next rain. The pit and the pump, if they were involved, are "
            + a("/berkley-sump-pump-repair", "a sump conversation")
            + ". The lateral is a plumber or a city inspection. This page is only the residue left inside "
            "the bungalow after the water left."
        ),
        callout(
            "Berkley limits on DIY disinfectant",
            ul([
                "Do not pour bleach into a basement drain that just backed up. You can splash yourself and you have not cleaned the room.",
                "Do not run the clothes dryer if the laundry sink overflowed into the machine area.",
                "Ask the provider whether belongings on shelves above the water line were splashed. Height matters in a low basement.",
                "We will not tell you a specific chemical brand to buy. The person doing the work should name what they are using and why.",
            ]),
        ),
        p("All Berkley services start at " + a("/berkley", "the city page") + "."),
        nearby_section("basement-sanitization", "Basement sanitization", "berkley"),
    ])


def clawson():
    return "\n".join([
        h2("Sanitizing after a Clawson backup or basement flood"),
        p(
            "Clawson basement sanitization is cramped. Mid-century brick bungalows and ranches, on "
            "small lots along and off 14 Mile, often have a single basement room. The floor drain, the "
            "laundry, and the furnace share it. After a sewer backup, every surface in that room is in "
            "play: the furnace cabinet bottom, the water-heater legs, the washer exterior, and the stair "
            "stringer. A spray that misses the backs of those appliances leaves the odor in the room."
        ),
        p(
            "Cross-contamination is the bungalow problem. There is no long hallway to isolate. The "
            "basement door opens into the house you live in. Bags, boots, and hoses have to be planned "
            "so sewage does not move upstairs. The company you hire should describe that plan. Oakland "
            "Sewer Pros will not be on the stair to enforce it. Reach a provider through "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " if someone is participating. We do not warrant their work."
        ),
        h3("Sequence that fits a small Clawson basement"),
        ul([
            "Stop the water and deal with electrical safety first. Sanitizing a live puddle near a panel is not a step.",
            "Extract sewage. That is " + a("/clawson-sewage-extraction", "sewage extraction in Clawson") + " and the backup context is " + a("/clawson-sewer-cleanup", "sewer backup cleanup") + ".",
            "Remove porous material that soaked it up. Then clean what remains.",
            "Dry the structure. Drying and repair decisions are " + a("/clawson-water-damage-restoration", "water damage restoration") + ". Pumping a clean flood is " + a("/clawson-flooded-basement", "basement water removal") + ".",
        ]),
        h2("Appliances and the pit"),
        p(
            "A washer that filled from a backed-up standpipe is not sanitized by running a cycle. Ask "
            "the provider whether the machine is a loss. A sump crock that received sewage needs to be "
            "emptied and cleaned as part of the job, and the pump may need repair under "
            + a("/clawson-sump-pump-repair", "Clawson sump pump repair")
            + ". Those are restoration and plumbing questions for the companies involved. Tight driveways "
            "also mean disinfectant containers and bagged debris have to leave without blocking the sidewalk. Say that when you hire."
        ),
        callout(
            "Clawson: one room, one rule",
            ul([
                "Nothing wet and soft goes up the stairs unpacked.",
                "Do not restart the furnace to 'dry the room' if the bottom of the unit was under water.",
                "Ask what will be hauled the same day. A sanitized floor next to a pile of wet drywall is not done.",
                "Insurance paperwork is your conversation with your insurer. This site does not write it.",
            ]),
        ),
        p("See " + a("/clawson", "Clawson's service overview") + " if you still need the sewer or flood page."),
        nearby_section("basement-sanitization", "Basement sanitization", "clawson"),
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
        ("Is Royal Oak basement sanitization a regular cleaning service?", "No. This page is about cleaning after sewage or a contaminated flood. A dry basement that just needs dusting is not the job."),
        ("Can I sanitize sewage residue myself with bleach?", "A household mop does not reach contamination inside drywall and pad, and mixing cleaners is unsafe. Have a restoration company remove ruined material and tell you what they are applying to what remains."),
        ("Does Oakland Sewer Pros guarantee the odor will be gone?", "No. We do not do the work and we do not guarantee results. Odor usually means a porous material was left behind. The company on site has to find it."),
    ],
    "troy": [
        ("Should a Troy playroom that had sewage be sprayed and kept?", "Soft contents that soaked up sewage are generally thrown away. Spraying the room without removing the pad and the ruined furnishings does not sanitize the lower level."),
        ("Who sanitizes the basement?", "The independent restoration company you hire. This website only refers the call."),
        ("Does sanitizing include drying the Troy basement?", "No. Drying is a different part of water damage restoration. Ask for both scopes if the materials are still wet."),
    ],
    "birmingham": [
        ("Can original Birmingham plaster be sanitized in place?", "Only if sewage did not soak through it. Soft or deeply stained plaster usually has to be removed. The provider should decide after looking, not from this page."),
        ("Is a deodorant fog enough after a Birmingham backup?", "No. Fog does not replace removing the contaminated material. The smell returns when humidity rises."),
        ("Do you certify the companies as specialists?", "No. We do not certify anyone. You verify license and insurance with the company you hire."),
    ],
    "berkley": [
        ("Why is sanitizing riskier in a Berkley bungalow?", "The basement air volume is small and the stair opens near living space, so residue and strong cleaners move upstairs quickly. Removal of ruined material matters more than a heavy spray."),
        ("Does a combined sewer change the cleaning?", "If the city confirms your block can surcharge sewage in a storm, treat the floodwater as sewage. Confirm the block. Do not skip extraction."),
        ("Will this site tell me which disinfectant to buy?", "No. The company performing the work should name the product and confirm the label fits sewage cleanup."),
    ],
    "clawson": [
        ("What gets missed in a one-room Clawson basement?", "The backs and bottoms of the furnace, water heater, and washer, plus the stair stringer. A floor-only mop leaves those."),
        ("Can I run the washer to clean it after a standpipe backup?", "Do not assume a cycle cleans a machine that filled with sewage. Ask the provider whether it should be discarded."),
        ("Does sanitizing fix the Clawson lateral?", "No. Cleaning the basement does not open the pipe. Expect a separate step if the line is still blocked."),
    ],
}

HERO = {
    "royal-oak": "Basement sanitization in Royal Oak means cleaning up after sewage or a contaminated flood, once the water is out. It is not a maid service. We refer you to an independent provider and do not do the cleaning.",
    "troy": "After a Troy lower-level backup, sanitizing means removing what sewage soaked, not spraying over carpet pad. This page connects you with an independent company. We do not perform the work.",
    "birmingham": "Sanitizing a Birmingham basement after sewage has to deal with plaster and wood, not just a concrete floor. Call for a referral. Oakland Sewer Pros does not apply cleaners or guarantee an odor-free date.",
    "berkley": "Basement sanitization in Berkley, MI is cleaning after sewage or a flood in a small bungalow, once the water is out. It is not the sewage cleanup page. We connect the call and do not clean the house.",
    "clawson": "Clawson sanitizing after a backup is a one-room job packed with mechanical equipment. Use this referral to reach an independent provider. We do not send a cleaning crew.",
}

ALT = {
    "royal-oak": "A basement floor after sewage removal, before sanitizing residue in a Royal Oak house",
    "troy": "A finished lower level stripped after a backup, the sanitizing stage in a Troy basement",
    "birmingham": "Lower-level finishes after a sewage backup, a Birmingham sanitizing and removal question",
    "berkley": "A small bungalow basement stair after a backup, where Berkley sanitizing has to contain mess",
    "clawson": "Utility equipment in a small basement after a flood, a Clawson sanitizing access problem",
}

DESCRIPTIONS = {
    "royal-oak": "Basement sanitization after sewage or flood in Royal Oak, MI. Independent providers. Call {PHONE_DISPLAY}.",
    "troy": "Basement sanitization after a Troy, MI backup or flood. We refer independent providers. Call {PHONE_DISPLAY}.",
    "birmingham": "Sanitize a Birmingham, MI basement after sewage or flood. Independent local help. Call {PHONE_DISPLAY}.",
    "berkley": "Basement sanitization in Berkley, MI after sewage or a flood. Not the extraction page. Call {PHONE_DISPLAY}.",
    "clawson": "Basement sanitization after a Clawson, MI backup or flood. Independent providers. Call {PHONE_DISPLAY}.",
}
