
import argparse
import sys

from config import TOOL_NAME, VERSION


def display_banner():
    print("=" * 55)
    print(f"       {TOOL_NAME} v{VERSION}")
    print("  Information Gathering & Reconnaissance Framework")
    print("=" * 55)


def validate_target(target):
    if not target or len(target) > 253:
        return False

    if any(char.isspace() for char in target):
        return False

    return True


def main():
    parser = argparse.ArgumentParser(
        description="SNIT Reconnaissance Framework"
    )

    parser.add_argument(
        "target",
        nargs="?",
        help="Target domain you are authorized to assess"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"{TOOL_NAME} {VERSION}"
    )

    args = parser.parse_args()

    display_banner()

    if args.target is None:
        parser.print_help()
        return

    if not validate_target(args.target):
        print("[!] Invalid target format.")
        sys.exit(1)

    print(f"[+] Target: {args.target}")
    print("[+] Framework initialized successfully.")
    print("[!] Reconnaissance modules will be added next.")


if __name__ == "__main__":
    main()
