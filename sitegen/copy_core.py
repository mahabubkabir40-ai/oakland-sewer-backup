"""Home, contact, about, privacy, terms, thank-you, and 404 copy."""

from site_config import BRAND, PHONE_DISPLAY, PHONE_TEL
from sitegen.render import a, h2, h3, p

def about_article():
    return "\n".join([
        h2("Who handles the cleanup"),
        p(
            f"{BRAND} is a referral line: we connect you with an independent local company, and that crew does the cleanup. "
            "Homeowners in Royal Oak, Troy, Birmingham, Berkley, and Clawson call for sewer backup cleanup, sewage extraction, "
            "flooded basement cleanup, water damage restoration, sump pump repair, and sanitizing after a flood or sewage "
            "backup. The crew brings the truck, and they'll tell you when they can be there."
        ),
        h2("What happens when you call"),
        p(
            f"You dial {PHONE_DISPLAY}. Say the city and whether the water came from a drain, a sump, or a storm."
        ),
        h2("What you still have to verify"),
        p(
            "Before work starts, ask the crew for the license and insurance the job requires, "
            "and for a written scope. The price comes from the crew. Insurance coverage for sewer backup or water "
            "damage is a question for your insurer. Your claim stays between you and your carrier."
        ),
        h2("No public office"),
        p(
            f"{BRAND} has no public office and no dispatch hub in Oakland County, so there is no street "
            "address to publish. Start at "
            + a("/services", "services")
            + " or a city overview such as "
            + a("/royal-oak", "Royal Oak")
            + "."
        ),
        p("Questions about the website itself go through " + a("/contact", "the contact page") + ". The legal summary is on " + a("/terms", "terms") + " and " + a("/privacy", "privacy") + "."),
    ])


def privacy_article():
    return "\n".join([
        h2("What the pages collect"),
        p(
            f"{BRAND} is a static website. The pages do not run an account system. The phone number is "
            "how you reach a local cleanup crew. A call is handled by the telephone routing attached to that "
            "number, which the site owner may later replace with a tracking number. This privacy page "
            "does not control that telephone network."
        ),
        h2("The forms do not store your details"),
        p(
            "The forms on the home page and the contact page ask for a name, phone number, city, and a "
            "description of the problem. The contact form also has an optional email field. Submitting "
            "a form does not email us, does not write to a database, and does not add your name, phone, "
            "or email to the web address. It only opens a confirmation page. If you need a person, call. "
            "Do not put sensitive information in the form expecting it to be read."
        ),
        h2("Cookies and analytics"),
        p(
            "The pages do not include a third-party analytics script and do not set advertising cookies. "
            "Your browser may still keep its own history of pages you visited. The host, Cloudflare, may "
            "process connection data such as IP address as part of delivering the site. That processing "
            "is the host's, described in Cloudflare's own privacy materials."
        ),
        h2("Who we share with"),
        p(
            "Because the forms are not stored, there is no form lead to sell or share. If you call, the "
            "call reaches a local cleanup crew. They'll tell you when they can be there, and they handle your number once you are talking with them."
        ),
        p("The footer note appears on every page. The legal summary is on " + a("/terms", "the terms page") + "."),
    ])


def terms_article():
    return "\n".join([
        h2("How a call works"),
        p(
            f"A local crew handles sewer and water damage work for homeowners in parts of Oakland County, Michigan. "
            f"They'll tell you when they can be there. The contract, the price, and the result are between you and that crew. Call {PHONE_DISPLAY}."
        ),
        h2("Your responsibility"),
        p(
            "You verify that the crew holds the license and insurance required for the work. "
            "The contract, the price, the arrival, and any insurance claim stay with you and that crew."
        ),
        h2("Information on the pages"),
        p(
            "City descriptions mention real streets, neighborhoods, and public agencies so you can tell "
            "the pages apart. They are not a survey, a soil report, or a statement of what is wrong at "
            "your address. Sewer maps and drainage-district boundaries should be confirmed with the city "
            "or with the Oakland County Water Resources Commissioner."
        ),
        h2("Sewage is hazardous"),
        p(
            "Water that came from a sewer can carry pathogens. Keep people and pets away from it."
        ),
        p("See also " + a("/privacy", "privacy") + " and " + a("/about", "about") + "."),
    ])


def contact_article():
    return "\n".join([
        h2("Call if water is in the house"),
        p(
            f"The working contact is {a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)}. Use it for sewer backup cleanup, "
            "sewage extraction, flooded basement water removal, water damage restoration, sump pump "
            "problems, and sanitizing after a backup. A local crew handles the visit, and they'll tell you when they can be there."
        ),
        h3("Cities"),
        p(
            "Royal Oak, Troy, Birmingham, Berkley, and Clawson are the pages we maintain. Other Oakland "
            "County addresses may or may not be a fit. The crew decides."
        ),
        p(
            "The form only opens a confirmation screen. It does not store your name, phone, or email. "
            "Submitting it shows a confirmation screen and leaves those details out of the page address. "
            "Read " + a("/privacy", "the privacy page") + " before you type anything you would not want left only on your own screen."
        ),
    ])


