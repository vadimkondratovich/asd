#from math import sqrt
#print('Введите коэффициенты')
#print('ax*2 + bx + c = 0:')
#a = float(input('a = '))
#b = float(input('b = '))
#c = float(input('c = '))
#D = b**2 - 4 * a * c
#print(D)


#if D > 0:
#    X1 = (-b + sqrt(D)) / 2
#   X2 = (-b - sqrt(D)) / 2
#    print(X1, X2)
#elif D == 0:
#    X = -b / (2 * a)
#    print(X)
#else:
#    print('Действительных корней нет')


from math import sqrt
from typing import NamedTuple


def enter_formula_quadratic_equation() -> float:
    w = float(input("ax*2 + bx + c = 0"))
    return w


class Coefficients(NamedTuple):
    a: float
    b: float
    c: float


def ask_user_to_input_letters() -> Coefficients:
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    return Coefficients(a, b, c)


class Roots(NamedTuple):
    x1:float
    x2:float


def solution(q: Coefficients) -> Roots:
    """
    Calculates a quadratic equation and shows three results.
    """
    d = discriminant(q.a, q.b, q.c)

    if d >= 0:
        x1 = (-q.b + sqrt(d)) / 2
        x2 = (-q.b - sqrt(d)) / 2

    else:
        raise ValueError("there are no square roots ")

    return Roots(x1=x1, x2=x2)


def discriminant(a, b, c) -> float:
    d = float(b**2 - 4 * a * c)
    return d


if __name__ == "__main__":
    C = ask_user_to_input_letters()
    R = solution(C)
    print(R)
