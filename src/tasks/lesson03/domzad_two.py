from math import sqrt
print('Введите коэффициенты')
print('ax*2 + bx + c = 0:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
D = b**2 - 4 * a * c
print(D)


if D > 0:
    X1 = (-b + sqrt(D)) / 2
    X2 = (-b - sqrt(D)) / 2
    print(X1, X2)
elif D == 0:
    X = -b / (2 * a)
    print(X)
else:
    print('Действительных корней нет')
