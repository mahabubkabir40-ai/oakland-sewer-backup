"""Sump pump pages: practical checks, no prices, unique per city."""
from site_config import PHONE_DISPLAY, PHONE_TEL

from sitegen.citations import (
    BERK_TIPS,
    BHAM,
    CLAW_DPW,
    CLAW_CCTV,
    MCL1419,
    RO_FLOOD,
    RO_SEWER,
    TROY_AGENDA,
    TROY_CLAIMS,
    WRC_GWK,
    cite,
)
from sitegen.render import a, callout, h2, h3, nearby_section, p, ul

def royal_oak():
    return "\n".join([
        h2("Sump pump trouble in Royal Oak's older basements"),
        p(
            "Sump pump repair in Royal Oak is a call about a pit that is overflowing or a pump that has quit. "
            "A sump lifts groundwater. A floor-drain backup is a different pipe, and Royal Oak says the city "
            "is responsible for the main while the homeowner owns the lateral up to and including the connection. "
            "What you can see from the stairs is whether the pit is overflowing."
        ),
        p(
            "Royal Oak explains that when a house's sewer line is blocked by tree roots, disposable diapers or grease, "
            "water from the weeping tile around the basement walls can't drain either, and it comes in through wall cracks, "
            "the floor-wall seam, and most often the floor drain. "
            "The regional storage for this system is the George W. Kuhn Retention Treatment Basin, under the I-75 overpass "
            "at 12 Mile Road in Madison Heights, which can hold and treat 150 million gallons."
        ),
        p(
            "Call "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " for a pump repair crew. If the floor "
            "is already under water, also tell them you may need "
            + a("/royal-oak-flooded-basement", "basement water removal")
            + ". If the water smells like a drain, it is "
            + a("/royal-oak-sewage-extraction", "sewage extraction")
            + ", not a clean pump overflow."
        ),
        h3("Checks you can do from the stairs"),
        ul([
            "Is the float pinned against the crock wall? A broom handle can free a stuck float. Do not climb into the pit.",
            "Is the pump humming and not moving water? Unplug it if you can do that from a dry spot so the motor does not cook.",
            "Is the discharge line frozen or disconnected outside? Michigan freeze-thaw will ice a line that runs across the yard.",
            "Did the power drop? DTE outages and sump floods travel together. A battery unit is something to ask the crew about.",
        ]),
        h2("What a pump tech is actually diagnosing"),
        p(
            "A stuck float, a check valve that lets water fall back into the pit, a clogged inlet screen, "
            "or a seized motor are the ordinary findings. In an older crock, the pit itself may be small for the storm. Replacing the pump without looking at "
            "the discharge line just burns the next motor. Ask the crew to say which of those they "
            "found. The price for each of those repairs comes from the crew."
        ),
        p(
            "A sump that took sewage needs cleaning as well as a mechanical repair. That residue work is "
            + a("/royal-oak-basement-sanitization", "sanitizing after the backup")
            + ". The broader wet-building process is "
            + a("/royal-oak-water-damage-restoration", "water damage restoration in Royal Oak")
            + ". City sewer mains are a "
            + a("https://www.romi.gov/384/Sewer-Division", "Sewer Division")
            + " question, separate from the pump in your floor."
        ),
        callout(
            "Royal Oak electrical line",
            ul([
                "If the water is at the outlet the pump uses, do not wade in to unplug it.",
                "Do not stand in the pit.",
                "Tell the crew the pump's age if you know it, and whether a second pump exists.",
                "Ask them to show license and insurance. Pump work and water removal may be different trades.",
            ]),
        ),
        nearby_section("sump-pump-repair", "Sump pump repair", "royal-oak"),
    ])


