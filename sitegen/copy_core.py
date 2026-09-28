"""Home, contact, about, privacy, terms, thank-you, and 404 copy."""

from site_config import BRAND, PHONE_DISPLAY, PHONE_TEL
from sitegen.render import a, h2, h3, p

def about_article():
    return "\n".join([
        h2("A referral line, not a restoration company"),
        p(
            f"{BRAND} helps homeowners in Royal Oak, Troy, Birmingham, Berkley, and Clawson reach "
            "independent local companies for sewer backup cleanup, sewage extraction, flooded basement "
            "cleanup, water damage restoration, sump pump repair, and sanitizing after a flood or sewage "
            "backup. The company you reach is independent. They bring their own crew and their own trucks, "
            "and the work is theirs."
        ),
        h2("What happens when you call"),
        p(
            f"You dial {PHONE_DISPLAY}. When a participating provider is available for your type of job "
            "and your location, the call is connected to them. How soon they can come depends on that "
            "company, the address, and who is free. If nobody is available, the line cannot invent a crew."
        ),
        h2("What you still have to verify"),
        p(
            "Before work starts, ask the company you hire for the license and insurance the job requires, "
            "and for a written scope. The price comes from that company. Insurance coverage for sewer backup or water "
            "damage is a question for your insurer. Your claim stays between you and your carrier."
        ),
        h2("No public office"),
        p(
            f"{BRAND} has no public office and no dispatch hub in Oakland County, so there is no street "
            "address to publish. Photos on the site show wet basements, not a crew we employ. "
            "The cities described here are the five listed above. Start at "
            + a("/services", "services")
            + " or a city overview such as "
            + a("/royal-oak", "Royal Oak")
            + "."
        ),
        p("Questions about the website itself go through " + a("/contact", "the contact page") + ". The legal summary is on " + a("/terms", "terms") + " and " + a("/privacy", "privacy") + "."),
    ])


def privacy_article():
    return "\n".join([
        h2("What this website collects"),
        p(
            f"{BRAND} is a static website. The pages do not run an account system. The phone number is "
            "how you reach a live referral. A call is handled by the telephone routing attached to that "
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
            "These pages do not include a third-party analytics script and do not set advertising cookies. "
            "Your browser may still keep its own history of pages you visited. The host, Cloudflare, may "
            "process connection data such as IP address as part of delivering the site. That processing "
            "is the host's, described in Cloudflare's own privacy materials."
        ),
        h2("Who we share with"),
        p(
            "Because the forms are not stored, there is no form lead to sell or share. If you call, the "
            "call can be connected to an independent provider. That provider is not our employee. Their "
            "handling of your phone number is their responsibility once the call is connected."
        ),
        p("The referral disclaimer also appears in the footer of every page and on " + a("/terms", "the terms page") + "."),
    ])


def terms_article():
    return "\n".join([
        h2("Referral service"),
        p(
            f"{BRAND} is an independent referral service for homeowners in parts of Oakland County, "
            "Michigan. We are not a plumbing contractor and we are not a water damage restoration "
            "contractor. Calls to the number on this site may be routed to independent businesses. "
            "Those businesses own the work. The contract and the result are between you and the company you hire."
        ),
        h2("Your responsibility"),
        p(
            "You verify that any company you hire holds the license and insurance required for the work. "
            "The contract, the price, the arrival, and any insurance claim stay with you and that company."
        ),
        h2("Information on these pages"),
        p(
            "City descriptions mention real streets, neighborhoods, and public agencies so you can tell "
            "the pages apart. They are not a survey, a soil report, or a statement of what is wrong at "
            "your address. Sewer maps and drainage-district boundaries should be confirmed with the city "
            "or with the Oakland County Water Resources Commissioner."
        ),
        h2("Sewage is hazardous"),
        p(
            "Water that came from a sewer can carry pathogens. Keep people and pets away from it. This "
            "website is not a substitute for staying out of the water."
        ),
        p("See also " + a("/privacy", "privacy") + " and " + a("/about", "about") + "."),
    ])


def contact_article():
    return "\n".join([
        h2("Call if water is in the house"),
        p(
            f"The working contact is {a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)}. Use it for sewer backup cleanup, "
            "sewage extraction, flooded basement water removal, water damage restoration, sump pump "
            "problems, and sanitizing after a backup. A live connection happens when a participating "
            "provider is available. How soon anyone can come is up to that company."
        ),
        h3("Cities"),
        p(
            "Royal Oak, Troy, Birmingham, Berkley, and Clawson are the pages we maintain. Other Oakland "
            "County addresses may or may not be accepted by a provider. The provider decides."
        ),
        p(
            "The form on this page only opens a confirmation screen. It does not store your name, phone, or email. "
            "Submitting it shows a confirmation screen and leaves those details out of the page address. "
            "Read " + a("/privacy", "the privacy page") + " before you type anything you would not want left only on your own screen."
        ),
    ])


THANK_YOU = [
    (
        "If this is an active backup, call",
        f"The form you just submitted was not saved and was not emailed. Nobody is reviewing a request from it. "
        f"If sewage or floodwater is in the house, call {PHONE_DISPLAY} now.",
    ),
    (
        "While you are on the phone",
        "Stop using water. Keep people and pets out of the flooded area. Do not step into water that has reached outlets, the panel, or the furnace. Do not snake a sewage backup with a household tool.",
    ),
]

