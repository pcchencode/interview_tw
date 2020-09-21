import pandas as pd
import random
import os
from selenium import webdriver  # 從library中引入webdriver
# from selenium.webdriver.common.by import By
# from fake_useragent import UserAgent # !pip install fake-useragent
from selenium.webdriver.chrome.options import Options
import time
import urllib
import argparse
pd.set_option('display.max_rows', 250)

ac = 'your_fb_account'
pw = 'your_fb_password'

browser = webdriver.Chrome('./chromedriver')
browser.get('https://interview.tw')

button = browser.find_element_by_xpath('//*[@id="navbar-share-btn"]') #尋找登入點擊按鈕
button.click()

fb_login = browser.find_element_by_xpath('/html/body/div[12]/div/div/div/div[1]/div/div[2]/button[1]/img')
fb_login.click()

account = browser.find_elements_by_xpath('//*[@id="email"]')
account[0].send_keys(ac)

password = browser.find_elements_by_xpath('//*[@id="pass"]')
password[0].send_keys(pw)

button_login = browser.find_element_by_xpath('//*[@id="loginbutton"]') 
button_login.click()

########
company = browser.find_element_by_xpath('//*[@id="iw-autocomplete"]')
company.click()
company.send_keys('中央研究院')

company_code = browser.find_element_by_xpath('//*[@id="step1"]/div[2]/div[2]/div[3]/input')
# company_code.click()
company_code[0].send_keys('03811209')

job_title = browser.find_element_by_xpath('//*[@id="jobTitle"]')
job_title.click()
job_title.send_keys('研究助理')

city = browser.find_element_by_xpath('//*[@id="select-city"]/option[2]')
city.click()











