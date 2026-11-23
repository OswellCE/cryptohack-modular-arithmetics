"""Example 3 - Modular arithmetic 1 (the congruence relation as a remainder).

Same computation as modular_arithmetics.modular_arithmetic_1():
    a = 11 % 6
    b = 8146798528947 % 17
    return min(a, b)
"""

def main():
    a = 11 % 6
    b = 8146798528947 % 17
    print(f"11 % 6                 = {a}")
    print(f"8146798528947 % 17     = {b}")
    print(f"min(a, b)              = {min(a, b)}")


if __name__ == "__main__":
    main()
