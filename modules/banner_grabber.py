
import socket
import ssl


def grab_banners(target, open_ports, timeout=2):
    """
    Collect basic service banners from ports already identified as open.
    Use only on systems you own or are authorized to assess.
    """

    results = []

    try:
        target_ip = socket.gethostbyname(target)
        print(f"\n[+] Banner Grabbing: {target}")
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
            response = connection.recv(1024)

            if response:
                banner = response.decode(
                    "utf-8", errors="replace"
                ).strip()

                status = "Banner received"

            connection.close()

        except (socket.timeout, TimeoutError):
            status = "Connection timed out"

        except ssl.SSLError as error:
            status = f"SSL error: {error}"

        except OSError as error:
            status = f"Connection error: {error}"

        results.append({
            "port": port,
            "service": service,
            "status": status,
            "banner": banner
        })

        print(f"[+] Port {port}/{service}: {status}")

        if banner:
            print(f"    {banner[:200]}")

    print(f"\n[+] Services checked: {len(results)}")

    return {
        "target": target,
        "ip_address": target_ip,
        "services": results
    }
