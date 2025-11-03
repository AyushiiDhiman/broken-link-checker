# 🔗 Broken Link Automation Checker  
### ✅ Python | Selenium | Requests | PyTest 

This project automatically scans any website for **broken, working, redirected, and timeout** links.  
It opens the website in a real browser using Selenium, extracts all `<a>` tags, validates their HTTP responses using Python’s Requests library, and generates **professional CSV + HTML reports**.

This is a beginner-friendly but industry-relevant automation project widely used in **UI testing**, **SEO audits**, and **web quality assurance**.

---

## ✅ Features

- ✅ **Extracts all hyperlinks** from any webpage  
- ✅ Detects **broken links (4xx, 5xx)**  
- ✅ Detects **working links (2xx)**  
- ✅ Detects **redirected links (3xx)**  
- ✅ Detects **timeout or unreachable URLs**  
- ✅ Generates **CSV report** (easy for analysis)  
- ✅ Generates **color-coded HTML report** (professional QA report)  
- ✅ Supports **command-line URL input**  
- ✅ Fully automated using **PyTest**  
- ✅ Beginner friendly + resume ready  

---

## ✅ Project Architecture

```
broken-link-checker/
│── drivers/
│   └── chromedriver.exe
│── reports/
│   ├── broken_links_report.csv
│── tests/
│   └── test_broken_links.py
│── requirements.txt
│── README.md
```

---

## ✅ Installation Guide

### 1️⃣ Clone the repository
```bash
git clone https://github.com/AyushiiDhiman/broken-link-checker.git
cd broken-link-checker
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Download ChromeDriver  
Make sure the ChromeDriver version matches your installed Chrome browser.  
Place the `.exe` file inside:

```
drivers/chromedriver.exe
```

---

## ✅ How to Run the Test

### ▶️ **Run with default website (practicetestautomation.com)**
```bash
pytest -s
```

### ▶️ **Run for ANY website (recommended)**
```bash
pytest -s -- https://google.com
```

---

## ✅ Sample Output Reports

### 📍 CSV Report (broken_links_report.csv)
```
URL,Status,Code
https://example.com,WORKING,200
https://broken-link.com,BROKEN,404
https://redirect.com,REDIRECT,301
```

### 📍 HTML Report (broken_links_report.html)

✅ Green → Working  
✅ Red → Broken  
✅ Yellow → Timeout/Redirect  

These reports help testers, developers, and SEO analysts understand link health easily.

---

## ✅ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.x** | Core scripting |
| **Selenium WebDriver** | Browser automation |
| **Requests Library** | HTTP status checking |
| **PyTest** | Test execution framework |
| **Pandas** | CSV generation |
| **Jinja2** | HTML report rendering |

---

## ✅ Why This Project Is Useful

✔ Helps identify broken links hurting user experience  
✔ Helps improve SEO & website quality  
✔ Validates large websites automatically  
✔ Practical project for QA internships  
✔ Strengthens Python + Selenium skills  

---

## ✅ Future Enhancements (If You Want to Improve Later)

- [ ] Support for multi-page crawling  
- [ ] Screenshot capture for broken pages  
- [ ] PDF report generation  
- [ ] Run tests in headless browser  
- [ ] Integrate with GitHub Actions for CI/CD  

---

## ✅ Professional Resume Description

**Broken Link Automation Checker (Python, Selenium, PyTest)**  
Developed a browser-based automation tool that scans webpages for broken, redirected, and timeout links using Selenium and the Requests API. Implemented command-line URL input, auto-generated HTML/CSV reports, and integrated PyTest for execution. Enhanced debugging by differentiating link statuses using color-coded reporting.

---

## ✅ Author

**Ayushi Dhiman**  
Automation & Testing Enthusiast  
📌 GitHub: https://github.com/AyushiiDhiman

If you like the project, ⭐ the repository!

 

---


