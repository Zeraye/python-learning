# importuje biblioteki
from selenium import webdriver
import time
import random

# ustawienia chrome
chrome_options = webdriver.ChromeOptions()

driver_email = webdriver.Chrome(
    executable_path='D:\SeleniumDrivers\chromedriver.exe')  # ścieżka do \SeleniumDrivers\chromedriver.exe
driver_email.set_window_size(800, 600)

driver_email.get('https://10minutemail.net/readmail.html?mid=welcome')  # nazwa strony -> driver.get('...')
driver_email.implicitly_wait(20)

# pobieganie email
email = driver_email.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div[4]/div/div[1]/h1[2]').text

# pobieranie ig
driver_ig = webdriver.Chrome(
    executable_path='D:\SeleniumDrivers\chromedriver.exe')  # ścieżka do \SeleniumDrivers\chromedriver.exe
driver_ig.set_window_size(800, 600)

driver_ig.get('https://www.instagram.com/accounts/emailsignup/')  # nazwa strony -> driver.get('...')
driver_ig.implicitly_wait(20)

names = open('names-list', 'r')
surnames = open('surnames-list', 'r')
accounts = open('ig-accs.txt', 'r+')

# wpisywanie 'Numer telefonu komórkowego lub adres e-mail'
email_box = driver_ig.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
email_box.send_keys(email)

# wpisywanie 'Imię i nazwisko'
names_list = names.readlines()
name = names_list[random.randint(0, len(names_list) - 1)]
surnames_list = surnames.readlines()
surname = surnames_list[random.randint(0, len(surnames_list) - 1)]
personal_data_box = driver_ig.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/div/label/input')
personal_data_box.send_keys(name + '' + surname)

# wpisywanie 'Nazwa użytkownika'
username = str(random.randint(100, 999)) + str(name) + str(surname) + str(random.randint(100, 999))
accounts.write(username + '\n')
accounts.close()
names.close()
surnames.close()
username_box = driver_ig.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[5]/div/label/input')
username_box.send_keys(username)

# wpisywanie 'Hasło'
password = '3A@p40bD%2&4)(8P'
password_box = driver_ig.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[6]/div/label/input')
password_box.send_keys(password)

# klikanie 'w powietrze', aby naprawił się błąd ze złym hasłem
driver_ig.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form').click()

time.sleep(5)

# klikanie dalej w początkowym ekranie
next1_btn = driver_ig.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[7]/div/button')
next1_btn.click()

# ustawianie miesiąca
month_btn = driver_ig.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[2]')
month_btn.click()

# ustawianie dnia
day_btn = driver_ig.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[10]')
day_btn.click()

# ustawianie roku
year_btn = driver_ig.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[26]')
year_btn.click()

time.sleep(5)

# klikanie dalej w ekranie daty urodzenia
next2_btn = driver_ig.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/article/div/div[1]/div/div[5]/div[2]/button')
next2_btn.click()

# odczekanie na przyjście email
time.sleep(120)

# wejście w email
driver_email.find_element_by_xpath('/html/body/div[1]/div[5]/div/table/tbody/tr[2]').click()

# pobranie z email kodu
code = driver_email.find_element_by_xpath(
    '/html/body/div[1]/div[4]/div/div/div[4]/div/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]').text

# zamknięcie strony z emailem
driver_email.close()

# wpisanie otrzymanego kodu
driver_ig.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/article/div/div[1]/div/div[3]/form/div[1]/input').send_keys(code)

# klikanie dalej w ekranie z kodem
next3_btn = driver_ig.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/article/div/div[1]/div/div[3]/form/div[2]/button')
next3_btn.click()

# zaknięcie strony z instagramem
driver_ig.close()

names.close()
surnames.close()
accounts.close()