import whois


def lookup_whois(domain):
    print(f"\n[*] WHOIS Lookup: {domain}")
    print("-" * 50)

    try:
        result = whois.whois(domain)

        fields = {
            "Registrar": result.registrar,
            "Creation Date": result.creation_date,
            "Expiration Date": result.expiration_date,
            "Updated Date": result.updated_date,
            "Domain Status": result.status,
            "Name Servers": result.name_servers,
        }

        for label, value in fields.items():
            print(f"\n[+] {label}:")
            print(value if value else "Not available")

    except Exception as error:
        print(f"[-] WHOIS lookup failed: {error}")
