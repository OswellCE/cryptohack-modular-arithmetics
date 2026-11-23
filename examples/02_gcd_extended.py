"""Example 2 - Extended Greatest Common Divisor (Bézout identity).

Returns (g, x, y) such that  a*x + b*y = g = gcd(a, b).
Same algorithm as modular_arithmetics.greatest_common_divisor_extended().
Re-implemented inline so this script can run on its own.
"""

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x, y = egcd(b % a, a)
    return g, y - (b // a) * x, x


def main():
    pairs = [(240, 46), (1071, 462), (17, 5)]
    for a, b in pairs:
        g, x, y = egcd(a, b)
        check = a * x + b * y
        print(f"egcd({a}, {b}) = (g={g}, x={x}, y={y})")
        print(f"  verify: {a}*({x}) + {b}*({y}) = {check}  (must equal g = {g})")
        # The modular inverse of a modulo b (when gcd == 1) is x mod b:
        if g == 1 and b > 1:
            print(f"  => inverse of {a} mod {b} = {x % b}")


if __name__ == "__main__":
    main()
