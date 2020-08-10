# problem: https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
import random

a = []
b = []

len_a = random.randint(1, 30)
i = 0

while len_a >= i:
    a.append(random.randint(1, 100))
    i += 1
else:
    pass

len_b = random.randint(1, 30)
i = 0

while len_b >= i:
    b.append(random.randint(1, 100))
    i += 1
else:
    pass

c = [num_a for num_a in a for num_b in b if num_b == num_a]

for num_c in c:
    if c.count(num_c) > 1:
        c.remove(num_c)
    else:
        pass

print(c)
