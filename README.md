# SNIT-Reconnaissance-Framework

Python-Based Information Gathering & Reconnaissance Framework

Features:
- Passive reconnaissance
- DNS information gathering
- WHOIS lookup
- Subdomain enumeration
- HTTP header analysis
- Technology detection
- Port scanning
- Banner grabbing
- HTML and TXT report generation
  
- 1. Proposed project structure
We will build it with a professional folder structure:
SNIT-Recon/
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
│
├── logs/
│
└── utils/
    ├── logger.py
    └── report_generator.py