def troy():
    return "\n".join([
        h2("Sump pump repair in Troy, where the lower level is finished"),
        p(
            "Troy sump pump repair matters because the pit often sits in a finished lower level, not a "
            "bare corner. Finished lower levels can have carpet within a few feet of the crock. When the pump stops during "
            "a spring thaw or a summer storm, the water does not stay in a utility nook. It is in the room."
        ),
        p(
            "If the pump runs constantly before it fails, tell the crew; that pattern changes the repair. A battery backup or a new pump comes from the crew. Call "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + ". If the carpet is already wet, add "
            + a("/troy-flooded-basement", "Troy basement water removal")
            + " to the request."
        ),
        h3("Failure modes that show up in these houses"),
        ul([
            "Short-cycling: a bad check valve lets the discharge column fall back, so the pump starts every few seconds until it overheats.",
            "A float trapped by the lid or by stored bins pushed against the pit. Finished rooms collect clutter around the only access hatch.",
            "Power loss. Storms that fill the pit also drop DTE lines. Without a second power source, an AC-only pump stops with the lights.",
            "A frozen or buried discharge outlet on the lawn, common after a thaw refreezes overnight.",
        ]),
        h2("Repair the pump and deal with the water as two scopes"),
        p(
            "A plumber or pump specialist may repair the unit. The soaked pad is water damage. Do not "
            "assume one company wants both. Ask. "
            + a("/troy-water-damage-restoration", "Water damage restoration in Troy")
            + " describes the drying side. If sewage entered the pit, stop calling it a clean overflow and "
            "read " + a("/troy-sewage-extraction", "sewage extraction")
            + " and " + a("/troy-basement-sanitization", "sanitizing")
            + "."
        ),
        p(
            "The price is the crew's written estimate. Get it before they replace a pump."
        ),
        callout(
            "Troy: keep the finished room in mind",
            ul([
                "Note whether carpet is touching the pit lid.",
                "Do not run a household fan across overflow water if you are unsure it is clean.",
                "Ask whether the quote includes hauling wet pad or only the pump.",
                "Verify insurance for both plumbing and, if needed, water removal.",
            ]),
        ),
        nearby_section("sump-pump-repair", "Sump pump repair", "troy"),
    ])


def birmingham():
    return "\n".join([
        h2("Sump pump repair in older Birmingham basements"),
        p(
            "Birmingham sump pump repair often means an older pit in an older home. "
            "Birmingham's FAQ says its older combined and storm sewers were designed for about 2 inches of rain in one hour; "
            "a longer or heavier storm is when a pit and a floor drain can both be working at once. "
            "The city posted an engineer's presentation on the August 24, 2023 rain event. "
            "A pump failure during a long rain is how those lower levels flood. The repair is mechanical. "
            "The water left behind is a separate restoration problem."
        ),
        p(
            "Call "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " to reach a local crew for the repair."
        ),
        h3("What fails in these installations"),
        ul([
            "Discharge lines that run out through old foundation walls and then freeze or crush in a planting bed.",
            "Floats that hang up in crocks that were not built to modern diameters.",
            "Check valves hidden in finished ceilings of a lower level, so the short-cycling is heard but not seen.",
            "Single plugs on circuits that also feed a freezer. A trip of that breaker looks like a dead pump.",
        ]),
        h2("Do not replace the pump and ignore the finishes"),
        p(
            "If water reached plaster or wood trim, pumping the pit back down does not undo "
            + a("/birmingham-water-damage-restoration", "water damage")
            + ". "
            + a("/birmingham-flooded-basement", "Basement water removal")
            + " is the flooding page. A backup that used the pit as a drain is sewage; see "
            + a("/birmingham-sewer-cleanup", "sewer backup cleanup")
            + " and " + a("/birmingham-basement-sanitization", "sanitizing")
            + ". Ask the crew which of those they actually do. Many pump companies do not dry plaster."
        ),
        p(
            "A long rain can keep a healthy pump running for hours. That is a load problem, "
            "not automatically a failed motor. A technician should measure or at least observe a cycle, "
            "not only swap the unit. You should see a written reason for a replacement. The price comes from that company."
        ),
        callout(
            "Birmingham questions for the pump company",
            ul([
                "Did the motor fail, or did the line freeze?",
                "Where is the check valve, and will you replace it in the same visit?",
                "Can you work without standing water on the finished floor, or do I need a water-removal company first?",
                "What license applies to this repair?",
            ]),
        ),
        nearby_section("sump-pump-repair", "Sump pump repair", "birmingham"),
    ])


