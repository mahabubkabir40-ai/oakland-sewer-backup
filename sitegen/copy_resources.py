"""Homeowner resource pages: claim guide, GWK drainage district explainer, flood checklist.

Every factual statement here was checked against the linked official source on 28 Sep 2026.
Re-check the city contacts every quarter; city websites change.
"""

from site_config import BRAND, PHONE_DISPLAY

from sitegen.render import a, callout, esc, h2, h3, note, ol, p, phone_link, ul

VERIFIED = "September 28, 2026"

# Official sources (final URLs after redirects, checked 28 Sep 2026)
SRC = {
    "mcl1416": "https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-691-1416",
    "mcl1417": "https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-691-1417",
    "mcl1418": "https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-691-1418",
    "mcl1419": "https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-691-1419",
    "wrc_claim": "https://www.oaklandcountymi.gov/government/water-resources-commissioner/services/basement-flooding-claim",
    "wrc_form": "https://forms.oakgov.com/259",
    "wrc_sewer": "https://www.oaklandcountymi.gov/government/water-resources-commissioner/wastewater/sewer",
    "wrc_brochure": "https://cdn.oaklandcountymi.gov/oakland-sitefinity-prod/docs/default-source/water-resources-commissioner/water-resources-commissioner/resources/customer-materials/wrc-sewer-backup-infographic-3-page.pdf",
    "wrc_gwk": "https://www.oaklandcountymi.gov/government/water-resources-commissioner/wastewater/facilities/george-w-khun-rtb",
    "wrc_rtbs": "https://www.oaklandcountymi.gov/government/water-resources-commissioner/wastewater/facilities/retention-treatment-basins",
    "wrc_rainsmart": "https://www.oaklandcountymi.gov/government/water-resources-commissioner/rainsmart-rebates",
    "county_press": "https://www.oaklandcountymi.gov/government/county-executive/state-of-the-county/press/2026/01/27/rainsmart-rebates-pilot-helps-manage-1-4-million-gallons-of-stormwater-annually",
    "gwk_fact_sheet": "https://cms7files1.revize.com/birmingham/Document_Center/Department/City%20manager/City%20Manager%20Report/Dec%202022/GWK%20Information%202022-12-13.pdf",
    "ro_flood": "https://www.romi.gov/386/Responding-to-Street-Basement-Flooding",
    "ro_faq": "https://www.romi.gov/Faq.aspx?QID=134",
    "ro_clerk": "https://www.romi.gov/FormCenter/City-Clerks-Office-5",
    "ro_cleanup": "https://www.romi.gov/390/Cleaning-Up-the-Mess-After-Basement-Floo",
    "troy_claims": "https://troymi.gov/departments/public_works/water_and_sewer/legal_claims.php",
    "bham_risk": "https://www.bhamgov.org/about_birmingham/city_departments/city_manager/risk_management.php",
    "berk_claim": "https://berkleymi.gov/government/city-manager/report-a-claim",
    "berk_tips": "https://www.berkleymi.gov/public-works/flood-tips-for-residents",
    "berk_valve": "https://www.berkleymi.gov/Community%20Development/Backwater%20Reimbursement%20Request.pdf",
    "claw_dpw": "https://www.cityofclawson.com/your_government/dpw_and_engineering/index.php",
    "claw_dispatch": "https://www.cityofclawson.com/your_government/police_department/dispatch_services.php",
    "claw_sewer": "https://www.cityofclawson.com/your_government/dpw_and_engineering/sewer.php",
    "dte_report": "https://outage.dteenergy.com/Report-Outage",
    "dte_faq": "https://www.dteenergy.com/us/en/residential/emergency-and-safety/safety/outage-faqs.html",
    "cdc_flood": "https://www.cdc.gov/floods/safety/index.html",
    "cpsc_gen": "https://www.cpsc.gov/Safety-Education/Safety-Guides/Carbon-Monoxide-Home/Generators-and-Engine-Driven-Tools",
}


def ext(key_or_url, text):
    """External citation link. Same look as internal links, opens in the same tab."""
    href = SRC.get(key_or_url, key_or_url)
    return (
        f'<a href="{esc(href)}" rel="noopener" class="text-red-400 hover:text-red-300 underline font-medium">'
        f"{text}</a>"
    )


def table(headers, rows):
    head = "".join(f'<th scope="col">{h}</th>' for h in headers)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="rs-table-wrap"><table class="rs-table"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'


def sources_block(items):
    lis = "".join(f"<li>{ext(key, label)}</li>" for key, label in items)
    return (
        h2("Sources")
        + p(f"Each source below was opened and read on {VERIFIED}. If a link has moved, search the agency's own website for the page title.")
        + f'<ul class="list-disc list-inside text-sm text-gray-300 space-y-1.5 pl-2 rs-sources">{lis}</ul>'
    )


NOT_LEGAL_ADVICE = (
    "This page is general information, not legal advice. Oakland Sewer Pros is a referral service for "
    "cleanup providers. We are not a law firm, we do not file claims for anyone, and we cannot tell you whether "
    "a claim will succeed. Read the statute yourself and, if the amount at stake matters to you, talk to a Michigan "
    "attorney. Deadlines and city procedures can change; confirm them with the agency."
)

RESOURCE_CSS = """
        .rs-table-wrap { overflow-x: auto; }
        .rs-table { width: 100%; border-collapse: collapse; font-size: 0.875rem; color: #d1d5db; }
        .rs-table th, .rs-table td { border: 1px solid #1e293b; padding: 0.5rem 0.75rem; text-align: left; vertical-align: top; }
        .rs-table th { color: #fff; background: rgba(2, 6, 23, 0.6); }
"""


# ---------------------------------------------------------------------------
# 1. Sewer backup claim guide
# ---------------------------------------------------------------------------

CLAIM_TITLE = "Sewer Backup Claim Guide: Michigan's 45-Day Notice Rule"
CLAIM_H1 = "Sewer backup claims in Royal Oak, Troy, Birmingham, Berkley and Clawson: the 45-day notice"
CLAIM_DESC = (
    "Michigan's 45-day written notice rule for sewer backup claims, explained for Royal Oak, Troy, "
    "Birmingham, Berkley and Clawson, with each city's contact."
)
CLAIM_LEAD = (
    "<p>If sewage came up into your basement and you believe a public sewer caused it, Michigan law gives you "
    "45 days from the day you discovered the damage to send written notice to the government agency responsible. "
    "Miss that window and the claim can be barred. This guide walks through the law (MCL 691.1416 to 691.1419), "
    "what to document, the timeline, and the official claim contact for each of the five cities this site covers.</p>"
)


