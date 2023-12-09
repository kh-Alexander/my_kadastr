from selenium import webdriver
from fake_useragent import UserAgent  # pip3 install fake-useragent
import time
from random import choice
import csv
from itertools import zip_longest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as econ

# ua = UserAgent()
# userAgent = ua.random
# print(userAgent)
#
# # выбираем proxy из файла proxies случайным образом
#
# try:
#     with open('proxies') as f:
#         proxies = []
#         for i in f:
#             x = ''.join(i)
#             proxies.append(x)
# except Exception as e:
#     print(e)
# proxy = choice(proxies)
# print(proxy)
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(f'--proxies-server={proxy}')
# chrome_options.add_argument(f'user-agent={userAgent}')

# driver = webdriver.Chrome(options=chrome_options, executable_path="/home/alex/programs/chromedriver")
driver = webdriver.Chrome('/home/alex/programs/chromedriver')

driver.get('http://www.google.com/')

driver.implicitly_wait(15)

driver.get("https://mail.google.com/mail/u/0/#inbox")
driver.implicitly_wait(15)

driver.get("https://accounts.google.com/AccountChooser?service=mail&amp;continue=https://mail.google.com/mail/")

wait = WebDriverWait(driver, 10)



time.sleep(7200)
driver.quit()

#
# if __name__ == '__main__':
#     main()
