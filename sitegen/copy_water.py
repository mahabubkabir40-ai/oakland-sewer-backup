"""Water damage restoration pages. County hub is in copy_hubs.py."""
from site_config import PHONE_DISPLAY, PHONE_TEL

from sitegen.render import a, callout, h2, h3, nearby_section, p, ul

def royal_oak():
    return "\n".join([
        h2("Water extraction in Royal Oak houses"),
        p(
            "Water damage restoration in Royal Oak begins with where the water entered. In most Royal Oak basements the usual paths are a basement floor drain, a window well, a "
            "failed sump, or a supply line at the laundry. Extraction is the removal of standing water "
            "and the soaked layers you can already see. It is not the whole restoration."
        ),
        p(
            "Many Royal Oak basements hold storage pushed against the walls. Extraction "
            "that stops at the open floor leaves the bottom of every box and the lower drywall wet. Ask "
            "the local crew, before they start, how far up they will open walls. Call "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " for the extraction."
        ),
        h2("Structural drying after the pump-out"),
        p(
            "Structural drying is the unglamorous middle of water damage repair. Air has to move across "
            "wet masonry and any wood that took on water, and someone has to recheck it on later days. "
            "Royal Oak owners sometimes expect a single afternoon because the floor looks dry by evening. "
            "The slab edge and the sill can still be wet. The crew should explain how they will "
            "measure that. Ask them for a drying plan in writing. The schedule comes from what they find in the walls."
        ),
        p(
            "If the loss is mostly a flooded basement from storm water or a sump, read "
            + a("/royal-oak-flooded-basement", "flooded basement cleanup and water removal in Royal Oak")
            + ". If a drain discharged sewage, drying alone is the wrong first step. "
            "Use " + a("/royal-oak-sewage-extraction", "sewage extraction")
            + " and " + a("/royal-oak-sewer-cleanup", "sewer backup cleanup") + "."
        ),
        h2("Sewage and other heavily contaminated water"),
        p(
            "Sewage, and water that has mixed with it, is heavily contaminated. Porous materials that absorbed it "
            "are usually removed, not "
            "dried and kept. Royal Oak backups through floor drains fall in that group. A clean supply-line "
            "break does not, unless the water sat long enough to become foul. "
            + a("/royal-oak-basement-sanitization", "Sanitizing after the backup")
            + " is the residue step, done by the crew. Ask that company what training and insurance they carry."
        ),
        h3("Basement flooding causes that show up in Royal Oak"),
        ul([
            "Roots in the private lateral, which the homeowner owns up to and including the connection.",
            "Window wells without a cover when the soil is already saturated.",
            "Sump failure. See " + a("/royal-oak-sump-pump-repair", "sump pump repair in Royal Oak") + ".",
            "A surcharged city main in a hard storm. Royal Oak's Sewer Division, (248) 246-3300, can speak to the public main.",
        ]),
        h2("Insurance questions for your insurer"),
        p(
            "Water damage and sewer backup are often treated differently on a homeowners policy. A sudden "
            "pipe break and a sewer backup are not the same endorsement. Groundwater is frequently limited "
            "or excluded. "
            "The crew may photograph and record moisture. Ask them whether documentation is "
            "included. Ask your insurer what your form actually says. A contractor's guess is not a coverage decision."
        ),
        p(
            "Royal Oak is a member of the former Twelve Towns program, now the George W. Kuhn Retention Treatment Basin. That is background for how regional storm water is handled, not a finding about your lateral."
        ),
        callout(
            "What to tell the crew on a Royal Oak water-damage call",
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
            + ". A local crew handles the drying. "
            "The air movers and the price come from that company."
        ),
        h2("Structural drying where the basement is living space"),
        p(
            "Drying a Troy family room in the basement fails if the furniture stays on the wet floor and "
            "the doors stay closed. The crew should say what has to be moved and whether contents "
            "manipulation is in the price. Structural drying also includes the cavity behind the wall if "
            "the water climbed. A palm test on the paint is not a measurement. Ask what instrument they "
            "use and when they will come back."
        ),
        p(
            "If the loss is a flooded basement, read "
            + a("/troy-flooded-basement", "flooded basement cleanup and basement water removal in Troy")
            + ". A sanitary backup is "
            + a("/troy-sewer-cleanup", "sewer backup cleanup")
            + " and " + a("/troy-sewage-extraction", "sewage extraction")
            + ". A pump that quit is " + a("/troy-sump-pump-repair", "sump pump repair") + "."
        ),
        h2("When Troy water is sewage"),
        p(
            "If a basement bath or floor drain overflowed, treat the loss as sewage. It is heavily contaminated. "
            "Carpet and pad in a finished Troy basement that sat in that water are "
            "typically discarded. Kids' furniture and cloth bins in the same room usually are too. "
            + a("/troy-basement-sanitization", "Sanitizing")
            + " comes after removal, not before. A clear sump overflow with no drain involvement is a "
            "different, often smaller, water damage repair. Do not let anyone dry sewage-soaked pad in place."
        ),
        h3("Basement flooding causes in Troy"),
        ul([
            "Sump pumps that lose power in a storm. DTE serves these neighborhoods. The outage and the flood are linked, and the pump may still need service after the lights return.",
            "Roots or a cracked joint in the private lateral under the yard.",
            "Street storm drains that overflow in a heavy rain. Street water and a basement backup are not automatically the same pipe.",
            "Window wells and lower-level doors that let in surface water during a long rain.",
        ]),
        h2("Insurance, without a coverage promise"),
        p(
            "A Troy water loss can be reduced when the policy excludes sewer backup, excludes "
            "groundwater, or requires the water to be sudden. Ask your insurer what your form says. The "
            "crew can document moisture if you ask them to. Troy discharges through three districts, and George W. Kuhn is one of them. Ask the Water Division, 248-524-3370, which one serves the house. A regional district does not explain a private lateral failure."
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
            "bedroom in the basement of a 1960s or 1970s house, or a utility corner that shares a wall "
            "with living space. Along the I-75 side of the city and near the Troy Historic Village, the "
            "lower level may still be the original unfinished room. Near Big Beaver and the subdivisions "
            "around Somerset Collection it is more often finished. The repair path is not the same. "
            "Unfinished concrete can be cleaned and dried. Carpet pad that sat in water usually cannot."
        ),
        p(
            "Ask the local crew to separate extraction, drying, and any rebuild in writing. "
            "The crew schedules the rebuild and chooses materials. Ask for that written scope before work starts. If the "
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
            "The number is " + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + ". "
            "Ask them for license, insurance, and a written scope before they start."
        ),
        h2("Structural drying of plaster and masonry"),
        p(
            "Plaster releases water slowly and stains when it stays damp. Structural drying in these "
            "houses is as much about time and rechecks as about the number of fans. A crew that wants "
            "to demolish every soft spot on hour one may be right, or they may be skipping a drying "
            "attempt you would rather try on intact trim. Ask them to mark what is definitely coming out "
            "and what they will test again. Water damage repair, in the sense of putting finishes back, "
            "is a later trade. The work to arrange now is the water and the damaged materials, not a remodeling bid."
        ),
        p(
            "Storm flooding and sump overflow sit on "
            + a("/birmingham-flooded-basement", "the flooded basement page")
            + ". Sewage is on " + a("/birmingham-sewer-cleanup", "sewer backup cleanup")
            + " and " + a("/birmingham-sewage-extraction", "sewage extraction")
            + ". Pumps are " + a("/birmingham-sump-pump-repair", "sump pump repair") + "."
        ),
        h2("Sewage in a finished Birmingham lower level"),
        p(
            "Sewage in a guest room or a lower-level office is heavily contaminated. Upholstery, rugs, and "
            "the back of built-in shelving that wicked it up are not a cleaning problem. "
            + a("/birmingham-basement-sanitization", "Sanitization")
            + " after removal is part of the same hire, not a separate maid appointment. A long rain can also push clear water in through the foundation. If you did not see a drain "
            "overflow and there is no sewage odor, say that. Mislabeling a seepage flood as sewage, or "
            "the reverse, sends the job down the wrong path."
        ),
        h3("Basement flooding causes in Birmingham"),
        ul([
            "Roots or a cracked joint in the private lateral.",
            "Window wells and stairwells on houses that sit slightly below the sidewalk grade.",
            "Downspouts that discharge at the foundation instead of about 6 feet out, as the city FAQ advises.",
            "Failed sumps during outages. The electric utility is DTE. Restoring power does not repair a burned pump.",
        ]),
        h2("What to ask about your insurance"),
        p(
            "Coverage for Birmingham water damage is a question for your insurer. Many policies handle a sudden "
            "plumbing discharge differently from sewer backup and from groundwater seepage. "
            "Ask the crew whether their documentation is itemized."
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
            "to you and the crew, on site."
        ),
        p(
            "A newer finished room in the same city, with standard drywall and replaceable carpet, can "
            "follow a faster demolition plan. Do not let a crew use one plan for both houses. "
            "Photograph the water line before anything is moved, especially on plaster, because the stain "
            "line is the record. The city index is "
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
            "original flooring. Berkley is a city of bungalows, with shops along 12 Mile and traffic on Coolidge. Extraction has to remove water "
            "from the basement without tracking it onto the oak or maple at the top of a steep stair. "
            "Joist bays are close to that floor. Wet insulation in those bays is water damage to the "
            "house you live in, not only to the cellar."
        ),
        p(
            "Call " + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " and say the stair is short and the first floor is original wood."
        ),
        h2("Structural drying in a low basement"),
        p(
            "There is little headroom for equipment, and the stair limits what can be carried down. "
            "Structural drying still requires air at the wet surfaces and a later moisture check. A "
            "single dehumidifier in the middle of a cluttered bungalow basement dries the air and not "
            "the sill. Ask the crew what they will move. Water damage repair of the first-floor "
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
            "Sewage in a Berkley basement does not stay downstairs. The stair, the door, and "
            "any return-air opening connect the rooms. Porous material comes out. Then someone sanitizes "
            "what remains. That sequence is "
            + a("/berkley-basement-sanitization", "basement sanitization after the backup")
            + ". Berkley's sewer is one combined pipe for stormwater and sewage, which can put sewage in the basement during rain. Until "
            "you know, do not treat a storm flood that smells like a drain as clean rainwater."
        ),
        h3("Basement flooding causes in Berkley"),
        ul([
            "Window wells and side-door stairwells that fill during a hard rain.",
            "Sump overload or a dead pump when the power drops.",
            "Roots or a cracked joint in the private lateral.",
            "Downspouts that discharge at the foundation because the side yard is only a few feet wide.",
        ]),
        h2("Insurance on a Berkley policy"),
        p(
            "Whether a Berkley bungalow's policy includes sewer backup, sudden discharge, "
            "or groundwater is a question for your insurer. A crew's photos help that conversation. They are not the "
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
            "first-floor material when you call. A crew that only plans for the cellar will miss it."
        ),
        p(
            "Laundry hookups in these original basements are a common clean-water source: a hose, a "
            "washer pan that was never there, a supply line at the back wall. That loss is still water "
            "damage, and it is not a sewer backup. Keep the two descriptions separate so the extraction "
            "and the insurer conversation match the house. Window wells and side stairs can fill in the same storm as a laundry leak. Every Berkley link is on "
            + a("/berkley", "the city overview")
            + "."
        ),
        nearby_section("water-damage-restoration", "Water damage restoration", "berkley"),
    ])