def berkley():
    return "\n".join([
        h2("Sump pump repair in Berkley"),
        p(
            "Berkley sump pump repair is a tight-space job. The pits are in short basements off 12 Mile and Coolidge. "
            "The pump may be the entire drainage plan for the "
            "basement. When it stops, the water is at the furnace before anyone notices, because the "
            "basement is one low room."
        ),
        p(
            "Call " + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + ". "
            "If water is already across the floor, say whether it is clear "
            "or whether the floor drain was involved. Clear overflow is "
            + a("/berkley-flooded-basement", "a flood")
            + ". Drain water is " + a("/berkley-sewage-extraction", "sewage") + "."
        ),
        p(
            "The regional storage for this system is the George W. Kuhn Retention Treatment Basin, under the I-75 overpass "
            "at 12 Mile Road in Madison Heights, which can hold and treat 150 million gallons. "
            "Berkley designs its streets to hold water during a hard rain and uses restrictor covers on catch basins, "
            "so curb ponding is expected, while a sump that stops is a separate, private problem."
        ),
        h3("Pump problems in these basements"),
        ul([
            "Lids buried under laundry hampers, so the float cannot rise.",
            "Discharge piping strapped along a low joist, then out a rim joist, where it freezes closer to outside air.",
            "A check valve that chatters because the vertical run is short and the water falls straight back.",
            "Extension cords across a wet floor to a pump that should have had a proper receptacle. Do not add another cord. Tell the crew what you see from the stairs.",
        ]),
        h2("Power, DTE, and a house with one stair"),
        p(
            "When the lights go out, an AC pump stops. Getting a generator or a battery unit into a "
            "Berkley stairwell is part of the practical question. Ask the company whether they even "
            "offer that, and whether the stair allows it. Drying afterward, if the joists got wet, is "
            + a("/berkley-water-damage-restoration", "water damage restoration")
            + " because the first floor is right there. Sanitizing a pit that took sewage is "
            + a("/berkley-basement-sanitization", "a different page")
            + ". Berkley's sewer is combined, so a storm can also push the "
            "floor drain. The pump did not cause that, and repairing the pump will not stop it."
        ),
        callout(
            "From the Berkley stair, before anyone arrives",
            ul([
                "Do not step in if you cannot see the floor around the panel.",
                "Listen: rapid clicking is often a check valve, not a 'strong' pump.",
                "Look outside at the discharge point if you can do it without going through the basement.",
                "Ask for a written quote. The price comes from the crew.",
            ]),
        ),
        nearby_section("sump-pump-repair", "Sump pump repair", "berkley"),
    ])


