import argparse
import logging
import json
from concurrent.futures import ThreadPoolExecutor

from app.browser.browser_factory import create_driver
from app.services.scraper import get_article_links, scrape_article
from app.services.translator import translate
from app.services.analyzer import repeated_words
from app.utils.reporter import save_report
from app.utils.config import BROWSERSTACK_CAPS

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
def run_test(mode="local", capability=None):

    # -------- Identify Environment --------
    if mode == "browserstack" and capability:
        if "deviceName" in capability:
            env_name = f"{capability['deviceName']} (OS {capability.get('osVersion', '')})"
        else:
            env_name = f"{capability.get('os', '')} {capability.get('osVersion', '')} - {capability.get('browserName', '')}"
    else:
        env_name = "Local Machine"

    driver = create_driver(mode, capability)
    result = {"environment": env_name, "articles": [], "translated_titles": []}
    status = "passed"
    reason = "Test executed successfully"

    # Collect logs instead of printing immediately
    env_logs = []
    env_logs.append(f"\n\n========== Environment: {env_name} ==========")

    try:
        links = get_article_links(driver)

        for i, link in enumerate(links):
            article = scrape_article(driver, link, i+1)
            translated = translate(article["title_es"])

            env_logs.append(f"\nArticle {i+1}")
            env_logs.append(f"Title (ES): {article['title_es']}")
            
            # Limit content to first 200 characters (clean)
            content_preview = article['content_es'][:200].replace("\n", " ")
            env_logs.append(f"Content (ES): {content_preview}...")
            
            env_logs.append(f"Title (EN): {translated}")

            result["articles"].append(article)
            result["translated_titles"].append(translated)

        # Repeated words
        repeated = repeated_words(result["translated_titles"])
        result["repeated_words"] = repeated

        if repeated:
            env_logs.append("\nRepeated words (count >= 2):")
            for word, count in repeated.items():
                env_logs.append(f"{word}: {count}")
        else:
            env_logs.append("No repeated words found")
    except Exception as e:
            status = "failed"
            reason = str(e)
    finally:
        if driver:
        # Set BrowserStack status only for remote sessions
            if mode == "browserstack":
                try:
                    driver.execute_script(
                    'browserstack_executor: ' + json.dumps({
                        "action": "setSessionStatus",
                        "arguments": {
                            "status": status,
                            "reason": reason
                        }
                    })
                )
                except Exception:
                    pass  

        try:
            driver.quit()
        except Exception:
            pass

        env_logs.append(f"========== Completed: {env_name} ==========\n")

    # Print logs together (no interleaving)
    for line in env_logs:
        logging.info(line)

    return result
def run_parallel_browserstack():
    all_results = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [
            executor.submit(run_test, "browserstack", cap)
            for cap in BROWSERSTACK_CAPS
        ]

        for f in futures:
            all_results.append(f.result())

    report_file = save_report(all_results)
    logging.info(f"Report saved: {report_file}")

def run_local():
    result = run_test("local")
    report_file = save_report(result)
    logging.info(f"Local report saved: {report_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["local", "browserstack"], default="local")
    args = parser.parse_args()

    if args.mode == "browserstack":
        run_parallel_browserstack()
    else:
        run_local()
