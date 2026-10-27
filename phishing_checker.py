import re
from urllib.parse import urlparse


def inspect_url(url):
    """Return a list of warning signs found in the URL text."""
    warnings = []
    text = url.strip()

    if not text:
        return ["No URL entered."]

    # Parse the text only; this does not visit the website.
    try:
        parsed = urlparse(text)
        hostname = parsed.hostname or ""
    except ValueError:
        return ["This text is not a valid URL format."]

    if "@" in text:
        warnings.append("The URL contains an @ symbol.")

    if len(text) > 100:
        warnings.append("The URL is longer than 100 characters.")

    # Check whether the hostname looks like an IPv4 address.
    ip_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    if re.match(ip_pattern, hostname):
        warnings.append("The hostname is an IP address, not a normal domain name.")

    if len([part for part in hostname.split(".") if part]) >= 5:
        warnings.append("The hostname has five or more dot-separated parts.")

    if "xn--" in hostname.lower():
        warnings.append("The hostname contains 'xn--' (possible punycode).")

    if parsed.scheme.lower() == "http":
        warnings.append("The URL uses HTTP instead of HTTPS.")

    if not warnings:
        warnings.append("No listed warning signs were found. This does NOT prove the URL is safe.")

    return warnings


def main():
    """Ask the user for URLs and display the results."""
    print("=" * 45)
    print("     PHISHING URL AWARENESS CHECKER")
    print("=" * 45)
    print("This tool checks URL text only. It does not open websites.")
    print("Type 'q' to quit.\n")

    while True:
        url = input("Enter a URL: ").strip()

        if url.lower() in {"q", "quit", "exit"}:
            print("Goodbye!")
            break

        results = inspect_url(url)
        print("\nResult:")
        for item in results:
            print("- " + item)
        print()


if __name__ == "__main__":
    main()
