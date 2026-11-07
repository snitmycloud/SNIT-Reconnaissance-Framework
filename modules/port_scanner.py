
import socket


COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    8080: "HTTP Alternate",
    8443: "HTTPS Alternate"
}


def scan_ports(target, ports=None, timeout=1):
    print(f"\n[*] TCP Port Scan: {target}")
    print("-" * 55)

    if ports is None:
        ports = list(COMMON_PORTS.keys())

    results = []

    try:
        ip_address = socket.gethostbyname(target)
        print(f"[+] Target IP: {ip_address}")

    except socket.gaierror as error:
        print(f"[-] DNS resolution failed: {error}")
        return results

    for port in ports:

        if not isinstance(port, int) or not 1 <= port <= 65535:
            print(f"[-] Invalid port: {port}")
            continue

        try:
            with socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            ) as sock:

                sock.settimeout(timeout)
                status = sock.connect_ex((ip_address, port))

                if status == 0:
                    service = COMMON_PORTS.get(port, "Unknown")

                    result = {
                        "port": port,
                        "protocol": "TCP",
                        "state": "Open",
                        "service": service
                    }

                    results.append(result)

                    print(
                        f"[+] Port {port}/TCP OPEN "
                        f"- {service}"
                    )

        except socket.timeout:
            continue

        except OSError as error:
            print(f"[-] Port {port}: {error}")

    print(f"\n[+] Open TCP ports found: {len(results)}")

    return results
