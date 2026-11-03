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
- 
## Project Structure

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
│
├── logs/
│
└── utils/
    ├── logger.py
    └── report_generator.py


    
## 2. Development Roadmap

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

```

## 3. Technologies

- **Programming Language:** Python 3
- **Operating System:** Kali Linux
- **HTTP Library:** Requests
- **DNS Enumeration:** dnspython
- **WHOIS Lookup:** python-whois
- **HTML Parsing:** BeautifulSoup
- **Network Programming:** Python Socket
- **Version Control:** Git
- **Code Hosting:** GitHub

- 
## 4. Installation

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


