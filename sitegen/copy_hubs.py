"""County service hubs and city hubs.

City overviews are written separately. They do not share a public-works paragraph,
a first-10-minutes list, or a nearby-cities sentence with the city name swapped in.
The five /[city]-sewer-cleanup pages keep their own templates in copy_sewer.py.
"""
from site_config import PHONE_DISPLAY

from sitegen.citations import (
    BERK_CLAIM,
    BERK_TIPS,
    BHAM,
    CLAW_SEWER,
    MCL1419,
    RO_115,
    RO_FLOOD,
    RO_SEWER,
    TROY_AGENDA,
    TROY_CLAIMS,
    WRC_GWK,
    cite,
)
from sitegen.render import a, esc, h2, h3, p, phone_link, ul


def ext(href, text):
    return (
        f'<a href="{esc(href)}" rel="noopener" class="text-red-400 hover:text-red-300 underline font-medium">'
        f"{esc(text)}</a>"
    )


def sources(items):
    return h2("Sources for these local facts") + ul(
        [ext(url, label) for url, label in items]
    )


_HOME = a("/", "Oakland Sewer Pros")
_GUIDE = a("/sewer-backup-claim-guide", "sewer backup claim guide")
_GWK = a("/george-w-kuhn-drainage-district", "George W. Kuhn Drainage District")
_CHECK = a("/basement-flood-checklist", "basement flood checklist")

GWK_PDF = (
    "https://cms7files1.revize.com/birmingham/Document_Center/Department/City%20manager/"
    "City%20Manager%20Report/Dec%202022/GWK%20Information%202022-12-13.pdf"
)
GWK_RTB = "https://www.oaklandcountymi.gov/government/water-resources-commissioner/wastewater/facilities/george-w-khun-rtb"
FEMA_2014 = "https://www.federalregister.gov/documents/2014/10/20/2014-24801/michigan-major-disaster-and-related-determinations"
NWS_2014 = "https://www.weather.gov/media/grr/GLOM2015/Abstracts/CMU-Saunders-DTX-Flash-flood-2014.pdf"


def services_article():
    return "\n".join([
        h2("Sewer backup and basement water help in Oakland County"),
        p(
            "Call " + phone_link() + " for sewer backup cleanup, sewage extraction, flooded basement cleanup, "
            "water damage restoration, sump pump repair, or basement sanitization in Royal Oak, Troy, Birmingham, "
            "Berkley, or Clawson. Ask the crew for proof of license and insurance before work starts."
        ),
        h2("Match the water to the right help"),
        p(
            "If you are not sure whether a drain, a sump, or a storm caused the water, read the county "
            "overview first, then your city, so you can describe the source when you call."
        ),
        p(
            a("/water-damage-restoration", "Water damage restoration")
            + " means getting water out, drying what remains, and handling sewage water damage. It is the broadest match for a wet basement."
        ),
        p(
            a("/sewer-backup-cleanup", "Sewer backup cleanup")
            + " means sewage that came up through a drain. Each city page covers the local steps."
        ),
        p(
            a("/sewage-extraction", "Sewage extraction")
            + " is the pumping and removal step when the water is contaminated."
        ),
        p(
            a("/flooded-basement-cleanup", "Flooded basement cleanup")
            + " is basement water removal when you are dealing with storm water, a window well, or a sump overflow. If a drain was involved, use the sewage pages."
        ),
        p(
            a("/sump-pump-repair", "Sump pump repair")
            + " is the mechanical pump. Overflow cleanup, if the floor is wet, is a water-damage job on top of the repair. A dead pump with a wet floor needs both the repair and the water removal."
        ),
        p(
            a("/basement-sanitization", "Basement sanitization")
            + " means cleaning after sewage or a contaminated flood. It is not a housekeeping service."
        ),
        h2("How a call is different from a city sewer report"),
        p(
            "City public works can look at the main in the street. A local cleanup crew can pump and dry the basement. "
            "Call " + phone_link() + " for that crew. If you think the municipal main caused the backup, you still have "
            "a separate written-notice deadline under Michigan law. The steps are in the "
            + _GUIDE
            + ". Storm prep, including the city numbers to keep by the phone, is on the "
            + _CHECK
            + ". Why so many of these basements sit upstream of the Red Run Drain is on the "
            + _GWK
            + " page."
        ),
        h2("Cities"),
        p(
            "Choose a city overview, then the service that matches the water: "
            + a("/royal-oak", "Royal Oak") + ", "
            + a("/troy", "Troy") + ", "
            + a("/birmingham", "Birmingham") + ", "
            + a("/berkley", "Berkley") + ", and "
            + a("/clawson", "Clawson") + ". "
            "Each overview has that city's own sewer description and the phone number the city publishes. "
            "Do not use one city's number for a house in another city."
        ),
        p(
            "About the company: "
            + a("/about", "about")
            + ", " + a("/contact", "contact")
            + ", " + a("/privacy", "privacy")
            + ", and " + a("/terms", "terms")
            + "."
        ),
    ])


def water_hub():
    return "\n".join([
        h2("What water damage restoration includes"),
        p(
            "Water damage restoration in Oakland County means getting water out of a house, deciding what "
            "materials cannot be saved, and drying what remains. Water damage repair is the phrase people "
            "use when finishes also have to be replaced. For either, call "
            + phone_link() + "."
        ),
        h3("Scope the crew should put in writing"),
        p(
            "Ask for three lines in the scope: what will be pumped, what porous material will be removed, "
            "and how moisture will be rechecked after the fans have run. Extraction is the standing water "
            "and the soaked layers. Structural drying is the days afterward. A clean supply-line break is a "
            "different scope from a basement full of sewage. If the water came from a sewer drain, restorers "
            "treat it as heavily contaminated water, and carpet pad, insulation, and swollen drywall usually come out. "
            "Say which water you have when you call. Get the price for each step in writing."
        ),
        h2("Safety before anyone arrives"),
        p(
            "Keep people and pets out of the water. If it has reached outlets, the furnace, or the panel, "
            "leave the basement and shut power off only from a dry location. Stop running faucets, the washer, "
            "and the dishwasher so more water does not arrive while you are on the phone. Do not shop-vac sewage "
            "through the living room. Do not mix household cleaners in a closed basement. The crew "
            "chooses the product after they see the water. A household mop does not turn a sewage loss into a clean-water loss."
        ),
        h2("Insurance and the paperwork that is easy to skip"),
        p(
            "Homeowners policies often exclude sewer backup unless an endorsement is on the form, and groundwater "
            "is often limited. A sudden supply-line break is a different coverage question from sewage at a floor drain. "
            "Ask your insurer. Photograph rooms before anything is torn out, list what you throw away, and keep the "
            "crew's written scope. The insurance claim stays between you and your carrier. "
            "A claim against a city, if you believe the public main caused the backup, is a separate 45-day written "
            "notice. That clock and each city's contact are in the " + _GUIDE + "."
        ),
        h2("When to call, and when it is a different problem"),
        p(
            "Call for restoration when materials are already wet and the question is drying or removal, not only "
            "a stuck float on a pump. If sewage is still coming up a drain, start at "
            + a("/sewer-backup-cleanup", "sewer backup cleanup")
            + " and tell the city as well. If the floor is wet from a storm or a sump and the drains stayed quiet, "
            + a("/flooded-basement-cleanup", "flooded basement cleanup")
            + " is the closer match, and restoration is the follow-on if finishes stayed wet. Sanitizing after "
            "contaminated water is " + a("/basement-sanitization", "basement sanitization") + ". "
            "Print the " + _CHECK + " before the next storm so the city numbers are not a search you do in the dark."
        ),
        h2("These five cities are not one basement"),
        p(
            "Basement flooding here is local, not one county-wide cause. All five cities drain, in whole or in part, to "
            "the " + _GWK + ", the regional district upstream of the Red Run Drain. "
            "The district does not tell you which pipe is in front of a particular house."
        ),
        p(
            "Royal Oak's older blocks and Woodward-side window wells are a different pattern from Troy's finished "
            "lower levels, Birmingham's plaster houses, Berkley's older homes on a combined sewer, and Clawson's "
            "small basements. Open the city page that matches the house:"
        ),
        ul([
            a("/royal-oak-water-damage-restoration", "Water damage restoration in Royal Oak"),
            a("/troy-water-damage-restoration", "Water damage restoration in Troy"),
            a("/birmingham-water-damage-restoration", "Water damage restoration in Birmingham"),
            a("/berkley-water-damage-restoration", "Water damage restoration in Berkley"),
            a("/clawson-water-damage-restoration", "Water damage restoration in Clawson"),
        ]),
        p(
            "Each city overview lists its sewer numbers: "
            + a("/royal-oak", "Royal Oak") + ", "
            + a("/troy", "Troy") + ", "
            + a("/birmingham", "Birmingham") + ", "
            + a("/berkley", "Berkley") + ", "
            + a("/clawson", "Clawson") + "."
        ),
    ])