def clawson():
    return "\n".join([
        h2("Sump pump repair on Clawson's small lots"),
        p(
            "Clawson sump pump repair has an access problem before it has a parts problem. Older homes "
            "stand on compact lots near 14 Mile, between Royal Oak and Troy. "
            "Clawson describes its combined sewer as strictly gravity fed: flow runs from smaller pipes to larger pipes, "
            "typically on major roads, before it enters the county system, with no pumps. "
            "The city has been cleaning and camera-inspecting its whole sanitary sewer system since December 2024, in 18 sections. "
            "The regional storage for this system is the George W. Kuhn Retention Treatment Basin, under the I-75 overpass "
            "at 12 Mile Road in Madison Heights, which can hold and treat 150 million gallons. "
            "The pit, the furnace, and the water heater share a small basement. A technician's cart and "
            "a homeowner's car share a short driveway. If you do not mention that, the visit starts with "
            "a surprise."
        ),
        p(
            "Call "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " and a local crew comes to look at the pump. Water already on the "
            "floor belongs on " + a("/clawson-flooded-basement", "the flooded basement page")
            + " as well. Sewage in the pit belongs on "
            + a("/clawson-sewage-extraction", "sewage extraction") + "."
        ),
        h3("What to look for without entering a flooded mechanical room"),
        ul([
            "A pump cord under water. Leave it. Power off from a dry location if you know how and can stay dry.",
            "A discharge line that pops apart outside and dumps against the same foundation, refilling the pit.",
            "Ice at the outlet after a thaw, which stalls the impeller and overheats the motor when power remains.",
            "A float rod bent because storage was stacked on the lid. Common when the basement is the only storage.",
        ]),
        h2("A replacement price comes from the company"),
        p(
            "The crew quotes "
            "the pump, the valve, and the labor after seeing the pit. Ask whether water removal is included; it is often a separate invoice from "
            + a("/clawson-water-damage-restoration", "water damage restoration")
            + ". A dirty crock after a backup is "
            + a("/clawson-basement-sanitization", "sanitizing")
            + ", not a favor added silently. Downspouts on these tight lots often discharge at the wall "
            "and keep a good pump from ever resting. A repair that ignores the downspout will be back. "
            "The regional drainage district associated with Clawson is the George W. Kuhn system under "
            "the Oakland County Water Resources Commissioner. Your pit is still yours."
        ),
        callout(
            "Clawson call script",
            ul([
                "Say the basement is one room and name what equipment is in the water.",
                "Say how short the driveway is.",
                "Ask which license covers pump replacement.",
                "Ask for the quote before a unit is unboxed.",
            ]),
        ),
        nearby_section("sump-pump-repair", "Sump pump repair", "clawson"),
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
        ("Is a sump overflow covered by Michigan's 45-day sewer claim rule?", "Usually not. Michigan's statute says it is not a sewage disposal system event if the main cause was a connection on your own property, such as a sump system, building drain, or downspout (MCL 691.1416). A floor drain backup from the city main can be different."),
        ("What should I do if the Royal Oak pit is overflowing and the power is on?", "From a dry place, you can unplug a humming pump and free a stuck float with a broom handle. Do not step into the water. Then call for a crew and, if the floor is wet, for water removal."),
        ("Will a new pump stop sewer backups?", "No. A sump handles groundwater at the pit. A floor-drain backup is a different pipe. Repairing one does not fix the other. Royal Oak says the city is responsible for the main and the homeowner for the lateral through the connection." + cite("City of Royal Oak Sewer Division", RO_SEWER)),
        ("Who do I call if the Royal Oak pit overflowed and the floor drain also moved?", "Treat drain water as sewage. City basement-water calls are (248) 246-3300 on weekdays and (248) 246-3500 after hours. Call (248) 825-8312 to reach a local crew for the pump and, if the floor is wet, for water removal." + cite("City of Royal Oak, Responding to Street and Basement Flooding", RO_FLOOD)),
        ("Does a stuck Royal Oak sump start the 45-day city notice?", "A sump handles groundwater at the pit. That overflow is not automatically a sewage disposal event. If the floor drain also discharged, written notice is due within 45 days of discovery, with your name, address, and phone, the property address, the discovery date, and a brief description. Confirm with the city who receives the letter." + cite("Michigan Legislature, MCL 691.1419", MCL1419)),
    ],
    "troy": [
        ("Why do Troy finished basements make pump failures expensive to ignore?", "Carpet and drywall start at the pit. Minutes of overflow become a water-damage scope, which is separate from the pump repair."),

        ("Who maintains Troy's street drains?", "The city handles street storm drains. Your sump is private. Wastewater leaves Troy through three districts, Evergreen-Farmington, Oakland-Troy, and George W. Kuhn. That map does not tell you why the pit failed." + cite("Troy City Council agenda, November 14, 2022", TROY_AGENDA)),
        ("Should I call Troy's Water Division about a dead sump pump?", "The Water Division at 248-524-3370, or Troy Police at 248-524-3477 after hours, is the city's sewer backup desk. A sump in the basement is a house repair. Call (248) 825-8312 for the pump." + cite("City of Troy, Legal Claims for Overflows and Backups", TROY_CLAIMS)),
        ("Can a battery backup be part of a Troy pump visit?", "Ask the crew. They quote a second power source after they see the pit. If carpet is already wet, drying is a separate job."),
        ("If a Troy floor drain gurgled while the pump failed, where does the letter go?", "The pit and the sanitary drain are different pipes. If sewage came up the drain and you believe the public system was involved, Troy directs written claims to the City Attorney's Office within 45 days of discovery. Include your name, address, and phone, the property address, the discovery date, and a brief description. A sewer-backup endorsement is a separate question for your insurer." + cite("City of Troy, Legal Claims for Overflows and Backups", TROY_CLAIMS)),
    ],
    "birmingham": [
        ("Is sump pump repair in Birmingham a plumbing visit or a restoration visit?", "The pump is a mechanical repair. Wet plaster is restoration. You may need both. Ask each company what they actually cover."),
        ("Should I replace a Birmingham pump that runs constantly?", "Not from a guess. Constant running can be groundwater load, a stuck switch, or a bad valve. Someone has to watch a cycle before they sell you a pump."),
        ("Will a repaired Birmingham pump hold back the next storm by itself?", "A repair fixes the pump. It does not change the city's gravity sewers, which have no municipal lift stations. Ask for a written reason before anyone replaces the unit." + cite("City of Birmingham Risk Management", BHAM)),
        ("Is a backflow preventer the same as sump pump repair in Birmingham?", "No. The city lists a backflow preventer, downspouts extended about 6 feet, and grading away from the foundation as prevention at the house. The sump in the basement is a different device. Call (248) 825-8312 for the pump." + cite("City of Birmingham Risk Management", BHAM)),
        ("If a Birmingham drain backed up while the sump failed, which form is the claim?", "The house sump and the sewer lateral are different devices. If sewage came up a drain, use the city's sewer backup claim form, not the water-event tracking form. Claims questions are 248.530.1808. Written notice is due within 45 days of discovery. Birmingham's sewers are gravity, and the city owns no pump or lift stations." + cite("City of Birmingham Risk Management", BHAM) + cite("Michigan Legislature, MCL 691.1419", MCL1419)),
    ],
    "berkley": [
        ("Can a battery backup pump fit in a short Berkley basement?", "Sometimes. It depends on the pit and where the unit can sit above the floor. Describe the short stair when you call, and ask whether they install battery units."),
        ("Why does my Berkley pump short-cycle?", "A failed check valve is a common reason: water falls back and the float rises again immediately. It can also be a stuck switch. Let the crew distinguish them."),
        ("Does Berkley repair the sump in my basement?", "No. The city's sewer is gravity with no pumps and no valves. The pit in your basement is yours. Call Public Works at 248-658-3490 if a floor drain is also surcharging, because that combined pipe is a different problem from a dead pump." + cite("City of Berkley, Flood Tips for Residents", BERK_TIPS)),
        ("What should I say when I call (248) 825-8312 about a Berkley pump?", "Describe the short stair, whether the floor is already wet, and whether the water is clear or smells like a drain. Clear overflow is a pump and water-removal job. Drain water is sewage."),
        ("Does Berkley's sewer lining program fix my sump?", "The city has spent up to 800,000 dollars a year on structural lining, and about 35 percent of the system has been lined over more than 20 years. That work is the public combined pipe. The pit in the basement is yours. If sewage also came up the floor drain, the Sewer Backup Claims Form and the 45-day written notice still apply. Public Works is 248-658-3490." + cite("City of Berkley, Flood Tips for Residents", BERK_TIPS) + cite("Michigan Legislature, MCL 691.1419", MCL1419)),
    ],
    "clawson": [
        ("Why does my Clawson pump keep running after it rains?", "On a tight lot, a downspout that discharges at the wall can refill the pit, and a discharge line that pops apart outside dumps water back at the foundation. Ask the crew to check both, not only the pump."),
        ("The pump sits next to the furnace and both are wet. Who do I call?", "Call for water removal and for a pump repair, and do not turn the furnace on. They may be different companies. Stay out of the room if power and water have mixed."),
        ("Who quotes a Clawson pump replacement?", "The company that sees the pit, in writing. Describe the short driveway when you call (248) 825-8312."),
        ("If the Clawson pump failed on a Friday, who is the city after-hours line?", "DPW is closed on Fridays. Clawson's non-emergency dispatch line is 248-524-3477, extension 1. Emergencies go to 911. That dispatch line does not repair the pump next to your furnace. The city sewer page also points to the George W. Kuhn basin, which is the regional system, not your crock." + cite("City of Clawson DPW page", CLAW_DPW)),
        ("Does a dead Clawson sump mean the George W. Kuhn basin failed?", "The basin is the regional system listed on the city sewer page, along with the Oakland County Water Resources Commissioner. Your crock is a private pump. If the floor drain also backed up, treat that water as sewage and ask the city in writing who receives the 45-day notice. The basin does not restart the pump next to the furnace." + cite("Oakland County Water Resources Commissioner, George W. Kuhn Retention Treatment Basin", WRC_GWK) + cite("Michigan Legislature, MCL 691.1419", MCL1419)),
    ],
}

