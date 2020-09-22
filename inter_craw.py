import pandas as pd
import random
import os
from selenium import webdriver  # 從library中引入webdriver
# from selenium.webdriver.common.by import By
from fake_useragent import UserAgent # !pip install fake-useragent
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options
import time
import urllib
import argparse
pd.set_option('display.max_rows', 250)

# 這邊修改成輸入你的臉書帳號及密碼
ac = 'your_fb_email'
pw = 'your_fb_password'

ua = UserAgent(verify_ssl=False)
user_agent = ua.random
options = Options()
options.add_argument("window-size=800,800")
options.add_argument(f'user-agent={user_agent}')
print(user_agent)

browser = webdriver.Chrome('./chromedriver', options=options)
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

########開始填寫

company = browser.find_element_by_xpath('//*[@id="iw-autocomplete"]')
company.click()
company.send_keys('中央研究院')
time.sleep(5)
sinica = browser.find_element_by_xpath('//*[@id="step1"]/div[1]/div[2]/div/div[1]')
sinica.click()

# company_code = browser.find_element_by_xpath('//*[@id="step1"]/div[2]/div[2]/div[3]/input')
# # company_code.click()
# company_code[0].send_keys('03811209')

job_title = browser.find_element_by_xpath('//*[@id="jobTitle"]')
job_title.click()
job_title.send_keys('研究助理')

city = browser.find_element_by_xpath('//*[@id="select-city"]/option[2]')
city.click()

date_time = browser.find_element_by_xpath('//*[@id="step1"]/div[5]/div[2]/input')
date_time.click()
jan = browser.find_element_by_xpath('//*[@id="datepickers-container"]/div/div/div/div/div[1]')
jan.click()

rate = browser.find_element_by_xpath('//*[@id="iw_rating"]/div[3]/label')
rate.click()

difficulty = browser.find_element_by_xpath('//*[@id="step1"]/div[7]/div[2]/div[3]/label')
difficulty.click()

result = browser.find_element_by_xpath('//*[@id="step1"]/div[8]/div[2]/div[1]/label')
result.click()

language = browser.find_element_by_xpath('//*[@id="choice1"]')
language.click()

exam = browser.find_element_by_xpath('//*[@id="hasTest2"]')
exam.click()

next_time = browser.find_element_by_xpath('//*[@id="nextTime2"]')
next_time.click()

how_long = browser.find_element_by_xpath('//*[@id="howLong1"]')
how_long.click()

nextPage = browser.find_element_by_xpath('//*[@id="step1"]/div[13]/button')
nextPage.click()

process = browser.find_element_by_xpath('//*[@id="inputTextProcess"]')
process.click()
process.send_keys('中央研究院是個古色古香的地方，非常適合學者做研究。基本上你來到這邊辦理完老師交代的事項，很多時間可以做自己的事情，非常適合想要出國深造的人當作跳板。')

question = browser.find_element_by_xpath('//*[@id="inputTextAskedTitle"]')
question.click()
question.send_keys('研究問題與興趣')

answer = browser.find_element_by_xpath('//*[@id="inputTextAskedContent"]')
answer.click()
answer.send_keys('照本宣科回答自己的研究問題。儘量跟老師的領域符合，不要老師專長是總體，你卻想要做應用個體，老師應該會傻眼貓咪。')

advice = browser.find_element_by_xpath('//*[@id="inputTextSuggestions"]')
advice.click()
advice.send_keys('中研院處在一個地靈人傑的地方，很適合寫讀書計畫與做研究，也可以學到很多東西，好好做努力做，老師不會虧待你的（幫忙寫推薦信）。')

share = browser.find_element_by_xpath('//*[@id="step2"]/div[4]/button')
share.click()

submit = browser.find_element_by_xpath('//*[@id="submitModal"]/div/div[3]/button[2]')
submit.click()

browser.close()