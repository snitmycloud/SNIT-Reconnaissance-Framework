
import dns.resolver
from pathlib import Path


def enumerate_subdomains(domain):
    print(f"\n[*] Subdomain Enumeration: {domain}")
    print("-" * 55)

    wordlist = Path(__file__).resolve().parent.parent / "wordlists" / "subdomains.txt"

    if not wordlist.exists():
        print("[-] Subdomain wordlist not found.")
        return []

    discovered = []

    try:
        with open(wordlist, "r", encoding="utf-8") as file:
            subdomains = [
                line.strip()
                for line in file
                if line.strip() and not line.startswith("#")
            ]

        resolver = dns.resolver.Resolver()
        resolver.timeout = 3
        resolver.lifetime = 5

        for name in subdomains:
            hostname = f"{name}.{domain}"

            try:
                answers = resolver.resolve(hostname, "A")
                ips = [answer.to_text() for answer in answers]

                discovered.append({
                    "subdomain": hostname,
                    "ip_addresses": ips
                })

                print(f"[+] {hostname} -> {', '.join(ips)}")

            except (
                dns.resolver.NXDOMAIN,
                dns.resolver.NoAnswer,
                dns.resolver.Timeout
            ):
                continue

            except Exception as error:
                print(f"[-] Error checking {hostname}: {error}")

    except OSError as error:
        print(f"[-] Could not read wordlist: {error}")
        return []

    print(f"\n[+] Total discovered: {len(discovered)}")

    return discovered
