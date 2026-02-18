import os
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.utils.config import BASE_URL, IMAGE_DIR

os.makedirs(IMAGE_DIR, exist_ok=True)


def ensure_spanish(driver):
    lang = driver.find_element(By.TAG_NAME, "html").get_attribute("lang")
    if not lang.startswith("es"):
        raise Exception("Website not in Spanish")


def get_article_links(driver):
    driver.get(BASE_URL)

    # Wait for articles to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "article"))
    )

    ensure_spanish(driver)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    links = []
    articles = soup.find_all("article")

    for art in articles:
        h2 = art.find("h2")
        if h2:
            a = h2.find("a", href=True)
            if a:
                url = a["href"]
                if not url.startswith("http"):
                    url = "https://elpais.com" + url
                links.append(url)

        if len(links) == 5:
            break

    return links


def scrape_article(driver, url, index):
    driver.get(url)

    # Wait for article title
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )

    soup = BeautifulSoup(driver.page_source, "html.parser")

    # --- Title ---
    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else "No title"

    # --- Content ---
    paragraphs = soup.select("article p")
    content = " ".join([p.get_text(strip=True) for p in paragraphs])

        # --- Image extraction (robust) ---
    image_path = None

    # Try to get main article image
    img_url = None

    figure = soup.find("figure")
    if figure:
        img = figure.find("img")
        if img:
            img_url = (
                img.get("src")
                or img.get("data-src")
            )

            # If srcset exists, take highest resolution
            if not img_url and img.get("srcset"):
                img_url = img["srcset"].split(",")[-1].split(" ")[0]

    # Download image
    if img_url and img_url.startswith("http"):
        try:
            headers = {
                "User-Agent": "Mozilla/5.0"
            }

            response = requests.get(img_url, headers=headers, timeout=10)

            if response.status_code == 200:
                content_type = response.headers.get("Content-Type", "")

                # Determine extension dynamically
                if "jpeg" in content_type or "jpg" in content_type:
                    ext = "jpg"
                elif "png" in content_type:
                    ext = "png"
                elif "webp" in content_type:
                    ext = "webp"
                elif "avif" in content_type:
                    ext = "avif"
                else:
                    ext = "jpg"

                image_path = f"{IMAGE_DIR}/article_{index}.{ext}"

                with open(image_path, "wb") as f:
                    f.write(response.content)

        except Exception:
            image_path = None

    return {
        "title_es": title,
        "content_es": content,
        "image": image_path
    }