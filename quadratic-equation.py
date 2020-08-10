import math

# ax^2 + bx + c = 0

print('ax^2 + bx + c = 0')
a = float(input('Type a >> '))
b = float(input('Type b >> '))
c = float(input('Type c >> '))
if a == 0:
    quit()
else:
    p = (-1) * (b / (2 * a))
    delta = b ** 2 - 4 * a * c
    q = (-1) * (delta / (4 * a))
    if delta < 0:
        roots = 'none'
    elif delta == 0:
        roots = p
        pass
    elif delta > 0:
        roots = [((((-1)*b) * ((-1) * (delta ** 0.5))) / (2 * a)), ((((-1) * b) * (delta ** 0.5)) / (2 * a))]


print('{}x^2 + {}x + {} = 0'.format(a, b, c))
print('p = {}'.format(p))
print('q = {}'.format(q))
print('delta = {}'.format(delta))
print('roots = {}'.format(roots))
