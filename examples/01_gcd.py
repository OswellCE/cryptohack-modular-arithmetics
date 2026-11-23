"""Example 1 - Greatest Common Divisor (Euclidean algorithm, recursive).

Demonstrates the same algorithm as modular_arithmetics.greatest_common_divisor().
Re-implemented inline so this script can run on its own.
"""

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def main():
    pairs = [(48, 18), (240, 46), (17, 5), (1071, 462), (0, 7)]
    for a, b in pairs:
        g = gcd(a, b)
        print(f"gcd({a}, {b}) = {g}")


if __name__ == "__main__":
    main()
