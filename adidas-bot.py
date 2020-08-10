# importuje biblioteki
from selenium import webdriver
import time as t

# ustawienia chrome
chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(executable_path='D:\SeleniumDrivers\chromedriver.exe')  # ścieżka do \SeleniumDrivers\chromedriver.exe
driver.set_window_size(1920, 1080)
driver.maximize_window()
driver.get('https://www.adidas.pl/yeezy')  # nazwa strony -> driver.get('...')
driver.implicitly_wait(20)

name = 'Jan'
surname = 'Nowal'
address = 'Różana 19'
post_code = '13-131'
city = 'Adamów'
phone = '123444654'
email = 'daaa@gmail.com'

# 1. strona
# 2. czekac na rozdanie
# 3. wybrać rozmiar
# 4. zamówić (nowy xpath po checkout)
# 5. wstawić dane blik ...


# jestes w poczekalni: /html/body/div[2]/div/div[1]/div/div[1]/h1 (to samo co prawie je masz)
# rozmiar: /html/body/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]
# koszyk: /html/body/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/button
# prawie je masz: /html/body/div[2]/div/div[1]/div/div[1]/h1
# rozmiar: /html/body/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/ul/li


while True:
    try:
            a = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[1]/div[2]/div')
    except Exception:
        print('wow')
        break
    t.sleep(5)

# country_btn = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div/div[1]/a/img')
# country_btn.click()

# news_close_btn = driver.find_element_by_xpath('/html/body/div[3]/div/div/button')
# news_close_btn.click()

# cookies_btn = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div/div[2]/button[1]')
# cookies_btn.click()

# select_size_btn = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div[3]/div/div[2]/div[2]/div[2]/div/div/form/div[2]/div[1]/div/div/button')
# select_size_btn.click()
#
# size_chose_btn = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div[3]/div/div[2]/div[2]/div[2]/div/div/form/div[2]/div[1]/div/div/div/div/ul/li[2]/button')
# size_chose_btn.click()
#
# add_to_bag_btn = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div[3]/div/div[2]/div[2]/div[2]/div/div/form/div[4]/button')
# add_to_bag_btn.click()
#
# checkout_btn = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[2]/div/a[2]')
# checkout_btn.click()
#
# name_box = driver.find_element_by_id('dwfrm_shipping_shiptoaddress_shippingAddress_firstName')
# name_box.send_keys(name)
#
# surname_box = driver.find_element_by_id('dwfrm_shipping_shiptoaddress_shippingAddress_lastName')
# surname_box.send_keys(surname)
#
# address_box = driver.find_element_by_id('dwfrm_shipping_shiptoaddress_shippingAddress_address1')
# address_box.send_keys(address)
#
# post_code_box = driver.find_element_by_id('dwfrm_shipping_shiptoaddress_shippingAddress_postalCode')
# post_code_box.send_keys(post_code)
#
# city_box = driver.find_element_by_id('dwfrm_shipping_shiptoaddress_shippingAddress_city')
# city_box.send_keys(city)
#
# phone_box = driver.find_element_by_id('dwfrm_shipping_shiptoaddress_shippingAddress_phone')
# phone_box.send_keys(phone)
#
# email_box = driver.find_element_by_id('dwfrm_shipping_email_emailAddress')
# email_box.send_keys(email)
#
# payment_btn = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div[2]/form/div[1]/ng-form/div[5]/div/button')
# payment_btn.click()
#
# send_btn = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div[1]/div[5]/div')
# send_btn.click()
#
# blik_btn = driver.find_element_by_id('channel_image_73')
# blik_btn.click()
#
# blik = input('Podaj blik >> ')
#
# city_box = driver.find_element_by_id('#')
# city_box.send_keys(blik)
