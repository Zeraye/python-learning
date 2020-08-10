# problem: https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html

pr = open("prime-numbers.txt", "r+")
hp = open("happy-numbers.txt", "r+")

pr_list = []
hp_list = []
ol_list = []

a = 0
while a < 168:
    pr_list.append(pr.readline().strip())
    a += 1

b = 0
while b < 143:
    hp_list.append(hp.readline().strip())
    b += 1

c = 0
d = 0
while c < len(pr_list):
    if pr_list[c] == hp_list[d]:
        ol_list.append(pr_list[c])
        c += 1
    elif d+2 > len(hp_list):
        d = 0
        c += 1
    else:
        d += 1

e = 0
while e < len(ol_list) - 1:
    print(ol_list[e], end=", ")
    e += 1
print(ol_list[len(ol_list)-1])
