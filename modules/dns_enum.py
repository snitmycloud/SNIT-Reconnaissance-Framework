
import dns.resolver


def enumerate_dns(domain):
    record_types = ["A", "AAAA", "MX", "NS", "TXT", "CNAME"]

    results = {}

    print(f"\n[*] DNS Enumeration: {domain}")
    print("-" * 50)

    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(
                domain,
                record_type,
                lifetime=5
            )

            results[record_type] = []

            print(f"\n[+] {record_type} Records:")

            for answer in answers:
                value = str(answer)
                results[record_type].append(value)
                print(f"    {value}")

        except dns.resolver.NXDOMAIN:
            print(f"[-] Domain does not exist.")
            break

        except dns.resolver.NoAnswer:
            print(f"[-] No {record_type} records found.")

        except dns.resolver.Timeout:
            print(f"[-] DNS query timed out.")

        except dns.resolver.NoNameservers:
            print(f"[-] No DNS nameservers available.")

        except Exception as error:
            print(f"[-] Error: {error}")

    return results