def sewer_hub():
    return "\n".join([
        h2("Sewage cleanup and sewer backup in Oakland County"),
        p(
            "Sewage cleanup in Oakland County means wastewater that came up a floor drain, "
            "a basement toilet, or a laundry standpipe. The line was full, and the lowest opening in the house let it "
            "out. That is sewer backup cleanup. Open your city for the local steps and the city's sewer number."
        ),
        h3("What the cleanup has to cover"),
        p(
            "Treat the water as heavily contaminated. People and pets stay out. A household vac spreads droplets "
            "onto stairs and joists. The local crew should say what will be pumped, which porous materials "
            "cannot be saved, and how the remaining surfaces will be cleaned. Pumping alone is "
            + a("/sewage-extraction", "sewage extraction")
            + ". Cleaning what remains is "
            + a("/basement-sanitization", "basement sanitization")
            + ". If the basement is wet but no drain moved, use "
            + a("/flooded-basement-cleanup", "flooded basement cleanup")
            + " or " + a("/water-damage-restoration", "water damage restoration") + " instead."
        ),
        h2("The public main and the lateral are different pipes"),
        p(
            "In these cities the municipality is generally responsible for the main in the street, and the "
            "homeowner is responsible for the private lateral in the yard. Royal Oak states that split directly: "
            "the city main is the city's, and the lateral up to and including the connection is the homeowner's. "
            "Other cities draw the line in their own documents. The crew should not guess which pipe failed. "
            "Call the city number published for that city if the backup looks like it is coming from the main, and call "
            + phone_link()
            + " if you need a cleanup company inside the house."
        ),
        h2("Written notice, separate from the insurance call"),
        p(
            "Michigan law requires written notice to the responsible government agency within 45 days of discovering "
            "the damage before compensation for a sewage disposal system event is possible. That notice is not the "
            "same phone call as hiring a restoration company, and it is not the same form as an insurance claim. "
            "Sewer backup coverage on a homeowners policy is often a separate endorsement. Ask your insurer. "
            "The statute, what to photograph, and each city's claim contact are in the " + _GUIDE + ". "
            "The " + _CHECK + " is the storm list. The regional pipes are explained on the " + _GWK + " page."
        ),
        h2("Why heavy rain shows up in these basements"),
        p(
            "The George W. Kuhn Drainage District, formerly Twelve Towns, serves all or part of 14 communities, "
            "including Berkley, Birmingham, Clawson, Royal Oak, and Troy. It covers about 24,500 acres upstream "
            "of the Red Run Drain, a tributary of the Clinton River. Dry-weather flow goes to the Detroit (GLWA) plant. "
            "In wet weather the combined flow is typically more than 93 percent stormwater. The retention treatment "
            "basin under the I-75 overpass at 12 Mile Road in Madison Heights can hold and treat 150 million gallons "
            "and discharges treated flow to the Red Run Drain. In a combined system, sanitary sewage and stormwater "
            "share pipes, so a hard rain can fill the pipe and push wastewater toward the lowest drain in a house. "
            "Those figures describe the district, not a count of damaged homes in any one city."
        ),
        h3("Sewage cleanup, by city"),
        p(
            "Royal Oak: the Sewer Division maintains about 300 miles of sanitary and storm sewers, and basement-water "
            "calls have a published weekday line plus after-hours police dispatch. "
            + "Start with "
            + a("/royal-oak-sewer-cleanup", "sewage cleanup in Royal Oak, MI")
            + ", or the " + a("/royal-oak", "Royal Oak overview") + "."
        ),
        p(
            "Troy: wastewater leaves through three districts, Evergreen-Farmington, Oakland-Troy, and George W. Kuhn. "
            "Do not describe Troy as fully combined or fully separated. "
            + "Start with "
            + a("/troy-sewer-cleanup", "sewage cleanup in Troy, MI")
            + ", or the " + a("/troy", "Troy overview") + "."
        ),
        p(
            "Birmingham: older areas have combined sewers, the system is gravity, and the city owns no pump or lift stations. "
            + "Start with "
            + a("/birmingham-sewer-cleanup", "sewage cleanup in Birmingham, MI")
            + ", or the " + a("/birmingham", "Birmingham overview") + "."
        ),
        p(
            "Berkley: one combined pipe, gravity, no pumps or valves, with flow toward the Clinton River side rather than the Rouge. "
            + "Start with "
            + a("/berkley-sewer-cleanup", "sewage cleanup in Berkley, MI")
            + ", or the " + a("/berkley", "Berkley overview") + "."
        ),
        p(
            "Clawson: the city sewer page points to the George W. Kuhn basin and the Oakland County Water Resources Commissioner. "
            + "Start with "
            + a("/clawson-sewer-cleanup", "sewage cleanup in Clawson, MI")
            + ", or the " + a("/clawson", "Clawson overview") + "."
        ),
        sources([
            (GWK_PDF, "Oakland County WRC letter in the Birmingham City Manager report (GWK district, December 2022)"),
            (GWK_RTB, "Oakland County: George W. Kuhn Retention Treatment Basin"),
            ("https://www.romi.gov/384/Sewer-Division", "Royal Oak Sewer Division"),
            ("https://apps.troymi.gov/Meetings/Meetings/DownloadPDF/5548482", "Troy City Council agenda item, November 14, 2022"),
            ("https://www.bhamgov.org/about_birmingham/city_departments/city_manager/risk_management.php", "Birmingham Risk Management FAQ"),
            ("https://www.berkleymi.gov/public-works/flood-tips-for-residents", "Berkley flood tips"),
            ("https://www.cityofclawson.com/your_government/dpw_and_engineering/sewer.php", "Clawson sewer page"),
        ]),
    ])


def sewage_hub():
    return "\n".join([
        h2("What sewage extraction is, and what it is not"),
        p(
            "Sewage extraction removes contaminated water that left the sanitary plumbing, plus the "
            "materials that soaked it up. It is not the sewage cleanup overview, and it is not mopping "
            "rain that came through a window. A household vac spreads it. A local crew with "
            "the right setup does the removal. The equipment belongs to that crew. Call "
            + phone_link() + "."
        ),
        h2("How removal should be sequenced"),
        p(
            "The crew should keep the contaminated area from walking into the rest of the house: shoes, "
            "hoses, and debris have a path that does not cross the living-room carpet. Standing wastewater "
            "is pumped first. Carpet pad, fiberglass insulation, and drywall that has wicked sewage usually "
            "come out rather than get dried in place. Hard surfaces that remain can be cleaned afterward. "
            "That later step is " + a("/basement-sanitization", "basement sanitization")
            + ", not a second pass with the same pump. Ask where the wastewater will be taken. Do not pump "
            "it into a street gutter or a storm catch basin yourself."
        ),
        h3("Safety while the basement is still wet"),
        p(
            "Stay out if water is near outlets or the furnace. Shut power off only from a dry spot. Stop using "
            "water upstairs so toilets and the washer do not add to the backup. Keep children and pets off the "
            "stairs. If you feel dizzy or smell a strong sewage odor in a small basement, leave the air to the "
            "company that has the equipment. Do not mix bleach with any other cleaner."
        ),
        h2("What to write down before debris leaves"),
        p(
            "Photograph each room before pad and drywall are removed. Note the time you discovered the water "
            "and whether a floor drain, a toilet, or a standpipe was the source. That timeline matters if you "
            "later send the 45-day written notice described in the " + _GUIDE
            + ". Your insurer will ask a different set of questions. Sewer backup is often excluded unless the "
            "policy has an endorsement. Ask the carrier. Ask the crew for a written scope and for proof of "
            "license and insurance."
        ),
        h2("When extraction is the wrong job"),
        p(
            "If the drains never moved and the water is storm water or a sump overflow, start at "
            + a("/flooded-basement-cleanup", "flooded basement cleanup")
            + ". If the pump itself failed, the mechanical page is "
            + a("/sump-pump-repair", "sump pump repair")
            + ", and extraction or drying is a second step only if the floor got wet. The backup overview, "
            "including the regional district, is " + a("/sewer-backup-cleanup", "sewer backup cleanup")
            + ". Storm steps are on the " + _CHECK + ". The district map in plain language is the " + _GWK + " page."
        ),
        p(
            "The regional storage for this system is the George W. Kuhn Retention Treatment Basin, under the I-75 overpass at 12 Mile Road in Madison Heights, which can hold and treat 150 million gallons. "
            "The district drains to the Red Run Drain, a tributary of the Clinton River. "
            "Troy's wastewater goes through three districts (Evergreen-Farmington, Oakland-Troy and George W. Kuhn), so not every Oakland County basement is on the same system."
        ),
        h2("Pumping help in each city"),
        p(
            a("/royal-oak-sewage-extraction", "Sewage extraction in Royal Oak")
            + " usually starts at a basement floor drain. The city's Sewer Division is the contact for the public main. "
            "See the " + a("/royal-oak", "Royal Oak overview") + "."
        ),
        p(
            a("/troy-sewage-extraction", "Sewage extraction in Troy")
            + " often means a finished lower floor. Troy's wastewater leaves through three districts, so do not "
            "assume one pipe type. See the " + a("/troy", "Troy overview") + "."
        ),
        p(
            a("/birmingham-sewage-extraction", "Sewage extraction in Birmingham")
            + " has to work around plaster and trim in early- and mid-1900s houses. The city system is gravity, "
            "with no municipal pump stations. See the " + a("/birmingham", "Birmingham overview") + "."
        ),
        p(
            a("/berkley-sewage-extraction", "Sewage extraction in Berkley, MI")
            + " means working down a short stair, on a combined, gravity sewer. See the "
            + a("/berkley", "Berkley overview") + "."
        ),
        p(
            a("/clawson-sewage-extraction", "Sewage extraction in Clawson")
            + " often means a compact lot and a one-room basement. See the " + a("/clawson", "Clawson overview") + "."
        ),
    ])


