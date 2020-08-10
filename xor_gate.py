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
            p = str(p) + "0"print(xor_gate(153,22))
        else:
            p = str(p) + "1"
        i += 1
    b = BitArray(bin=p)
    return b.uint
