# SNIT Reconnaissance Framework

### Python-Based Information Gathering & Reconnaissance Framework

**SNIT Recon** is a Python-based reconnaissance framework developed by SNIT Training Institute for information gathering, network discovery, technology identification, and basic security assessment.

It combines multiple reconnaissance modules into a single command-line tool and generates structured HTML and TXT reports.

## 1. Features

### Information Gathering
- DNS Information Gathering
- WHOIS Lookup
- Subdomain Enumeration
- HTTP Security Header Analysis
- Website Technology Detection

### Network Reconnaissance
- TCP Port Scanning
- Service Detection
- Banner Grabbing

### Security Analysis
- SSL/TLS Certificate Analysis
- Certificate Expiration Monitoring
- TLS Protocol and Cipher Identification
- Security Header Inspection

### Reporting
- Automated HTML Report Generation
- TXT Report Generation
- Structured Reconnaissance Results
- Centralized Assessment Reports

## 2. Project Structure

```text
SNIT-Reconnaissance-Framework/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
│
├── modules/
│   ├── dns_enum.py
│   ├── whois_lookup.py
│   ├── subdomain_enum.py
│   ├── http_headers.py
│   ├── tech_detect.py
│   ├── port_scanner.py
│   ├── banner_grabber.py
│   └── ssl_analyzer.py
│
├── utils/
│   └── report_generator.py
│
├── wordlists/
│   └── subdomains.txt
│
└── reports/
```

## 3. Development Roadmap

| Phase | Development | Level |
|---|---|---|
| 1 | Python Project Structure | Beginner |
| 2 | WHOIS and DNS Lookup | Beginner |
| 3 | Subdomain Enumeration | Intermediate |
| 4 | HTTP Header Analysis | Intermediate |
| 5 | Website Technology Detection | Intermediate |
| 6 | TCP Port Scanning | Advanced |
| 7 | Service Detection and Banner Grabbing | Advanced |
| 8 | SSL/TLS Certificate Analysis | Advanced |
| 9 | HTML and TXT Report Generation | Advanced |
| 10 | CLI Interface and Documentation | Professional |

## 4. Technologies

1. **Programming Language:** Python 3
2. **Operating Systems:** Kali Linux and Windows
3. **HTTP Library:** Requests
4. **DNS Enumeration:** dnspython
5. **WHOIS Lookup:** python-whois
6. **HTML Parsing:** BeautifulSoup
7. **Network Programming:** Python Socket
8. **SSL/TLS Analysis:** Python SSL
9. **Date and Time Processing:** Python datetime
10. **Version Control:** Git
11. **Code Hosting:** GitHub

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

**Kali Linux:**

```bash
source venv/bin/activate
```

**Windows CMD:**

```cmd
venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the Framework

Display available command-line options:

```bash
python main.py --help
```

## 6. Usage

SNIT Recon accepts a target domain as a positional command-line argument.

### Basic Reconnaissance

```bash
python main.py example.com
```

This executes all integrated reconnaissance modules.

### Example Using an Authorized Domain

```bash
python main.py yourdomain.com
```

### Generated Reports

After successful execution, reports are saved in the `reports/` directory.

```text
reports/
├── example_com.html
└── example_com.txt
```

The HTML report provides a readable assessment summary, while the TXT report provides a text-based record of the collected results.

## 7. Security and Authorization Disclaimer

SNIT Reconnaissance Framework is developed for educational purposes, cybersecurity training, research, and authorized security assessments.

- Use the framework only against systems you own or have explicit permission to assess.
- Obtain authorization before performing network scanning or service identification.
- Respect applicable laws, organizational policies, and third-party service terms.
- Avoid using reconnaissance results to access, exploit, or disrupt unauthorized systems.

The developers are not responsible for misuse or unauthorized activities conducted using this framework.

## 8. Author

**SNIT Training Institute**

GitHub: https://github.com/snitmycloud

Project: SNIT Reconnaissance Framework

**Developed for Cybersecurity Education, Practical Training, and Authorized Security Assessment.**
