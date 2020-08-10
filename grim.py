def mex(arr):
    i = 0
    while True:
        if arr.count(i) != 0:
            i += 1
        else:
            return i


def xor_gate(x, y):
    from bitstring import BitArray
    x = "{0:b}".format(x)
    y = "{0:b}".format(y)
    while len(x) != len(y):
        if len(x) < len(y):
            x = "0" + str(x)
        else:
            y = "0" + str(y)
    i = 0
    p = ""
    while i < min(len(x), len(y)):
        if x[i] == y[i]:
            p = str(p) + "0"
        else:
            p = str(p) + "1"
        i += 1
    b = BitArray(bin=p)
    return b.uint


def f(n):
    if n == 0 or n == 1:
        return 0
    else:
        arr = []
        k = 0
        while k < n:
            arr.append(xor_gate(f(k), f(n-k-1)))
            k += 1
        return mex(arr)

