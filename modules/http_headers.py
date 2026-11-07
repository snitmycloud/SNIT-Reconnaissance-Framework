
import requests


SECURITY_HEADERS = {
    "Strict-Transport-Security": "Enforces HTTPS connections",
    "Content-Security-Policy": "Controls permitted content sources",
    "X-Frame-Options": "Helps prevent clickjacking",
    "X-Content-Type-Options": "Prevents MIME sniffing",
    "Referrer-Policy": "Controls referrer information",
    "Permissions-Policy": "Controls browser feature access"
}


def analyze_http_headers(domain):
    print(f"\n[*] HTTP Header Analysis: {domain}")
    print("-" * 55)

    url = f"https://{domain}"
    results = {}

    try:
        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True
        )

        results["Final URL"] = response.url
        results["HTTP Status"] = response.status_code
        results["Server"] = response.headers.get(
            "Server", "Not disclosed"
        )

        print(f"[+] Final URL: {response.url}")
        print(f"[+] HTTP Status: {response.status_code}")
        print(f"[+] Server: {results['Server']}")

        results["Security Headers"] = {}

        print("\n[+] Security Header Analysis:")

        for header, description in SECURITY_HEADERS.items():
            value = response.headers.get(header)

            status = "Present" if value else "Missing"

            results["Security Headers"][header] = {
                "description": description,
                "status": status,
                "value": value or "Not returned"
            }

            if value:
                print(f"[+] {header}: Present")
            else:
                print(f"[-] {header}: Missing")

        return results

    except requests.RequestException as error:
        print(f"[-] HTTP request failed: {error}")
        results["Error"] = str(error)
        return results
