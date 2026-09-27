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
            "backup. We do not employ those companies. We do not own their trucks. We do not supervise "
            "their jobs, and we do not warrant or guarantee the work."
        ),
        h2("What happens when you call"),
        p(
            f"You dial {PHONE_DISPLAY}. When a participating provider is available for your type of job "
            "and your location, the call can be connected to them. If no provider is participating, "
            "availability is not something this site can create. Same-day and 24/7 coverage depends on "
            "that provider, the address, technician availability, and demand. It is not a promise."
        ),
        h2("What you still have to verify"),
        p(
            "Before work starts, ask the company you hire for the license and insurance the job requires, "
            "and for a written scope. Prices are theirs. Insurance coverage for sewer backup or water "
            "damage is a question for your insurer, not for us. We do not file claims and we do not bill carriers."
        ),
        h2("What we do not have"),
        p(
            f"{BRAND} does not publish a street address because we do not operate a public office or a "
            "dispatch hub in Oakland County. Photos on the site are not pictures of a staff or of "
            "contractors we employ. The cities we describe are the five listed above. Start at "
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
            "We do not own, manage, or guarantee their work."
        ),
        h2("Your responsibility"),
        p(
            "You are responsible for verifying that any company you hire holds the license and insurance "
            "required for the work. You are responsible for the contract, the price, and any insurance "
            "claim. We do not warrant results, arrival times, or prices."
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
            "website cannot make a basement safe by being read."
        ),
        p("See also " + a("/privacy", "privacy") + " and " + a("/about", "about") + "."),
    ])


def contact_article():
    return "\n".join([
        h2("Call if water is in the house"),
        p(
            f"The working contact is {a(f"tel:{PHONE_TEL}", PHONE_DISPLAY)}. Use it for sewer backup cleanup, "
            "sewage extraction, flooded basement water removal, water damage restoration, sump pump "
            "problems, and sanitizing after a backup. 24/7 coverage exists only when a participating "
            "provider is available. This site does not promise that someone will answer or arrive."
        ),
        h3("Cities"),
        p(
            "Royal Oak, Troy, Birmingham, Berkley, and Clawson are the pages we maintain. Other Oakland "
            "County addresses may or may not be accepted by a provider. The provider decides."
        ),
        p(
            "The form on this page does not create a ticket. It does not store your name, phone, or email. "
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
