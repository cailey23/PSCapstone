import os

from moviepy.editor import VideoFileClip
from selenium import webdriver
from selenium.webdriver.common.by import By


def upload_video(video_name):
    while os.path.getsize(video_name)> 85*1000000:
        video = VideoFileClip(video_name)
        video_resized = video.resize(0.7)
        video_name="video_resized.mp4"
        video_resized.write_videofile(video_name)
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    browser = webdriver.Chrome('chromedriver', options=options)
    browser.get('https://www.rit.edu/marketing/utilities/feeds/time-lapse/')

    files = browser.find_element(By.NAME, 'files[]')
    submit= browser.find_element(By.NAME, 'submit')
    files.send_keys([video_name])
    submit.click()
    # elem.send_keys('seleniumhq' + Keys.RETURN)
    browser.quit()