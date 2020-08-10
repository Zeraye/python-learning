# importuje biblioteki
from selenium import webdriver
import time as t

# ustawienia chrome
chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(
    executable_path='D:\SeleniumDrivers\chromedriver.exe')  # ścieżka do \SeleniumDrivers\chromedriver.exe
driver.set_window_size(1920, 1080)
driver.maximize_window()
driver.get('https://csgoempire.com/login')  # nazwa strony -> driver.get('...')
driver.implicitly_wait(20)

# wpisywanie loginu
username_box = driver.find_element_by_id('steamAccountName')
username_box.send_keys('xersun')  # login do konta steam

# wpisywanie hasła
password_box = driver.find_element_by_id('steamPassword')
password_box.send_keys('@tuK4kr4Ht0gz')  # hasło do konta steam

# klikanie zaloguj
login_btn = driver.find_element_by_class_name('btn_green_white_innerfade')
login_btn.click()

# steam guard
steam_guard = input("Steam guard >> ")

# wpisywanie steam guarda
steam_guard_box = driver.find_element_by_id('twofactorcode_entry')
steam_guard_box.send_keys(steam_guard)

# klikanie potwierdzenia
steam_guard_btn = driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div/div/form/div[4]/div[1]/div[1]/div[1]')
steam_guard_btn.click()


# wpisywanie piedziędzy w pole, x podawaj jako słowo, a nie liczbę
def money_write(x):
    money_write_box = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div[5]/div/div[1]/input')
    money_write_box.send_keys(x)


# sprawdzanie stanu konta
def check_balance():
    balance = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[2]/div[3]/div/div/span/span')
    return balance.text


# stawianie pieniędzy na zielone
def click_green():
    money_bet_green_btn = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div[6]/div[2]/button')
    money_bet_green_btn.click()


# usuwanie postawionej puli
def clear():
    clear_btn = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div[5]/div/div[2]/div/div[1]/button')
    clear_btn.click()


# zamiana liczby np. 10,5 -> 10.2
def converter(a):
    arr = str(a).split(',')
    return arr[0] + '.' + arr[1]


# pobieranie z serwera czasu do następnej rundy
def check_time():
    rolling_time = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div[3]/div[3]/div/div[2]')
    return rolling_time.text


total_income = 0  # przychód ze wszystkich rund
t.sleep(15)  # naprawa błędu związana z basic_money (należy poczekać na całą animacje wzrastania pieniędzy)

# naprawa błędu związana z IndexError gdy nie ma licznika czasu po włączeniu strony
try:
    _ = float(converter(check_time()))
except IndexError:
    t.sleep(10)

while True:
    basic_money = float(converter(check_balance()))  # pieniądze na początku
    spent = 0  # wydane pieniądze (bez zielonego)
    rounds = 1  # rundy bez zielonego
    place = 0.01  # ile środków stawiasz
    add = 0.01  # po ile środków dodajesz (na początku place = add)

    # granie na zielone
    while rounds < 45:
        # czekanie aż czas do losowania będzie między 5-6 sekund
        while True:
            time = float(converter(check_time()))
            if 6 >= time >= 5:
                break
        spent += place  # licznik wydanych pieniędzy (bez zielonego)
        if basic_money - place < 0:  # jeżeli nie ma pieniędzy wyrzuć program
            break
        money_write(str(place))  # wpisywanie w odpowiednie miejsce pieniędzy
        click_green()  # kliknij przycisk na zielone
        clear()  # zresetuj postawione pieniądze (na stronie)
        print("---------------------")
        print("Pieniądze >> ", round(basic_money, 2))
        print("Wydane pieniądze >> ", round(spent, 2))
        print("Rundy bez zielonego >> ", rounds)
        print("---------------------")
        t.sleep(20)
        money = float(converter(check_balance()))  # pieniądze po postawieniu
        if money > basic_money:  # jeżeli wygrana zagraj od nowa
            income = money - basic_money  # przychód (pieniądze końcowe - pieniądze początkowe)
            total_income += round(income, 2)  # dodanie przychodu do przychodu całkowitego
            print("Zysk >> ", round(total_income, 2))
            break
        else:  # jeżeli przegrana postaw więcej
            while True:
                if place * 14 < spent + place:  # jeżeli strata jest większa niż możliwy zysk zwięszk postawioną kwote
                    place += add
                else:  # jeżeli zysk jest większy graj dalej
                    break
        rounds += 1  # licznik rund

        income = money - basic_money  # przychód (pieniądze końcowe - pieniądze początkowe)
        total_income += round(income, 2)  # dodanie przychodu do przychodu całkowitego

        print("Zysk >> ", round(total_income, 2))

        basic_money = float(converter(check_balance()))  # sprawdzanie pieniędzy po grze

        if basic_money == 0:  # jeżeli nie ma pieniędzy zatrzymaj
            break
