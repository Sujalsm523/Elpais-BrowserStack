import requests
from app.utils.config import TRANSLATE_URL

def translate(text):
    try:
        params = {
            "client": "gtx",
            "sl": "es",
            "tl": "en",
            "dt": "t",
            "q": text
        }
        r = requests.get(TRANSLATE_URL, params=params, timeout=10)
        return r.json()[0][0][0]
    except:
        return text
