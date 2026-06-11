# test_quera_polynomial_value.py
from polynomial_value_quera import evaluate_poly, MOD


def test_quadratic():
    # P(x) = 2x^2 + 3x + 5 at x = 2  ->  19
    assert evaluate_poly(2, [2, 3, 5]) == 19


def test_constant():
    # P(x) = 5  (degree 0) -> 5 regardless of x
    assert evaluate_poly(123, [5]) == 5


def test_root():
    # P(x) = x + 1 at x = -1  ->  0
    assert evaluate_poly(-1, [1, 1]) == 0


def test_modulo_overflow():
    # P(x) = x^2 at x = 1e9  ->  1e18 mod (1e9+7) = 49
    assert evaluate_poly(10**9, [1, 0, 0]) == 49


def test_negative_result_wraps():
    # P(x) = x - 1e9 at x = 1  ->  -999999999 mod (1e9+7) = 8
    result = evaluate_poly(1, [1, -(10**9)])
    assert result == 8
    assert 0 <= result < MOD
