# importuje biblioteki
from selenium import webdriver
import time as t

# ustawienia chrome
chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(
    executable_path='D:\SeleniumDrivers\chromedriver.exe')  # ścieżka do \SeleniumDrivers\chromedriver.exe
driver.set_window_size(1920, 1080)
driver.maximize_window()
driver.get('https://namecensus.com/male_names.htm')  # nazwa strony -> driver.get('...')
driver.implicitly_wait(20)

i = 2
while i < 301:
    i += 1
    print(driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div[2]/div[2]/div/table/tbody/tr[{}]/td[1]'.format(i)).text)
