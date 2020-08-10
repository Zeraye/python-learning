import random as r


# stawianie
def bet(x):
    roll = r.randint(0, 14)
    if roll == 0:
        return x * 13 * 2
    elif 7 >= roll >= 1:
        return x
    else:
        return 0


sims = 400
curr_sim = 1
money = 394
basic_money = 394
place = 1
total_income = 0

while curr_sim < sims:
    gain = bet(place)
    money -= 3 * place
    money += gain
    income = money - basic_money
    total_income += income
    print("Pieniądze na start >> ", basic_money)
    print("Pieniądze na koniec >> ", money)
    print("Zysk z rundy >> ", income)
    print("Zysk ze wszytkich rund >> ", total_income)
    print("--------------------")
    basic_money += income
    curr_sim += 1

print(curr_sim)
