from selenium import webdriver
import time as t

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(executable_path='D:\SeleniumDrivers\chromedriver.exe')
driver.set_window_size(1920, 1080)
driver.maximize_window()
driver.get('https://om.mimuw.edu.pl/post/44')
driver.implicitly_wait(20)
counter = 0
while True:
    try:
        a = driver.find_element_by_xpath('/html/body/p')
        counter += 1
        print("Repeats >> ", counter)
        print("Time (secs) >> ", counter*15)
    except Exception:
        driver.close()
        driver = webdriver.Chrome(executable_path='D:\SeleniumDrivers\chromedriver.exe')
        driver.set_window_size(1920, 1080)
        driver.maximize_window()
        driver.get('http://y2u.be/_Z3ra0CxCE0')
        driver.implicitly_wait(20)
        break
    driver.refresh()
    t.sleep(15)
