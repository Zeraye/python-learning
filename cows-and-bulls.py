# problem: https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html
import random

main_loop = True
while main_loop:
    rnd_num = str(random.randint(1000, 9999))
    print("Welcome in cows and bulls game!")
    print(rnd_num)
    game_loop = True
    tries = 0

    while game_loop:
        tpd_num = str(input("Write 4-digit number: "))
        if tpd_num == "exit":
            quit()
        tries += 1
        rnd_num_list = [rnd_num[0], rnd_num[1], rnd_num[2], rnd_num[3]]
        tpd_num_list = [tpd_num[0], tpd_num[1], tpd_num[2], tpd_num[3]]
        bulls = 0
        cows = 0

        if tpd_num[0] == rnd_num[0]:
            cows += 1
        else:
            if tpd_num[0] == rnd_num[0] or tpd_num[0] == rnd_num[1] or tpd_num[0] == rnd_num[2] or tpd_num[0] == rnd_num[3]:
                bulls += 1
        if tpd_num[1] == rnd_num[1]:
            cows += 1
        else:
            if tpd_num[1] == rnd_num[0] or tpd_num[1] == rnd_num[1] or tpd_num[1] == rnd_num[2] or tpd_num[1] == rnd_num[3]:
                bulls += 1
        if tpd_num[2] == rnd_num[2]:
            cows += 1
        else:
            if tpd_num[2] == rnd_num[0] or tpd_num[2] == rnd_num[1] or tpd_num[2] == rnd_num[2] or tpd_num[2] == rnd_num[3]:
                bulls += 1
        if tpd_num[3] == rnd_num[3]:
            cows += 1
        else:
            if tpd_num[3] == rnd_num[0] or tpd_num[3] == rnd_num[1] or tpd_num[3] == rnd_num[2] or tpd_num[3] == rnd_num[3]:
                bulls += 1

        if cows == 4:
            print("You won!")
            print("Tries: {}".format(tries))
            quit()
        else:
            print("cows: {}, bulls: {}, tries: {}".format(cows, bulls, tries))
