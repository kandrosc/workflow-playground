from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

import pickle
import os

OPTIONS = Options()
OPTIONS.add_argument('--headless')
OPTIONS.add_argument('--no-sandbox')
OPTIONS.add_argument('--disable-dev-shm-usage')
OPTIONS.add_argument('--allow-running-insecure-content')
class ClassNotFoundError(Exception): pass


FILEPATH = os.path.dirname(os.path.abspath(__file__))+"/"

if __name__ == "__main__":
    url = "http://[2605:fd00:4:1001:f816:3eff:fe53:c1c4]/memoryGame/"
    r = requests.get(url)
    print(r.text)
    browser = webdriver.Chrome(FILEPATH+"lin_chromedriver",options=OPTIONS)
    browser.get(url)
    browser.close()