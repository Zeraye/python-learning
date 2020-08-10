# problem: https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

num = int(input("Enter the length of the Fibonacci sequence: "))
seq = [1, 1]

i = 1
dur = 3

while dur <= num:
    new_num = int(seq[i - 1] + seq[i])
    seq.append(new_num)
    i += 1
    dur += 1

print(seq)
