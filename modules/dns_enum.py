
import dns.resolver


def enumerate_dns(domain):
    print(f"\n[*] DNS Enumeration: {domain}")
    print("-" * 55)

    record_types = ["A", "AAAA", "MX", "NS", "TXT", "CNAME"]
    results = {}

    resolver = dns.resolver.Resolver()
    resolver.timeout = 3
    resolver.lifetime = 5

    for record_type in record_types:
        records = []

        try:
            answers = resolver.resolve(domain, record_type)

            for answer in answers:
                records.append(answer.to_text())

            print(f"\n[+] {record_type} Records:")

            for record in records:
                print(f"    {record}")

        except dns.resolver.NXDOMAIN:
            print(f"[-] Domain does not exist.")
        except dns.resolver.NoAnswer:
            print(f"[-] No {record_type} records found.")
        except dns.resolver.Timeout:
            print(f"[-] DNS query timed out for {record_type}.")
        except dns.exception.DNSException as error:
            print(f"[-] DNS error: {error}")

        results[record_type] = records

    return results