def clawson():
    return "\n".join([
        h2("Water extraction on Clawson's compact lots"),
        p(
            "Water damage restoration in Clawson starts with access. Brick "
            "bungalows and ranches sit on small lots along 14 Mile Road and the blocks between Royal Oak and Troy. "
            "The basement is often one room. Extraction equipment, wet debris, and the family's cars "
            "are competing for a short driveway. A crew that has not heard that description may show "
            "up with a plan that does not fit. Tell them on the call."
        ),
        p(
            "Call "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " for extraction and drying. Get the price in writing first."
        ),
        h2("Structural drying next to the furnace"),
        p(
            "In a one-room basement the furnace and water heater are in the drying zone. Structural "
            "drying cannot ignore them. If water reached the burners or the controls, the crew and "
            "a heating contractor decide whether the unit runs. Water damage repair "
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
        h2("Sewage in a shared basement room"),
        p(
            "A floor-drain backup in that single room contaminates the mechanical equipment and the "
            "storage together. Treat that water as heavily contaminated. Soft goods come out. Metal "
            "cabinets may be cleaned. The crock, if sewage entered it, is not clean because the floor "
            "was mopped. "
            + a("/clawson-basement-sanitization", "Sanitizing after the Clawson backup")
            + " belongs in the same scope as the extraction. A rain flood through a low window, with "
            "quiet drains and no odor, is a smaller and different water damage job. Describe which one you have."
        ),
        h3("Basement flooding causes in Clawson"),
        ul([
            "Downspouts discharging against the foundation on a lot with almost no side yard.",
            "Roots or a cracked joint in the private lateral.",
            "Sump or power failure during a storm, with the pit in the same room as the furnace.",
            "Load on older sanitary lines in heavy regional rain. The city can discuss the main. Clawson's sewer page lists the George W. Kuhn basin for the regional system.",
        ]),
        h2("Coverage questions for your insurer"),
        p(
            "Ask your insurer whether sewer backup, sudden discharge, or groundwater is on your Clawson "
            "policy. The payment decision is theirs. A written scope "
            "from the crew is what you compare to that conversation. License and insurance for the "
            "work come from the crew."
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
            "put back in service. That decision belongs to the heating contractor and the restoration "
            "crew on site."
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
        ("What does water damage restoration include in Royal Oak?", "Extraction of standing water, removal of materials that cannot be saved, drying of what remains, and, if the water was sewage, sanitizing. Get that scope in writing."),
        ("Is water damage repair the same as restoration?", "Close. Restoration is getting the water out and drying. Repair usually means replacing finishes after that. Drying comes first."),
        ("Does Royal Oak water damage restoration cover sewage backups?", "Yes. Say which water you have. Sewage is a stricter cleanup: carpet pad and the bottom of the drywall usually come out. Call (248) 825-8312."),
        ("If the Royal Oak loss started at a floor drain, who owns the pipe?", "The city is responsible for the main. You are responsible for the lateral up to and including the connection. Weekday basement-water calls are (248) 246-3300. After hours, (248) 246-3500 dispatches sewer personnel. Drying the basement does not decide which pipe failed."),
        ("Does drying the house replace the 45-day Royal Oak notice?", "No. If you believe a sewage disposal event caused the damage, written notice is due within 45 days of discovery. Ask your insurer whether a sewer-backup endorsement is on the policy. Photograph the water line before walls are opened."),
    ],
    "troy": [
        ("Why is Troy water damage restoration often a finished-basement job?", "Many Troy lower levels are carpeted living space in split-levels and subdivisions. The pad and drywall hold more water than an empty utility cellar."),
        ("How is drying a finished Troy lower level different from a bare basement?", "Carpet, pad, and drywall hold water that bare concrete does not. In a 1960s or 1970s finished lower level, expect moisture checks on the pad and the bottom of the drywall, and removal if the water was sewage."),
        ("How is basement flooding different from water damage in Troy?", "Flooding is water in the room. Water damage is what it leaves in carpet, pad, and drywall in a finished lower level. Call (248) 825-8312 for drying."),
        ("Does Troy's three-district sewer map change a water-damage scope?", "It tells you to ask the city which district serves the address: Evergreen-Farmington, Oakland-Troy, or George W. Kuhn. It does not dry the basement. If a drain overflowed, also call the Water Division at 248-524-3370, or Troy Police at 248-524-3477 after hours."),
        ("Does drying a Troy lower level replace the written claim?", "Drying carpet and drywall is the cleanup. If you believe a sewage disposal event caused the loss, written notice to the City Attorney's Office is still due within 45 days of discovery. Ask your insurer whether a sewer-backup endorsement is on the policy. Photograph the water line before the pad is pulled."),
    ],
    "birmingham": [
        ("Can water damage restoration save Birmingham plaster?", "Sometimes, if the wetting is shallow and someone monitors drying. Deeply soaked plaster and sewage-soaked trim often have to come out. The crew decides on site."),
        ("Does drying Birmingham plaster include rebuilding the trim?", "Not automatically. Drying comes before any rebuild, and plaster or trim soaked with sewage often has to come out. Ask for that scope in writing."),
        ("Did Birmingham build relief sewers?", "In part of the city. Birmingham's FAQ says a late-1990s bond financed relief sewers, and that older neighborhoods have combined sewer and storm systems. Drying a wet lower level is still a separate job at the house."),
        ("What rain were Birmingham's older sewers designed around?", "The city says combined and storm sewers were historically designed for about 2 inches in one hour. The system is gravity, with no city pump stations. A backflow preventer and downspouts extended about 6 feet are prevention. Water already in the plaster is a drying and removal job. Claims questions are 248.530.1808, not the water-event line (248) 530-1703."),
        ("Does drying Birmingham plaster replace the 45-day notice?", "Drying is the restoration work. Written notice is still due within 45 days of discovery if you believe a sewage disposal event caused the damage. Use the sewer backup claim form. The water-event line collects flooding data and is not the claim. A late-1990s bond financed relief sewers in part of the city, not on every street."),
    ],
    "berkley": [
        ("Can basement water reach Berkley hardwood floors?", "Yes, through a short stair and through wet joists under the subfloor. Mention original floors when you call so protection and joist checks are in the scope."),
        ("Is water damage restoration appropriate for a sewage backup?", "Yes, as the overall process, with extraction and sanitizing included because sewage is heavily contaminated water. Do not hire a dry-only visit for a backup."),
        ("Who dries a Berkley bungalow?", "A local water damage crew. Call (248) 825-8312 and mention the short stair and any original hardwood above the joists."),
        ("Can Berkley's combined sewer turn a rain flood into a sewage drying job?", "Yes, if wastewater came up the floor drain. The city describes one gravity pipe with no pumps or valves, and flow toward the Clinton through the George W. Kuhn district. Confirm the block with Public Works at 248-658-3490. Written notice for a sewage event is due within 45 days of discovery."),
        ("Does Berkley's lining budget dry the bungalow?", "The city describes up to 800,000 dollars a year on structural lining of the public pipe, with about 35 percent of the system lined over more than 20 years. That is not fans in the basement. The crew dries what remains after sewage or floodwater. Flow still leaves toward the Clinton through the George W. Kuhn district, not the Rouge."),
    ],
    "clawson": [
        ("Can the furnace run while a Clawson basement dries?", "Not if water reached the burners or the controls. The heating contractor and the restoration crew decide whether the unit runs. Drying equipment still has to reach the walls around it."),
        ("Does restoration include the sewer repair?", "No. Removing and drying water does not dig up a lateral or repair a city main. Those are separate."),
        ("Who quotes water damage repair in a Clawson bungalow?", "The cleanup company, in writing, before you agree. Tell them the basement is one room and the driveway is short."),
        ("Who is the Clawson city contact if the water came from a drain?", "The city line on the sewer page is (248) 435-4500; public works is open Monday through Thursday, 7:00 a.m. to 3:30 p.m. Fridays the department is closed. After hours, dispatch is 248-524-3477, extension 1. The city page lists the George W. Kuhn basin. Drying the room does not identify the lateral. A camera does. The 45-day written notice is separate from the drying invoice."),
        ("Will insurance pay the drying bill on a Clawson bungalow?", "Not automatically. Sewer backup is often an added endorsement. Ask your insurer, and photograph damaged items before they leave the one-room basement. The 45-day letter to the city is a separate track. The crew sets the drying price."),
    ],
}

HERO = {
    "royal-oak": "The basement in your Royal Oak house is wet, and sewage makes the cleanup stricter than a clean leak. A local cleanup crew does the water damage restoration in Royal Oak, and they'll tell you when they can be there.",
    "troy": "A finished Troy lower level is wet through the carpet, the pad, and the drywall. Call, and a local cleanup crew does the water damage restoration in Troy. They'll tell you when they can be there.",
    "birmingham": "Water has reached the plaster and older trim in a Birmingham lower level. When you call, you reach a local cleanup crew for water damage restoration in Birmingham, and they'll tell you when they can be there.",
    "berkley": "Water in a Berkley bungalow basement is close to the first floor and a short stair. Your call puts you through to a local cleanup crew for water damage restoration in Berkley, and they'll tell you when they can be there.",
    "clawson": "Water is in a small Clawson basement on a tight lot, and the finishes are soaked. Call, and a local cleanup crew handles water damage restoration in Clawson. They'll tell you when they can be there.",
}

ALT = {
    "royal-oak": "Wet basement materials after a leak or backup, the start of water damage restoration in Royal Oak",
    "troy": "A wet finished basement, a common Troy water damage restoration setting",
    "birmingham": "Water damage on lower-level finishes in an older house, relevant to Birmingham restoration",
    "berkley": "Water in a bungalow basement under living space, a Berkley water damage path",
    "clawson": "A small basement with standing water near mechanical equipment, a Clawson water damage scene",
}

DESCRIPTIONS = {
    "royal-oak": "Water damage restoration in Royal Oak, MI. A local crew extracts water, dries walls and floors, and handles sewage safely. Call (248) 825-8312.",
    "troy": "Water damage restoration in Troy, MI. A local crew dries carpet, pad and drywall in finished lower levels and checks moisture. Call (248) 825-8312.",
    "birmingham": "Water damage restoration in Birmingham, MI. A local crew dries plaster, trim and older lower levels, then rechecks moisture. Call (248) 825-8312.",
    "berkley": "Water damage restoration in Berkley, MI. A local crew removes the water, dries the joists and checks the hardwood above. Call (248) 825-8312.",
    "clawson": "Water damage restoration in Clawson, MI. A local crew removes the water, dries the basement and sorts what can be saved. Call (248) 825-8312 now.",
}