def flood_hub():
    return "\n".join([
        h2("Basement flood cleanup when a drain did not cause it"),
        p(
            "Basement flood cleanup in Oakland County means getting standing water off the floor and out "
            "of the materials it entered, when the source is rain, a window well, surface water, or a sump "
            "that overflowed. Flooded basement cleanup is that work plus the mess it left. If a sewer drain "
            "was the source, do not treat it as a rain flood. Use "
            + a("/sewage-extraction", "sewage extraction")
            + " or " + a("/sewer-backup-cleanup", "sewage cleanup")
            + ". If finishes are still wet after the pump-out, the longer process is "
            + a("/water-damage-restoration", "water damage restoration")
            + ". A local crew pumps the basement. Call " + phone_link() + "."
        ),
        h2("What the water-removal visit is for"),
        p(
            "The useful scope is simple: where the water entered, how deep it got, what it touched, and "
            "whether the sump is still running. Window-well water and a failed pump are not the same job as "
            "sewage at a laundry standpipe. Tell the crew which one you see. Carpet that held clean storm "
            "water may be a drying question. Carpet that held sewage is a removal question. If you are not "
            "sure the water is clean, treat it as contaminated until someone who does this work says otherwise. "
            "Do not run a household vac through the stairwell."
        ),
        h3("Power, and the pump that quit because the power quit"),
        p(
            "A storm that floods a basement often knocks out power at the same time. Do not stand in water "
            "to reach a panel or a sump cord. A dead pump during the storm is "
            + a("/sump-pump-repair", "sump pump repair")
            + " after it is safe to be in the room. Water already on the floor is still this cleanup. "
            "The " + _CHECK + " lists DTE outage reporting next to the city sewer numbers so both calls are on one sheet."
        ),
        h2("Insurance, photos, and city notice"),
        p(
            "Groundwater and surface water are often limited on a standard homeowners form. Sewer backup, "
            "if a drain was involved after all, is often an endorsement. Ask your insurer before you assume "
            "either will pay. Photograph depth and damaged finishes before debris is carried out. If you "
            "later decide the public system was involved, the 45-day written notice in the " + _GUIDE
            + " runs from discovery, not from the day the insurance adjuster visits. The city letter and the insurance call are yours to make."
        ),
        h2("August 2014, as a county storm, not a city scorecard"),
        p(
            "On August 11 through 13, 2014, severe storms flooded parts of southeast Michigan. A presidential "
            "major disaster, FEMA-4195-DR, was declared on September 25, 2014, for Macomb, Oakland, and Wayne "
            "counties, for individual and public assistance. A National Weather Service conference paper "
            "describes about 4 to 6.5 inches in parts of those three counties, most of it in roughly four hours. "
            "Those rainfall figures are not a count of damaged houses in Royal Oak, Troy, Birmingham, "
            "Berkley, or Clawson. Royal Oak's own gauge reading from that day is on the "
            + a("/royal-oak", "Royal Oak overview")
            + ", attributed to the report that quoted the city gauge. The regional pipes those storms loaded are "
            "described on the " + _GWK + " page."
        ),
        p(
            "The regional storage for this system is the George W. Kuhn Retention Treatment Basin, under the I-75 overpass at 12 Mile Road in Madison Heights, which can hold and treat 150 million gallons. "
            "Birmingham's older sewers were designed for about 2 inches of rain in one hour. "
            "In a heavy downpour, Royal Oak says street flooding is usually caused by debris sitting on the sewer grate, so clearing leaves and grass clippings off the grate in front of your house helps."
        ),
        h3("The five city versions"),
        p(
            a("/royal-oak-flooded-basement", "Flooded basement cleanup in Royal Oak")
            + " starts by telling a window-well flood apart from a true drain backup. See the "
            + a("/royal-oak", "Royal Oak overview") + "."
        ),
        p(
            a("/troy-flooded-basement", "Flooded basement cleanup in Troy")
            + " often means a finished lower level or split-level where carpet holds the water. Troy discharges "
            "through three wastewater districts. See the " + a("/troy", "Troy overview") + "."
        ),
        p(
            a("/birmingham-flooded-basement", "Flooded basement cleanup in Birmingham")
            + " works around plaster in older houses. The city's sewers are gravity, with no city pump stations, "
            "and the city has said its older combined pipes were designed for about 2 inches of rain in an hour. "
            "See the " + a("/birmingham", "Birmingham overview") + "."
        ),
        p(
            a("/berkley-flooded-basement", "Flooded basement cleanup in Berkley")
            + " happens at the bottom of a short stair. Berkley's combined sewer is designed so streets hold water on "
            "purpose. See the " + a("/berkley", "Berkley overview") + "."
        ),
        p(
            a("/clawson-flooded-basement", "Flooded basement cleanup in Clawson, MI")
            + " often means a one-room basement with the furnace close to the water. See the "
            + a("/clawson", "Clawson overview") + "."
        ),
        sources([
            (FEMA_2014, "Federal Register: FEMA-4195-DR, Michigan major disaster (September 25, 2014)"),
            (NWS_2014, "National Weather Service conference paper on the August 11, 2014 rainfall"),
        ]),
    ])


def sump_hub():
    return "\n".join([
        h2("Sump pump repair in Oakland County, Michigan"),
        p(
            "A sump pump lifts groundwater "
            "out of a pit. When the float sticks, the check valve fails, the discharge line freezes, or "
            "the power drops, the pit overflows. Repairing that pump is a mechanical visit. Drying "
            "the carpet it ruined is water damage. The crew sets the price. "
            "A dead pump is not the same problem as a sewer backup. Say which one you have so the right company comes."
        ),
        h2("What a pump visit can and cannot fix"),
        p(
            "A technician can replace a failed pump, a stuck switch, or a check valve that lets water fall "
            "back into the crock. That visit does not remove sewage that came up a floor drain, and it does "
            "not dry a finished room. If the floor is already wet from the pit, open "
            + a("/flooded-basement-cleanup", "flooded basement cleanup")
            + " as well. If the water smells like sewage or a basement toilet burped, the pump is the wrong "
            "first call. Start with " + a("/sewer-backup-cleanup", "sewer backup cleanup") + ". "
            "Call " + phone_link() + " and say whether the crock overflowed or a drain did."
        ),
        h3("Power and discharge, without a parts list"),
        p(
            "During a storm, do not step into the pit or grab a submerged cord. If the pump died because "
            "the house lost power, deal with the utility outage first. The " + _CHECK
            + " includes DTE's outage line next to city sewer numbers. A discharge line that freezes or "
            "disconnects at the wall will send water back into the basement even when the motor runs. "
            "The crew should look at that line. The parts price and the labor rate come from that company."
        ),
        h2("Insurance and what to record"),
        p(
            "Overflow from groundwater is often treated differently from a sewer backup endorsement. "
            "Ask your insurer which one your form covers before you assume the visit is reimbursed. "
            "Photograph the pit, the water line on the wall, and any finished materials that got wet. "
            "Ask the crew for license and insurance. The warranty on the pump comes from that company. If you also believe a city main contributed "
            "sewage, the 45-day notice in the " + _GUIDE + " is a separate letter."
        ),
        p(
            "Royal Oak explains that when a house's sewer line is blocked by tree roots, disposable diapers or grease, water from the weeping tile around the basement walls can't drain either, and it comes in through wall cracks, the floor-wall seam, and most often the floor drain. "
            "Berkley and Clawson both describe their city sewers as gravity systems with no pumps, and Birmingham owns no sewage pump or lift stations, so the sump in your basement is the only pump in the picture."
        ),
        h2("Where the pits are"),
        p(
            "In " + a("/royal-oak-sump-pump-repair", "Royal Oak")
            + ", the city's Sewer Division is a "
            "different call from a pump repair. See the " + a("/royal-oak", "Royal Oak overview") + "."
        ),
        p(
            "In " + a("/troy-sump-pump-repair", "Troy")
            + ", pits often sit next to finished living space in houses largely from the 1960s and 1970s. "
            "See the " + a("/troy", "Troy overview") + "."
        ),
        p(
            a("/birmingham-sump-pump-repair", "Sump pump repair in Birmingham, Michigan")
            + " often means an older pit in an early- or mid-1900s house. The city owns no sewage pump or lift stations, so the sump "
            "is the homeowner's pump. See the "
            + a("/birmingham", "Birmingham overview") + "."
        ),
        p(
            "In " + a("/berkley-sump-pump-repair", "Berkley")
            + ", the pit sits in a short basement. The city's sewer is gravity, with no pumps or valves, "
            "so a household sump is a separate machine. See the " + a("/berkley", "Berkley overview") + "."
        ),
        p(
            "In " + a("/clawson-sump-pump-repair", "Clawson")
            + ", the pit often shares a small room with the furnace. See the " + a("/clawson", "Clawson overview") + "."
        ),
    ])


