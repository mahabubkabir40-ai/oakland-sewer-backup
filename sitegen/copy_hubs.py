"""County service hubs and city hubs."""
from site_config import PHONE_DISPLAY, PHONE_TEL

from sitegen.render import a, h2, h3, p, ul

def services_article():
    return "\n".join([
        h2("What this site actually does"),
        p(
            "Oakland Sewer Pros is a referral service for homeowners in Royal Oak, Troy, Birmingham, "
            "Berkley, and Clawson. You call, and when a participating independent company is available, "
            "you are connected with them. We do not employ technicians, own trucks, or warrant the work. "
            "You confirm the license and insurance that the job requires."
        ),
        h2("Services, and the page to start with"),
        p(a("/water-damage-restoration", "Water damage restoration") + " is the county page for extraction, drying, and sewage water damage. It is the broadest match for a wet basement."),
        p(a("/sewer-backup-cleanup", "Sewer backup cleanup") + " is for sewage that came up through a drain. The five city pages under it are the ones that already focus on that phrase."),
        p(a("/sewage-extraction", "Sewage extraction") + " is the pumping and removal step when the water is contaminated."),
        p(a("/flooded-basement-cleanup", "Flooded basement cleanup") + " is basement water removal when you are dealing with storm water, a window well, or a sump overflow. If a drain was involved, use the sewage pages."),
        p(a("/sump-pump-repair", "Sump pump repair") + " is the mechanical pump. Overflow cleanup, if the floor is wet, is a water-damage job on top of the repair."),
        p(a("/basement-sanitization", "Basement sanitization") + " means cleaning after sewage or a contaminated flood. It is not a housekeeping service."),
        p(
            "Company pages, which are part of the site and not a service: "
            + a("/about", "about this referral line")
            + ", " + a("/contact", "contact")
            + ", " + a("/privacy", "privacy")
            + ", and " + a("/terms", "terms")
            + "."
        ),
        h2("Cities"),
        p(
            "Choose a city overview, then the service that matches the water: "
            + a("/royal-oak", "Royal Oak") + ", "
            + a("/troy", "Troy") + ", "
            + a("/birmingham", "Birmingham") + ", "
            + a("/berkley", "Berkley") + ", and "
            + a("/clawson", "Clawson") + "."
        ),
    ])


def water_hub():
    return "\n".join([
        h2("Water damage restoration across Oakland County"),
        p(
            "Water damage restoration, for the five cities on this site, means getting water out of a "
            "house, deciding what materials cannot be saved, and drying what remains. Water damage repair "
            "is the phrase people use when finishes also have to be replaced. Oakland Sewer Pros does not "
            "do that work. The phone number connects you with an independent provider when one is participating."
        ),
        h2("Water extraction, drying, and sewage"),
        p(
            "Extraction is the standing water and the soaked layers. Structural drying is the days afterward, "
            "with someone rechecking moisture. If the water came from a sewer drain, restorers treat it as "
            "Category 3, heavily contaminated water. Porous materials usually come out. A clean supply-line "
            "break is a different scope from a basement full of sewage. Say which one you have when you call."
        ),
        h3("Basement flooding in these cities"),
        p(
            "Basement flood cleanup in Oakland County is the county page for storm water and sump overflows: "
            + a("/flooded-basement-cleanup", "flooded basement cleanup")
            + ". Sewage cleanup and sewer backup, when a drain was the source, are "
            + a("/sewer-backup-cleanup", "the sewer backup hub")
            + ". Basement flooding here is local, not one county-wide cause. Royal Oak's older blocks and "
            "Woodward-side window wells are a different pattern from Troy's finished split-levels near "
            "Big Beaver, Birmingham's plaster houses near Quarton and Poppleton, Berkley's flat bungalow "
            "grid, and Clawson's small brick-bungalow basements on 14 Mile. Each city page below is written "
            "for that place."
        ),
        ul([
            a("/royal-oak-water-damage-restoration", "Water damage restoration in Royal Oak"),
            a("/troy-water-damage-restoration", "Water damage restoration in Troy"),
            a("/birmingham-water-damage-restoration", "Water damage restoration in Birmingham"),
            a("/berkley-water-damage-restoration", "Water damage restoration in Berkley"),
            a("/clawson-water-damage-restoration", "Water damage restoration in Clawson"),
        ]),
        h2("What this hub will not tell you"),
        p(
            "It will not quote a price, promise a 24/7 arrival, or say your insurance will pay. Sewer "
            "backup coverage is often a separate endorsement. Groundwater is often limited. Ask your "
            "insurer. Ask the provider for a written scope and for license and insurance. Related county "
            "pages: " + a("/flooded-basement-cleanup", "flooded basement cleanup")
            + ", " + a("/sewer-backup-cleanup", "sewer backup cleanup")
            + ", and " + a("/basement-sanitization", "sanitizing after sewage") + "."
        ),
        p(
            "Homeowner resources: the " + a("/basement-flood-checklist", "printable basement flood checklist")
            + " and the " + a("/sewer-backup-claim-guide", "sewer backup claim guide") + " for the 45-day notice rule."
        ),
    ])


