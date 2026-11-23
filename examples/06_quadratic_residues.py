"""Example 6 - Quadratic residues.

A number a is a quadratic residue mod p if there exists x with  x^2 ≡ a (mod p).
This script lists all square roots of every a in `ints` modulo p,
exactly as modular_arithmetics.quadratic_residues() does.
"""

def quadratic_residues(p, ints):
    return [x for x in range(p) if pow(x, 2, p) in ints]


def main():
    # The default call from the menu in modular_arithmetics.py:
    p = 29
    ints = [14, 6, 11]
    roots = quadratic_residues(p, ints)
    print(f"p = {p}, ints = {ints}")
    print(f"Square roots found: {roots}")
    print()

    # Show, for each a in ints, whether it is a QR and what its roots are.
    for a in ints:
        rs = [x for x in range(p) if pow(x, 2, p) == a]
        if rs:
            print(f"  {a:>2} IS   a quadratic residue mod {p};  roots = {rs}")
            for r in rs:
                print(f"      check: {r}^2 mod {p} = {pow(r, 2, p)}")
        else:
            print(f"  {a:>2} is NOT a quadratic residue mod {p}")


if __name__ == "__main__":
    main()