def sanit_hub():
    return "\n".join([
        h2("Basement sanitization after sewage or a contaminated flood"),
        p(
            "Sanitizing means cleaning what remains after sewage or foul floodwater has "
            "been removed and the ruined porous materials have been taken out. It is not a recurring "
            "maid service, and a fogger is not a substitute for throwing away a soaked pad. The company "
            "that extracted the water should say what product they will use and why the label fits that "
            "surface. A local crew does that cleaning. Call " + phone_link() + "."
        ),
        h2("What has to happen before a cleaner does any good"),
        p(
            "Extraction comes first. See " + a("/sewage-extraction", "sewage extraction")
            + ". Carpet pad, paper-faced drywall, and fiberglass that soaked up sewage are usually removed, "
            "not sprayed and left. What remains should be hard surfaces, framing that can be cleaned, and "
            "belongings you are willing to discard or that a restorer says can be kept. Fogging a room that "
            "still has a wet pad does not finish the job. If the loss never involved contaminated water, "
            "you may not need a sanitizing visit at all. Storm-water drying is "
            + a("/water-damage-restoration", "water damage restoration") + "."
        ),
        h3("Safety with products"),
        p(
            "Do not mix household bleach with ammonia or with any acid cleaner. Do not run a fogger in a "
            "room you cannot ventilate, and do not ask children or pets to wait inside while it runs. "
            "The crew should name the product and the surfaces. If you want a second opinion on the "
            "scope, ask for it in writing before work starts."
        ),
        p(
            "A room is not finished because the smell dropped. Sewage odor can fade while residue is still "
            "in the tack strip, the sill plate, or the back of a baseboard that was left in place. Ask the "
            "company which of those they will open or remove, and how they will know the remaining wood is "
            "ready to close up. If the structure is still wet, that question belongs on "
            + a("/water-damage-restoration", "water damage restoration")
            + ", not on a second spray of the same chemical. Air the house before anyone sleeps in the "
            "basement. Ask the company on site when the room is ready to use again."
        ),
        h2("Documentation, insurance, and the city letter"),
        p(
            "Photograph residue and the materials that were removed. Keep the list. Insurers often treat "
            "sewer backup as an endorsement, not as automatic dwelling coverage. Ask your carrier. "
            "A city claim, if the public system was involved, still needs the written notice in the "
            + _GUIDE + " within 45 days of discovery. Sanitizing the basement does not pause that clock. "
            "The " + _CHECK + " is for the next storm. The " + _GWK
            + " page explains the regional combined flow behind many of these backups."
        ),
        p(
            "Royal Oak's flood page links cleanup and sanitizing procedures, 'Cleaning Up the Mess After Basement Flooding', drafted by the Michigan Municipal Risk Management Authority's Public Works advisory committee. "
            "Part of Birmingham drains to the George W. Kuhn district, where wet-weather flow in the shared pipes is typically more than 93 percent stormwater, so what comes up a floor drain in a storm is diluted but still sewage."
        ),
        h2("Leftover problems, city by city"),
        p(
            a("/royal-oak-basement-sanitization", "Basement sanitization in Royal Oak")
            + " usually follows a floor-drain backup, and Royal Oak's Sewer Division "
            "answers for the public main. See the " + a("/royal-oak", "Royal Oak overview") + "."
        ),
        p(
            a("/troy-basement-sanitization", "Basement sanitization in Troy")
            + " often means carpet, pad, and contents in finished rooms of 1960s and 1970s houses. See the "
            + a("/troy", "Troy overview") + "."
        ),
        p(
            a("/birmingham-basement-sanitization", "Basement sanitization in Birmingham")
            + " has to deal with plaster and wood trim in early- and mid-1900s houses, and some of it will not survive a wipe-down. "
            "See the " + a("/birmingham", "Birmingham overview") + "."
        ),
        p(
            a("/berkley-basement-sanitization", "Basement sanitization in Berkley, MI")
            + " happens in a short basement on a combined sewer, often with the stair opening near the living room. "
            "See the " + a("/berkley", "Berkley overview") + "."
        ),
        p(
            a("/clawson-basement-sanitization", "Basement sanitization in Clawson")
            + " often covers a single room that also holds the furnace and the water heater. See the "
            + a("/clawson", "Clawson overview") + "."
        ),
    ])


def city_royal_oak():
    return "\n".join([
        h2("Royal Oak's sewer main: which pipe is the city's"),
        p(
            "The City of Royal Oak Sewer Division says it maintains about 300 miles of sanitary and storm sewers. "
            "For basement water, the city lists (248) 246-3300 on weekdays from 7:30 a.m. to 4:00 p.m. After hours, "
            "the police non-emergency number (248) 246-3500 dispatches sewer personnel. The city is responsible for "
            "the main. The homeowner is responsible for the lateral up to and including the connection to that main."
        ),
        p(
            "Call (248) 246-3300 when the city should look at the main, especially while water is still coming in. "
            "Call " + phone_link()
            + " for a local crew to pump or dry the house. While you wait, stop using water, keep people "
            "and pets out, and leave the basement if water is near the furnace."
        ),
        h2("Twelve Towns, then the George W. Kuhn basin"),
        p(
            "Royal Oak's flood-response page says the city is a member of the former Twelve Towns program, now the "
            "George W. Kuhn Retention Treatment Basin, and that the basin was expanded in 2006. "
            "The regional storage for this system is the George W. Kuhn Retention Treatment Basin, under the I-75 overpass at 12 Mile Road in Madison Heights, which can hold and treat 150 million gallons. "
            "In a heavy downpour, Royal Oak says street flooding is usually caused by debris sitting on the sewer grate, so clearing leaves and grass clippings off the grate in front of your house helps. "
            "Flooded streets during working hours (Monday–Friday, 7:30 a.m.–2:30 p.m.) go to the Department of Public Service at (248) 246-3300; the city says street water usually isn't handled after hours unless it is excessive. "
            "The basin's size "
            "and how much of its wet-weather flow is stormwater are on the "
            + _GWK + " page. Membership does not tell you whether the street main or your "
            "lateral failed today."
        ),
        h2("August 11, 2014, using the city's gauge and the federal declaration"),
        p(
            "FEMA-4195-DR, declared September 25, 2014, covered Macomb, Oakland, and Wayne counties for individual and "
            "public assistance. A National Weather Service paper describes about 4 to 6.5 inches in parts of those "
            "counties, most of it in about four hours on August 11. A report the next day said Royal Oak's DPS rain "
            "gauge recorded 4.98 inches that day, 1.12 inches of it in 30 minutes, as reported by Oakland County 115 the next day. "
            "No count of damaged houses is stated here."
        ),
        h2("Older blocks, and which problem you have"),
        p(
            "Royal Oak's residential blocks run off Main and Washington, along Woodward, and toward West Ten Mile."
        ),
        p(
            "If sewage came through a floor drain, a basement toilet, or a laundry standpipe, open "
            + a("/royal-oak-sewer-cleanup", "sewer backup cleanup in Royal Oak")
            + ". The pumping step, once you have hired someone, is "
            + a("/royal-oak-sewage-extraction", "sewage extraction in Royal Oak")
            + ". Storm water, a window well, or a sump, with the drains quiet, is "
            + a("/royal-oak-flooded-basement", "flooded basement cleanup in Royal Oak")
            + ". Drying and the decision about finishes are "
            + a("/royal-oak-water-damage-restoration", "water damage restoration in Royal Oak")
            + ". The pit itself is "
            + a("/royal-oak-sump-pump-repair", "sump pump repair in Royal Oak")
            + ". Cleaning after sewage has been removed is "
            + a("/royal-oak-basement-sanitization", "basement sanitization in Royal Oak") + "."
        ),
        h2("Insurance paperwork and the 45-day letter"),
        p(
            "Photograph the drain before anything is thrown away. Ask your insurer about a sewer-backup endorsement. "
            "The crew sets the scope and the price, and you confirm that company's license and insurance. A claim "
            "against the city is not the same call as " + PHONE_DISPLAY
            + ". The 45-day written notice is in the " + _GUIDE + ". The " + _CHECK
            + " already lists (248) 246-3300 for the next storm."
        ),
        h2("Neighboring cities use different sewer rules"),
        p(
            "Berkley publishes a single combined pipe. Troy splits flow across three districts. Birmingham's system "
            "is gravity with no city pump stations. Clawson's after-hours line is Troy dispatch, not Royal Oak police. "
            "Open the overview for the city where the house stands: "
            + a("/berkley", "Berkley") + ", " + a("/troy", "Troy") + ", "
            + a("/birmingham", "Birmingham") + ", and " + a("/clawson", "Clawson") + "."
        ),
        sources([
            ("https://www.romi.gov/384/Sewer-Division", "Royal Oak Sewer Division"),
            ("https://www.romi.gov/386/Responding-to-Street-Basement-Flooding", "Royal Oak basement flooding page"),
            (GWK_PDF, "Oakland County WRC letter, December 13, 2022"),
            (GWK_RTB, "George W. Kuhn Retention Treatment Basin"),
            (FEMA_2014, "Federal Register notice for FEMA-4195-DR"),
            (NWS_2014, "NWS paper on the August 11, 2014 rainfall"),
            ("https://oaklandcounty115.com/2014/08/12/royal-oak-flooding-information/", "August 12, 2014 report quoting the Royal Oak DPS rain gauge"),
        ]),
    ])