def sewer_hub():
    return "\n".join([
        h2("Sewage cleanup and sewer backup in Oakland County"),
        p(
            "Sewage cleanup in Oakland County, on this site, means wastewater that came up a floor drain, "
            "a basement toilet, or a laundry standpipe. A backup drain in Oakland County is the same "
            "problem worded differently: the line was full and the lowest opening in the house let it "
            "out. Sewer backup cleanup is that job. The five city pages own the city phrases. This hub "
            "only routes you. An independent provider you hire does the work."
        ),
        h3("Sewage cleanup, by city"),
        p("Royal Oak: older houses near Woodward, downtown, Vinsetta, and Northwood, with a city Sewer Division for the public main. " + a("/royal-oak-sewer-cleanup", "Sewage cleanup in Royal Oak, MI") + "."),
        p("Troy: split-levels and subdivision basements near Big Beaver, with storm drainage under the city's Streets and Drains Division. " + a("/troy-sewer-cleanup", "Sewage cleanup in Troy, MI") + "."),
        p("Birmingham: older houses, plaster, and mature trees around Poppleton, Quarton, and downtown. " + a("/birmingham-sewer-cleanup", "Sewage cleanup in Birmingham, MI") + "."),
        p("Berkley: 1940s–1950s bungalows on a flat grid along 12 Mile, where some older sections are described as combined sewers. Confirm that with the city. " + a("/berkley-sewer-cleanup", "Sewage cleanup in Berkley, MI") + "."),
        p("Clawson: brick bungalows on compact lots around 14 Mile. " + a("/clawson-sewer-cleanup", "Sewage cleanup in Clawson, MI") + "."),
        p(
            "If the basement is wet but the drains never moved, start at "
            + a("/flooded-basement-cleanup", "flooded basement cleanup")
            + " or " + a("/water-damage-restoration", "water damage restoration")
            + " instead. Extraction detail is on " + a("/sewage-extraction", "the sewage extraction hub") + "."
        ),
        h3("If you think the public sewer caused it"),
        p(
            "Michigan law requires written notice to the responsible agency within 45 days of discovering the damage before "
            "compensation for a sewer backup is possible. The steps and each city's claim contact are in the "
            + a("/sewer-backup-claim-guide", "sewer backup claim guide")
            + ". Why combined sewers in this part of the county back up in heavy rain is explained on the "
            + a("/george-w-kuhn-drainage-district", "George W. Kuhn Drainage District page") + "."
        ),
    ])