def claim_article():
    return "\n".join([
        '<div class="bg-red-950/40 border border-red-500/30 p-5 rounded-xl space-y-3">'
        '<p class="text-base font-outfit font-extrabold text-red-300">Not legal advice</p>'
        + p(esc(NOT_LEGAL_ADVICE)) + "</div>",
        h2("The short version"),
        ol([
            "Report the backup to your city while it is happening, by phone. Royal Oak says it is important that the city "
            "is notified and able to investigate while the event is taking place (" + ext("ro_flood", "City of Royal Oak") + ").",
            "Photograph and film everything before cleanup starts. The Oakland County Water Resources Commissioner (WRC) "
            "tells claimants to take photographs of any damage (" + ext("wrc_brochure", "WRC sewer backup infographic") + ").",
            "Within 45 days of discovering the damage, send a written notice to the responsible agency with six pieces of "
            "information: your name, address and phone number, the address of the affected property, the date you discovered "
            "the damage, and a brief description of the claim (" + ext("mcl1419", "MCL 691.1419(1) and (2)(c)") + ").",
            "Keep a copy of the notice and write down how and when you sent it.",
            "Expect that the agency may ask to inspect the damage. The law says a claimant shall not unreasonably refuse (" + ext("mcl1419", "MCL 691.1419(5)") + ").",
            "If you and the agency have not agreed on compensation within 45 days after it received your notice, a lawsuit "
            "may be filed, but not before those 45 days pass (" + ext("mcl1419", "MCL 691.1419(6)") + ").",
        ]),
        h2("What Michigan law says: MCL 691.1416 to 691.1419"),
        p(
            "Sections 16 to 19 of Michigan's Governmental Immunity Act (Act 170 of 1964) were added by 2001 Public Act 222 and "
            "took effect January 2, 2002 (" + ext("mcl1417", "MCL 691.1417, history note") + "). Government agencies are generally "
            "immune from lawsuits over sewer overflows and backups. These sections create a narrow exception and say they are the "
            "sole remedy for damage caused by a \"sewage disposal system event\" (" + ext("mcl1417", "MCL 691.1417(2)") + ")."
        ),
        h3("What counts as an \"event\""),
        p(
            "An event is the overflow or backup of a sewage disposal system onto real property. It is not an event if the "
            "substantial proximate cause was an obstruction in your service lead that the government did not cause, or a "
            "connection on your own property such as a sump system, building drain, surface drain, gutter or downspout. "
            "\"Substantial proximate cause\" means 50% or more of the cause (" + ext("mcl1416", "MCL 691.1416(k) and (l)") + "). "
            "The service lead is the pipe that connects the house to the public sewer and that the government does not own or maintain "
            "(" + ext("mcl1416", "MCL 691.1416(i)") + ")."
        ),
        h3("What a claimant has to show"),
        p("To get compensation from an agency, the claimant has to show that all of the following existed at the time of the event (" + ext("mcl1417", "MCL 691.1417(3)") + "):"),
        ul([
            "The agency was an \"appropriate governmental agency\": it owned or operated, or directly or indirectly discharged into, the part of the system that allegedly caused the damage (" + ext("mcl1416", "MCL 691.1416(b)") + ").",
            "The sewage disposal system had a defect (construction, design, maintenance, operation or repair).",
            "The agency knew, or with reasonable diligence should have known, about the defect.",
            "The agency had the legal authority to fix it and failed to take reasonable steps in a reasonable amount of time.",
            "The defect was a substantial proximate cause of the event and of the damage.",
        ]),
        p(
            "The claimant also has to show reasonable proof of ownership and value for damaged personal property (records, "
            "testimony or photos can count) and that the 45-day notice rule was followed (" + ext("mcl1417", "MCL 691.1417(4)") + "). "
            "Compensation is limited to economic damages, except where the backup caused death, serious impairment of body function "
            "or permanent serious disfigurement (" + ext("mcl1418", "MCL 691.1418") + ")."
        ),
        p(
            "The WRC puts it plainly: filing a claim or a lawsuit does not guarantee you will be compensated, so it is important to "
            "protect your property in other ways too (" + ext("wrc_brochure", "WRC sewer backup infographic") + ")."
        ),
        h2("The 45-day written notice, step by step"),
        h3("The deadline"),
        p(
            "Written notice must reach the agency within 45 days after the date the damage was discovered, or should have been "
            "discovered with reasonable diligence (" + ext("mcl1419", "MCL 691.1419(1)") + "). Count from discovery, not from "
            "the day you finish cleaning. Put the 45th day on a calendar the day it happens."
        ),
        h3("What the notice must contain"),
        p("The statute limits the required content to these items (" + ext("mcl1419", "MCL 691.1419(2)(c)") + "):"),
        ul([
            "Your name, address and telephone number",
            "The address of the affected property",
            "The date you discovered the property damage or injury",
            "A brief description of the claim",
        ]),
        p(
            "Troy, Berkley and Birmingham each publish a claim form that asks for this information, and the WRC has an online form "
            "for the systems it runs (" + ext("wrc_form", "WRC Basement Flooding Claim (PA 222) form") + ")."
        ),
        h3("Who the notice goes to"),
        p(
            "The notice must be sent to the individual the agency designates (" + ext("mcl1419", "MCL 691.1419(1)") + "). If you "
            "call or write the city about the backup before you send a formal notice, the city has to give you, in writing, an "
            "explanation of the notice rules, the name and address of the person who receives notices, and the required content "
            "(" + ext("mcl1419", "MCL 691.1419(2)") + "). If you contacted the city within the 45 days and missed the formal notice "
            "because the city did not give you that information, the law says the missed notice does not bar your lawsuit "
            "(" + ext("mcl1419", "MCL 691.1419(3)") + "). Asking in writing, early, protects you."
        ),
        h3("If you picked the wrong agency"),
        p(
            "An agency that receives a notice and believes a different or additional agency may be responsible must tell that "
            "other agency in writing within 15 business days (" + ext("mcl1419", "MCL 691.1419(4)") + "). That rule helps, but it "
            "is not a reason to skip the question of which agency owns your sewer."
        ),
        h3("Timeline at a glance"),
        table(
            ["When", "What happens", "Source"],
            [
                ["During the backup", "Call the city's sewer or public works line (after hours: the number the city lists).", ext("ro_flood", "City pages")],
                ["Day 0", "The day you discover the damage. The 45-day clock starts here, or on the day you should have discovered it.", ext("mcl1419", "691.1419(1)")],
                ["By day 45", "Written notice with the required content reaches the designated person at the agency.", ext("mcl1419", "691.1419(1), (2)(c)")],
                ["Within 15 business days of the notice", "If the agency thinks another agency is responsible, it must tell that agency in writing.", ext("mcl1419", "691.1419(4)")],
                ["After notice", "The agency may inspect the damaged property.", ext("mcl1419", "691.1419(5)")],
                ["45 days after the agency receives notice", "If there is no agreement on compensation, a civil action may be filed. Not earlier.", ext("mcl1419", "691.1419(6)")],
            ],
        ),
        h2("City or county: which agency?"),
        p(
            "Start with your sewer bill. The WRC's first step for any basement flooding claim is to determine which agency maintains "
            "your sewer lines by looking at the bill (" + ext("wrc_claim", "WRC Basement Flooding Claim page") + "). The WRC lists the "
            "communities where Oakland County operates or maintains the local sewage system. Royal Oak, Troy, Birmingham, Berkley and "
            "Clawson are not on that list, and the WRC says residents elsewhere should contact their own service provider "
            "(" + ext("wrc_claim", "same page") + "). Each of the five cities describes its own sewer responsibilities and claim steps, below."
        ),
        p(
            "There is a regional layer too. The local sewers in all five cities drain, in whole or in part, to the George W. Kuhn "
            "Drainage District system run by the WRC. Birmingham, for example, says the WRC is responsible for the regional sewer drains "
            "that the city's system discharges into (" + ext("bham_risk", "City of Birmingham Risk Management") + "). Because the law "
            "defines the responsible agency to include one that \"directly or indirectly discharged into\" the part of the system that "
            "caused the damage (" + ext("mcl1416", "MCL 691.1416(b)") + "), whether more than one agency should get a notice is a "
            "question for an attorney, not for a referral line. Background on the regional system is in our "
            + a("/george-w-kuhn-drainage-district", "George W. Kuhn Drainage District explainer") + "."
        ),
        h2("City-by-city contacts"),
        p(f"Checked on the cities' own websites on {VERIFIED}. Phone numbers and hours are quoted as the city lists them."),
        h3("Royal Oak"),
        ul([
            "Basement water: Department of Public Service, (248) 246-3300, Monday to Friday, 7:30 a.m. to 4:00 p.m. After hours: Police non-emergency, (248) 246-3500, which dispatches a sewer representative (" + ext("ro_flood", "Responding to Street &amp; Basement Flooding") + ").",
            "Responsibility: the city maintains the main sewer; the owner is responsible for the sewer service lead from the house to the main, including the connection (" + ext("ro_faq", "Royal Oak Sewer Division FAQ") + ").",
            "Written notice: we did not find a dedicated sewer backup claim form on romi.gov. The City Clerk's Office is at 203 S. Troy Street, Royal Oak, MI 48067, (248) 246-3000 (" + ext("ro_clerk", "City Clerk contact page") + "). Under the statute a city clerk is one of the offices that can receive notice of an event (" + ext("mcl1416", "MCL 691.1416(d)") + "). Ask the city, in writing, who the designated person for sewer backup claims is.",
            "Cleanup guidance the city publishes: " + ext("ro_cleanup", "Cleaning Up the Mess After Basement Flooding") + ".",
        ]),
        h3("Troy"),
        ul([
            "Report an overflow or backup immediately: Water Division, 248.524.3370, during business hours. After hours: Troy Police, 248.524.3477 (" + ext("troy_claims", "Legal Claims for Overflows and Backups") + ").",
            "Written claim within 45 days to the City of Troy City Attorney's Office, 500 W. Big Beaver, Troy, MI 48084, by email, mail, fax (248-524-3259) or drop-off. The page links a Notice of Sewer Backup Claim form (" + ext("troy_claims", "same page") + ").",
        ]),
        h3("Birmingham"),
        ul([
            "Sewer backup claims: download the city's Sewer Backup Claim form from the Risk Management page. Questions: 248.530.1808 (" + ext("bham_risk", "Birmingham Risk Management") + ").",
            "The city's water event tracking form and water event notification line, (248) 530-1703, collect flooding data. The city says the tracking form is not a sewer backup claim (" + ext("bham_risk", "same page") + ").",
            "Claims against the city are sent to Meadowbrook Claims Service, the administrator for the Michigan Municipal League Liability &amp; Property Pool, for a liability decision (" + ext("bham_risk", "same page") + ").",
        ]),
        h3("Berkley"),
        ul([
            "Report basement flooding to Public Works, 248-658-3490 (" + ext("berk_tips", "Flood Tips for Residents") + ").",
            "The city's Notice of Claim form for sewage disposal or stormwater events is returned to City of Berkley, Attn: City Manager's Office, 3338 Coolidge Highway, Berkley, MI 48072. Questions: 248-658-3350 (" + ext("berk_claim", "Report a Claim") + ").",
            "Like Birmingham, Berkley sends claims to Meadowbrook Claims Service for the Michigan Municipal League Liability &amp; Property Pool (" + ext("berk_claim", "same page") + ").",
        ]),
        h3("Clawson"),
        ul([
            "Department of Public Works, 635 W. Elmwood, Clawson, MI 48017, (248) 288-3222, Monday to Thursday, 7:00 a.m. to 3:30 p.m. (" + ext("claw_dpw", "Clawson DPW &amp; Engineering") + ").",
            "After hours: (248) 524-3477. The DPW page lists it for after-hours DPW emergencies (" + ext("claw_dpw", "Clawson DPW") + "). It is the same number as Troy Police because Clawson contracts with the Troy Police Department for 24-hour dispatch; Clawson's police page lists it, extension 1, as the non-emergency line (" + ext("claw_dispatch", "Clawson Police: Dispatch Services") + "). Call 911 for emergencies.",
            "The city's Sanitary &amp; Storm Sewer page links to George W. Kuhn and WRC information and to a \"Public Act 222\" document. When we checked on " + VERIFIED + ", that document link returned an error (" + ext("claw_sewer", "Clawson Sanitary &amp; Storm Sewer System") + ").",
            "Written notice: we did not find a posted claim form. Call the DPW, then ask in writing for the name and address of the person who receives sewer backup notices. The city must provide it in writing if you contacted it first (" + ext("mcl1419", "MCL 691.1419(2)") + ").",
        ]),
        h2("What to document"),
        p("Start before anything is thrown out. The statute requires reasonable proof of ownership and value for personal property (" + ext("mcl1417", "MCL 691.1417(4)(a)") + "), and the WRC claim form asks for supporting items (" + ext("wrc_form", "WRC claim form checklist") + ")."),
        ul([
            "The date and time you discovered the water, and whether it was still rising.",
            "Photos and video of the water line on walls, the floor drain or fixture it came from, and every damaged item, before cleanup.",
            "A written list of damaged items with approximate age, purchase price and any receipts, manuals or bank records you can find.",
            "Invoices for extraction, cleanup and repairs, and receipts for anything you bought to deal with the water.",
            "The declaration page of your homeowner's policy showing your deductible, and any payment or denial letter from your insurer. The WRC form asks for both.",
            "A log of calls to the city: date, time, the number you called and who you spoke with.",
            "If a plumber cleans or inspects your lateral, ask for the camera video. Birmingham recommends a video record of pipe conditions (" + ext("bham_risk", "Birmingham FAQ") + ").",
        ]),
        h2("Insurance is a separate track"),
        p(
            "A notice to the city is not an insurance claim. Many homeowner policies cover sewer backup only with an added endorsement; "
            "the WRC suggests adding one (" + ext("wrc_brochure", "WRC sewer backup infographic") + "). Call your insurer or agent at the same "
            "time you notify the city. Your insurance claim stays with you and your carrier."
        ),
        h2("Where this site fits"),
        p(
            f"{esc(BRAND)} connects Oakland County homeowners with independent cleanup providers. If sewage is in the basement now, "
            f"call {phone_link()} to be connected when a participating provider is available. The provider sets the scope and price. "
            "For the steps before, during and after a storm, use the printable "
            + a("/basement-flood-checklist", "basement flood checklist") + ". City cleanup pages: "
            + a("/royal-oak-sewer-cleanup", "Royal Oak") + ", " + a("/troy-sewer-cleanup", "Troy") + ", "
            + a("/birmingham-sewer-cleanup", "Birmingham") + ", " + a("/berkley-sewer-cleanup", "Berkley") + " and "
            + a("/clawson-sewer-cleanup", "Clawson") + "."
        ),
        note(f"Last verified {VERIFIED}. If a city contact listed here is out of date, the city's own website is the authority."),
        sources_block([
            ("mcl1416", "Michigan Legislature: MCL 691.1416, definitions"),
            ("mcl1417", "Michigan Legislature: MCL 691.1417, what a claimant must show"),
            ("mcl1418", "Michigan Legislature: MCL 691.1418, damages"),
            ("mcl1419", "Michigan Legislature: MCL 691.1419, notice of claim"),
            ("wrc_claim", "Oakland County WRC: Basement Flooding Claim"),
            ("wrc_form", "Oakland County WRC: Basement Flooding Claim (PA 222) online form"),
            ("wrc_brochure", "Oakland County WRC: Sewer Backup Infographic, 3-page (PDF)"),
            ("ro_flood", "City of Royal Oak: Responding to Street &amp; Basement Flooding"),
            ("ro_faq", "City of Royal Oak: Sewer Division FAQ"),
            ("ro_clerk", "City of Royal Oak: City Clerk's Office"),
            ("troy_claims", "City of Troy: Legal Claims for Overflows and Backups"),
            ("bham_risk", "City of Birmingham: Risk Management"),
            ("berk_claim", "City of Berkley: Report a Claim"),
            ("berk_tips", "City of Berkley: Flood Tips for Residents"),
            ("claw_dpw", "City of Clawson: DPW &amp; Engineering"),
            ("claw_sewer", "City of Clawson: Sanitary &amp; Storm Sewer System"),
            ("claw_dispatch", "City of Clawson Police: Dispatch Services (Troy dispatch contract, non-emergency line)"),
        ]),
    ])