def city_troy():
    return "\n".join([
        h2("Troy discharges through three districts"),
        p(
            "A Troy City Council agenda item from November 14, 2022, states that Troy discharges wastewater through "
            "three districts: Evergreen-Farmington, Oakland-Troy, and the George W. Kuhn Drainage District, and that "
            "the Oakland County Water Resources Commissioner is responsible for those district facilities. "
            "So Troy is neither fully combined nor fully separated. One subdivision can sit in a different district from the next. Ask the city "
            "which district serves the address before anyone theorizes about the pipe in the street."
        ),
        p(
            "The " + _GWK + " page covers the regional basin: 14 communities, about 24,500 acres upstream of the Red Run "
            "Drain, dry-weather flow to Detroit, and wet-weather flow that is typically more than 93 percent stormwater. "
            "Troy is one of the communities in that district. The other two districts are not that basin. Do not paste "
            "the Kuhn description onto an Evergreen-Farmington address."
        ),
        h2("The backup number Troy publishes, and the claim that follows"),
        p(
            "Troy tells residents to report an overflow or backup to the Water Division at 248-524-3370 during business "
            "hours. After hours, the city lists Troy Police at 248-524-3477. A written claim goes to the City Attorney's "
            "Office, and state law sets 45 days from discovery. The form, the photos, and the deadline are in the "
            + _GUIDE + ". The claim goes to the city. A local cleanup crew handles the basement."
        ),
        p(
            "For pumping, drying, or cleanup inside the house, call " + phone_link()
            + " and describe the room: finished lower level, carpet, and whether a drain backed up."
        ),
        h2("Houses from the 1960s and 1970s"),
        p(
            "Troy's housing is largely from the 1960s and 1970s. The wet basements are in those houses. A finished "
            "lower level holds carpet even when the water looks shallow."
        ),
        h2("Match the water to the right Troy help"),
        p(
            "Sewage at a floor drain or basement bath is "
            + a("/troy-sewer-cleanup", "sewage cleanup in Troy")
            + ". Pumping that water out is "
            + a("/troy-sewage-extraction", "sewage extraction in Troy")
            + ". A carpeted lower level wet from a storm or a sump, with drains that stayed quiet, is "
            + a("/troy-flooded-basement", "flooded basement cleanup in Troy")
            + ". Drying after the water is gone is "
            + a("/troy-water-damage-restoration", "water damage restoration in Troy")
            + ". A dead pump in a finished room is "
            + a("/troy-sump-pump-repair", "sump pump repair in Troy")
            + ". Residue on contents after sewage is "
            + a("/troy-basement-sanitization", "basement sanitization in Troy") + "."
        ),
        h2("Photos, the policy, and what not to do upstairs"),
        p(
            "Stop running water. Keep people and pets off the lower level. Do not snake a drain that is producing sewage. "
            "Leave the room if water is near outlets. Photograph the water before carpet is pulled. Ask the insurer whether "
            "sewer backup is endorsed and whether groundwater is covered. Those are different questions. The crew "
            "should give you a written scope. You check their license and insurance yourself. The "
            + _CHECK + " is the sheet to print before the next storm, with Troy's numbers already on it."
        ),
        h2("If the house is not actually in Troy"),
        p(
            "A mile road or a freeway is easy to use as shorthand and easy to get wrong at the city limit. Birmingham's "
            "sewers are a gravity system with no city pump stations, and the city posts a separate water-event line that "
            "is not a claim. Clawson contracts Troy Police for dispatch, so the non-emergency number looks familiar, but "
            "Clawson adds extension 1 and its weekday DPW hours are not Troy's Water Division. Royal Oak's after-hours "
            "sewer dispatch is Royal Oak police, (248) 246-3500, not 248-524-3477. Start at "
            + a("/birmingham", "Birmingham") + ", " + a("/clawson", "Clawson") + ", or "
            + a("/royal-oak", "Royal Oak") + " if that is where the house stands. Berkley, on a single combined pipe, has its own page."
        ),
        sources([
            ("https://apps.troymi.gov/Meetings/Meetings/DownloadPDF/5548482", "Troy City Council agenda PDF, November 14, 2022 (three districts)"),
            ("https://troymi.gov/departments/public_works/water_and_sewer/legal_claims.php", "Troy legal claims for overflows and backups"),
            (GWK_PDF, "Oakland County WRC letter on the GWK district, December 2022"),
            (GWK_RTB, "Oakland County: George W. Kuhn Retention Treatment Basin"),
        ]),
    ])


def city_birmingham():
    return "\n".join([
        h2("Birmingham's sewers are gravity, and the city owns no pump stations"),
        p(
            "Birmingham's Risk Management FAQ says older communities have combined sewer and storm systems. A late-1990s "
            "bond financed relief sewers in part of the city, not a claim that every street was separated. The city says "
            "combined and storm sewers were historically designed for about 2 inches of rain in one hour, which it calls "
            "a 10-year storm. The system is gravity. Birmingham owns no sewage pump or lift stations. If a basement backs "
            "up, it is not because a municipal lift station lost power. There isn't one."
        ),
        p(
            "Birmingham housing is largely early- to mid-1900s: plaster, trim, and older laterals around Shain Park and "
            "Old Woodward, Maple Road, Poppleton Park, and Quarton Lake."
        ),
        h2("What the city tells homeowners to change at the house"),
        p(
            "The same FAQ lists homeowner measures: a backflow preventer, downspouts disconnected from the sewer and "
            "extended about 6 feet from the foundation, and soil graded away from the house. Those are the city's "
            "suggestions for the private side. They are not a cleanup. They also do not replace a call while water is "
            "in the basement. A backflow preventer and a downspout check are separate hires from the cleanup call."
        ),
        h2("The water-event line is not the claim line"),
        p(
            "Birmingham's water event notification line is (248) 530-1703. The city uses it to collect flooding data. "
            "It is not a sewer backup claim. Questions about claims go to 248.530.1808. The city says claims are handled "
            "through the Michigan Municipal League Liability and Property Pool and Meadowbrook Claims Service. State law "
            "still requires written notice within 45 days of discovery. The city's claim form lives on the city's site. The "
            + _GUIDE + " explains the deadline and what to document. "
            "Call " + phone_link() + " for a local cleanup crew."
        ),
        h3("August 24, 2023"),
        p(
            "The city posted an engineer presentation about the August 24, 2023 rain. Read the presentation on the city's Risk Management page for the city's own figures. Regional context for the combined district Birmingham belongs to is the " + _GWK + " page."
        ),
        h2("Which Birmingham service matches the basement"),
        p(
            "A drain backup in an older house starts at "
            + a("/birmingham-sewer-cleanup", "sewer backup cleanup in Birmingham")
            + ". Contaminated water already inside is "
            + a("/birmingham-sewage-extraction", "sewage extraction in Birmingham")
            + ". Storm water and basement water removal are "
            + a("/birmingham-flooded-basement", "flooded basement cleanup in Birmingham")
            + ". Plaster, trim, or finishes that have to be dried or opened are "
            + a("/birmingham-water-damage-restoration", "water damage restoration in Birmingham")
            + ". A household sump, which is not a city pump station, is "
            + a("/birmingham-sump-pump-repair", "sump pump repair in Birmingham, Michigan")
            + ". Cleaning after sewage, with plaster that may not survive a wipe-down, is "
            + a("/birmingham-basement-sanitization", "basement sanitization in Birmingham") + "."
        ),
        h2("Records to keep, and the hazard in the stair"),
        p(
            "Keep people out. Do not cut out wet plaster or drywall before the crew has seen it. "
            "Sewage-soaked material is contaminated, and opening walls can spread it. Photograph rooms first. "
            "Ask the insurer about a sewer-backup endorsement. Ask the crew for a written scope, the price, "
            "and proof of license and insurance. A local crew does the work. The "
            + _CHECK + " is the printable list for the next storm, including (248) 530-1703 so it is not confused "
            "with the claims number."
        ),
        h2("Nearby cities have their own sewer contacts"),
        p(
            "Royal Oak has its own Sewer Division, and there the homeowner owns the lateral up to and including "
            "the connection. Troy's wastewater leaves through three districts, and Troy has its own backup numbers. "
            "Berkley's sewer is also combined and gravity, and Berkley publishes a lining program and street storage "
            "that Birmingham's FAQ does not describe. If the house is in "
            + a("/royal-oak", "Royal Oak") + ", " + a("/troy", "Troy") + ", "
            + a("/berkley", "Berkley") + ", or " + a("/clawson", "Clawson") + ", open that city's page."
        ),
        sources([
            ("https://www.bhamgov.org/about_birmingham/city_departments/city_manager/risk_management.php", "Birmingham Risk Management: sewer FAQ, phones, and the August 24, 2023 presentation"),
            (GWK_PDF, "Oakland County WRC letter listing Birmingham in the GWK district"),
            (GWK_RTB, "Oakland County: George W. Kuhn Retention Treatment Basin"),
        ]),
    ])


