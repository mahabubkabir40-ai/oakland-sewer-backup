"""Site-wide constants for oaklandsewerpros.com.

Change the phone number here, then run `python generate_site.py` (or `python build.py`).
The owner will swap this local number for a Marketcall tracking number later.
"""

BRAND = "Oakland Sewer Pros"
DOMAIN = "https://oaklandsewerpros.com"
PHONE_DISPLAY = "(248) 825-8312"
PHONE_TEL = "2488258312"
PHONE_E164 = "+12488258312"
LASTMOD = "2026-09-28"

# Marketcall offer 8915 required footer text. [This site] / [this site] replaced with the brand.
DISCLAIMER = (
    f"{BRAND} is a free service to assist homeowners in connecting with local service providers. "
    f"All contractors/providers are independent and {BRAND} does not warrant or guarantee any work performed. "
    "It is the responsibility of the homeowner to verify that the hired contractor furnishes the necessary "
    "license and insurance required for the work being performed. All persons depicted in a photo or video "
    f"are actors or models and not contractors listed on {BRAND}."
)

# Required wherever "24/7" or "same-day" appears.
AVAILABILITY_DISCLAIMER = (
    "Same-day and 24/7 emergency services are subject to provider participation, location, technician "
    "availability, and demand. Availability is not guaranteed and may vary by market and appointment capacity."
)