# ---------------------------------------------------------------------------
# 2. George W. Kuhn Drainage District explainer
# ---------------------------------------------------------------------------

GWK_TITLE = "George W. Kuhn Drainage District: A Homeowner's Guide"
GWK_H1 = "The George W. Kuhn Drainage District, explained for homeowners"
GWK_DESC = (
    "What the George W. Kuhn Drainage District is, the 14 Oakland County communities it serves, why combined "
    "sewers back up in heavy rain, and prevention steps."
)
GWK_LEAD = (
    "<p>If you live in Royal Oak, Berkley, Clawson, Birmingham or Troy, your house may drain to a regional combined "
    "sewer system whose name never appears on your bill. The George W. Kuhn (GWK) Drainage District is that system: "
    "which communities it serves, why its combined sewers can back up into "
    "basements during heavy rain, and what homeowners can do about it. Facts come from the Oakland County Water "
    "Resources Commissioner (WRC) and the cities.</p>"
)

GWK_COMMUNITIES = [
    "Berkley", "Beverly Hills (village)", "Birmingham", "Clawson", "Ferndale", "Hazel Park", "Huntington Woods",
    "Madison Heights", "Oak Park", "Pleasant Ridge", "Royal Oak", "Royal Oak Township", "Southfield", "Troy",
]


