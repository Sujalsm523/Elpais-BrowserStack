from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from app.utils.config import BS_URL

def create_driver(mode="local", capability=None):
    if mode == "local":
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        return webdriver.Chrome(options=options)

    elif mode == "browserstack":
        options = Options()
        options.set_capability("bstack:options", {
            "projectName": "ElPais Assignment",
            "buildName": "Parallel Cross Browser",
            **capability
        })
        return webdriver.Remote(command_executor=BS_URL, options=options)
