import random as r


# stawianie na zielone
def bet_green(x):
    roll = r.randint(0, 14)
    if roll == 0:
        return x * 14
    else:
        return 0


total_income = 0  # całkowity przychód ze wszystkich sumulacji
sims = 1000  # ilość symulacji
basic_money = 500  # początkowe pieniądze (nimi operuje się między symulacjami)
curr_sim = 1  # numer obecnej symulacji

while curr_sim < sims:
    money = basic_money  # pieniądze (nimi operuje się podczas losowania)
    spent = 0  # wydane pieniądze
    rounds = 1  # ilość rund
    place = 1  # początkowa kwota stawiania
    add = 1  # po ile dodawać (na starcie place = add)

    # główna pętla, losowanie
    while rounds < 45:
        spent += place  # dodawnie pięniedzy do wydatków
        if money - place < 0:  # jeżeli nie ma wystarczająco pieniędzy zatrzymaj program
            break
        money -= place  # odjęcie pieniędzy z puli
        gain = bet_green(place)  # wywoływanie funkcji stawiania na zielone
        if gain != 0:  # jeżeli wygrana, nowa gra od początku
            money += gain
            break
        elif gain == 0:  # jeżeli przegrana, postaw jeszcze raz
            while True:
                if place * 14 < spent + place:  # brak zysku
                    place += add  # powiększanie stawianej kwoty
                else:
                    break
        rounds += 1  # licznik rund

    income = money - basic_money  # przychód w danej rundzie
    total_income += income  # całkowity przychód ze wszystkich rund

    # wyświetlanie informacji o danej symulacji
    print("Rundy >> ", rounds)
    print("Pieniądze na start >> ", basic_money)
    print("Pieniądze na koniec >> ", money)
    print("Zysk z rundy >> ", income)
    print("Zysk ze wszytkich rund >> ", total_income)
    print("--------------------")
    basic_money += income  # zmiana początkowej kwoty pieniędzy w następnej symulacji
    curr_sim += 1  # licznik obecnej symulacji
    if basic_money == 0:  # jeżeli brak pieniędzy zatrzymaj program
        break

print(curr_sim)  # wyświetl numer symulacji po ktorym progam przestał działać