def gwk_article():
    return "\n".join([
        h2("What the district is"),
        p(
            "The George W. Kuhn Drainage District, formerly the Twelve Towns Drainage District, serves all or part of 14 "
            "communities and covers a drainage area of 24,500 acres upstream of the Red Run Drain, a tributary of the Clinton "
            "River (" + ext("wrc_rtbs", "WRC: Retention Treatment Basins") + "). The WRC operates the district's retention treatment basin. Royal Oak describes itself "
            "as a member of the program formerly called the Twelve Town Drainage Enhancement Program, now the George W. Kuhn "
            "Retention Treatment Basin, named for the late former Oakland County Drain Commissioner (" + ext("ro_flood", "City of Royal Oak") + ")."
        ),
        h2("Which communities it serves"),
        p(
            "Oakland County's January 27, 2026 press release on the RainSmart Rebates pilot lists the municipalities the George W. Kuhn "
            "Drain Drainage District serves, all or part of each (" + ext("county_press", "Oakland County press release") + "). An older basin "
            "fact sheet names the same 14, identifying Royal Oak Township as a charter township and Beverly Hills as a village "
            "(" + ext("gwk_fact_sheet", "GWK fact sheet, PDF posted by the City of Birmingham") + "):"
        ),
        ul([esc(name) for name in GWK_COMMUNITIES]),
        p(
            "The district serves \"all or part\" of these places (" + ext("wrc_rtbs", "WRC") + "), so a city being on the list does "
            "not mean every street in it drains to the GWK system. The boundary follows sewers, not city limits. The WRC's RainSmart "
            "Rebates program uses the district as its service area and has an online eligibility tool that checks a specific address "
            "(" + ext("wrc_rainsmart", "WRC: RainSmart Rebates") + "). That is a practical way to see whether your property is inside it."
        ),
        h2("Combined sewers, and why they back up in heavy rain"),
        p(
            "In a separated system, one set of pipes carries stormwater and another carries sanitary flow from toilets, sinks and "
            "showers to a treatment plant. In a combined system, both travel in the same pipes (" + ext("wrc_gwk", "WRC: GWK Retention Treatment Basin") + "). "
            "The GWK system is combined. In dry weather, all of its flow goes to the Great Lakes Water Authority's wastewater treatment "
            "facility in Detroit (" + ext("wrc_gwk", "same page") + "). During heavy rainfall, the combined flow, typically more than 93 "
            "percent stormwater, exceeds the outlet capacity to Detroit, and the excess is diverted to the retention treatment basin "
            "(" + ext("wrc_rtbs", "WRC: Retention Treatment Basins") + ")."
        ),
        p(
            "When very large amounts of stormwater enter a combined system in a short time, the system can reach the limit of what it "
            "can hold and carry (" + ext("wrc_gwk", "WRC") + "). Water that cannot move downstream looks for the lowest opening, and in "
            "many older homes that is a basement floor drain. Birmingham explains that older communities have combined sewer and storm "
            "systems, which increase the chance of flooding compared with modern separate systems, and that sewers have long been designed "
            "for about two inches of rain in one hour, the \"10-year\" storm with a 10% chance in any year. The city says recent extreme "
            "storms have far exceeded that and may have overwhelmed parts of the system (" + ext("bham_risk", "City of Birmingham FAQ") + ")."
        ),
        p(
            "Not every wet basement is the public sewer's fault. Royal Oak lists tree roots, disposable diapers and grease in a home's own "
            "service line as key causes of backups, and says the owner is responsible for that line up to and including the connection to "
            "the city main (" + ext("ro_flood", "City of Royal Oak") + "). The WRC names three common causes: a blockage in the sewer pipe, "
            "intense rainfall and indoor plumbing problems (" + ext("wrc_brochure", "WRC sewer backup infographic") + ")."
        ),
        h2("The retention treatment basin"),
        p(
            "The George W. Kuhn Retention Treatment Basin sits beneath the I-75 overpass at 12 Mile Road in Madison Heights. The WRC "
            "describes an underground tunnel the size of a four-lane highway that can hold and treat 150 million gallons, and says it serves "
            "14 municipalities in southeast Oakland County (" + ext("wrc_gwk", "WRC: GWK Retention Treatment Basin") + ")."
        ),
        p(
            "In the basin, giant screens filter out debris and disinfectant is added while the flow is stored. At the same time, pumps "
            "send the stored flow on to the Detroit treatment facility as capacity returns. The WRC says what the basin discharges to the "
            "Red Run Drain is treated (" + ext("wrc_gwk", "same page") + "). An older fact sheet on the 2006 expansion, posted by the City of Birmingham, says the expansion "
            "reduced combined sewer overflows to an average of seven per year, down from a historical average of about 10 treated discharges "
            "a year (" + ext("gwk_fact_sheet", "GWK fact sheet") + "). The same fact sheet gives a total storage figure of 124 million gallons "
            "after that expansion; the WRC's current facility page gives 150 million. We report both because the sources differ."
        ),
        p(
            "What the basin does not do: it is built to store and treat combined flow before it reaches the river. It does not make a "
            "street's local sewer bigger, and it cannot stop water from backing up through a blocked private lateral or a floor drain with "
            "no protection. The WRC itself tells homeowners to protect their property in other ways, because filing a claim does not "
            "guarantee compensation (" + ext("wrc_brochure", "WRC sewer backup infographic") + ")."
        ),
        h2("Practical prevention for homes in the district"),
        p("These steps come from the WRC, the cities and federal safety agencies. A licensed plumber should size and install anything that ties into your sewer."),
        ul([
            "Backwater or backflow valve. The WRC suggests considering a backflow prevention system (" + ext("wrc_brochure", "WRC") + "), Birmingham lists a backflow preventer on the sewer lateral (" + ext("bham_risk", "Birmingham") + "), and CDC flood guidance recommends backflow valves or plugs for drains, toilets and other sewer connections (" + ext("cdc_flood", "CDC") + "). Permits are required in Berkley, and the city offers reimbursement of the permit fee, not the valve or installation, after inspection (" + ext("berk_valve", "Berkley reimbursement form") + ").",
            "Downspouts. Make sure roof downspouts are not connected to the sewer lateral and discharge at least six feet from the building (" + ext("bham_risk", "Birmingham") + "). This also matters for claims: a backup substantially caused by a downspout or sump connection on your property is not an \"event\" under the law (" + ext("mcl1416", "MCL 691.1416(k)") + ").",
            "Grading. Ground around the house should slope away from it, and landscaping should not trap water against the foundation (" + ext("bham_risk", "Birmingham") + ").",
            "Sump pump with backup power (" + ext("cdc_flood", "CDC") + "). Storms that overload sewers can also knock out power.",
            "Lateral inspection. Hire a licensed plumber to evaluate your sewer piping and ask about a camera inspection or cleaning schedule (" + ext("wrc_brochure", "WRC") + ").",
            "What goes down the drain. No fats, oils or grease, and no wipes, even ones labeled flushable (" + ext("wrc_brochure", "WRC") + ").",
            "Storage. Keep valuables off the basement floor, on shelves or in cabinets (" + ext("wrc_brochure", "WRC") + ").",
            "Insurance. Ask about a sewer backup endorsement (" + ext("wrc_brochure", "WRC") + ").",
            "Slow the rain down. The WRC encourages green infrastructure to reduce rainwater entering the system (" + ext("wrc_brochure", "WRC") + "). Its RainSmart Rebates program pays a one-time rebate to district homeowners for rain barrels, rain gardens and trees. The county says it is not accepting more applications for 2026 (" + ext("wrc_rainsmart", "RainSmart Rebates") + ").",
        ]),
        h2("If your basement floods anyway"),
        p(
            "Call your city's sewer line while it is happening, document everything, and remember the 45-day written notice rule for "
            "claims against a public agency. The details and each city's contact are in the "
            + a("/sewer-backup-claim-guide", "sewer backup claim guide") + ", and the "
            + a("/basement-flood-checklist", "printable basement flood checklist") + " covers before, during and after. For "
            "contaminated water that has to be removed, see " + a("/sewer-backup-cleanup", "sewer backup cleanup in Oakland County")
            + " or call " + phone_link() + " to be connected with an independent provider when one is available."
        ),
        p(
            "City overviews on this site: " + a("/royal-oak", "Royal Oak") + ", " + a("/berkley", "Berkley") + ", "
            + a("/clawson", "Clawson") + ", " + a("/birmingham", "Birmingham") + " and " + a("/troy", "Troy") + "."
        ),
        note(f"{esc(BRAND)} is not affiliated with the Oakland County Water Resources Commissioner or any city. Last verified {VERIFIED}."),
        sources_block([
            ("wrc_gwk", "Oakland County WRC: George W. Kuhn Retention Treatment Basin"),
            ("wrc_rtbs", "Oakland County WRC: Retention Treatment Basins"),
            ("county_press", "Oakland County press release, 27 Jan 2026: RainSmart Rebates pilot (lists the 14 district municipalities)"),
            ("gwk_fact_sheet", "George W. Kuhn Retention Treatment Basin fact sheet (PDF, posted by the City of Birmingham, Dec 2022)"),
            ("wrc_rainsmart", "Oakland County WRC: RainSmart Rebates"),
            ("wrc_brochure", "Oakland County WRC: Sewer Backup Infographic, 3-page (PDF)"),
            ("ro_flood", "City of Royal Oak: Responding to Street &amp; Basement Flooding"),
            ("bham_risk", "City of Birmingham: Risk Management and flooded basement FAQ"),
            ("berk_valve", "City of Berkley: Backwater Valve Permit Fee Reimbursement Request (PDF)"),
            ("cdc_flood", "CDC: Preparing for Floods"),
            ("mcl1416", "Michigan Legislature: MCL 691.1416"),
        ]),
    ])


