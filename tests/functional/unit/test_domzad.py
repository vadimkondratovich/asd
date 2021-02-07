import pytest

from tasks.lesson03.domzad_two import discriminant


@pytest.mark.unit
def test_discriminant():
    # b ** 2 - 4ac

    test_data = {
        (0, 0, 0): 0,
        (1, 1, 1): -3,
        (1, 10, 2): 92,
        (-1, -1, -1): -3,
    }

    for ((a, b, c), d_expected) in test_data.items():
        d_real = discriminant(a, b, c)
        assert \
            d_real == d_expected, \
            f'fuck off:' \
            f' on {a=},{b=},{c=}' \
            f' expected {d_expected},' \
            f' got {d_real}'
