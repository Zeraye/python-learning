spend = 0
games = 0
new_game = 0
bet = 1
possi_win = bet * 14
print("Round" + " | " + "Possible profit" + " | " + "Spent" + " | " + "Bet")
while games < 100:
    new_game = games
    while new_game == games:
        if possi_win >= spend + bet:
            spend += bet
            games += 1
        else:
            bet += 1
            possi_win = bet * 14
    possi_win = bet * 14
    print(str(games) + " | " + str(possi_win-spend) + " | " + str(spend) + " | " + str(bet))
    # print(str(games) + " | " + str(bet))
