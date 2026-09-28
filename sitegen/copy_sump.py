"""Sump pump pages: practical checks, no prices, referral voice, unique per city."""
from site_config import PHONE_DISPLAY, PHONE_TEL

from sitegen.render import a, callout, h2, h3, nearby_section, p, ul

def royal_oak():
    return "\n".join([
        h2("Sump pump trouble in Royal Oak's older basements"),
        p(
            "Sump pump repair in Royal Oak is usually a phone call from a pre-1960s house in Vinsetta, "
            "Northwood, or a Woodward-side block, where a pit in the basement is the only thing keeping "
            "clay-rich soil from putting water on the floor. The soils in this part of Oakland County "
            "are commonly slow-draining glacial clays. That is a regional description, not a test of "
            "your yard. What you can see is whether the pit is overflowing."
        ),
        p(
            "Oakland Sewer Pros does not repair pumps and does not sell replacements. "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " can connect you with an independent provider when one is participating. If the floor "
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
            "Did the power drop? DTE outages and sump floods travel together. A battery unit is a conversation with the company you hire, not a product we install.",
        ]),
        h2("What an independent tech is actually diagnosing"),
        p(
            "A stuck float, a check valve that lets water fall back into the pit, a clogged inlet screen, "
            "or a seized motor are the ordinary findings. In Royal Oak crocks that have been in place for "
            "decades, the pit itself may be small for the storm. Replacing the pump without looking at "
            "the discharge line just burns the next motor. Ask the provider to say which of those they "
            "found. We will not quote a price for any of them. The company you hire writes the number."
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
                "Tell the provider the pump's age if you know it, and whether a second pump exists.",
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
            "bare corner. Split-levels near Big Beaver and subdivision basements, including areas like "
            "Northfield Hills, can have carpet within a few feet of the crock. When the pump stops during "
            "a spring thaw or a summer storm, the water does not stay in a utility nook. It is in the room."
        ),
        p(
            "Lower lots along the Big Beaver corridor are where homeowners talk about pumps that run "
            "constantly and then fail. Treat 'high water table' as a pattern to mention to the provider, "
            "not as a measured fact about your lot. Oakland Sewer Pros does not install battery backups "
            "or cast-iron pumps. Call "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " for a referral. If the carpet is already wet, add "
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
            + ". Troy storm drains in the street are the Streets and Drains Division, not the pump in your floor."
        ),
        p(
            "We do not publish a Troy price range. Any figure you remember from an old version of this "
            "site is withdrawn. The provider's written estimate is the only price that counts, and you "
            "should have it before they replace a pump."
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
            "Birmingham sump pump repair often means an older pit in a house near Quarton, Poppleton Park, "
            "or the side streets off Old Woodward and Maple. The foundations are older, the yards have "
            "mature trees, and the lower level may be finished with materials you would rather not soak. "
            "A pump failure during a long rain is how those lower levels flood. The repair is mechanical. "
            "The water left behind is a separate restoration problem."
        ),
        p(
            "We do not sell a particular pump brand and do not claim a technician is standing by in "
            "downtown Birmingham near Shain Park. Call "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " to reach an independent provider if one is available. Oakland Sewer Pros does not turn "
            "wrenches."
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
            + ". Ask the provider which of those they actually do. Many pump companies do not dry plaster."
        ),
        p(
            "Low ground near Quarton can keep a healthy pump running for hours. That is a load problem, "
            "not automatically a failed motor. A technician should measure or at least observe a cycle, "
            "not only swap the unit. You should see a written reason for a replacement. We will not give "
            "you a price band for that replacement."
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
        h2("Sump pump repair in Berkley bungalows"),
        p(
            "Berkley sump pump repair is a tight-space job. The pits are in short basements under 1940s "
            "and 1950s bungalows, on a flat grid off 12 Mile and Coolidge. "
            "Rain does not leave these lots quickly. The pump may be the entire drainage plan for the "
            "basement. When it stops, the water is at the furnace before anyone notices, because the "
            "basement is one low room."
        ),
        p(
            "Call " + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + ". Oakland Sewer Pros refers independent providers. We do not stock pumps for Berkley and "
            "we do not guarantee a visit. If water is already across the floor, say whether it is clear "
            "or whether the floor drain was involved. Clear overflow is "
            + a("/berkley-flooded-basement", "a flood")
            + ". Drain water is " + a("/berkley-sewage-extraction", "sewage") + "."
        ),
        h3("Bungalow-specific pump problems"),
        ul([
            "Lids buried under laundry hampers, so the float cannot rise.",
            "Discharge piping strapped along a low joist, then out a rim joist, where it freezes closer to outside air.",
            "A check valve that chatters because the vertical run is short and the water falls straight back.",
            "Extension cords across a wet floor to a pump that should have had a proper receptacle. Do not add another cord. Tell the provider what you see from the stairs.",
        ]),
        h2("Power, DTE, and a house with one stair"),
        p(
            "When the lights go out, an AC pump stops. Getting a generator or a battery unit into a "
            "Berkley stairwell is part of the practical question. Ask the company whether they even "
            "offer that, and whether the stair allows it. Drying afterward, if the joists got wet, is "
            + a("/berkley-water-damage-restoration", "water damage restoration")
            + " because the first floor is right there. Sanitizing a pit that took sewage is "
            + a("/berkley-basement-sanitization", "a different page")
            + ". Older combined-sewer descriptions for parts of Berkley mean a storm can also push the "
            "floor drain. The pump did not cause that, and repairing the pump will not stop it. Confirm "
            "the street with the city."
        ),
        callout(
            "From the Berkley stair, before anyone arrives",
            ul([
                "Do not step in if you cannot see the floor around the panel.",
                "Listen: rapid clicking is often a check valve, not a 'strong' pump.",
                "Look outside at the discharge point if you can do it without going through the basement.",
                "Ask for a written quote. This site has no Berkley price list.",
            ]),
        ),
        nearby_section("sump-pump-repair", "Sump pump repair", "berkley"),
    ])


