import os
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

ROOT_PATH = Path(__file__).parent.parent


def make_chrome_browser(*options):
    chrome_options = webdriver.ChromeOptions()

    for option in options:
        chrome_options.add_argument(option)

    selenium_headless = os.environ.get('SELENIUM_HEADLESS', '1')
    if selenium_headless != '0':
        chrome_options.add_argument('--headless=new')

    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-background-networking')
    chrome_options.add_argument('--disable-features=Translate,BackForwardCache')
    chrome_options.add_argument('--remote-allow-origins=*')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--disable-popup-blocking')

    for attempt in range(2):
        try:
            return webdriver.Chrome(options=chrome_options)
        except WebDriverException:
            if attempt == 1:
                raise
            sleep(1)


if __name__ == '__main__':
    browser = make_chrome_browser('--headless')
    browser.get('http://www.udemy.com/')
    sleep(5)
    browser.quit()