# ---------------------------------------------------------------------------
# 3. Printable basement flood checklist
# ---------------------------------------------------------------------------

CHECK_TITLE = "Basement Flood Checklist for Oakland County (Printable)"
CHECK_H1 = "Basement flood checklist for Oakland County homes: before, during and after"
CHECK_DESC = (
    "A printable basement flood checklist for Oakland County homes: storm prep, DTE outage reporting, "
    "city sewer contacts, and the 45-day claim notice step."
)
CHECK_LEAD = (
    "<p>Print this checklist and keep it near the basement stairs. It lists what to do before a storm, while water is "
    "coming in, and in the days after, with the phone numbers and deadlines that apply in Royal Oak, Troy, Birmingham, "
    "Berkley and Clawson.</p>"
)

CHECK_CSS = RESOURCE_CSS + """
        .ck-list { list-style: none; padding-left: 0; margin: 0; }
        .ck-list li { display: flex; gap: 0.6rem; align-items: flex-start; font-size: 0.875rem; line-height: 1.55; color: #d1d5db; padding: 0.35rem 0; border-bottom: 1px dashed #1e293b; }
        .ck-box { flex: 0 0 auto; width: 1rem; height: 1rem; margin-top: 0.2rem; border: 2px solid #f87171; border-radius: 3px; }
        .print-btn { display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.6rem 1.1rem; border: 1px solid #f87171; border-radius: 0.6rem; color: #fff; background: transparent; font-weight: 700; font-size: 0.875rem; cursor: pointer; }
        .print-btn:hover { background: rgba(220, 38, 38, 0.2); }
        .print-only { display: none; }
        @media print {
            @page { margin: 0.6in; }
            html, body { background: #fff !important; color: #000 !important; }
            body { padding-bottom: 0 !important; }
            header, nav, .pulse-btn, .print-btn, .no-print, a[href^="tel:"].fixed, details, #faq { display: none !important; }
            main section { background: #fff !important; border: 0 !important; padding: 0 !important; }
            main *, footer * { color: #000 !important; background: transparent !important; box-shadow: none !important; }
            h1 { font-size: 20pt !important; }
            h2 { font-size: 14pt !important; margin-top: 12pt !important; break-after: avoid; }
            .ck-list li { border-bottom: 1px solid #999; break-inside: avoid; }
            .ck-box { border-color: #000; }
            .rs-sources a::after { content: " (" attr(href) ")"; font-size: 8pt; word-break: break-all; }
            .print-only { display: block !important; }
            footer { background: #fff !important; color: #000 !important; border: 0 !important; padding-top: 12pt !important; font-size: 8pt !important; }
            .rs-table th, .rs-table td { border-color: #999 !important; }
        }
"""