def city_berkley():
    return "\n".join([
        h2("Berkley's sewer is one combined pipe, and it is all gravity"),
        p(
            "Berkley's flood-tips page describes a combined sewer system: a single pipe for stormwater and sewage, "
            "entirely gravity-based, with no pumps and no valves. Streets are designed to hold water so that flow "
            "enters the pipe more slowly. Restrictor covers in catch basins are part of that design. Ponding at the "
            "curb during a hard rain is something the city describes on purpose. It is not, by itself, a sign that something in the system failed."
        ),
        p(
            "The city says it spends up to 800,000 dollars a year on structural lining, and that about 35 percent of "
            "the system has been lined over more than 20 years. Lining is city work on the city's pipe; it does not clean a basement that has already taken water."
        ),
        h2("Flow leaves toward the Clinton, not the Rouge"),
        p(
            "Berkley's wastewater in this system moves toward the Clinton River side: the George W. Kuhn district, "
            "then the Red Run Drain, then the Clinton. It does not go to the Rouge. Berkley is one of the 14 communities "
            "the district serves, across the 24,500 acres upstream of the Red Run. The district explanation, including "
            "why wet-weather flow is typically more than 93 percent stormwater, is the " + _GWK
            + " page. Ask the city about a specific block if you need the pipe in front of the house confirmed."
        ),
        h2("Who to call in Berkley while the basement is wet"),
        p(
            "Berkley says to report basement flooding to Public Works at 248-658-3490, and it posts a Sewer Backup "
            "Claims Form. Written notice under state law is due within 45 days of discovery. The " + _GUIDE
            + " walks through that letter. It is not the same step as hiring a cleanup company. For the company, call "
            + phone_link() + "."
        ),
        h2("Older homes, and the help that fits"),
        p(
            "Berkley is a small city of older homes. Downtown runs along 12 Mile Road. Coolidge "
            "is the main north-south road. The city designs its streets to hold water during a hard rain. Basements are short, "
            "and the stair lands close to first-floor living space. A household vac on sewage water on that stair is "
            "how contamination reaches the room upstairs. Wait for a company equipped for it."
        ),
        p(
            "Sewage at a floor drain: " + a("/berkley-sewer-cleanup", "sewage cleanup in Berkley")
            + ". The pumping step: " + a("/berkley-sewage-extraction", "sewage extraction in Berkley")
            + ". Window wells, stairwells, and storm water with quiet drains: "
            + a("/berkley-flooded-basement", "flooded basement cleanup in Berkley")
            + ". Joists and first-floor hardwood that got wet from below: "
            + a("/berkley-water-damage-restoration", "water damage restoration in Berkley")
            + ". A sump in a low basement: "
            + a("/berkley-sump-pump-repair", "sump pump repair in Berkley")
            + ". Cleaning a small air volume after sewage: "
            + a("/berkley-basement-sanitization", "basement sanitization in Berkley") + "."
        ),
        h2("What to keep for your insurer"),
        p(
            "Ask your insurer whether sewer backup is endorsed. A combined system that surcharges in the rain is the "
            "situation those endorsements are written for, but the endorsement still has to be on your form. Photograph "
            "the drain, the stair, and the water line. Keep a list of what is discarded. The crew's written scope "
            "is the document that should match that list. Ask the company for license and insurance. Print the " + _CHECK + " before spring storms. It already includes 248-658-3490."
        ),
        h2("The next city over uses a different sewer"),
        p(
            "Royal Oak's Sewer Division describes hundreds of miles of sanitary and storm sewers and a lateral the "
            "homeowner owns through the connection. Birmingham is gravity as well, but its FAQ talks about a design "
            "storm of about 2 inches in an hour, relief sewers from a late-1990s bond, and no city pump stations, "
            "plus a water-event line that Berkley does not use. Do not swap the phone numbers. Overviews: "
            + a("/royal-oak", "Royal Oak") + ", " + a("/birmingham", "Birmingham") + ", "
            + a("/troy", "Troy") + ", and " + a("/clawson", "Clawson") + "."
        ),
        sources([
            ("https://www.berkleymi.gov/public-works/flood-tips-for-residents", "Berkley flood tips for residents (combined sewer, lining, restrictors, Public Works phone)"),
            (GWK_PDF, "Oakland County WRC letter listing Berkley in the GWK district and the Clinton River path"),
            (GWK_RTB, "Oakland County: George W. Kuhn Retention Treatment Basin"),
        ]),
    ])


def city_clawson():
    return "\n".join([
        h2("What Clawson's sewer page tells residents to read"),
        p(
            "The City of Clawson sewer page lists the George W. Kuhn Retention Treatment Basin and the Oakland County "
            "Water Resources Commissioner. It links a combined-sewer explainer and Public Act 222, the state sewage-backup "
            "statute. Ask the city which pipe serves your street. The regional district those links point at, including the 14 communities and "
            "the Red Run Drain, is summarized on the " + _GWK + " page."
        ),
        p(
            "The city main line published on that sewer page is (248) 435-4500. Public works hours are Monday through "
            "Thursday, 7:00 a.m. to 3:30 p.m., and the department is closed on Fridays."
        ),
        h2("After hours, Clawson uses Troy Police dispatch"),
        p(
            "Clawson contracts with Troy Police for dispatch. The non-emergency number Clawson publishes is 248-524-3477, "
            "extension 1. That contract does not make Clawson's sewers part of Troy's three wastewater districts, and it "
            "does not make Troy's Water Division at 248-524-3370 the Clawson backup desk. Use the extension Clawson lists. "
            "On a Friday, when DPW is closed, that dispatch line is the after-hours path the city has described. It is the city's line, separate from a cleanup company."
        ),
        p(
            "For cleanup inside the house, call " + phone_link()
            + ". The price comes from that company."
        ),
        h2("Small lots, one-room basements, and the matching help"),
        p(
            "Clawson is largely older homes on compact "
            "lots. 14 Mile Road is the downtown street. The city sits between Royal Oak and Troy. Basements are often a "
            "single room that holds the furnace, the water heater, and the floor drain. A backup in that room is also an "
            "electrical and heating problem. Stay out if water is near the furnace or the panel."
        ),
        p(
            "A backup starts at " + a("/clawson-sewer-cleanup", "sewage cleanup in Clawson")
            + ". Limited access for hoses is " + a("/clawson-sewage-extraction", "sewage extraction in Clawson")
            + ". Water in the mechanical room from a storm or a sump, rather than a drain, is "
            + a("/clawson-flooded-basement", "flooded basement cleanup in Clawson")
            + ". Drying after extraction is "
            + a("/clawson-water-damage-restoration", "water damage restoration in Clawson")
            + ". The pit beside the furnace, with no published price, is "
            + a("/clawson-sump-pump-repair", "sump pump repair in Clawson")
            + ". Keeping residue off the only stair is "
            + a("/clawson-basement-sanitization", "basement sanitization in Clawson") + "."
        ),
        h2("The 45-day notice, and the insurance question beside it"),
        p(
            "Public Act 222 is why the city links the statute. Written notice is due within 45 days of discovering the "
            "damage if you want a government claim to remain possible. How to write it, and what Clawson has posted, is "
            "in the " + _GUIDE + ". Your homeowners policy is a separate question: sewer backup is often excluded "
            "without an endorsement. Ask the insurer. Photograph the room before the furnace is moved or the pad is "
            "thrown out. The crew's license and insurance are yours to verify. The " + _CHECK
            + " is worth printing because Friday closures and the dispatch extension are easy to forget during a storm."
        ),
        h2("Royal Oak and Troy are the neighbors, not the same phone tree"),
        p(
            "Royal Oak's basement-water line is (248) 246-3300 on weekdays and Royal Oak police non-emergency after hours, "
            "and Royal Oak states that the homeowner owns the lateral through the connection. Troy's backup line is the "
            "Water Division, and Troy's wastewater leaves through Evergreen-Farmington, Oakland-Troy, and George W. Kuhn. "
            "Sharing a dispatch contractor with Troy does not put a Clawson house into those districts. Open "
            + a("/royal-oak", "Royal Oak") + " or " + a("/troy", "Troy") + " only when the house is in that city. "
            "Birmingham and Berkley are " + a("/birmingham", "Birmingham") + " and " + a("/berkley", "Berkley") + "."
        ),
        sources([
            ("https://www.cityofclawson.com/your_government/dpw_and_engineering/sewer.php", "Clawson sewer page (GWK, WRC, main line, DPW hours)"),
            ("https://www.cityofclawson.com/your_government/police_department/dispatch_services.php", "Clawson dispatch services (Troy Police contract, non-emergency extension)"),
            (GWK_RTB, "Oakland County: George W. Kuhn Retention Treatment Basin"),
            (GWK_PDF, "Oakland County WRC letter listing Clawson among GWK communities"),
        ]),
    ])


CITY_ARTICLES = {
    "royal-oak": city_royal_oak,
    "troy": city_troy,
    "birmingham": city_birmingham,
    "berkley": city_berkley,
    "clawson": city_clawson,
}

CITY_H1 = {
    "royal-oak": "Royal Oak sewer main, lateral, and basement water help",
    "troy": "Troy wastewater districts and basement water help",
    "birmingham": "Birmingham gravity sewers and basement water help",
    "berkley": "Berkley combined sewer and basement help",
    "clawson": "Clawson sewer calls and basement water help",
}

CITY_HERO = {
    "royal-oak": "Royal Oak's Sewer Division maintains about 300 miles of public sewer and publishes the basement-water number. For the cleanup inside the house, a local cleanup crew handles the visit, and they'll tell you when they can be there.",
    "troy": "Troy discharges wastewater through three districts, not one system you can label combined or separated. For basement water in a 1960s or 1970s house, a local cleanup crew handles the visit, and they'll tell you when they can be there. Troy's Water Division is a different number, listed below.",
    "birmingham": "Birmingham's sewers are gravity, and the city owns no pump or lift stations. Older areas are combined. If the lower level is wet, a local cleanup crew handles the visit, and they'll tell you when they can be there.",
    "berkley": "Berkley's sewer is a single combined pipe, entirely gravity, with no city pumps or valves. If the basement is wet, a local cleanup crew handles the visit, and they'll tell you when they can be there.",
    "clawson": "Clawson's sewer page points to the George W. Kuhn basin, and after-hours police calls go to Troy dispatch. For the basement itself, a local cleanup crew handles the visit, and they'll tell you when they can be there.",
}

CITY_DESC = {
    "royal-oak": "Royal Oak, MI sewer backup and flooded basement help: city sewer numbers, who owns the lateral, and a local cleanup crew. Call (248) 825-8312.",
    "troy": "Troy, MI sewer backup and flooded basement help: city numbers, the three wastewater districts, and a local cleanup crew. Call (248) 825-8312.",
    "birmingham": "Birmingham, MI sewer backup and flooded basement help for older homes. The city numbers to call, plus a local cleanup crew at (248) 825-8312.",
    "berkley": "Berkley, MI sewer backup and flooded basement help. The city's combined sewer can back up in hard rain. Reach a local cleanup crew: (248) 825-8312.",
    "clawson": "Clawson, MI sewer backup and flooded basement help: city sewer numbers, after-hours dispatch, and a local cleanup crew. Call (248) 825-8312.",
}

