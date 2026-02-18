
📦 El País BrowserStack Automation

A Python-based automation project that scrapes articles from the El País Spanish news site and runs browser automation tests in parallel across multiple environments using Selenium and BrowserStack.

🚀 Overview

This solution demonstrates:
	•	🕸️ Web scraping & browser automation
	•	🖼️ Image download and local storage
	•	🌐 Translation API integration (Spanish → English)
	•	🧠 Text analysis (word frequency)
	•	📊 Parallel cross-browser execution on BrowserStack
	•	📦 Structured JSON reporting

⸻

🧱 Features
	1.	Website Validation
Loads and verifies El País homepage with proper Spanish language detection.
	2.	Opinion Section Scraping
	•	Navigates to the Opinion section
	•	Fetches the first 5 articles
	•	Extracts titles, contents, and cover images
	3.	Title Translation
Uses Google Translate API to convert Spanish article titles to English.
	4.	Text Analysis
Combines all translated titles and highlights repeated words with counts.
	5.	Cross-Browser Execution (BrowserStack)
Runs tests in parallel across 5 environments:
Desktop
	•	Windows 11 — Chrome
	•	Windows 10 — Edge
	•	macOS Monterey — Firefox
Mobile
	•	iPhone 14 (iOS 16)
	•	Samsung Galaxy S22 (Android 12)
Each run logs results separately and produces a JSON report.

⸻

📂 Project Structure

elpais-browserstack/
├── app/
│   ├── browser/
│   │   └── driver_factory.py      # Local & BrowserStack driver setup
│   ├── scraper.py                 # Web scraping logic
│   ├── translator.py              # Title translation using API
│   ├── analyzer.py                # Text frequency analyzer
│   ├── utils/
│   ├── reporter.py                # JSON report generation
│   └── config.py                  # Environment configuration
├── data/
│   ├── images/                    # Downloaded article images
│   └── reports/                   # Generated execution reports
├── benv/                          # Python virtual environment
├── main.py                       # Main entry point
├── requirements.txt              # Dependencies
├── .env.example                  # Example env config
└── README.md                    # Project documentation


⸻

🛠️ Setup Instructions

1. Clone the Repository

git clone https://github.com/Sujalsm523/Elpais-BrowserStack.git
cd Elpais-BrowserStack

2. Install Dependencies

pip install -r requirements.txt

3. Configure Environment Variables

Create a .env file in the root:

BS_USERNAME=your_browserstack_username
BS_ACCESS_KEY=your_browserstack_access_key

Get your credentials from your BrowserStack account settings.

⸻

▶️ Running the Project

🧪 Local Execution

python main.py --mode local

This runs the scraper and analysis locally without BrowserStack.

⸻

☁️ Run on BrowserStack (Parallel)

python main.py --mode browserstack

This executes across multiple environments on .

⸻

🧾 Sample Output

========== Environment: Windows 11 - Chrome ==========
Article 1 Title (ES): Catástrofe en la ayuda al desarrollo
Content (ES): Los drásticos recortes de Trump...
Title (EN): Catastrophe in development aid

Repeated words (count > 2): No words repeated more than twice
========== Completed: Windows 11 - Chrome ==========


⸻

🧠 Technical Highlights
	•	Selenium WebDriver with local & remote drivers
	•	Parallel execution via ThreadPoolExecutor
	•	Environment-based configuration (.env)
	•	Robust image handling (JPEG / PNG / WebP / AVIF)
	•	Structured, environment-specific logging
	•	JSON reporting for automated test runs

⸻

🧑‍💻 Author

Sujal More

⸻
