
import argparse

from config import TOOL_NAME, VERSION
from modules.dns_enum import enumerate_dns
from modules.whois_lookup import lookup_whois
from modules.subdomain_enum import enumerate_subdomains
from modules.http_headers import analyze_http_headers
from modules.tech_detect import detect_technologies


def display_banner():
    print("=" * 55)
    print(f"       {TOOL_NAME} v{VERSION}")
    print("  Information Gathering & Reconnaissance Framework")
    print("=" * 55)


def main():
    parser = argparse.ArgumentParser(
        description="SNIT Reconnaissance Framework"
    )

    parser.add_argument(
        "target",
        help="Target domain you are authorized to assess"
    )

    args = parser.parse_args()
    target = args.target.strip()

    display_banner()

    print(f"[+] Target: {target}")
    print("\n[*] Starting reconnaissance...")

    print("\n[1] DNS Enumeration")
    enumerate_dns(target)

    print("\n[2] WHOIS Lookup")
    lookup_whois(target)
    
    print("\n[3] Subdomain Enumeration")
    enumerate_subdomains(target)

    print("\n[4] HTTP Header Analysis")
    analyze_http_headers(target)

    print("\n[5] Technology Detection")
    detect_technologies(target)
    
    print("\n[+] Reconnaissance completed.")


if __name__ == "__main__":
    main()