CITY_FAQS = {
    "royal-oak": [
        ("Which number does Royal Oak use for the city sewer?", "(248) 246-3300 on weekdays, 7:30 a.m. to 4:00 p.m. After hours, the police non-emergency line (248) 246-3500 dispatches sewer personnel. The city checks the main in the street." + cite("City of Royal Oak, Responding to Street and Basement Flooding", RO_FLOOD)),
        (
            "Is the pipe from my Royal Oak house to the street mine?",
            "Yes, up to and including the connection to the main. The city is responsible for the main. A cleanup company should not guess which pipe failed. A plumber's camera inspection checks a specific lateral." + cite("City of Royal Oak Sewer Division", RO_SEWER),
        ),
        (
            "Did the August 2014 federal disaster declaration include Oakland County?",
            "Yes. FEMA-4195-DR was declared September 25, 2014, for Macomb, Oakland, and Wayne counties. A next-day report said Royal Oak's DPS gauge recorded 4.98 inches on August 11, with 1.12 inches in 30 minutes, as reported by Oakland County 115. The reports do not give a count of damaged homes." + cite("Oakland County 115, August 12, 2014", RO_115) + cite("Federal Register, FEMA-4195-DR", FEMA_2014),
        ),
        (
            "What cleanup do I need if the Royal Oak floor drain never moved?",
            "Open flooded basement cleanup when the water is from a storm, a window well, or a sump. Open water damage restoration if finishes are already soaked. Open sewer backup cleanup only when sewage came up through a drain, a basement toilet, or a laundry standpipe.",
        ),
        ("Does the George W. Kuhn basin keep my Royal Oak basement dry?", "Not by itself. Royal Oak's flood-response page says the city is in the former Twelve Towns program, now the George W. Kuhn Retention Treatment Basin, expanded in 2006. That does not tell you whether your lateral or the street main failed. If you believe the city is involved, send written notice within 45 days of discovery." + cite("City of Royal Oak, Responding to Street and Basement Flooding", RO_FLOOD) + cite("Michigan Legislature, MCL 691.1419", MCL1419)),
    ],
    "troy": [
        (
            "Is Troy in the George W. Kuhn district?",
            "Partly. George W. Kuhn is one of three districts Troy discharges wastewater through, along with Evergreen-Farmington and Oakland-Troy, and the Oakland County Water Resources Commissioner is responsible for those facilities. Ask the Water Division, 248-524-3370, which one serves your address." + cite("Troy City Council agenda, November 14, 2022", TROY_AGENDA),
        ),
        ("What number does Troy publish for a sewer backup?", "The Water Division, 248-524-3370, during business hours. After hours, Troy Police at 248-524-3477." + cite("City of Troy, Legal Claims for Overflows and Backups", TROY_CLAIMS)),
        ("How do I send Troy's written sewer claim?", "To the City Attorney's Office by email, mail, fax (248-524-3259), or drop-off, within 45 days of discovery. The city's page links a Notice of Sewer Backup Claim form." + cite("City of Troy, Legal Claims for Overflows and Backups", TROY_CLAIMS)),
        (
            "What help fits a wet Troy lower level if the drains stayed quiet?",
            "Flooded basement cleanup for the water removal, water damage restoration if carpet and finishes have to be dried, and sump pump repair if the pit is what failed. Sewer backup cleanup is for sewage that came out of a drain.",
        ),
        ("Why does Clawson use the same after-hours number as Troy?", "Clawson contracts Troy Police for dispatch. Troy residents call Troy Police at 248-524-3477 after hours for a backup; Clawson residents use the same number with extension 1. Troy's Water Division, 248-524-3370, is the business-hours line." + cite("City of Clawson, Sanitary and Storm Sewer System", CLAW_SEWER) + cite("City of Troy, Legal Claims for Overflows and Backups", TROY_CLAIMS)),
    ],
    "birmingham": [
        (
            "Does Birmingham run sewage pump stations?",
            "No. The city's Risk Management FAQ says the system is gravity and that the city owns no pump or lift stations. A sump in a house is the homeowner's pump, not a municipal station." + cite("City of Birmingham Risk Management", BHAM),
        ),
        (
            "Is (248) 530-1703 the claim line?",
            "No. That is the water event notification line for flooding data. Claims questions are 248.530.1808. The city says claims go through the MML Liability and Property Pool and Meadowbrook Claims Service. The water-event form is not a claim, and the 45-day written notice still applies." + cite("City of Birmingham Risk Management", BHAM) + cite("Michigan Legislature, MCL 691.1419", MCL1419),
        ),
        (
            "What rainfall were the older Birmingham sewers designed for?",
            "The city says combined and storm sewers were historically designed for about 2 inches of rain in one hour, which it calls a 10-year storm. A late-1990s bond financed relief sewers in part of the city. That is not a statement that every street was rebuilt." + cite("City of Birmingham Risk Management", BHAM),
        ),
        ("What does the city suggest homeowners do at the house?", "The FAQ lists a backflow preventer, downspouts disconnected and extended about 6 feet, and grading away from the foundation. Those prevent water; they do not remove water already inside. For that, call (248) 825-8312." + cite("City of Birmingham Risk Management", BHAM)),
        (
            "Where do Birmingham sewer claims get decided?",
            "The city says claims go to Meadowbrook Claims Service, the administrator for the Michigan Municipal League Liability and Property Pool, for a liability decision. Download the Sewer Backup Claim form from the city's Risk Management page; questions go to 248.530.1808. Written notice is due within 45 days of discovery." + cite("City of Birmingham Risk Management", BHAM) + cite("Michigan Legislature, MCL 691.1419", MCL1419),
        ),
    ],
    "berkley": [
        (
            "Does Berkley's sewer use pumps or valves?",
            "No. Berkley describes a single combined pipe for stormwater and sewage that is entirely gravity-based, with no pumps and no valves. Streets are designed to hold water, and catch basins use restrictor covers. Do not pry those covers off." + cite("City of Berkley, Flood Tips for Residents", BERK_TIPS),
        ),
        (
            "Does Berkley's flow go to the Rouge River?",
            "No. Flow from this system goes toward the Clinton River side, through the George W. Kuhn district and the Red Run Drain. Berkley is one of the communities that district serves." + cite("Oakland County Water Resources Commissioner, George W. Kuhn Retention Treatment Basin", WRC_GWK),
        ),
        ("What number does Berkley give for basement flooding?", "Public Works, 248-658-3490. The city also posts a Sewer Backup Claims Form. For cleanup inside the house, call (248) 825-8312." + cite("City of Berkley, Flood Tips for Residents", BERK_TIPS) + cite("City of Berkley, Report a Claim", BERK_CLAIM)),
        (
            "How much of Berkley's sewer has been lined?",
            "The city says about 35 percent of the system has been lined over more than 20 years, and that it spends up to 800,000 dollars a year on structural lining. That figure is the city's maintenance spending, not a cleanup price." + cite("City of Berkley, Flood Tips for Residents", BERK_TIPS),
        ),
        ("Does Berkley's sewer lining program protect my basement?", "Not directly. Berkley says it spends up to 800,000 dollars a year on structural lining and has lined about 35 percent of the system over more than 20 years. That is work on the city's pipe. Water already in your basement is a separate cleanup." + cite("City of Berkley, Flood Tips for Residents", BERK_TIPS)),
    ],
    "clawson": [
        (
            "What are Clawson DPW days for sewer questions?",
            "Monday through Thursday, 7:00 a.m. to 3:30 p.m. The department is closed on Fridays. The city main line listed on the sewer page is (248) 435-4500." + cite("City of Clawson, Sanitary and Storm Sewer System", CLAW_SEWER),
        ),
        (
            "Who answers Clawson's after-hours line?",
            "Clawson contracts Troy Police for dispatch. The non-emergency number is 248-524-3477, extension 1. That is not Troy's Water Division backup line, and it is not a city sewer crew." + cite("City of Clawson, Sanitary and Storm Sewer System", CLAW_SEWER),
        ),
        (
            "Does the Clawson sewer page mean every street is a combined sewer?",
            "The page links a combined-sewer explainer and lists the George W. Kuhn basin and the Oakland County Water Resources Commissioner. Ask the city which pipe serves a specific street." + cite("City of Clawson, Sanitary and Storm Sewer System", CLAW_SEWER),
        ),
        (
            "What help does a wet one-room Clawson basement need first?",
            "If sewage came up the floor drain, open sewer backup cleanup. If the furnace room is wet from a storm or a sump and the drain stayed quiet, open flooded basement cleanup. If you only need the pump looked at, open sump pump repair, and add water damage restoration if finishes are soaked.",
        ),
        ("Where does Clawson's sewer flow in a heavy storm?", "Clawson's sewer page points to the George W. Kuhn Retention Treatment Basin and the Oakland County Water Resources Commissioner. The basin, under I-75 at 12 Mile in Madison Heights, can hold and treat 150 million gallons and sends treated flow to the Red Run Drain." + cite("Oakland County Water Resources Commissioner, George W. Kuhn Retention Treatment Basin", WRC_GWK)),
    ],
}

