import random

PLAYERS = 8


def counter(pos):
    global shots
    if pos == 1:
        shots += PLAYERS
    if pos == 2:
        pass
    if pos == 3:
        shots += PLAYERS - 1
    if pos == 4:
        return 4
    if pos == 5:
        pass
    if pos == 6:
        shots += PLAYERS * 0.5
    if pos == 7:
        shots += PLAYERS * 0.5
    if pos == 8:
        pass
    if pos == 9:
        shots += PLAYERS * 0.25
    if pos == 10:
        pass
    if pos == 11:
        shots += PLAYERS
    if pos == 12:
        shots += 3
    if pos == 13:
        shots += 1
    if pos == 14:
        return 22
    if pos == 15:
        shots += 1
    if pos == 16:
        shots += PLAYERS - 1
    if pos == 17:
        pass
    if pos == 18:
        shots += 1
    if pos == 19:
        shots += 3
    if pos == 20:
        shots += PLAYERS
    if pos == 21:
        return 29
    if pos == 22:
        shots += 1
    if pos == 23:
        shots += 2
    if pos == 24:
        shots += 2
    if pos == 25:
        shots += PLAYERS
    if pos == 26:
        shots += 1
    if pos == 27:
        shots += PLAYERS * 0.5
    if pos == 28:
        pass
    if pos == 29:
        pass
    if pos == 30:
        shots += PLAYERS
    if pos == 31:
        return 33
    if pos == 32:
        pass
    if pos == 33:
        pass
    if pos == 34:
        pass
    if pos == 35:
        shots += 1
    if pos == 36:
        shots += 1
    if pos == 37:
        shots += PLAYERS * 0.5
    if pos == 38:
        shots += 1
    if pos == 39:
        shots += PLAYERS * 0.5
    if pos == 40:
        pass
    if pos == 41:
        shots += 1
    if pos == 42:
        shots += 1
    if pos == 43:
        shots += PLAYERS
    if pos == 44:
        return 3
    if pos == 45:
        shots += PLAYERS - 1
    if pos == 46:
        pass
    if pos == 47:
        shots += PLAYERS - 1
    if pos == 48:
        pass
    if pos == 49:
        shots += PLAYERS
    if pos == 50:
        shots += 1
    return -1


k = 0
average_sum = 0
while k < 1000:
    i = 0
    position = 0
    shots = 0
    while i < 8:
        position = 0
        while position < 51:
            throw = random.randint(1, 6)
            position += throw
            if position < 51:
                new_position = counter(position)
                if new_position != -1:
                    position = new_position
        i += 1

    average_sum += shots/PLAYERS
    k += 1

print(average_sum/k)
