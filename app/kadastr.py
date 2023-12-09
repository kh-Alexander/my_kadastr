from selenium import webdriver
from fake_useragent import UserAgent  # pip3 install fake-useragent
import time
from random import choice
import csv
from itertools import zip_longest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as econ

ua = UserAgent()
userAgent = ua.random
print(userAgent)

# выбираем proxy из файла proxies случайным образом

try:
    with open('proxies') as f:
        proxies = []
        for i in f:
            x = ''.join(i)
            proxies.append(x)
except Exception as e:
    print(e)
proxy = choice(proxies)
print(proxy)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxies-server={proxy}')
chrome_options.add_argument(f'user-agent={userAgent}')

driver = webdriver.Chrome(options=chrome_options, executable_path="/home/alex/programs/chromedriver")

# Вход в браузер со своим proxy и userAgent

# driver = webdriver.Chrome('/home/alex/programs/chromedriver')

driver.get("https://spv.kadastr.ru/")
driver.implicitly_wait(15)

wait = WebDriverWait(driver, 30)


def my_kadastr():

    button = driver.find_element_by_xpath('//button[@class="btn btn-primary"]')
    time.sleep(3)
    print(button)
    button.click()
    time.sleep(3)
    try:
        elem = driver.find_element_by_name('login')
    except Exception as a:
        print(a)
        elem = driver.find_element_by_id('login')
    elem.clear()
    login = '113-562-732-34'
    elem.send_keys(login)
    time.sleep(3)
    try:
        elm = driver.find_element_by_name('password')
    except Exception as a:
        print(a)
        elm = driver.find_element_by_id('password')
    elm.clear()
    password = '+KNup"1X0fhn'
    elm.send_keys(password)
    time.sleep(1)

    # wait = WebDriverWait(driver, 30)

    # нажимаем на кнопку Войти

    try:
        wait.until(econ.element_to_be_clickable((By.XPATH, '//button[@id="loginByPwdButton"]'))).click()
    except Exception as a:
        print(a)

    # нажимаем на кнопку Заказы
    time.sleep(5)
    try:

        wait.until(
            econ.element_to_be_clickable((By.XPATH, '//ul[@class="header-user"]/li[4]/a'))).click()
    except Exception as a:
        print(a)
    time.sleep(10)


def my_actions():
    # Определяем количество страниц в Заказе

    try:
        pages = wait.until(
            econ.presence_of_all_elements_located((By.XPATH, '//li[@class="page-item"]')))
    except Exception as a:
        print(a)
        pages = ''
    print("pages", len(pages))

    # Определяем ордера

    try:
        orders_all = wait.until(
            econ.presence_of_all_elements_located((By.XPATH, '//div[@class="col-md-2 bis-appeal--value number"]/a[1]')))
    except Exception as a:
        print(a)
        orders_all = ''

    all_orders = []
    for k in orders_all:
        l = k.get_attribute('href').split('/')[4]
        lm = ''.join(l).split('?')[0] + ' '
        all_orders.append(lm)
    print('all_orders = ', all_orders)

    # Определяем Обработан, Ожидает оплату, Не оплачен

    try:
        status = wait.until(
            econ.presence_of_all_elements_located((By.XPATH, '//div[@class="row appealsrow block-card"]/div[2]')))
    except Exception as a:
        print(a)
        status = ''
    print('st', status)
    st_text = []
    for j in status:
        stt = j.text + '_'
        st_text.append(stt)
    print('st_text', st_text)

    # кликаем на загрузки

    try:
        zagruzka = wait.until(
            econ.presence_of_all_elements_located((By.XPATH, '//div[@class="col-md-1 bis-appeal--value load"]/a')))
    except Exception as a:
        print(a)
        zagruzka = ''
    for j in zagruzka:
        j.click()

    # Определяем цены

    try:
        price = wait.until(
            econ.presence_of_all_elements_located((By.XPATH, '//div[@class="container bis-appeal"]/div/div[5]')))
    except Exception as a:
        print(a)
        price = ''
    print('pr', len(price))
    price_text = []
    for j in price:
        t = j.get_attribute("textContent").split()
        tt = " ".join(t) + 'dd'
        print(tt)
        price_text.append(tt)
    print('price_text', price_text)

    # Объеденяем: название, номер ордера, цену

    name = []
    for j in range(len(all_orders)):
        name.append(st_text[j])
        name.append(all_orders[j])
        name.append(price_text[j])
    print(name)

    #  переводим список в строку и разделяем по 'dd' и обратно переводим в строку

    name_divide = ''.join(name).split('dd')
    print('name_divide =', name_divide)
    wait_paid = []
    not_paid = []
    done = []
    for j in name_divide:
        y = j.split('_')[0]
        if y == 'ожидает оплату':
            wait_paid.append(j)
        elif y == 'неоплачен':
            not_paid.append(j)
        elif y == 'обработан':
            done.append(j)
    print(wait_paid, not_paid, done, sep="\n")

    #  Записываем в CSV

    # n = ['']
    # data = [wait_paid, not_paid, done, n]
    path = 'output.csv'
    with open(path, 'w') as f:
        csv_w = csv.writer(f)
        for c, d, t in zip_longest(wait_paid, not_paid, done):
            csv_w.writerow((c, d, t))

    return pages

def pages_click(pages):
    for j in range(len(pages)):
        pages[j].click()
    print("finish")


def main():
    my_kadastr()
    n = my_actions()
    time.sleep(5)
    pages_click(n)
    time.sleep(5)
    my_actions()

    time.sleep(7200)
    driver.quit()


if __name__ == '__main__':
    main()
