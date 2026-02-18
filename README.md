# El País Opinion Scraper – BrowserStack Automation

## Overview

This project automates the extraction and analysis of articles from the **El País** Spanish news website using Selenium.

The solution demonstrates:

- Web automation and scraping
- Image downloading and file handling
- Translation API integration
- Text processing and analysis
- Parallel cross-browser execution using BrowserStack

---

## Assignment Requirements Covered

### 1. Website Validation
- Opens the El País website
- Verifies that the page language is Spanish (`lang="es"`)

---

### 2. Scrape Opinion Articles
- Navigates to the **Opinion** section
- Fetches the **first 5 articles**
- Extracts:
  - Title (Spanish)
  - Content (Spanish)
  - Cover image (if available)

Images are saved locally in the `data/images/` directory.

---

### 3. Translate Article Titles
- Uses Google Translate API
- Translates titles from **Spanish to English**
- Prints translated titles

---

### 4. Analyze Translated Headers
- Combines all translated titles
- Identifies words that appear **more than twice** across all titles
- Prints each repeated word along with its occurrence count
- Displays a message if no such words are found

---

### 5. Cross-Browser Testing (BrowserStack)

The solution runs in parallel across **5 environments**:

**Desktop**
- Windows 11 – Chrome  
- Windows 10 – Edge  
- macOS Monterey – Firefox  

**Mobile**
- iPhone 14 (iOS 16)  
- Samsung Galaxy S22 (Android 12)  

Each environment:
- Executes independently
- Logs results separately
- Generates structured output

---

## Project Structure

```
elpais-browserstack/
│
├── app/
│   ├── browser/
│   │   └── driver_factory.py
│   │
│   ├── services/
│   │   ├── scraper.py
│   │   ├── translator.py
│   │   └── analyzer.py
│   │
│   ├── utils/
│   │   └── reporter.py
│   │
│   ├── config.py
│   └── runner.py
│
├── data/
│   ├── images/
│   └── reports/
│
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Sujalsm523/Elpais-BrowserStack/
cd elpais-browserstack
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Configure BrowserStack Credentials

Create a `.env` file in the project root:

```
BS_USERNAME=your_browserstack_username
BS_ACCESS_KEY=your_browserstack_access_key
```

Get your credentials from:  
https://www.browserstack.com/accounts/settings

---

## Running the Project

### Run Locally

```bash
python main.py --mode local
```

---

### Run on BrowserStack (Parallel Execution)

```bash
python main.py --mode browserstack
```

---

## Sample Output

```
========== Environment: Windows 11 - Chrome ==========

Article 1
Title (ES): Catástrofe en la ayuda al desarrollo
Content (ES): Los drásticos recortes de Trump...
Title (EN): Catastrophe in development aid

Repeated words (count > 2):
No words repeated more than twice

========== Completed: Windows 11 - Chrome ==========
```

---

## Generated Artifacts

- Downloaded images → `data/images/`
- Execution reports → `data/reports/report_<timestamp>.json`
- BrowserStack sessions → https://automate.browserstack.com/dashboard

Each session includes:
- OS / Device details
- Browser information
- Execution logs
- Video recording

---

## Technical Highlights

- Selenium WebDriver (Local + Remote)
- Parallel execution using `ThreadPoolExecutor`
- Environment-based configuration using `.env`
- Production-style modular architecture
- Robust image handling (JPEG / PNG / WebP / AVIF)
- Clean environment-wise logging
- Structured JSON reporting

---

## Author

**Sujal More**  
