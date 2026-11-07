
import requests


SECURITY_HEADERS = {
    "Strict-Transport-Security": "HSTS",
    "Content-Security-Policy": "CSP",
    "X-Frame-Options": "Clickjacking Protection",
    "X-Content-Type-Options": "MIME Sniffing Protection",
    "Referrer-Policy": "Referrer Information Control",
    "Permissions-Policy": "Browser Feature Restrictions",
}


def analyze_http_headers(domain):
    print(f"\n[*] HTTP Header Analysis: {domain}")
    print("-" * 55)

    url = f"https://{domain}"

    try:
        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True
        )

        print(f"[+] Final URL: {response.url}")
        print(f"[+] HTTP Status: {response.status_code}")
        print(f"[+] Server: {response.headers.get('Server', 'Not disclosed')}")

        print("\n[+] Security Header Analysis:")

        results = []

        for header, description in SECURITY_HEADERS.items():
            value = response.headers.get(header)

            if value:
                status = "Present"
                print(f"[+] {header}: {status}")
            else:
                status = "Missing"
                print(f"[-] {header}: {status}")

            results.append({
                "header": header,
                "description": description,
                "status": status,
                "value": value
            })

        return results

    except requests.RequestException as error:
        print(f"[-] HTTP request failed: {error}")
        return []
