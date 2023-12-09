from time import sleep
from selenium import webdriver  # pip3 install selenium
import csv
import re
#
driver = webdriver.Firefox()
#
#
def write_csv(data):
    with open('cian.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((
            data['lists']
        ))

def get_all_information():


    base_url = 'https://bryansk.cian.ru/cat.php?deal_type=sale&engine_version=2&location%5B0%5D=245228&minsite=7' \
               '&object_type%5B0%5D=1&offer_type=suburban&totime=2592000 '
    url_gen = base_url
    driver.get(url_gen)
    number_proposals = driver.find_element_by_xpath("//div[@data-name='SummaryHeader']/h3[1]")
    a = number_proposals.text
    nums = re.findall(r'\d+', a)
    d = ''.join(nums)
    elem = int(d)
    print(elem)

    sleep(3)
    href = driver.find_elements_by_xpath("//div[@data-name='LinkArea']/a[1]")
    offers = driver.find_elements_by_xpath("//div[@data-name='TitleComponent']/span[1]")
    prices = driver.find_elements_by_xpath("//span[@data-mark='MainPrice']")

    count = 0
    all_offers = []
    for m in offers:
        count = count + 1
        if count > elem:
            break
        n = m.text
        all_offers.append(n)
    all_offers = [i + '\n' for i in all_offers]
    print(all_offers)

    count = 0
    all_prices = []
    for m in prices:
        count = count + 1
        if count > elem:
            break
        n = m.text
        all_prices.append(n)
    print(all_prices)
    all_prices = [i + '\n' for i in all_prices]

    count = 0
    links_href = []
    for k in href:
        lm = k.get_attribute('href')
        count = count + 1
        if count > elem:
            break
        links_href.append(lm)
    print(links_href)
    links_href = [i + '\n' for i in links_href]

    count = 0
    all_phone = []
    all_address = []
    for k in links_href:
        count = count + 1
        if count > elem:
            break
        driver.get(k)
        sleep(2)
        button = driver.find_element_by_xpath("//button[@class='button_component-button-67NQ7d4m "
                                              "button_component-M-1dfZ3E6O3 button_component-default-19JDy9Ehh "
                                              "button_component-primary-EZIW0gJD']")
        button.click()
        sleep(2)
        phone = driver.find_element_by_xpath("//a[@class='a10a3f92e9--phone--3XYRR']").text
        all_phone.append(phone)
        try:
            address = driver.find_element_by_xpath("//div[@data-name='Geo']/span[@itemprop='name']")
            address = address.get_attribute('content')
        except Exception as e:
            print(e)
            continue
        all_address.append(address)
    print(all_address)
    print(all_phone)
    all_phone = [i + '\n,\n' for i in all_phone]
    all_address = [i + '\n' for i in all_address]
    print(all_phone)
    #
    z = len(all_offers)
    s = len(links_href)
    f = len(all_phone)
    t = len(all_address)
    print(z, s, f, t, sep="; ")
    #
    name = []
    for i in range(t):
        name.append(all_offers[i])
        name.append(all_prices[i])
        name.append(links_href[i])
        name.append(all_address[i])
        name.append(all_phone[i])
    print(name)
    #
    for h in name:
        j = ''.join(h)
        data = {'lists': j}
        write_csv(data)
    #
    x = ''.join(name)  # делает из списка строку
    print(x)
# 
# 
if __name__ == '__main__':
    get_all_information()