def clawson():
    return "\n".join([
        h2("Sump pump repair on Clawson's small bungalow lots"),
        p(
            "Clawson sump pump repair has an access problem before it has a parts problem. Mid-century brick "
            "bungalows and ranches stand on compact lots near 14 Mile, between Royal Oak and Troy. "
            "The pit, the furnace, and the water heater share a small basement. A technician's cart and "
            "a homeowner's car share a short driveway. If you do not mention that, the visit starts with "
            "a surprise."
        ),
        p(
            "We do not repair the pump. "
            + a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)
            + " is a referral to independent providers, subject to availability. Water already on the "
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
        h2("Replacement is not a price on this page"),
        p(
            "Any dollar table that used to sit on Clawson sump pages has been removed. The provider quotes "
            "the pump, the valve, and the labor after seeing the pit. Ask whether water removal is included. "
            "Many are not the same invoice as "
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
        ("Does Oakland Sewer Pros repair sump pumps in Royal Oak?", "No. An independent provider may. We connect the call and do not set the price or the parts."),
        ("What should I do if the Royal Oak pit is overflowing and the power is on?", "From a dry place, you can unplug a humming pump and free a stuck float with a broom handle. Do not step into the water. Then call for a provider and, if the floor is wet, for water removal."),
        ("Will a new pump stop sewer backups?", "No. A sump handles groundwater at the pit. A floor-drain backup is a different pipe. Repairing one does not fix the other."),
    ],
    "troy": [
        ("Why do Troy finished basements make pump failures expensive to ignore?", "Carpet and drywall start at the pit. Minutes of overflow become a water-damage scope, which is separate from the pump repair."),
        ("Can you install a battery backup in Troy?", "We do not install anything. Ask the provider you hire whether they offer a second power source and what it costs. We will not quote it."),
        ("Who maintains Troy's street drains?", "The city's Streets and Drains Division handles public storm drainage. Your sump is private."),
    ],
    "birmingham": [
        ("Is sump pump repair in Birmingham a plumbing visit or a restoration visit?", "The pump is a mechanical repair. Wet plaster is restoration. You may need both. Ask each company what they actually cover."),
        ("Should I replace a Birmingham pump that runs constantly near Quarton?", "Not on this page's advice. Constant running can be groundwater load, a stuck switch, or a bad valve. Someone has to watch a cycle before they sell you a pump."),
        ("Do you guarantee the next storm will stay out?", "No. We do not guarantee pump performance or a dry basement."),
    ],
    "berkley": [
        ("Can a Berkley stair fit a battery-backup system?", "Sometimes. Describe the stair when you call. The provider decides if the equipment fits. We do not."),
        ("Why does my Berkley pump short-cycle?", "A failed check valve is a common reason: water falls back and the float rises again immediately. It can also be a stuck switch. Let the provider distinguish them."),
        ("Does the city repair my sump?", "No. The pit in your basement is not the city main. The city is the contact if a public sewer is surcharging."),
    ],
    "clawson": [
        ("What if the Clawson driveway cannot hold a work truck?", "Say so before the appointment. The provider should agree to a street setup or decline. We do not scout the lot."),
        ("The pump sits next to the furnace and both are wet. Who do I call?", "Call for water removal and for a pump repair, and do not turn the furnace on. They may be different companies. Stay out of the room if power and water have mixed."),
        ("Are the old prices on this page still valid?", "There is no price list. Earlier dollar ranges were removed because this site does not control what providers charge."),
    ],
}

HERO = {
    "royal-oak": "Sump pump repair in Royal Oak is a referral to an independent provider for a pit that is stuck, dead, or overflowing. We do not repair pumps or quote a price. If the floor is wet, say so.",
    "troy": "Troy sump pump repair often protects a finished lower level near Big Beaver and in subdivisions. Call for an independent provider. Oakland Sewer Pros does not install pumps or promise a visit.",
    "birmingham": "Sump pump repair in Birmingham, Michigan is the mechanical half of a wet lower level in an older Oakland County house, not a Birmingham, Alabama job. We refer you to an independent provider. We do not sell pumps or guarantee a dry basement.",
    "berkley": "Berkley sump pump repair happens in a short bungalow basement that may flood fast when the pump stops. This is a referral line, not a repair shop, and it has no price list.",
    "clawson": "Clawson sump pump repair has to fit a small basement and a short driveway. Call to reach an independent provider. We do not do the repair and we do not publish prices.",
}

ALT = {
    "royal-oak": "A basement sump pit, the equipment Royal Oak homeowners call about when the pump stops",
    "troy": "A sump pump in a finished lower level, a Troy repair and overflow risk",
    "birmingham": "An older basement sump installation, relevant to Birmingham pump repairs",
    "berkley": "A sump pump in a small bungalow basement, a Berkley repair setting",
    "clawson": "A sump pump beside other basement equipment, typical of tight Clawson mechanical rooms",
}

DESCRIPTIONS = {
    "royal-oak": "Sump pump repair in Royal Oak, Michigan. We refer independent providers and do not quote prices. Call {PHONE_DISPLAY}.",
    "troy": "Sump pump repair in Troy, Michigan for overflowing pits and dead pumps. Independent providers. Call {PHONE_DISPLAY}.",
    "birmingham": "Sump pump repair in Birmingham, Michigan, Oakland County. Not Alabama. Independent providers. Call {PHONE_DISPLAY}.",
    "berkley": "Sump pump repair in Berkley, Michigan bungalows. Connect with an independent provider. Call {PHONE_DISPLAY}.",
    "clawson": "Sump pump repair in Clawson, Michigan. Independent providers, no price list on this site. Call {PHONE_DISPLAY}.",
}