def sewage_hub():
    return "\n".join([
        h2("What sewage extraction is"),
        p(
            "Sewage extraction removes contaminated water that left the sanitary plumbing, plus the "
            "materials that soaked it up. It is not the sewage cleanup overview, and it is not mopping "
            "rain that came through a window. A household vac spreads it. An independent company with "
            "the right setup does the removal. Oakland Sewer Pros does not own that equipment."
        ),
        h3("City pages"),
        p(a("/royal-oak-sewage-extraction", "Sewage extraction in Royal Oak") + " focuses on floor drains in older houses off Woodward and downtown."),
        p(a("/troy-sewage-extraction", "Sewage extraction in Troy") + " focuses on split-level lower floors and finished subdivision basements."),
        p(a("/birmingham-sewage-extraction", "Sewage extraction in Birmingham") + " focuses on plaster, trim, and older laterals."),
        p(a("/berkley-sewage-extraction", "Sewage extraction in Berkley, MI") + " focuses on small bungalow stairs and tight basements."),
        p(a("/clawson-sewage-extraction", "Sewage extraction in Clawson") + " focuses on compact lots and one-room basements."),
        p("After extraction, sanitizing is " + a("/basement-sanitization", "its own hub") + ". The backup overview is " + a("/sewer-backup-cleanup", "sewer backup cleanup") + "."),
    ])


def flood_hub():
    return "\n".join([
        h2("Basement flood cleanup in Oakland County"),
        p(
            "Basement flood cleanup in Oakland County means getting standing water off the floor and out "
            "of the materials it entered. Flooded basement cleanup is that work plus the mess it left. "
            "If a sewer drain was the source, do not treat it as a rain flood. Use "
            + a("/sewage-extraction", "sewage extraction")
            + " or the city's "
            + a("/sewer-backup-cleanup", "sewage cleanup page")
            + ". If finishes are wet after the pump-out, the longer process is "
            + a("/water-damage-restoration", "water damage restoration") + "."
        ),
        h3("The five city versions"),
        p(a("/royal-oak-flooded-basement", "Flooded basement cleanup in Royal Oak") + ": window wells and older basements, versus a true drain backup."),
        p(a("/troy-flooded-basement", "Flooded basement cleanup in Troy") + ": finished lower levels and split-levels, where carpet holds the water."),
        p(a("/birmingham-flooded-basement", "Flooded basement cleanup in Birmingham") + ": plaster and low ground near Quarton, with downtown and Poppleton as the other housing stock."),
        p(a("/berkley-flooded-basement", "Flooded basement cleanup in Berkley") + ": short stairs and first-floor hardwood over a flat lot."),
        p(a("/clawson-flooded-basement", "Flooded basement cleanup in Clawson, MI") + ": one-room basements, furnaces in the water, short driveways."),
        p("A failed pump may be why the water is there. That repair is " + a("/sump-pump-repair", "sump pump repair") + ", not a substitute for removing the water."),
        p("Before the next storm, print the " + a("/basement-flood-checklist", "basement flood checklist for Oakland County") + ". It lists city sewer numbers, DTE outage reporting, and the 45-day claim notice step."),
    ])


def sump_hub():
    return "\n".join([
        h2("Sump pump repair in Oakland County, Michigan"),
        p(
            "These pages are for Oakland County, Michigan. Birmingham on this site is Birmingham, "
            "Michigan, next to Royal Oak and Troy, not Birmingham, Alabama. A sump pump lifts groundwater "
            "out of a pit. When the float sticks, the check valve fails, the discharge line freezes, or "
            "the power drops, the pit overflows. Repairing that pump is often a plumbing visit. Drying "
            "the carpet it ruined is water damage. This site used to show dollar ranges. Those ranges "
            "are gone, because we do not control what an independent company charges."
        ),
        h3("Where the pits are"),
        p(a("/royal-oak-sump-pump-repair", "Royal Oak") + ": older crocks in pre-1960s basements."),
        p(a("/troy-sump-pump-repair", "Troy") + ": pits next to finished living space."),
        p(a("/birmingham-sump-pump-repair", "Sump pump repair in Birmingham, Michigan") + ": older houses where the discharge line and the trim both matter."),
        p(a("/berkley-sump-pump-repair", "Berkley") + ": short basements and steep stairs."),
        p(a("/clawson-sump-pump-repair", "Clawson") + ": the pit in the same small room as the furnace."),
        p("If the floor is wet, start the water conversation at " + a("/flooded-basement-cleanup", "flooded basement cleanup") + " as well."),
    ])


