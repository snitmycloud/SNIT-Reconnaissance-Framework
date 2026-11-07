
import socket
import ssl


def parse_http_response(response):
    """Extract useful information from an HTTP response."""

    parsed = {
        "http_status": None,
        "server": None,
        "platform": None,
        "web_server": None,
        "php_version": None,
        "redirect": None,
        "security_headers": {},
        "other_headers": {}
    }

    if not response:
        return parsed

    lines = response.splitlines()

    if lines:
        parsed["http_status"] = lines[0].strip()

    for line in lines[1:]:
        if ":" not in line:
            continue

        key, value = line.split(":", 1)
        key = key.strip().lower()
        value = value.strip()

        if key == "server":
            parsed["server"] = value

        elif key == "platform":
            parsed["platform"] = value

        elif key == "x-turbo-charged-by":
            parsed["web_server"] = value

        elif key == "x-powered-by":
            parsed["php_version"] = value

        elif key == "location":
            parsed["redirect"] = value

        elif key in (
            "content-security-policy",
            "strict-transport-security",
            "x-frame-options",
            "x-content-type-options",
            "referrer-policy",
            "permissions-policy"
        ):
            parsed["security_headers"][key] = value

        else:
            parsed["other_headers"][key] = value

    return parsed


def grab_banners(target, open_ports, timeout=2):
    """Collect and parse basic service banners."""

    results = []

    try:
        target_ip = socket.gethostbyname(target)
        print(f"\n[+] Banner Analysis: {target}")
        print(f"[+] Target IP: {target_ip}")

    except socket.gaierror as error:
        print(f"[-] DNS resolution failed: {error}")
        return {
            "target": target,
            "ip_address": None,
            "services": []
        }

    for item in open_ports:
        port = item.get("port")
        service = item.get("service", "Unknown")

        if not port:
            continue

        connection = None
        banner = ""
        status = "No banner received"

        try:
            connection = socket.create_connection(
                (target_ip, port),
                timeout=timeout
            )

            if port in (80, 8080):
                connection.sendall(
                    f"HEAD / HTTP/1.1\r\n"
                    f"Host: {target}\r\n"
                    f"Connection: close\r\n\r\n".encode()
                )

            elif port in (443, 8443):
                context = ssl.create_default_context()

                connection = context.wrap_socket(
                    connection,
                    server_hostname=target
                )

                connection.sendall(
                    f"HEAD / HTTP/1.1\r\n"
                    f"Host: {target}\r\n"
                    f"Connection: close\r\n\r\n".encode()
                )

            connection.settimeout(timeout)
            response = connection.recv(4096)

            if response:
                banner = response.decode(
                    "utf-8", errors="replace"
                )

                status = "Banner received"

        except (socket.timeout, TimeoutError):
            status = "Connection timed out"

        except ssl.SSLError as error:
            status = f"SSL error: {error}"

        except OSError as error:
            status = f"Connection error: {error}"

        finally:
            if connection:
                connection.close()

        parsed = parse_http_response(banner)

        service_result = {
            "port": port,
            "service": service,
            "status": status,
            "details": parsed,
            "raw_banner": banner
        }

        results.append(service_result)

        print(f"\n[+] Port {port}/{service}: {status}")

        if parsed["http_status"]:
            print(f"    HTTP Status: {parsed['http_status']}")

        if parsed["server"]:
            print(f"    Server: {parsed['server']}")

        if parsed["platform"]:
            print(f"    Platform: {parsed['platform']}")

        if parsed["web_server"]:
            print(f"    Web Server: {parsed['web_server']}")

        if parsed["php_version"]:
            print(f"    PHP: {parsed['php_version']}")

        if parsed["redirect"]:
            print(f"    Redirect: {parsed['redirect']}")

    print(f"\n[+] Services checked: {len(results)}")

    return {
        "target": target,
        "ip_address": target_ip,
        "services": results
    }
