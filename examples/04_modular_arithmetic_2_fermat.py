"""Example 4 - Modular arithmetic 2: Fermat's little theorem.

Fermat:  if c is prime and gcd(a, c) = 1, then  a^(c-1) ≡ 1 (mod c).
The original function does  pow(a, b) % c , which is correct but inefficient
(it materialises the full a^b). The idiomatic, constant-memory form is
pow(a, b, c). This script shows both, plus a Fermat-style reduction.

Same algorithm as modular_arithmetics.modular_arithmetic_2().
"""

def modular_arithmetic_2_naive(a, b, c):
    """As written in the original program: full exponentiation, then reduce."""
    return pow(a, b) % c


def modular_arithmetic_2_fast(a, b, c):
    """Idiomatic Python: built-in modular exponentiation."""
    return pow(a, b, c)


def main():
    # Small demo
    print("Fermat's little theorem:  a^(c-1) ≡ 1 (mod c) for prime c, gcd(a,c)=1")
    for (a, c) in [(2, 13), (5, 17), (10, 7)]:
        print(f"  {a}^({c}-1) mod {c} = {pow(a, c - 1, c)}  (should be 1)")

    # Compare the naive vs the fast form on a Fermat-sized exponent
    a, b, c = 5, 100, 13
    naive = modular_arithmetic_2_naive(a, b, c)
    fast = modular_arithmetic_2_fast(a, b, c)
    print(f"\npow({a}, {b}) % {c}   = {naive}   (original code)")
    print(f"pow({a}, {b}, {c})     = {fast}   (idiomatic; same result, far less memory)")

    # Fermat reduction: a^b mod c = a^(b mod (c-1)) mod c   (when gcd(a,c)=1)
    reduced_exp = b % (c - 1)
    print(f"By Fermat:  {a}^{b} mod {c} = {a}^{reduced_exp} mod {c} = {pow(a, reduced_exp, c)}")


if __name__ == "__main__":
    main()
