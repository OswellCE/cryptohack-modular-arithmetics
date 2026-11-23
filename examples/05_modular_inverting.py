"""Example 5 - Modular inverting via Fermat's little theorem.

For prime p and gcd(a, p) = 1:
    a^(p-1) ≡ 1 (mod p)
    a^(p-2) ≡ a^(-1) (mod p)

So  a^(-1) mod p  =  pow(a, p-2, p).

Same algorithm as modular_arithmetics.modular_inverting().
"""

def modular_inverting(a, p):
    return pow(a, p - 2, p)


def main():
    cases = [(3, 11), (7, 13), (5, 23), (271, 389)]
    for a, p in cases:
        inv = modular_inverting(a, p)
        # Verify: a * inv ≡ 1 (mod p)
        check = (a * inv) % p
        print(f"inverse of {a:>3} mod {p:>3} = {inv:>3};  "
              f"check: {a}*{inv} mod {p} = {check}  (must be 1)")


if __name__ == "__main__":
    main()