def checks(items):
    lis = "".join(f'<li><span class="ck-box" aria-hidden="true"></span><span>{item}</span></li>' for item in items)
    return f'<ul class="ck-list">{lis}</ul>'


def print_button():
    return (
        '<p class="no-print"><button type="button" class="print-btn" onclick="window.print()">'
        "Print this checklist</button></p>"
        f'<p class="print-only text-xs">Printed from oaklandsewerpros.com/basement-flood-checklist. Referral line: {esc(PHONE_DISPLAY)}. Verified {VERIFIED}.</p>'
    )


def checklist_article():
    return "\n".join([
        print_button(),
        h2("Numbers to write down now"),
        table(
            ["City", "Basement water or sewer backup", "After hours (as listed by the city)"],
            [
                ["Royal Oak", "DPS (248) 246-3300, Mon to Fri 7:30 a.m. to 4:00 p.m.", "Police non-emergency (248) 246-3500 (" + ext("ro_flood", "source") + ")"],
                ["Troy", "Water Division 248.524.3370, business hours", "Troy Police 248.524.3477 (" + ext("troy_claims", "source") + ")"],
                ["Birmingham", "Water event line (248) 530-1703 (data tracking, not a claim); claims questions 248.530.1808", "Not listed on the page we checked (" + ext("bham_risk", "source") + ")"],
                ["Berkley", "Public Works 248-658-3490", "Not listed on the page we checked (" + ext("berk_tips", "source") + ")"],
                ["Clawson", "DPW (248) 288-3222, Mon to Thu 7:00 a.m. to 3:30 p.m. (" + ext("claw_dpw", "source") + ")", "(248) 524-3477, ext. 1: Troy Dispatch, which Clawson contracts for 24-hour dispatch (" + ext("claw_dispatch", "source") + ")"],
                ["Power outage (DTE)", ext("dte_report", "outage.dteenergy.com/Report-Outage"), "(800) 477-4747 automated line (" + ext("dte_faq", "source") + ")"],
            ],
        ),
        p(
            "Also write down your insurance agent's number, your policy number, and the name of a licensed plumber. "
            f"{esc(BRAND)}'s referral line for cleanup providers is {phone_link()}."
        ),
        h2("Before a storm"),
        checks([
            "Find out who maintains your sewer. The WRC says to check your sewer bill (" + ext("wrc_claim", "WRC") + ").",
            "Know where your sewer pipe and cleanout are (" + ext("wrc_brochure", "WRC") + ").",
            "Have a licensed plumber evaluate your sewer lateral and ask about a camera inspection (" + ext("wrc_brochure", "WRC") + ").",
            "Ask the plumber about a backwater or backflow valve on the lateral (" + ext("bham_risk", "Birmingham") + ", " + ext("cdc_flood", "CDC") + "). Berkley requires a permit and reimburses the permit fee after inspection (" + ext("berk_valve", "Berkley form") + ").",
            "Test the sump pump. Add backup power (" + ext("cdc_flood", "CDC") + ").",
            "Disconnect downspouts from the sewer lateral and extend them at least six feet from the house (" + ext("bham_risk", "Birmingham") + ").",
            "Check that the ground slopes away from the foundation (" + ext("bham_risk", "Birmingham") + ").",
            "Move valuables, papers and electronics off the basement floor onto shelves (" + ext("wrc_brochure", "WRC") + ").",
            "Ask your insurer whether you have a sewer backup endorsement (" + ext("wrc_brochure", "WRC") + ").",
            "Take dated photos of the finished basement and its contents now. After a loss, you may need proof of what you owned and its value (" + ext("mcl1417", "MCL 691.1417(4)(a)") + ").",
            "Keep grease and wipes out of drains (" + ext("wrc_brochure", "WRC") + ").",
            "Bookmark the " + ext("dte_report", "DTE outage report page") + " and sign up for outage alerts in your DTE account (" + ext("dte_faq", "DTE") + ").",
            "Keep rubber boots and waterproof gloves where you can reach them (" + ext("cdc_flood", "CDC") + ").",
        ]),
        h2("During: water is coming in"),
        checks([
            "Keep people and pets out of the water. Do not step into water that may be touching outlets, cords, the furnace or appliances.",
            "Turn off power only if you can reach the breaker without touching water. CDC advises turning off power when water is in the home (" + ext("cdc_flood", "CDC") + "), but not at the cost of wading in.",
            "Call your city's line from the table above now, while it is happening. Royal Oak says it is important the city can investigate during the event (" + ext("ro_flood", "Royal Oak") + ").",
            "If the power is out, report it to DTE online or at (800) 477-4747. DTE says not to assume it already knows (" + ext("dte_faq", "DTE") + ").",
            "Never run a portable generator in the basement, garage or house. Use it outside, away from windows, doors and vents (" + ext("cpsc_gen", "CPSC") + ").",
            "Hold off on laundry, dishwashers and extra flushing until the drains are moving again.",
            "Photograph and film the water level, where it is coming from (floor drain, toilet, wall, window well) and the time.",
            "Write down each call: time, number, who answered, and what they said.",
        ]),
        h2("After: the first days"),
        checks([
            "Write down the date you discovered the damage. Count 45 days and mark it on a calendar.",
            "If you think a public sewer caused it, send written notice to the right agency within 45 days. It must include your name, address and phone, the property address, the discovery date, and a brief description (" + ext("mcl1419", "MCL 691.1419") + "). City-by-city steps: " + a("/sewer-backup-claim-guide", "sewer backup claim guide") + ".",
            "Birmingham residents: the water event tracking form is not a claim (" + ext("bham_risk", "Birmingham") + ").",
            "Call your insurance company. Keep the declaration page showing your deductible and any payment or denial letter; the WRC claim form asks for both (" + ext("wrc_form", "WRC form") + ").",
            "Photograph every damaged item before it leaves the house, and list it with its age and value. Keep receipts.",
            "Treat sewage as contaminated. Throw away items that cannot be disinfected, such as drywall, rugs and cloth (" + ext("cdc_flood", "CDC") + "). Royal Oak publishes cleanup and sanitizing steps (" + ext("ro_cleanup", "Royal Oak") + ").",
            "Dry the space with fans and dehumidifiers once the water is out (" + ext("cdc_flood", "CDC") + ").",
            "Have a licensed plumber check the lateral and ask for the camera video (" + ext("bham_risk", "Birmingham") + ").",
            "Get written scopes and proof of license and insurance from any cleanup company before work starts. Keep every invoice.",
            "If the city or county asks to inspect, allow reasonable access (" + ext("mcl1419", "MCL 691.1419(5)") + ").",
        ]),
        h2("Getting sewage or floodwater removed"),
        p(
            f"{esc(BRAND)} is a referral line. Call {phone_link()} to be connected with an independent provider when one is available "
            "for your address. How soon they can come, and what they charge, come from that company. Related pages: "
            + a("/flooded-basement-cleanup", "flooded basement cleanup") + ", "
            + a("/sewer-backup-cleanup", "sewer backup cleanup") + ", "
            + a("/water-damage-restoration", "water damage restoration") + ", and the "
            + a("/george-w-kuhn-drainage-district", "George W. Kuhn Drainage District explainer") + "."
        ),
        note("This checklist is general safety and preparation information, not legal, electrical or plumbing advice. Last verified " + VERIFIED + "."),
        sources_block([
            ("mcl1419", "Michigan Legislature: MCL 691.1419, notice of claim"),
            ("mcl1417", "Michigan Legislature: MCL 691.1417"),
            ("wrc_claim", "Oakland County WRC: Basement Flooding Claim"),
            ("wrc_form", "Oakland County WRC: Basement Flooding Claim (PA 222) form"),
            ("wrc_brochure", "Oakland County WRC: Sewer Backup Infographic, 3-page (PDF)"),
            ("dte_report", "DTE Energy: Report Your Outage"),
            ("dte_faq", "DTE Energy: Outage FAQs"),
            ("cdc_flood", "CDC: Preparing for Floods"),
            ("cpsc_gen", "U.S. CPSC: Generators and Engine-Driven Tools"),
            ("ro_flood", "City of Royal Oak: Responding to Street &amp; Basement Flooding"),
            ("ro_cleanup", "City of Royal Oak: Cleaning Up the Mess After Basement Flooding"),
            ("troy_claims", "City of Troy: Legal Claims for Overflows and Backups"),
            ("bham_risk", "City of Birmingham: Risk Management"),
            ("berk_tips", "City of Berkley: Flood Tips for Residents"),
            ("berk_valve", "City of Berkley: Backwater Valve Permit Fee Reimbursement (PDF)"),
            ("claw_dpw", "City of Clawson: DPW &amp; Engineering"),
            ("claw_dispatch", "City of Clawson Police: Dispatch Services"),
        ]),
    ])


