from selenium import webdriver
from fake_useragent import UserAgent  # pip3 install fake-useragent
import time
from random import choice
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as econ

login = '113-562-732-34'
password = '+KNup"1X0fhn'
url = 'https://spv.kadastr.ru/'
my_namber_card = '2202200503742041'
my_time_card = '07/23'
my_name_in_card = 'ALEX KHRIST'
my_ovs = '784'
my_email_name = 'khristenkoyura@gmail.com'
# cadaster_number = 'Москва, Щукино, ул. Новощукинская, д. 3, кв. 12'
# cadaster_number = '77:08:0009005:1596'


def my_object_request():
    ua = UserAgent()
    user_agent = ua.random
    print(user_agent)
    # proxies = open('proxies').read().split('\n')

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

    proxy = choice(proxies)
    print(proxy)

    # активируем Сrome

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'--proxies-server={proxy}')
    chrome_options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(options=chrome_options, executable_path="/home/alex/programs/chromedriver")
    driver.get(url)
    wait = WebDriverWait(driver, 30)

    #  Вход на  страницу Госуслуги

    try:
        wait.until(econ.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-primary"]'))).click()
    except Exception as e:
        print(e)
    time.sleep(1)
    # Авторизация
    elem = driver.find_element_by_name('login')
    elem.clear()
    elem.send_keys(login)
    time.sleep(1)
    elem = driver.find_element_by_name('password')
    elem.clear()
    elem.send_keys(password)

    # кнопка ввода логина и пароля

    try:
        wait.until(econ.element_to_be_clickable((By.XPATH, '//button[@id="loginByPwdButton"]'))).click()
    except Exception as e:
        print(e)

    # Ввод адреса или кадастровый номер объекта

    try:
        address_input = wait.until(econ.element_to_be_clickable((By.XPATH, '//div[@role="combobox"]/input[1]')))
    except Exception as e:
        print(e)
        address_input = ''
        time.sleep(3)
    address_input.clear()
    # address = cadaster_number
    address_input.send_keys(address)

    # Кликаем на введенный адрес
    try:
        wait.until(econ.element_to_be_clickable((By.XPATH, '//ul[@id="19-suggestions"]/li[2]'))).click()
    except Exception as e:
        print(e)

    # Отображение основных данных

    try:
        request1 = wait.until(
            econ.presence_of_all_elements_located((By.XPATH, '//div[@class="bis-kindlist"]/button')))
    except Exception as e:
        print(e)
        request1 = ''
    print("request1 = ", len(request1))
    aa = []
    aaa = []
    for i in request1:
        x = i.get_attribute("textContent").split()
        y = " ".join(x[0:3])
        z = " ".join(x[4:])
        print(x)
        aa.append(y)
        aaa.append(z)
    print('aa = ', aa)
    print('aaa =', aaa)

    # кликаем на Об основных характеристиках

    try:
        wait.until(econ.element_to_be_clickable((By.XPATH, '//div[@class="bis-kindlist"]/button[1]'))).click()
    except Exception as e:
        print(e)
    time.sleep(3)
    # кликаем на  Об объекте недвижимости

    try:
        wait.until(econ.element_to_be_clickable((By.XPATH, '//div[@class="bis-kindlist"]/button[2]'))).click()
    except Exception as e:
        print(e)
    time.sleep(3)
    # кликаем на Другие выписки

    try:
        wait.until(
            econ.element_to_be_clickable((By.XPATH, '//div[@class="bis-kindlist"]/a'))).click()
    except Exception as e:
        print(e)
    time.sleep(1)

    # кликаем на О переходе прав на объект недвижимости

    try:
        wait.until(
            econ.element_to_be_clickable((By.XPATH, '//div[@class="bis-kindlist"]/a/div/button[1]'))).click()
    except Exception as e:
        print(e)

    # кликаем на О зарегистрированных договорах в долевом строительстве

    try:
        wait.until(
            econ.element_to_be_clickable((By.XPATH, '//div[@class="bis-kindlist"]/a/div/button[2]'))).click()
    except Exception as e:
        print(e)
    try:
        request3 = wait.until(
            econ.presence_of_all_elements_located((By.XPATH, '//div[@class="bis-popup"]/button/div[1]')))
    except Exception as e:
        print(e)
        request3 = ''
    print("request3 = ", len(request3))
    bb = []
    for i in request3:
        x = i.get_attribute("textContent").split()
        y = " ".join(x)
        bb.append(y)
    print('bb = ', bb[0:2])
    try:
        request4 = wait.until(
            econ.presence_of_all_elements_located((By.XPATH, '//div[@class="bis-popup"]/button/div[2]')))
    except Exception as e:
        print(e)
        request4 = ''
    print("request4 = ", len(request4))
    bbb = []
    for i in request4:
        x = i.get_attribute("textContent").split()
        y = " ".join(x)
        bbb.append(y)
    print('bbb =', bbb)

    # кликаем на Корзину

    wait1 = WebDriverWait(driver, 40)
    try:
        wait1.until(
            econ.element_to_be_clickable((By.XPATH, '//ul[@class="header-user"]/li[5]/a'))).click()
    except Exception as e:
        print(e)

    # кликаем на Оформить заказ

    try:
        wait.until(
            econ.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-success btn-order"]'))).click()
    except Exception as e:
        print(e)
    time.sleep(1)

    # кликаем на Я согласен

    try:
        box = wait.until(
            econ.presence_of_element_located((By.XPATH,
                                              '//div[@class="bis-checkout"]/div/div[9]/div[1]/div[1]/label/span')))
    except Exception as e:
        print(e)
        box = ''
    print('box =', box)
    time.sleep(1)
    box.click()

    # кликаем на Перейти к оплате

    try:
        boxx = wait.until(
            econ.presence_of_element_located(
                (By.XPATH, '//button[@class="btn btn-primary btn-checkout"]')))
    except Exception as e:
        print(e)
        boxx = ''
    print('boxx =', boxx)
    time.sleep(3)
    boxx.click()

    # Выбираем Банковскую карту

    try:
        wait.until(
            econ.element_to_be_clickable(
                (By.XPATH, '//button[@class="pay-method__button pay-method__button--card pay-method__button--active"]'))
        ).click()
    except Exception as e:
        print(e)

    # Выбор карты, выбираю Мир

    try:
        wait.until(
            econ.element_to_be_clickable(
                (By.XPATH, '//li[@class="mir-icn30"]'))).click()
    except Exception as e:
        print(e)

    # Ввожу данные карты

    # - Вводим номер карты

    try:
        bk = wait.until(
            econ.presence_of_element_located(
                (By.XPATH, '//input[@name="cc-number" ]')))
    except Exception as e:
        print(e)
        bk = ''
    print('bk =', bk)
    bk.clear()
    bk.send_keys(my_namber_card)
    time.sleep(1)

    # - Вводим срок действия

    try:
        bt = wait.until(
            econ.presence_of_element_located(
                (By.XPATH, '//input[@name="cc-exp"]')))
    except Exception as e:
        print(e)
        bt = ''
    print('bt =', bt)
    bt.clear()
    bt.send_keys(my_time_card)
    time.sleep(1)

    # - Вводим имя владельца

    try:
        bn = wait.until(
            econ.presence_of_element_located(
                (By.XPATH, '//input[@name="cc-name"]')))
    except Exception as e:
        print(e)
        bn = ''
    print('bn =', bn)
    bn.clear()
    bn.send_keys(my_name_in_card)
    time.sleep(1)

    # - Вводим OVS карты

    try:
        bs = wait.until(
            econ.presence_of_element_located(
                (By.XPATH, '//input[@id="cvv"]')))
    except Exception as e:
        print(e)
        bs = ''
    print('bs =', bs)
    bs.clear()
    bs.send_keys(my_ovs)
    time.sleep(1)

    # Уведомление о проведении платежа

    try:
        bkv = wait.until(
            econ.presence_of_element_located(
                (By.XPATH, '//div[@class="kvitantsia"]')))
    except Exception as e:
        print(e)
        bkv = ''
    print('bkv =', bkv)
    bkv.click()
   # Вводим email
    try:
        bem = wait.until(
            econ.presence_of_element_located(
                (By.XPATH, '//input[@class="justify masked_email"]')))
    except Exception as e:
        print(e)
        bem = ''
    print('bs =', bs)
    bem.clear()
    time.sleep(5)
    bem.send_keys(my_email_name)
    time.sleep(1)

    # Получить квитанцию

    try:
        bkv = wait.until(
            econ.presence_of_element_located(
                (By.XPATH, '//div[@class="kvitantsia__content"]/div/label')))
    except Exception as e:
        print(e)
        bkv = ''
    print('bkv =', bkv)
    bkv.click()

    # Кликаем на Оплатить

    try:
        bop = wait.until(
            econ.presence_of_element_located(
                (By.XPATH, '//div[@class="pm-box__button pm-box__button--card"]/button')))
    except Exception as e:
        print(e)
        bop = ''
    print('bop =', bop)
    # bop.click()

    print('finish')

    time.sleep(10)
    driver.quit()


def main():
    try:
        with open('cadasters') as f:
            cadaster_s = []
            for i in f:
                x = ''.join(i).split()
                cadaster_s.append(x)
                if i == 'finish\n':
                    break
            y = cadaster_s[:-1]
            print(y)
    except Exception as e:
        print(e)

    for j in y:
        global address
        address = ''.join(j)
        print(address)
        my_object_request()


if __name__ == '__main__':
    main()
