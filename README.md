
# SNIT-Reconnaissance-Framework

### Python-Based Information Gathering & Reconnaissance Framework

## 1. Features

- Passive Reconnaissance
- DNS Information Gathering
- WHOIS Lookup
- Subdomain Enumeration
- HTTP Header Analysis
- Technology Detection
- Port Scanning
- Banner Grabbing
- HTML and TXT Report Generation

## 2. Project Structure

```text
SNIT-Reconnaissance-Framework/
│
├── main.py
├── requirements.txt
├── README.md
├── config.py
│
├── modules/
│   ├── whois_lookup.py
│   ├── dns_enum.py
│   ├── subdomain_enum.py
│   ├── http_headers.py
│   ├── tech_detect.py
│   ├── port_scanner.py
│   └── banner_grabber.py
│
├── reports/
├── logs/
│
└── utils/
    ├── logger.py
    └── report_generator.py
```

## 3. Development Roadmap

| Phase | Development | Level |
|:---:|---|:---:|
| 1 | Python Project Structure | Beginner |
| 2 | WHOIS and DNS Lookup | Beginner |
| 3 | Subdomain Enumeration | Intermediate |
| 4 | HTTP Headers and Technology Detection | Intermediate |
| 5 | Port Scanning | Advanced |
| 6 | Banner Grabbing | Advanced |
| 7 | HTML Reporting | Advanced |
| 8 | CLI Interface and Documentation | Professional |

## 4. Technologies

1. **Programming Language:** Python 3
2. **Operating System:** Kali Linux
3. **HTTP Library:** Requests
4. **DNS Enumeration:** dnspython
5. **WHOIS Lookup:** python-whois
6. **HTML Parsing:** BeautifulSoup
7. **Network Programming:** Python Socket
8. **Version Control:** Git
9. **Code Hosting:** GitHub

## 5. Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/snitmycloud/SNIT-Reconnaissance-Framework.git
```

### Step 2: Navigate to the Project Directory

```bash
cd SNIT-Reconnaissance-Framework
```

### Step 3: Create a Virtual Environment

```bash
python3 -m venv venv
```

### Step 4: Activate the Virtual Environment

```bash
source venv/bin/activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the Tool

```bash
python3 main.py --help
```

## 6. Usage

Use the tool only against systems you own or have explicit permission to assess.

Example:

```bash
python3 main.py example.com --subdomains --whois --dns
```

## 7. Disclaimer

SNIT Reconnaissance Framework is developed for educational purposes, cybersecurity research, and authorized security testing.

Users are responsible for ensuring they have proper authorization before conducting reconnaissance or scanning activities.

The developers are not responsible for unauthorized or illegal use of this tool.

## 8. Author

**SNIT Training Institute**

GitHub: https://github.com/snitmycloud

Project: SNIT Reconnaissance Framework
