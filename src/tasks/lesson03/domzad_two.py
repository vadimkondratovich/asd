#: from math import sqrt
#: Вычислить квадратное уравнение ax2 + bx + c = 0 (*)
#: D = b2 – 4ac;
#: x1,2 = (-b +/- sqrt (D)) / 2a
#: Предусмотреть 3 варианта:
#: Два действительных корня
#: Один действительный корень
#: Нет действительных корней


from math import sqrt
from typing import NamedTuple


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