RESOURCE_PAGES = [
    # slug, title, h1, description, lead html, article fn, extra css, nav label
    ("sewer-backup-claim-guide", CLAIM_TITLE, CLAIM_H1, CLAIM_DESC, CLAIM_LEAD, claim_article, RESOURCE_CSS, "Sewer backup claim guide"),
    ("george-w-kuhn-drainage-district", GWK_TITLE, GWK_H1, GWK_DESC, GWK_LEAD, gwk_article, RESOURCE_CSS, "George W. Kuhn Drainage District"),
    ("basement-flood-checklist", CHECK_TITLE, CHECK_H1, CHECK_DESC, CHECK_LEAD, checklist_article, CHECK_CSS, "Basement flood checklist"),
]


RESOURCE_FAQS = {
    "sewer-backup-claim-guide": [
        (
            "What has to be in the 45-day written notice?",
            "Michigan law limits the required content to your name, address, and phone number, the address of the affected property, the date you discovered the damage, and a brief description. The 45 days run from discovery, or from the day you should have discovered it, not from the day cleanup finishes. Keep a copy and write down how you sent it.",
        ),
        (
            "Do Royal Oak, Troy, Birmingham, Berkley, and Clawson file this with Oakland County?",
            "Start with the sewer bill. The Water Resources Commissioner lists communities where the county operates the local system, and these five cities are not on that list. Call the city while it is happening: Royal Oak (248) 246-3300 weekdays, after hours (248) 246-3500; Troy Water Division 248-524-3370, after hours 248-524-3477; Birmingham claims questions 248.530.1808; Berkley Public Works 248-658-3490; Clawson DPW (248) 288-3222, Monday through Thursday. Whether the George W. Kuhn system should also receive a notice is a question for an attorney.",
        ),
        (
            "Is the letter to the city the same as an insurance claim?",
            "No. A notice to the city is not an insurance claim. Many homeowner policies cover sewer backup only with an added endorsement, and the Water Resources Commissioner suggests asking about one. Call your insurer when you notify the city. Keep the declaration page and any payment or denial letter.",
        ),
        (
            "What should I photograph before cleanup starts?",
            "Photograph and film the water, the floor drain or fixture it came from, and every damaged item before anything is thrown out. Write down the date and time you found the water. The statute asks for reasonable proof of ownership and value of damaged personal property. Keep invoices and a log of each city call.",
        ),
        (
            "Does calling (248) 825-8312 file the 45-day notice?",
            "The call connects you with an independent cleanup company when one is participating for your address. The written notice is still a letter you send to the city or other responsible agency. The company sets the cleanup scope and the price. This page is general information, not legal advice.",
        ),
        (
            "What if the city has not told me who receives the letter?",
            "If you contact the city about the backup first, the statute says the city must give you, in writing, the notice rules, the name and address of the person who receives notices, and the required content. Ask in writing early. When this guide was checked, Royal Oak had no dedicated claim form posted, and Clawson's Public Act 222 document link returned an error. Troy, Berkley, and Birmingham each publish a claim form.",
        ),
    ],
    "george-w-kuhn-drainage-district": [
        (
            "What is the George W. Kuhn Drainage District?",
            "It is the regional drainage district formerly called Twelve Towns. It serves all or part of 14 communities and covers about 24,500 acres upstream of the Red Run Drain, a tributary of the Clinton River. The Oakland County Water Resources Commissioner operates the retention treatment basin.",
        ),
        (
            "Are Royal Oak, Troy, Birmingham, Berkley, and Clawson in it?",
            "All five appear on the county list of communities the district serves, in whole or in part. A city on the list does not mean every street drains to the system. The boundary follows sewers, not city limits. The county's RainSmart eligibility tool can check a specific address.",
        ),
        (
            "Why can a hard rain push sewage into a basement here?",
            "The district system is combined: stormwater and sanitary flow share pipes. In dry weather the flow goes to the Great Lakes Water Authority plant in Detroit. In heavy rain the combined flow, typically more than 93 percent stormwater, can exceed the outlet to Detroit. Water that cannot move downstream looks for a low opening, often a basement floor drain. A blocked private lateral can cause a backup on its own.",
        ),
        (
            "How much can the retention treatment basin hold?",
            "The basin is under the I-75 overpass at 12 Mile Road in Madison Heights. The Water Resources Commissioner says it can hold and treat 150 million gallons and serves 14 municipalities. An older fact sheet posted by Birmingham gives 124 million gallons after the 2006 expansion. The sources differ, so both figures are reported here. The basin does not make the local sewer on your street larger.",
        ),
        (
            "What should I do if the basement floods anyway?",
            "Call your city's sewer line while it is happening, photograph the damage, and send written notice within 45 days if you believe a public sewage system caused the loss. A backflow preventer, downspouts extended about 6 feet, and a sewer-backup endorsement are prevention steps. They do not remove water already on the floor. Call (248) 825-8312 to be connected with an independent cleanup company when one is available.",
        ),
    ],
    "basement-flood-checklist": [
        (
            "Which city number do I call while water is coming in?",
            "Royal Oak: (248) 246-3300 on weekdays, after hours police non-emergency (248) 246-3500. Troy: Water Division 248-524-3370, after hours Troy Police 248-524-3477. Birmingham's water event line (248) 530-1703 collects flooding data and is not a claim; claims questions are 248.530.1808. Berkley Public Works is 248-658-3490. Clawson DPW is (248) 288-3222 Monday through Thursday; after hours is (248) 524-3477, extension 1. For a power outage, DTE lists (800) 477-4747.",
        ),
        (
            "What should an Oakland County homeowner do before the next storm?",
            "Check the sewer bill to see who maintains the line. Ask a plumber about the lateral and a backflow valve. Berkley reimburses the permit fee after inspection, not the valve. Extend downspouts at least six feet, which Birmingham lists, and keep valuables off the floor. Ask your insurer whether a sewer-backup endorsement is on the policy. Test the sump pump.",
        ),
        (
            "What should I avoid while sewage is on the basement floor?",
            "Keep people and pets out of the water. Do not step in if it may be touching outlets, the furnace, or appliances. Turn off power only if you can reach the breaker without wading. Never run a portable generator in the basement, garage, or house. Hold off on laundry and extra flushing until the drains move again.",
        ),
        (
            "When does the 45-day written notice start?",
            "Write down the date you discovered the damage and count 45 days from that day. If you think a public sewer caused it, the notice needs your name, address, and phone, the property address, the discovery date, and a brief description. Birmingham's water-event form is not that claim. The city letter and the call to your insurer are separate.",
        ),
        (
            "When should I call (248) 825-8312?",
            "Call when sewage or floodwater in the house needs to be removed. The line connects you with an independent provider when one is available for your address. How soon they can come, and what they charge, come from that company. Ask for a written scope and for proof of license and insurance before work starts.",
        ),
    ],
}