NOT_FOUND_LINKS_INTRO = (
    "That address is not a page on this site. Use the links below to reach a city or a service, "
    f"or call {PHONE_DISPLAY} if you need a provider."
)


ABOUT_FAQS = [
    (
        "Is Oakland Sewer Pros a restoration company?",
        "It is a referral line for homeowners in Royal Oak, Troy, Birmingham, Berkley, and Clawson. Independent local companies do the cleanup. Ask the company you hire for the license and insurance the job requires, a written scope, and the price.",
    ),
    (
        "What happens when I call (248) 825-8312?",
        "When a participating provider is available for your type of job and your city, the call is connected to that company. They bring their own crew. How soon they can come depends on that company, the address, and who is free.",
    ),
    (
        "Which Oakland County cities are on this site?",
        "Royal Oak, Troy, Birmingham, Berkley, and Clawson. Berkley's sewer is a combined gravity pipe. Troy discharges through the Evergreen-Farmington, Oakland-Troy, and George W. Kuhn districts. Birmingham's system is gravity and the city owns no pump stations. Open the city where the house stands.",
    ),
    (
        "Does this line send the 45-day notice to my city?",
        "The call is for cleanup. Written notice of a sewage disposal event is a letter you send to the responsible agency within 45 days of discovering the damage. Each of the five cities publishes its own contact. That letter is not your insurance claim.",
    ),
    (
        "Do you have a public office in Oakland County?",
        "There is no public office and no street address to publish. Photos on the site show wet basements. Questions about the website go through the contact page. The company you hire is the one that comes to the house.",
    ),
]


CONTACT_FAQS = [
    (
        "What is the working contact if sewage is in the house?",
        "Call (248) 825-8312. That is how you reach a live referral for sewer backup, sewage extraction, flooded basement cleanup, water damage, sump pump trouble, or sanitizing after a backup in Oakland County.",
    ),
    (
        "Does the form on this page create a work order?",
        "Submitting the form only opens a confirmation screen. It does not email anyone, does not store your name or phone, and does not add those details to the web address. If you need a person, call.",
    ),
    (
        "Which cities can I ask about?",
        "Royal Oak, Troy, Birmingham, Berkley, and Clawson each have their own pages. Other Oakland County addresses may or may not be accepted. The provider decides.",
    ),
    (
        "What happens on the call?",
        "When a participating independent company is available for the job and the city, you are connected to them. How soon they can come is up to that company. Ask them for a written scope, the price, and proof of license and insurance.",
    ),
    (
        "Can this phone line file my 45-day city notice?",
        "The phone line is for a cleanup referral. The 45-day written notice goes to the city or other responsible agency, with your name, address, and phone, the property address, the discovery date, and a brief description. Royal Oak, Troy, Birmingham, Berkley, and Clawson each list their own contact on the claim guide.",
    ),
]


PRIVACY_FAQS = [
    (
        "Does the form store my name and phone?",
        "No. The home and contact forms do not email us, do not write to a database, and do not put your name, phone, or email in the web address. Submitting only opens a confirmation page. Call (248) 825-8312 if you need a person.",
    ),
    (
        "If I call, who receives my number?",
        "A call can be connected to an independent provider serving Royal Oak, Troy, Birmingham, Berkley, or Clawson when one is participating. That company is not an employee of this site. Once the call is connected, they handle the number.",
    ),
    (
        "Does this website set advertising cookies?",
        "These pages do not include a third-party analytics script and do not set advertising cookies. Your browser may still keep its own history. The host, Cloudflare, may process connection data such as an IP address while delivering the site.",
    ),
    (
        "Should I type a sewer claim into the form?",
        "Call instead. The form is not read and is not stored. A 45-day written notice to Royal Oak, Troy, Birmingham, Berkley, or Clawson is a letter to that city, not a field on this page. Insurance questions stay with your insurer.",
    ),
    (
        "Is (248) 825-8312 a city dispatch line?",
        "It is the referral line on this site. City sewer calls are separate: Royal Oak (248) 246-3300, Troy 248-524-3370, Birmingham claims questions 248.530.1808, Berkley 248-658-3490, and Clawson (248) 435-4500 on the city sewer page. After-hours numbers are on each city page.",
    ),
]


TERMS_FAQS = [
    (
        "Is this site a plumbing contractor in Oakland County?",
        "Oakland Sewer Pros is a referral service for homeowners in Royal Oak, Troy, Birmingham, Berkley, and Clawson. Calls may be routed to independent businesses. The contract and the result are between you and the company you hire.",
    ),
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
        "A call is a cleanup referral. Written notice of a sewage disposal event is due within 45 days of discovering the damage, sent to the agency that city or county designates. That letter is separate from any insurance claim.",
    ),
    (
        "Is sewage in a basement safe to mop?",
        "Water from a sewer can carry pathogens. Keep people and pets away from it. This website is not a substitute for staying out of the water. An independent cleanup company handles removal when you are connected and you hire them.",
    ),
]
