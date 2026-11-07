
import socket
import ssl
from datetime import datetime, timezone


def analyze_ssl(target, port=443, timeout=5):
    """
    Analyze SSL/TLS certificate information.
    Use only on authorized assessment targets.
    """

    print(f"\n[+] SSL/TLS Certificate Analysis: {target}")
    print("-" * 55)

    result = {
        "target": target,
        "port": port,
        "status": "Analysis failed",
        "certificate": {},
        "tls_version": None,
        "cipher": None,
        "errors": []
    }

    try:
        context = ssl.create_default_context()

        with socket.create_connection(
            (target, port), timeout=timeout
        ) as connection:

            with context.wrap_socket(
                connection,
                server_hostname=target
            ) as tls_socket:

                certificate = tls_socket.getpeercert()

                result["status"] = "Certificate verified"
                result["tls_version"] = tls_socket.version()
                result["cipher"] = tls_socket.cipher()

                subject = dict(
                    (key, value)
                    for group in certificate.get("subject", [])
                    for key, value in group
                )

                issuer = dict(
                    (key, value)
                    for group in certificate.get("issuer", [])
                    for key, value in group
                )

                not_before = datetime.strptime(
                    certificate["notBefore"],
                    "%b %d %H:%M:%S %Y %Z"
                ).replace(tzinfo=timezone.utc)

                not_after = datetime.strptime(
                    certificate["notAfter"],
                    "%b %d %H:%M:%S %Y %Z"
                ).replace(tzinfo=timezone.utc)

                now = datetime.now(timezone.utc)
                days_remaining = (not_after - now).days

                san = [
                    value
                    for name, value in certificate.get(
                        "subjectAltName", []
                    )
                    if name == "DNS"
                ]

                result["certificate"] = {
                    "subject": subject,
                    "issuer": issuer,
                    "valid_from": not_before.isoformat(),
                    "valid_until": not_after.isoformat(),
                    "days_remaining": days_remaining,
                    "expiration_status": (
                        "Expired" if days_remaining < 0
                        else "Expires within 30 days"
                        if days_remaining <= 30
                        else "Valid"
                    ),
                    "subject_alternative_names": san
                }

                print("[+] Certificate verification successful")
                print(f"[+] TLS Version: {result['tls_version']}")
                print(f"[+] Cipher: {result['cipher']}")
                print(f"[+] Subject: {subject}")
                print(f"[+] Issuer: {issuer}")
                print(f"[+] Valid Until: {not_after}")
                print(f"[+] Days Remaining: {days_remaining}")
                print(
                    f"[+] Expiration Status: "
                    f"{result['certificate']['expiration_status']}"
                )

    except ssl.SSLCertVerificationError as error:
        result["status"] = "Certificate verification failed"
        result["errors"].append(str(error))
        print(f"[-] Certificate verification failed: {error}")

    except (socket.timeout, TimeoutError) as error:
        result["status"] = "Connection timed out"
        result["errors"].append(str(error))
        print("[-] SSL connection timed out")

    except (socket.gaierror, OSError, ssl.SSLError) as error:
        result["status"] = "Connection or SSL error"
        result["errors"].append(str(error))
        print(f"[-] SSL analysis error: {error}")

    return result
