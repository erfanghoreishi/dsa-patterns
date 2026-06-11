"""
Polynomial Evaluation (Horner's Method) mod 1e9+7
Source: Quera — not on LeetCode

Strictly a math problem, but a clean intro to DP-style thinking: each step
builds on the previous result  (dp0 -> dp1 -> dp2 -> dp3 -> ...).

We are given:
    P(x) = a_n x^n + a_{n-1} x^{n-1} + ... + a_0

We must compute:
    P(x) mod (10^9 + 7)

Reason for modulo:
    - Values of P(x) can become extremely large (up to ~x^n)
    - Prevent integer overflow and keep computations bounded
    - All operations are done under modular arithmetic

Key property:
    (a * b + c) mod M = ((a mod M) * (b mod M) + c mod M) mod M

Algorithm (Horner's method):
    result = a_n
    for i from n-1 down to 0:
        result = (result * x + a_i) % M

Time complexity:
    O(n)

Input:
    n x
    a_n a_{n-1} ... a_0
"""

MOD = 10**9 + 7


def evaluate_poly(x, coeffs):
    """Evaluate P(x) mod MOD via Horner's method.

    coeffs are ordered from highest degree (a_n) down to a_0.
    Python's % keeps the result in [0, MOD), so negative x / coeffs are fine.
    """
    result = 0
    for a in coeffs:
        # Reduce each operand to guard 64-bit overflow in C/C++/Java; unneeded in
        # Python (big ints, no overflow). Plain: result = (result * x + a) % MOD
        result = ((result % MOD) * (x % MOD) + (a % MOD)) % MOD
    return result


if __name__ == "__main__":
    n, x = map(int, input().split())
    coeffs = list(map(int, input().split()))
    print(evaluate_poly(x, coeffs))
