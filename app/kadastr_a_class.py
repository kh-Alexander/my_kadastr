from selenium import webdriver
from fake_useragent import UserAgent  # pip3 install fake-useragent
import time
from random import choice
import csv

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as econ

ua = UserAgent()
userAgent = ua.random
print(userAgent)
proxies = open('proxies').read().split('\n')
proxy = choice(proxies)
print(proxy)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxies-server={proxy}')
chrome_options.add_argument(f'user-agent={userAgent}')

# wait = WebDriverWait(driver, 30)


class Bot:
    def __init__(self, driver):
        self.driver = webdriver.Chrome(options=chrome_options, executable_path="/home/alex/programs/chromedriver")
        self.navigate()
        self.entry_first()
        self.login_password_install()
        self.entry_second()
        self.orders_my()
        self.orders_all()

        # self.wait = WebDriverWait(driver, 30)

    def navigate(self):
        self.driver.get("https://spv.kadastr.ru/")
        self.driver.implicitly_wait(15)

    def entry_first(self):
        # wait = WebDriverWait(driver, 30)
        # try:
        #     wait.until(econ.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-primary"]'))).click()
        # except Exception as e:
        #     print(e)

        button = self.driver.find_element_by_xpath('//button[@class="btn btn-primary"]')
        time.sleep(3)
        print(button)
        button.click()
        time.sleep(3)

    def login_password_install(self):
        try:
            elem = self.driver.find_element_by_name('login')
        except Exception as e:
            print(e)
            elem = self.driver.find_element_by_id('login')
        elem.clear()
        login = '113-562-732-34'
        elem.send_keys(login)
        time.sleep(3)
        try:
            elm = self.driver.find_element_by_name('password')
        except Exception as e:
            print(e)
            elm = self.driver.find_element_by_id('password')
        elm.clear()
        password = '+KNup"1X0fhn'
        elm.send_keys(password)
        time.sleep(3)

    def entry_second(self):
        button_log = self.driver.find_element_by_xpath('//button[@id="loginByPwdButton"]')
        print(button_log)
        button_log.click()
        time.sleep(5)

    def orders_my(self):
        try:
            href_orders = self.driver.find_elements_by_xpath("//a[@href='/appeals']")
        except Exception as e:
            print(e)
            href_orders = ''
        print('href_orders = ', href_orders)
        for k in href_orders:
            k.click()
            time.sleep(5)

    def orders_all(self):
        try:
            orders_all = self.driver.find_elements_by_xpath("//div[@class='col-md-2 bis-appeal--value number']/a[1]")
        except Exception as e:
            print(e)
            orders_all = ''
        all_orders = []
        for k in orders_all:
            lm = k.get_attribute('href').split('/')[-1] + 'dd'
            all_orders.append(lm)
        print('all_orders = ', all_orders)
        try:
            status = self.driver.find_elements_by_xpath("//div[@class='row appealsrow block-card']/div[2]")
        except Exception as e:
            print(e)
            status = ''
        time.sleep(3)
        print('st', status)
        st_text = []
        for i in status:
            stt = i.text + '_'
            st_text.append(stt)
        print('st_text', st_text)
        # try:
        #     # price = self.driver.find_elements_by_xpath("//div[@class='col-md-1 bis-appeal--value right total']")
        #     price = self.driver.find_elements_by_xpath("//div[@class='row appealsrow block-card']/div[5]")
        #     # price = self.driver.find_elements_by_class_name('col-md-1 bis-appeal--value right total')
        # except Exception as e:
        #     print(e)
        #     price = ''
        # time.sleep(10)
        # print('pr', price)
        #
        # price_text = []
        # for i in price:
        #     tt = i.text
        #     price.append(tt)
        # print('price_text', price_text)
        name = []
        for j in range(len(all_orders)):
            name.append(st_text[j])
            name.append(all_orders[j])
        print(name)
        name_divide = ''.join(name).split('dd')
        print('name_divide =', name_divide)
        wait_paid = []
        not_paid = []
        done = []
        for j in name_divide:
            x = j.split('_')[0]
            if x == 'ожидает оплату':
                wait_paid.append(j)
            elif x == 'неоплачен':
                not_paid.append(j)
            elif x == 'обработан':
                done.append(j)
        print(wait_paid, not_paid, done, sep="\n")
        n = ['']
        data = [wait_paid, not_paid, done, n]
        path = "output.csv"
        with open(path, 'a+', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)
        # def orders_executed(self):
        #
        #     try:
        #         made_orders = self.driver.find_elements_by_xpath("//div[@class='col-md-1 bis-appeal--value load']/a[1]")
        #     except Exception as e:
        #         print(e)
        #         made_orders = ''
        #
        #     links_made = []
        #     for k in made_orders:
        #         k.click()
        #         lm = k.get_attribute('href')
        #         links_made.append(lm)
        #     print('links_made = ', links_made)
        #
        time.sleep(7200)
        self.driver.quit()


def main():
    b = Bot()


if __name__ == '__main__':
    main()
