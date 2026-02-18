import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

BASE_URL = "https://elpais.com/opinion/"
TRANSLATE_URL = "https://translate.googleapis.com/translate_a/single"

BS_USERNAME = os.getenv("BS_USERNAME")
BS_ACCESS_KEY = os.getenv("BS_ACCESS_KEY")
BS_URL = f"https://{BS_USERNAME}:{BS_ACCESS_KEY}@hub.browserstack.com/wd/hub"

BROWSERSTACK_CAPS = [
    {"browserName": "Chrome", "browserVersion": "latest", "os": "Windows", "osVersion": "11"},
    {"browserName": "Firefox", "browserVersion": "latest", "os": "OS X", "osVersion": "Monterey"},
    {"browserName": "Edge", "browserVersion": "latest", "os": "Windows", "osVersion": "10"},
    {"deviceName": "iPhone 14", "realMobile": "true", "osVersion": "16"},
    {"deviceName": "Samsung Galaxy S22", "realMobile": "true", "osVersion": "12"}
]

BASE_DIR = Path(__file__).resolve().parent.parent

# Data directories
DATA_DIR = BASE_DIR / "data"
IMAGE_DIR = DATA_DIR / "images"
REPORT_DIR = DATA_DIR / "reports"

# Create directories if they don't exist
IMAGE_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

