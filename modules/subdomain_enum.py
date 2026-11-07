
import dns.resolver
from pathlib import Path


def enumerate_subdomains(domain):
    print(f"\n[*] Subdomain Enumeration: {domain}")
    print("-" * 55)

    wordlist = (
        Path(__file__).resolve().parent.parent
        / "wordlists"
        / "subdomains.txt"
    )

    results = []

    if not wordlist.exists():
        print("[-] Subdomain wordlist not found.")
        return results

    resolver = dns.resolver.Resolver()
    resolver.timeout = 3
    resolver.lifetime = 5

    try:
        with open(wordlist, "r", encoding="utf-8") as file:
            subdomains = [
                line.strip()
                for line in file
                if line.strip() and not line.startswith("#")
            ]

        for name in subdomains:
            hostname = f"{name}.{domain}"

            try:
                answers = resolver.resolve(hostname, "A")
                ip_addresses = [
                    answer.to_text() for answer in answers
                ]

                entry = {
                    "subdomain": hostname,
                    "ip_addresses": ip_addresses
                }

                results.append(entry)

                print(
                    f"[+] {hostname} -> "
                    f"{', '.join(ip_addresses)}"
                )

            except (
                dns.resolver.NXDOMAIN,
                dns.resolver.NoAnswer,
                dns.resolver.Timeout
            ):
                continue

            except dns.exception.DNSException as error:
                print(f"[-] DNS error for {hostname}: {error}")

    except OSError as error:
        print(f"[-] Wordlist error: {error}")
        return results

    print(f"\n[+] Total discovered: {len(results)}")

    return results
