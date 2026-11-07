
import requests
import re


def detect_technologies(domain):
    print(f"\n[*] Technology Detection: {domain}")
    print("-" * 55)

    results = {
        "Website": None,
        "HTTP Status": None,
        "Detected Technologies": []
    }

    url = f"https://{domain}"

    try:
        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True
        )

        headers = response.headers
        html = response.text

        results["Website"] = response.url
        results["HTTP Status"] = response.status_code

        detected = set()

        # Web server and CDN
        server = headers.get("Server", "")

        if server:
            detected.add(f"Web Server: {server}")

        if "cloudflare" in server.lower() or "cf-ray" in headers:
            detected.add("CDN: Cloudflare")

        # CMS detection
        if re.search(r"wp-content|wp-includes", html, re.I):
            detected.add("CMS: WordPress")

        if "Joomla!" in html or "com_content" in html:
            detected.add("CMS: Joomla")

        if "Drupal.settings" in html or "/sites/default/" in html:
            detected.add("CMS: Drupal")

        # JavaScript frameworks
        if re.search(r"__NEXT_DATA__|/_next/", html):
            detected.add("Framework: Next.js")

        if "ng-version" in html or "ng-app" in html:
            detected.add("Framework: Angular")

        if re.search(r"data-reactroot|__REACT_DEVTOOLS_GLOBAL_HOOK__", html):
            detected.add("Framework: React")

        if "data-v-" in html:
            detected.add("Framework: Vue.js")

        # Server-side technology hints
        powered_by = headers.get("X-Powered-By")

        if powered_by:
            detected.add(f"Technology: {powered_by}")

        results["Detected Technologies"] = sorted(detected)

        print(f"[+] Website: {response.url}")
        print(f"[+] HTTP Status: {response.status_code}")

        if detected:
            print("\n[+] Detected Technologies:")

            for technology in sorted(detected):
                print(f"    {technology}")
        else:
            print("\n[-] No technologies identified.")

        return results

    except requests.RequestException as error:
        print(f"[-] Technology detection failed: {error}")
        results["Error"] = str(error)
        return results
