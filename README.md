

El País Opinion Scraper – BrowserStack Automation

Overview

This project automates the extraction and analysis of articles from the El País Spanish news website using Selenium.

The solution demonstrates:
	•	Web scraping and browser automation
	•	Image download and file handling
	•	Translation API integration
	•	Text analysis
	•	Parallel cross-browser execution using BrowserStack

⸻

Features

1. Website Validation
	•	Opens the El País website.
	•	Verifies that the page language is Spanish (lang="es").

⸻

2. Opinion Section Scraping
	•	Navigates to the Opinion section.
	•	Fetches the first 5 articles.
	•	Extracts:
	•	Title (Spanish)
	•	Content (Spanish)
	•	Cover image (if available)

Images are saved locally.

⸻

3. Title Translation
	•	Translates article titles from Spanish to English using Google Translate API.
	•	Prints translated titles for each article.

⸻

4. Text Analysis
	•	Combines all translated titles.
	•	Identifies words that appear more than twice across all titles.
	•	Prints each repeated word with its occurrence count.
	•	Displays a message if no such words are found.

⸻

5. Cross-Browser Execution (BrowserStack)

The solution runs in parallel across 5 environments:

Desktop
	•	Windows 11 – Chrome
	•	Windows 10 – Edge
	•	macOS Monterey – Firefox

Mobile
	•	iPhone 14 (iOS 16)
	•	Samsung Galaxy S22 (Android 12)

Each environment:
	•	Executes independently
	•	Logs results separately
	•	Generates a structured JSON report

⸻

Project Structure

elpais-browserstack/
│
├── app/
│   ├── browser/
│   │   └── driver_factory.py      # Local & BrowserStack driver setup
│   │
│   ├── services/
│   │   ├── scraper.py             # Article scraping logic
│   │   ├── translator.py          # Title translation
│   │   └── analyzer.py            # Repeated word analysis
│   │
│   ├── utils/
│   │   └── reporter.py            # JSON report generation
│   │
│   ├── config.py                  # Environment configuration
│   └── runner.py                  # Execution logic
│
├── data/
│   ├── images/                    # Downloaded article images
│   └── reports/                   # Execution reports
│
├── main.py                        # Entry point
├── requirements.txt
├── .env.example
└── README.md


⸻

Setup Instructions

1. Clone the Repository

git clone <your-repo-url>
cd elpais-browserstack


⸻

2. Install Dependencies

pip install -r requirements.txt


⸻

3. Configure BrowserStack Credentials

Create a .env file in the root directory:

BS_USERNAME=your_browserstack_username
BS_ACCESS_KEY=your_browserstack_access_key

Get credentials from:
https://www.browserstack.com/accounts/settings

⸻

Running the Project

Run Locally

python main.py --mode local


⸻

Run on BrowserStack (Parallel)

python main.py --mode browserstack


⸻

Sample Output

========== Environment: Windows 11 - Chrome ==========

Article 1
Title (ES): Catástrofe en la ayuda al desarrollo
Content (ES): Los drásticos recortes de Trump...
Title (EN): Catastrophe in development aid

Repeated words (count > 2):
No words repeated more than twice

========== Completed: Windows 11 - Chrome ==========


⸻

Generated Artifacts
	•	Images → data/images/
	•	Reports → data/reports/report_<timestamp>.json
	•	BrowserStack sessions → Available in Automate Dashboard

Dashboard:
https://automate.browserstack.com/dashboard

Each session includes:
	•	OS / Device details
	•	Browser information
	•	Execution logs
	•	Video recording

⸻

Technical Highlights
	•	Selenium WebDriver (Local + Remote)
	•	Parallel execution using ThreadPoolExecutor
	•	Environment-based configuration (.env)
	•	Production-style project structure
	•	Robust image handling (JPEG / PNG / WebP / AVIF)
	•	Clean environment-wise logging
	•	Structured JSON reporting

⸻

Author

Sujal More
