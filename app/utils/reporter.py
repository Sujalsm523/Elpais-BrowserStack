import json
import os
from datetime import datetime
from app.utils.config import REPORT_DIR

os.makedirs(REPORT_DIR, exist_ok=True)

def save_report(data):
    filename = REPORT_DIR / f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    
    return str(filename)