HUB_FAQS = {
    "services": [
        ("Which job should I describe when I call?", "Whether the water came from a floor drain, a sump, or a storm, and your city. Ask the crew for proof of license and insurance and a written scope."),
        (
            "What kind of cleanup do I need?",
            "If sewage came up a drain, open sewer backup cleanup. If the water is storm or sump water and the drains stayed quiet, open flooded basement cleanup. If materials are already soaked, open water damage restoration. Then open the city page for the house.",
        ),
        (
            "Which Oakland County cities can I call about?",
            "Royal Oak, Troy, Birmingham, Berkley, and Clawson. Each has its own sewer description. Berkley's pipe is combined and gravity. Troy discharges through three districts. Birmingham's system is gravity with no city pump stations. Use the city where the house stands." + cite("City of Berkley, Flood Tips for Residents", BERK_TIPS) + cite("Troy City Council agenda, November 14, 2022", TROY_AGENDA) + cite("City of Birmingham Risk Management", BHAM),
        ),
        ("Is sewage extraction the same as sanitizing?", "No. Extraction pumps out the contaminated water and removes soaked material. Sanitizing cleans and disinfects what remains after the water is gone. After a sewer backup you usually need both, in that order."),
        (
            "Is the George W. Kuhn district the same as my city's sewer?",
            "It is the regional district upstream of the Red Run Drain. It serves all or part of 14 communities, including Berkley, Birmingham, Clawson, Royal Oak, and Troy, about 24,500 acres. It does not tell you whether the street main or your lateral failed today. Ask your city." + cite("Oakland County Water Resources Commissioner, George W. Kuhn Retention Treatment Basin", WRC_GWK),
        ),
    ],
    "water-damage-restoration": [
        ("What does water damage restoration include?", "Removing standing water, discarding porous materials that cannot be saved, and drying what remains. If the water came from a sewer drain, the cleanup is stricter: carpet pad, insulation, and swollen drywall usually come out."),
        (
            "Is sewage handled the same way as a supply-line leak?",
            "No. Sewage is heavily contaminated water. Carpet pad and wet drywall usually come out. A clean supply-line break can be a smaller scope.",
        ),
        (
            "Will insurance pay for the drying?",
            "Not automatically. Sewer backup is often an endorsement, and groundwater is often limited. Ask your insurer. The city letter, if you believe a public sewer caused the loss, is a separate 45-day written notice." + cite("Michigan Legislature, MCL 691.1419", MCL1419),
        ),
        (
            "Has Oakland County had a declared flood disaster?",
            "FEMA-4195-DR was declared September 25, 2014, for Macomb, Oakland, and Wayne counties, after storms on August 11 through 13. A National Weather Service paper describes about 4 to 6.5 inches in parts of those counties, mostly in about four hours. That is a county storm record, not a count of damaged houses." + cite("Federal Register, FEMA-4195-DR", FEMA_2014),
        ),
        ("What should I tell the crew about water damage?", "The city and whether the water came from a drain, a sump, or a storm. Ask for the drying plan and the price in writing before work starts."),
    ],
    "sewer-backup-cleanup": [
        (
            "What counts as a sewer backup?",
            "Wastewater that came up a floor drain, a basement toilet, or a laundry standpipe because the line was full. Storm water that never touched a drain is flooded basement cleanup.",
        ),
        (
            "Who fixes the public main?",
            "The city that owns it. Royal Oak, for example, says the city is responsible for the main and the homeowner for the lateral through the connection. Call the city number for that city. Call (248) 825-8312 for a cleanup company inside the house." + cite("City of Royal Oak Sewer Division", RO_SEWER),
        ),
        (
            "How long do I have to notify a city?",
            "Michigan law requires written notice within 45 days of discovering the damage before compensation for a sewage disposal event is possible. Include your name, address, and phone, the property address, the discovery date, and a brief description. You send that letter. The claim guide lists each city's contact." + cite("Michigan Legislature, MCL 691.1419", MCL1419),
        ),
        (
            "Why does heavy rain show up in Oakland County basements?",
            "In a combined system, sanitary sewage and stormwater share pipes. The George W. Kuhn district's wet-weather flow is typically more than 93 percent stormwater. The retention basin under the I-75 overpass at 12 Mile Road in Madison Heights can hold and treat 150 million gallons. Those figures describe the district, not a single house." + cite("Oakland County Water Resources Commissioner, George W. Kuhn Retention Treatment Basin", WRC_GWK),
        ),
        ("Is a sewer backup my pipe or the city's?", "It depends where the blockage is. The city generally handles the main in the street and the homeowner the lateral in the yard; Royal Oak says the homeowner's part runs up to and including the connection. If water is still coming in, call your city's sewer number so it can check the main." + cite("City of Royal Oak Sewer Division", RO_SEWER)),
    ],
    "sewage-extraction": [
        ("Can I shop-vac sewage myself?", "No. A household vac sprays contaminated water onto stairs, joists, and anyone standing nearby. Sewage needs pumps built for wastewater."),
        (
            "Does extraction include sanitizing?",
            "Pumping and removing soaked porous materials come first. Cleaning what remains is the basement sanitization page. A fogger is not a substitute for throwing away a soaked pad.",
        ),
        (
            "Where should the wastewater go?",
            "The crew should say where they will take it. Do not pump sewage into a street gutter or a storm drain yourself.",
        ),
        (
            "Should I call the city and an extraction company?",
            "Yes, if you suspect the public main. Royal Oak, for example, takes basement-water calls at (248) 246-3300 on weekdays. The extraction company removes water from the house. Call (248) 825-8312 to reach that company. They are not substitutes for each other." + cite("City of Royal Oak, Responding to Street and Basement Flooding", RO_FLOOD),
        ),
        (
            "Does pumping the basement file the 45-day notice?",
            "No. The clock starts when you discover the damage. The notice goes to the responsible government agency. Your insurer, and any sewer-backup endorsement, is a separate call." + cite("Michigan Legislature, MCL 691.1419", MCL1419),
        ),
    ],
    "flooded-basement-cleanup": [
        (
            "Is a sewage backup handled the same way as a storm flood?",
            "No. When sewage came up a drain, the job is sewer backup cleanup and sewage extraction. Flooded basement cleanup is for storm water, window wells, surface water, and sump overflows.",
        ),
        (
            "Did FEMA declare a disaster for the August 2014 storms?",
            "Yes. FEMA-4195-DR was declared September 25, 2014, for Macomb, Oakland, and Wayne counties. A National Weather Service paper describes about 4 to 6.5 inches in parts of those counties, mostly in about four hours. Those reports do not give a house-by-house damage count." + cite("Federal Register, FEMA-4195-DR", FEMA_2014),
        ),
        ("Who removes the water?", "A local cleanup crew with pumps and drying equipment. Call (248) 825-8312 and say your city and whether a drain was involved."),
        (
            "Does a flooded Oakland County basement always mean the George W. Kuhn district?",
            "No. The district serves all or part of Berkley, Birmingham, Clawson, Royal Oak, and Troy, among 14 communities, upstream of the Red Run Drain. A window well or a dead sump can flood a basement on a street that never surcharged. Describe what you saw." + cite("Oakland County Water Resources Commissioner, George W. Kuhn Retention Treatment Basin", WRC_GWK),
        ),
        (
            "What should I photograph before the water is pumped?",
            "The water line, the room, and whether a floor drain, a window well, or a sump was the source. That record helps your insurer. If the water was sewage from a public system, it also supports the 45-day written notice." + cite("Michigan Legislature, MCL 691.1419", MCL1419),
        ),
    ],
    "sump-pump-repair": [
        ("Can a failed sump pump cause a sewer backup?", "Not by itself. A sump lifts groundwater out of a pit; a sewer backup comes up a floor drain or fixture. In a storm both can happen at once. If the water smells like sewage, treat all of it as sewage."),
        (
            "Does Birmingham, Michigan, operate city sewage pump stations?",
            "No. Birmingham says its sewer system is gravity and that the city owns no pump or lift stations. A sump in a Birmingham basement is the homeowner's equipment." + cite("City of Birmingham Risk Management", BHAM),
        ),
        (
            "The pump ran but the floor is still wet. What help do I need?",
            "Two jobs: sump pump repair for the machine, and flooded basement cleanup or water damage restoration for the water and the finishes. If a drain produced sewage, treat it as a sewer backup instead.",
        ),
        (
            "Does Berkley's city sewer include my sump pump?",
            "No. Berkley describes its municipal sewer as gravity, with no pumps and no valves. A household sump is a private machine in the basement. If the floor drain also backed up, that combined pipe is a city call to Public Works at 248-658-3490." + cite("City of Berkley, Flood Tips for Residents", BERK_TIPS),
        ),
        ("What should I do when the sump pump stops?", "Do not step into water near outlets or the panel. From a dry step, check whether the pit is overflowing and whether the floor drain is involved. Clear overflow needs the pump fixed and the water removed; drain water is sewage. Call (248) 825-8312."),
    ],
    "basement-sanitization": [
        (
            "Is sanitizing a regular cleaning visit?",
            "No. It is cleaning after sewage or foul floodwater, once the water and the ruined porous materials are gone. It is not a maid service.",
        ),
        (
            "Can I fog the room and keep the carpet pad?",
            "A soaked pad that took up sewage should come out. Fogging over it does not finish the job. The company on site should say what stays and what goes.",
        ),
        (
            "Does cleaning the basement extend the 45-day notice deadline?",
            "No. The written notice to the responsible agency runs from discovery of the damage. The claim guide explains the contents. Sanitizing is a separate hire." + cite("Michigan Legislature, MCL 691.1419", MCL1419),
        ),
        (
            "Should sewage residue in a combined-sewer city be cleaned like rainwater?",
            "No. Berkley, for example, describes a single pipe for stormwater and sewage. If that pipe pushed wastewater into the basement, treat the residue as sewage. Birmingham's FAQ says its older areas are combined too." + cite("City of Berkley, Flood Tips for Residents", BERK_TIPS) + cite("City of Birmingham Risk Management", BHAM),
        ),
        ("What should I ask before a basement is sanitized?", "Ask what they will throw away, what product they will use, and which surfaces they will treat. If standing sewage is still on the floor, extraction comes first."),
    ],
}
