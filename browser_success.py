from selenium import webdriver
import pickle
import os

class ClassNotFoundError(Exception): pass


FILEPATH = os.path.dirname(os.path.abspath(__file__))+"/"

if __name__ == "__main__":
    url = "http://[2605:fd00:4:1001:f816:3eff:fe53:c1c4]/memoryGame/"
    browser = webdriver.Chrome(FILEPATH+"lin_chromedriver")
    browser.get(url)
    cookies = pickle.load(open(FILEPATH+"cookies.pkl","rb"))
    for cookie in cookies: browser.add_cookie(cookie)