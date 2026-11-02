#!/usr/bin/env python3
"""Wait for a manual Hacker News login, then submit the Show HN and first comment.

Keeps the Marionette session alive while the user logs in, so the browser is
not restarted and session cookies are not lost.
"""

from __future__ import annotations

import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

TITLE = "Show HN: Spyware detection tools and the caveats that matter"
URL = "https://github.com/ranjithrajv/awesome-spyware-detection"
COMMENT = (
    "I kept seeing the same failure mode: someone reads a spyware story, runs one tool, "
    "gets a clean result, and concludes they're safe. This list puts the tools next to what "
    "each one can actually examine, plus a printable handout for trainers and helplines.\n\n"
    "Two things I'd like feedback on: which Windows and macOS stalkerware resources are "
    "missing, and whether the \"a hit means\" column is honest enough.\n\n"
    "(No affiliation with any listed vendor; the list is CC0.)"
)

service = Service(
    executable_path=".venv-reddit/bin/geckodriver",
    service_args=["--connect-existing", "--marionette-port", "2828"],
)
driver = webdriver.Firefox(service=service, options=Options())
driver.set_page_load_timeout(40)


def logged_in() -> bool:
    cookies = {c["name"] for c in driver.get_cookies()}
    if "user" in cookies:
        return True
    return "news.ycombinator.com/news" in driver.current_url or driver.current_url.endswith("/news")


driver.get("https://news.ycombinator.com/login?goto=news")
print("waiting for manual login at:", driver.current_url, flush=True)

deadline = time.time() + 20 * 60
while time.time() < deadline:
    if logged_in():
        print("login detected", flush=True)
        break
    time.sleep(3)
else:
    print("timeout waiting for login", flush=True)
    sys.exit(1)

driver.get("https://news.ycombinator.com/submit")
time.sleep(1)
if "login" in driver.current_url:
    print("still on login page; aborting", flush=True)
    sys.exit(1)

driver.find_element(By.NAME, "title").send_keys(TITLE)
driver.find_element(By.NAME, "url").send_keys(URL)
driver.find_element(By.CSS_SELECTOR, "input[type=submit][value=submit]").click()
time.sleep(4)
print("after submit:", driver.current_url, flush=True)
body = driver.find_element(By.TAG_NAME, "body").text
print(body[:400].replace("\n", " | "), flush=True)

# Find the item URL on the newest page.
driver.get("https://news.ycombinator.com/newest")
time.sleep(2)
item = None
for link in driver.find_elements(By.CSS_SELECTOR, "a"):
    try:
        if link.text.strip() == TITLE:
            item = link.get_attribute("href")
            break
    except Exception:
        continue
print("item:", item, flush=True)
if not item:
    print("could not locate submitted item", flush=True)
    sys.exit(2)

driver.get(item)
time.sleep(2)
driver.find_element(By.NAME, "text").send_keys(COMMENT)
driver.find_element(By.CSS_SELECTOR, "input[type=submit][value='add comment']").click()
time.sleep(4)
print("final:", driver.current_url, flush=True)
print("done", flush=True)
driver.quit()
