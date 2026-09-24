🛡️ ShieldCheck – Website Security Assessment Tool

ShieldCheck is a lightweight web-based cybersecurity tool designed to perform a safe and non-intrusive security assessment of websites.

The tool analyzes a given website URL for HTTPS configuration and important HTTP security headers, then generates a security score, risk level, and recommendations based on the detected security configurations.

📌 Project Overview

Website security depends not only on application-level security but also on proper server and HTTP security configurations.

ShieldCheck provides a simple way to check commonly used security configurations without performing any intrusive or harmful testing.

🔍 What ShieldCheck Checks

- HTTPS configuration
- Content-Security-Policy (CSP)
- Strict-Transport-Security (HSTS)
- X-Frame-Options
- X-Content-Type-Options
- Referrer-Policy
- X-XSS-Protection header presence

The tool provides the results in an easy-to-understand dashboard.

✨ Features

- 🔗 Website URL validation
- 🔒 HTTPS security check
- 🛡️ HTTP security header analysis
- 📊 Security score out of 100
- ⚠️ Risk level identification
- 💡 Security recommendations
- 📋 Detailed security check results
- ⚡ Simple and responsive web interface
- 🔍 Safe and non-intrusive scanning

🏗️ Project Structure

ShieldCheck/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   │
│   └── scanner/
│       ├── __init__.py
│       ├── url_validator.py
│       ├── security_scanner.py
│       └── score_calculator.py
│
└── frontend/
    ├── templates/
    │   ├── index.html
    │   └── results.html
    │
    └── static/
        ├── style.css
        └── script.js

⚙️ Technologies Used

Technology| Purpose
Python| Backend programming
Flask| Web application framework
Requests| HTTP requests and header analysis
HTML| Webpage structure
CSS| User interface and styling
JavaScript| Client-side interaction

🔄 Working Process

Enter Website URL
        ↓
   URL Validation
        ↓
   Website Request
        ↓
 HTTPS & Header Checks
        ↓
   Security Analysis
        ↓
 Score Calculation
        ↓
 Risk Level + Recommendations

📊 Security Score

ShieldCheck calculates a score based on the presence of selected security configurations.

Security Check| Score
HTTPS| 20
Content-Security-Policy| 20
Strict-Transport-Security| 20
X-Frame-Options| 15
X-Content-Type-Options| 15
Referrer-Policy| 10
X-XSS-Protection| Informational

Total Score: 100

«Note: "X-XSS-Protection" is treated as an informational header because it is a legacy/deprecated browser security mechanism. Modern applications generally rely on protections such as Content-Security-Policy.»

🚦 Risk Levels

Score| Risk Level
90–100| Excellent
70–89| Good
40–69| Moderate
0–39| Poor

🚀 Installation & Setup

1. Clone the Repository

git clone https://github.com/YOUR-USERNAME/ShieldCheck.git
cd ShieldCheck

2. Create a Virtual Environment

python -m venv venv

3. Activate the Virtual Environment

Windows:

venv\Scripts\activate

4. Install Dependencies

cd backend
pip install -r requirements.txt

5. Run the Application

python app.py

6. Open in Browser

http://127.0.0.1:5000

🧪 Example

Enter a website URL such as:

https://example.com

ShieldCheck analyzes the website configuration and displays:

- HTTPS status
- Security header status
- Security score
- Risk level
- Missing security configurations
- Recommendations

🔐 Security Scope

ShieldCheck is intentionally designed as a non-intrusive security assessment tool.

It does not perform:

- ❌ SQL Injection attacks
- ❌ Cross-Site Scripting attacks
- ❌ Brute-force attacks
- ❌ Password attacks
- ❌ DDoS attacks
- ❌ Port scanning
- ❌ Exploitation
- ❌ Unauthorized access

The project focuses on analyzing publicly accessible HTTP/HTTPS configuration information.

🎯 Project Objectives

- To understand basic website security configurations.
- To analyze HTTP security headers.
- To understand the importance of HTTPS.
- To calculate a simple website security score.
- To provide security recommendations through a user-friendly interface.
- To demonstrate practical implementation of cybersecurity concepts.

👩‍💻 Academic Project

Project: ShieldCheck – Website Security Assessment Tool
Course: BSc Cybersecurity
Project Type: Academic Mini Project

📄 Disclaimer

ShieldCheck is developed for educational and authorized security assessment purposes only.

Users should scan only websites they own or have permission to assess. The tool is designed for safe configuration analysis and does not attempt to exploit vulnerabilities or gain unauthorized access.

⭐ Future Enhancements

Possible future improvements include:

- Additional security header checks
- SSL/TLS configuration analysis
- Detailed security reports
- PDF report generation
- Scan history
- Improved security recommendations
- More advanced website security configuration analysis

---

🛡️ ShieldCheck

A simple approach to understanding website security configurations.