HERO = {
    "royal-oak": "The sump in your Royal Oak basement is stuck, dead, or overflowing. A local crew does the sump pump repair in Royal Oak, and they'll tell you when they can be there. If the floor is wet, say so.",
    "troy": "The sump quit under a finished Troy lower level, and the carpet is next. Call, and a local crew does the sump pump repair in Troy. They'll tell you when they can be there.",
    "birmingham": "The sump failed in an older Birmingham, Michigan house and the lower level is getting wet. When you call, you reach a local crew for sump pump repair in Birmingham, and they'll tell you when they can be there.",
    "berkley": "The pump stopped in a short Berkley basement, and the water can rise fast. Your call puts you through to a local crew for sump pump repair in Berkley, and they'll tell you when they can be there.",
    "clawson": "The pump stopped in a small Clawson basement with a short driveway. Call, and a local cleanup crew handles sump pump repair in Clawson. They'll tell you when they can be there.",
}

ALT = {
    "royal-oak": "A basement sump pit, the equipment Royal Oak homeowners call about when the pump stops",
    "troy": "A sump pump in a finished lower level, a Troy repair and overflow risk",
    "birmingham": "An older basement sump installation, relevant to Birmingham pump repairs",
    "berkley": "A sump pump in a small basement, a Berkley repair setting",
    "clawson": "A sump pump beside other basement equipment, typical of tight Clawson mechanical rooms",
}

DESCRIPTIONS = {
    "royal-oak": "Sump pump repair in Royal Oak, MI. A local crew can check the pump and deal with the water if the basement floor is wet. Call (248) 825-8312.",
    "troy": "Sump pump repair in Troy, MI. A local crew can check the pump and deal with the water under a finished lower level. Call (248) 825-8312 now.",
    "birmingham": "Sump pump repair in Birmingham, MI. A local crew can check the pump and deal with the water. Ask before any replacement. Call (248) 825-8312.",
    "berkley": "Sump pump repair in Berkley, MI. A local crew can check the pump and deal with the water in a small basement. Get a written quote: (248) 825-8312.",
    "clawson": "Sump pump repair in Clawson, MI. A local crew can check the pump and deal with the water next to the furnace. Get the quote in writing: (248) 825-8312.",
}
