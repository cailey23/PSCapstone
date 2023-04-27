import time
import unittest

import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



def upload_video(video_name):
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    # options.add_argument("disable-gpu")

    browser = webdriver.Chrome('chromedriver', options=options)
    browser.get('https://www.rit.edu/marketing/utilities/feeds/time-lapse/')

    files = browser.find_element(By.NAME, 'files[]')
    submit= browser.find_element(By.NAME, 'submit')
    files.send_keys([video_name])
    submit.click()
    # elem.send_keys('seleniumhq' + Keys.RETURN)
    time.sleep(30)
    browser.quit()