def sanit_hub():
    return "\n".join([
        h2("Basement sanitization after sewage or a contaminated flood"),
        p(
            "Sanitizing, on this site, means cleaning what remains after sewage or foul floodwater has "
            "been removed and the ruined porous materials have been taken out. It is not a recurring "
            "maid service, and a fogger is not a substitute for throwing away a soaked pad. The company "
            "that extracted the water should say what chemical they will use and why the label fits."
        ),
        p(a("/royal-oak-basement-sanitization", "Basement sanitization in Royal Oak") + " is about residue in older basements after a floor-drain backup."),
        p(a("/troy-basement-sanitization", "Basement sanitization in Troy") + " is about finished rooms, carpet, and contents."),
        p(a("/birmingham-basement-sanitization", "Basement sanitization in Birmingham") + " is about plaster and wood that may not survive a wipe-down."),
        p(a("/berkley-basement-sanitization", "Basement sanitization in Berkley, MI") + " is about a small stair that opens into the living room."),
        p(a("/clawson-basement-sanitization", "Basement sanitization in Clawson") + " is about one room full of mechanical equipment."),
        p("Extraction comes first. See " + a("/sewage-extraction", "sewage extraction") + "."),
    ])


def city_royal_oak():
    return "\n".join([
        h2("Royal Oak houses this line covers"),
        p(
            "Royal Oak, for these pages, means the older residential blocks: downtown side streets off "
            "Main and Washington, the Woodward Avenue corridor, Vinsetta, Northwood, and the neighborhoods "
            "toward the Detroit Zoo on West Ten Mile. Many of those houses predate the 1960s and were "
            "built with clay or cast-iron laterals. The city Sewer Division, on the city's own website, "
            "is the contact for the public main. This overview is not that department."
        ),
        h2("Which Royal Oak page to open"),
        p(a("/royal-oak-sewer-cleanup", "Sewer backup cleanup") + " if sewage came through a drain. That page is the long-standing URL for the phrase."),
        p(a("/royal-oak-sewage-extraction", "Sewage extraction in Royal Oak") + " for the removal step itself."),
        p(a("/royal-oak-flooded-basement", "Flooded basement cleanup in Royal Oak") + " when the water is storm, a window well, or a sump, not a drain."),
        p(a("/royal-oak-water-damage-restoration", "Water damage restoration") + " for drying and the broader wet-building scope, including water damage repair decisions."),
        p(a("/royal-oak-sump-pump-repair", "Sump pump repair") + " for the pit, with no prices listed."),
        p(a("/royal-oak-basement-sanitization", "Basement sanitization") + " after sewage or a contaminated flood, not as routine cleaning."),
        p("Royal Oak is part of the regional " + a("/george-w-kuhn-drainage-district", "George W. Kuhn Drainage District") + ". If a backup damages your basement, the city's contacts and the 45-day notice rule are in the " + a("/sewer-backup-claim-guide", "sewer backup claim guide") + "."),
        p("Nearby city overviews: " + a("/berkley", "Berkley") + ", " + a("/clawson", "Clawson") + ", " + a("/birmingham", "Birmingham") + ", and " + a("/troy", "Troy") + "."),
    ])


