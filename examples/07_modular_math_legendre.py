"""Example 7 - Legendre symbol / Euler criterion and the p ≡ 3 (mod 4) square-root shortcut.

Euler criterion:   a^((p-1)/2) mod p  =  1  if a is a QR mod p
                                       =  p-1 (i.e. -1)  if a is a QNR mod p
                                       =  0  if a ≡ 0 (mod p)

Square-root shortcut (Tonelli, p ≡ 3 (mod 4) ONLY):
    sqrt(a) ≡ a^((p+1)/4) (mod p)

This script:
  * runs the shortcut for a CORRECT prime  p = 23  (23 ≡ 3 (mod 4));
  * runs the shortcut for a WRONG prime  p = 29  (29 ≡ 1 (mod 4)) and shows
    that it produces a wrong square root, illustrating the caveat in the README.
"""

def euler_criterion(a, p):
    """Returns 1 if a is a QR mod p, -1 (i.e. p-1) if a is a QNR, 0 if a ≡ 0."""
    return pow(a, (p - 1) // 2, p)


def legendre_sqrt(a, p):
    """a^((p+1)/4) mod p  -- valid only when p ≡ 3 (mod 4)."""
    return pow(a, (p + 1) // 4, p)


def main():
    # ---- Correct case: p = 23 (23 ≡ 3 (mod 4)) ----
    print("CORRECT case:  p = 23  (23 mod 4 =", 23 % 4, ")")
    p = 23
    # Find some actual QRs mod 23 to use as `ints`.
    ints = sorted({pow(x, 2, p) for x in range(1, p)})
    print(f"  All QRs mod {p}: {ints}")
    # Demonstrate the shortcut on a few of them
    for a in [2, 4, 9]:
        e = euler_criterion(a, p)
        if e == 1:
            r = legendre_sqrt(a, p)
            print(f"  a = {a:>2}  |  Euler = {e} (QR)  |  "
                  f"a^((p+1)/4) = {r}  |  verify: {r}^2 mod {p} = {pow(r, 2, p)}")
        else:
            print(f"  a = {a:>2}  |  Euler = {e} (not a QR)")

    print()

    # ---- Wrong case: p = 29 (29 ≡ 1 (mod 4)) ----
    print("WRONG case:  p = 29  (29 mod 4 =", 29 % 4, " — NOT 3)")
    p = 29
    # 6 is a QR mod 29 with roots 8 and 21.
    a = 6
    e = euler_criterion(a, p)
    r = legendre_sqrt(a, p)
    print(f"  a = {a}  |  Euler = {e} (so a IS a QR)")
    print(f"  a^((p+1)/4) = a^{(p+1)//4} = {r}  (the shortcut 'root')")
    print(f"  But  {r}^2 mod {p} = {pow(r, 2, p)}  ≠  {a}  -- the shortcut FAILED.")
    print("  True roots of 6 mod 29 are:", [x for x in range(p) if pow(x, 2, p) == a])
    print("  => For p ≡ 1 (mod 4) you need the full Tonelli-Shanks algorithm.")


if __name__ == "__main__":
    main()
