#: Условие задачи:
#: Ввести число, проверить на то, что было введено именно число.
#: Возвести его в куб.

from typing import NamedTuple


class Number(NamedTuple):
    a: float


def ask_user_to_input_a_number() -> Number:
    a = float(input('Введите целое число: a = '))
    return Number(a)

def what_is_A(a) -> float:
    k = isinstance(a, (int, float))
    return k

class Exp(NamedTuple):
    e: float


def solution(x: Number) -> Exp:
    """
    Multiplies a number three times.
    """
    e = float(expo(x.a))
    return Exp(e = e)


def expo(a) -> float:
    e = float(a ** 3)
    return e

if __name__ == "__main__":
    C = ask_user_to_input_a_number()
    R = solution(C)
    print(R)
