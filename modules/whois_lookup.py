
import whois
from datetime import datetime


def format_value(value):
    if value is None:
        return "Not available"

    if isinstance(value, (list, tuple, set)):
        return [format_value(item) for item in value]

    if isinstance(value, datetime):
        return value.strftime("%d %B %Y, %H:%M:%S UTC")

    return str(value)


def lookup_whois(domain):
    print(f"\n[*] WHOIS Lookup: {domain}")
    print("-" * 55)

    results = {}

    try:
        data = whois.whois(domain)

        fields = {
            "Registrar": data.registrar,
            "Creation Date": data.creation_date,
            "Expiration Date": data.expiration_date,
            "Updated Date": data.updated_date,
            "Domain Status": data.status,
            "Name Servers": data.name_servers
        }

        for label, value in fields.items():
            formatted = format_value(value)
            results[label] = formatted

            print(f"\n[+] {label}:")
            print(formatted)

    except Exception as error:
        print(f"[-] WHOIS lookup failed: {error}")
        results["Error"] = str(error)

    return results