THANK_YOU = [
    (
        "If this is an active backup, call",
        f"The form you just submitted was not saved and was not emailed. Nobody is reviewing a request from it. "
        f"If sewage or floodwater is in the house, call {PHONE_DISPLAY} now. They'll tell you when they can be there.",
    ),
    (
        "While you are on the phone",
        "Stop using water. Keep people and pets out of the flooded area. Do not step into water that has reached outlets, the panel, or the furnace. Do not snake a sewage backup with a household tool.",
    ),
]

NOT_FOUND_LINKS_INTRO = (
    "That address is not a page here. Use the links below to reach a city or a service, "
    f"or call {PHONE_DISPLAY}. They'll tell you when they can be there."
)


ABOUT_FAQS = [
    ("What should I do in the first minutes of a backup?", "Stop using water. Keep people and pets out of the water. Do not plunge or snake the drain, and leave the basement if water is near outlets, the panel, or the furnace. Then call (248) 825-8312."),
    (
        "Is Oakland Sewer Pros part of a city or the county?",
        "No. Oakland Sewer Pros is not affiliated with any city or with the Oakland County Water Resources Commissioner. City sewer numbers are separate from (248) 825-8312, and each city page lists its own.",
    ),
    ("Which Oakland County cities are covered?", "Royal Oak, Troy, Birmingham, Berkley, and Clawson. Berkley's sewer is a combined gravity pipe. Troy discharges through the Evergreen-Farmington, Oakland-Troy, and George W. Kuhn districts. Birmingham's system is gravity and the city owns no pump stations. Open the city where the house stands."),
    (
        "Will my call notify the city about the backup?",
        "The call is for cleanup. Written notice of a sewage disposal event is a letter you send to the responsible agency within 45 days of discovering the damage. Each of the five cities publishes its own contact. That letter is not your insurance claim.",
    ),
    ("Do you have a public office in Oakland County?", "There is no public office and no street address to publish. Call (248) 825-8312; the crew is the one that comes to the house."),
]


CONTACT_FAQS = [
    ("What is the working contact if sewage is in the house?", "Call (248) 825-8312 for sewer backup, sewage extraction, flooded basement cleanup, water damage, sump pump trouble, or sanitizing after a backup in Royal Oak, Troy, Birmingham, Berkley, or Clawson."),
    (
        "Does the form create a work order?",
        "Submitting the form only opens a confirmation screen. It does not email anyone, does not store your name or phone, and does not add those details to the web address. If you need a person, call.",
    ),
    (
        "Which cities can I ask about?",
        "Royal Oak, Troy, Birmingham, Berkley, and Clawson each have their own pages. Other Oakland County addresses may or may not be accepted. The crew decides.",
    ),
    ("What happens on the call?", "Say the city and whether the water came from a drain, a sump, or a storm. Ask for a written scope, the price, and proof of license and insurance."),
    ("Does calling file my 45-day city notice?", "No. The call is for cleanup. The 45-day written notice goes to the city or other responsible agency, with your name, address, and phone, the property address, the discovery date, and a brief description. The claim guide lists each city's contact."),
]


PRIVACY_FAQS = [
    (
        "Does the form store my name and phone?",
        "No. The home and contact forms do not email us, do not write to a database, and do not put your name, phone, or email in the web address. Submitting only opens a confirmation page. Call (248) 825-8312 if you need a person.",
    ),
    ("If I call, who receives my number?", "The local crew that answers your call. Once you are talking with them, they handle your number."),
    (
        "Do the pages set advertising cookies?",
        "The pages do not include a third-party analytics script and do not set advertising cookies. Your browser may still keep its own history. The host, Cloudflare, may process connection data such as an IP address while delivering the site.",
    ),
    (
        "Should I type a sewer claim into the form?",
        "Call instead. The form is not read and is not stored. A 45-day written notice to Royal Oak, Troy, Birmingham, Berkley, or Clawson is a letter to that city, not a form field. Insurance questions stay with your insurer.",
    ),
    ("Is (248) 825-8312 a city number?", "No. City sewer numbers are separate: Royal Oak (248) 246-3300, Troy 248-524-3370, Berkley 248-658-3490, Clawson (248) 435-4500, and Birmingham claims questions 248.530.1808."),
]


TERMS_FAQS = [
    ("Where do the city phone numbers on the pages come from?", "From each city's own website: Royal Oak's Sewer Division pages, Troy's legal claims page, Birmingham's Risk Management page, Berkley's flood tips, and Clawson's sewer and dispatch pages. Numbers can change, so confirm them with the city."),
    (
        "Who checks the license and insurance?",
        "You do, before work starts. Ask the company for the license and insurance the job requires, and for a written scope. The price and the arrival come from that company.",
    ),
    (
        "Are the city sewer descriptions a survey of my house?",
        "They describe real public systems so the five city pages can be told apart. They are not a soil report or a statement of the pipe at your address. Confirm sewer maps with the city or the Oakland County Water Resources Commissioner.",
    ),
    (
        "Does a call file the 45-day notice?",
        "A call is a cleanup call. Written notice of a sewage disposal event is due within 45 days of discovering the damage, sent to the agency that city or county designates. That letter is separate from any insurance claim.",
    ),
    ("Is sewage in a basement safe to mop?", "No. Water from a sewer can carry pathogens. Keep people and pets away, and let a crew equipped for sewage remove it."),
]