def city_troy():
    return "\n".join([
        h2("Troy, beyond the Big Beaver commercial strip"),
        p(
            "Troy's landmarks that people name first are Big Beaver Road, Somerset Collection at Coolidge, "
            "and I-75. The wet basements are in the houses: 1960s and 1970s split-levels near Big Beaver, "
            "and subdivisions such as Northfield Hills. Troy Historic Village sits in the city as a "
            "landmark, not as a service yard. Storm drainage is a Streets and Drains Division topic. A "
            "sanitary backup in a lower level is not the same call."
        ),
        h2("Troy service pages"),
        p(a("/troy-sewer-cleanup", "Sewage cleanup in Troy, MI") + " keeps the original URL and the sewer backup heading."),
        p(a("/troy-sewage-extraction", "Sewage extraction in Troy") + " for contaminated water in a split-level or finished basement."),
        p(a("/troy-flooded-basement", "Flooded basement cleanup in Troy") + " for carpeted lower levels and basement water removal."),
        p(a("/troy-water-damage-restoration", "Water damage restoration") + " for drying after the water is out."),
        p(a("/troy-sump-pump-repair", "Sump pump repair") + " when the pit in a finished room quits."),
        p(a("/troy-basement-sanitization", "Basement sanitization in Troy") + " after sewage has touched contents and pad."),
        p("Troy takes written sewer backup claims through the City Attorney's Office. The details, and the 45-day deadline, are in the " + a("/sewer-backup-claim-guide", "sewer backup claim guide") + "."),
        p("Other cities: " + a("/birmingham", "Birmingham") + ", " + a("/clawson", "Clawson") + ", " + a("/royal-oak", "Royal Oak") + "."),
    ])


def city_birmingham():
    return "\n".join([
        h2("Birmingham's older housing, not a generic suburb page"),
        p(
            "Birmingham pages on this site talk about early- and mid-20th-century houses, plaster, "
            "and tree-lined laterals. The landmarks used so you know which Birmingham this is: Shain Park "
            "and Old Woodward downtown, Maple Road, Poppleton Park, and Quarton Lake. Low ground near "
            "Quarton behaves differently from a house up by downtown. None of that is a claim that we "
            "have an office in the city. We do not."
        ),
        h2("Open the matching Birmingham service"),
        p(a("/birmingham-sewer-cleanup", "Sewer backup cleanup") + " for a drain backup in an older house."),
        p(a("/birmingham-sewage-extraction", "Sewage extraction in Birmingham") + " when contaminated water is already inside."),
        p(a("/birmingham-flooded-basement", "Flooded basement cleanup") + " for storm water and basement water removal around those neighborhoods."),
        p(a("/birmingham-water-damage-restoration", "Water damage restoration") + " when plaster, trim, or finishes have to be dried or opened."),
        p(a("/birmingham-sump-pump-repair", "Sump pump repair in Birmingham, Michigan") + " for the pit, quoted by the provider, not by us."),
        p(a("/birmingham-basement-sanitization", "Basement sanitization in Birmingham") + " after sewage, with a warning about plaster and fog-only treatments."),
        p("Birmingham's water event tracking form is not a sewer backup claim. The claim form, the 45-day rule, and what to document are in the " + a("/sewer-backup-claim-guide", "sewer backup claim guide") + "."),
        p("Adjacent overviews: " + a("/royal-oak", "Royal Oak") + " and " + a("/troy", "Troy") + "."),
    ])


def city_berkley():
    return "\n".join([
        h2("Berkley's bungalow blocks"),
        p(
            "Berkley is a small city of mostly 1940s and 1950s bungalows. Downtown is along 12 Mile Road. "
            "Coolidge is a main north-south road. The lots are flat, "
            "so heavy rain does not run off quickly. The city's master plan describes its sewers as a "
            "combined storm and sanitary system that drains to the regional George W. Kuhn Drain (see the "
            + a("/george-w-kuhn-drainage-district", "George W. Kuhn Drainage District explainer")
            + "). Ask the city about a specific "
            "street. Basements are short, and the stair lands close to the first-floor living space."
        ),
        h2("Berkley pages"),
        p(a("/berkley-sewer-cleanup", "Sewage cleanup in Berkley, MI") + " for sewage at a bungalow floor drain."),
        p(a("/berkley-sewage-extraction", "Sewage extraction in Berkley, MI") + " with the stair and a household vac called out as the wrong tool."),
        p(a("/berkley-flooded-basement", "Flooded basement cleanup") + " for window wells, stairwells, and basement water removal."),
        p(a("/berkley-water-damage-restoration", "Water damage restoration") + " including the risk to first-floor hardwood from wet joists."),
        p(a("/berkley-sump-pump-repair", "Sump pump repair") + " in a low basement, with no price table."),
        p(a("/berkley-basement-sanitization", "Basement sanitization in Berkley, MI") + " after sewage, sized to a small air volume."),
        p("Filing a claim with the city after a backup: " + a("/sewer-backup-claim-guide", "sewer backup claim guide") + ". Getting ready for the next storm: " + a("/basement-flood-checklist", "basement flood checklist") + "."),
        p("Neighbors on this site: " + a("/royal-oak", "Royal Oak") + " and " + a("/birmingham", "Birmingham") + "."),
    ])


def city_clawson():
    return "\n".join([
        h2("Clawson bungalows and short driveways"),
        p(
            "Clawson is largely mid-century brick bungalows and ranches, mostly built from the 1940s to the 1960s, on compact lots. "
            "14 Mile Road is the downtown street. The city sits between Royal Oak and Troy. Basements "
            "are often a single room that holds the furnace, the water heater, and the floor drain. "
            "Laterals from that era are commonly clay or cast iron. Regional drainage context includes "
            "the " + a("/george-w-kuhn-drainage-district", "George W. Kuhn Drainage District") + " and the Oakland County Water Resources Commissioner. Confirm "
            "anything you need for a city complaint with those agencies. This overview is a referral map."
        ),
        h2("Clawson services"),
        p(a("/clawson-sewer-cleanup", "Sewage cleanup in Clawson, MI") + " for a bungalow backup."),
        p(a("/clawson-sewage-extraction", "Sewage extraction in Clawson") + " when access is limited by the lot."),
        p(a("/clawson-flooded-basement", "Flooded basement cleanup in Clawson, MI") + " for water removal when the mechanical room is wet."),
        p(a("/clawson-water-damage-restoration", "Water damage restoration") + " for drying after extraction."),
        p(a("/clawson-sump-pump-repair", "Sump pump repair") + " next to the furnace, without a published price."),
        p(a("/clawson-basement-sanitization", "Basement sanitization in Clawson") + " so residue does not walk up the only stair."),
        p("After a backup, the 45-day written notice rule and Clawson's contacts are in the " + a("/sewer-backup-claim-guide", "sewer backup claim guide") + "."),
        p("See also " + a("/royal-oak", "Royal Oak") + " and " + a("/troy", "Troy") + "."),
    ])


CITY_ARTICLES = {
    "royal-oak": city_royal_oak,
    "troy": city_troy,
    "birmingham": city_birmingham,
    "berkley": city_berkley,
    "clawson": city_clawson,
}

CITY_HERO = {
    "royal-oak": "Royal Oak services on this site are a referral menu for sewer backups, sewage extraction, flooded basements, water damage restoration, sump pumps, and post-sewage sanitizing. We do not operate a Royal Oak office.",
    "troy": "Troy services here cover sewer backups and water damage in split-levels and subdivision basements, not a storefront at Somerset. Calling connects you with an independent provider when one is available.",
    "birmingham": "Birmingham services on Oakland Sewer Pros are for older houses and wet lower levels. We are a referral line. We are not a Birmingham contractor and we do not have a local office.",
    "berkley": "Berkley services match bungalow basements: backups, extraction, water removal, drying, pumps, and sanitizing after sewage. The work is done by independent providers, not by this website.",
    "clawson": "Clawson services account for small lots and one-room basements. Use the links below, then call to reach an independent provider. Oakland Sewer Pros does not send a city crew.",
}

CITY_DESC = {
    "royal-oak": "Royal Oak, MI sewer backup, water damage, and flooded basement help. A referral line. Call {PHONE_DISPLAY}.",
    "troy": "Troy, MI sewer backup, sump pump, and water damage referrals. Independent providers. Call {PHONE_DISPLAY}.",
    "birmingham": "Birmingham, MI sewer and water damage referrals for older homes. Independent providers. Call {PHONE_DISPLAY}.",
    "berkley": "Berkley, MI sewer backup and flooded basement referrals for bungalows. Call {PHONE_DISPLAY}.",
    "clawson": "Clawson, MI sewer, water damage, and sump referrals for bungalows. Call {PHONE_DISPLAY} today.",
}
