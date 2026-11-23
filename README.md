# Cryptohack Modular Arithmetics

Some Python I wrote while going through the **Modular Math** section on [CryptoHack](https://cryptohack.org/).

It's version 00 — just the first, simple functions. GCD, extended GCD, Fermat's little theorem, modular inverses, quadratic residues, and a Legendre-symbol thing. The kind of stuff that shows up over and over in crypto challenges, so I figured I'd write them out myself to actually understand them.

The code in `modular_arithmetics.py` is left exactly as I wrote it. This repo just documents it and gives you some examples to run.

---

## What's in here

```
cryptohack-modular-arithmetics/
├── modular_arithmetics.py     # the original program (unchanged)
├── README.md                  # this file
├── examples/                  # one little script per function
│   ├── 01_gcd.py
│   ├── 02_gcd_extended.py
│   ├── 03_modular_arithmetic_1.py
│   ├── 04_modular_arithmetic_2_fermat.py
│   ├── 05_modular_inverting.py
│   ├── 06_quadratic_residues.py
│   └── 07_modular_math_legendre.py
└── LICENSE
```

The example scripts re-implement each function inline, so you can run them on their own without touching `modular_arithmetics.py` (which has a small unfinished bit in option 7 — see [the gotchas](#heads-up) below).

---

## Run it

Just Python, no dependencies:

```bash
git clone https://github.com/OswellCE/cryptohack-modular-arithmetics.git
cd cryptohack-modular-arithmetics
python3 modular_arithmetics.py
```

You get a little menu:

```
Menu Options
1.-Greatest Common Divisor
2.-Greatest Common Divisor Extended
3.-Modular Arithmetic 1
4.-Modular Arithmetic 2: Fermats Theorem
5.-Modular Inverting: Fermats Theorem
6.-Quadratic Residues
7.-Modular Math Legendre Symbol
:
```

Options 1–6 work. Option 7 isn't finished yet.

To run a single example instead:

```bash
python3 examples/01_gcd.py
```

---

## What each function does

**`greatest_common_divisor(a, b)`** — the Euclidean algorithm, recursively. Keeps doing `gcd(b % a, a)` until `a` hits 0, then returns `b`.

**`greatest_common_divisor_extended(a, b)`** — same idea, but also gives you the Bézout coefficients `x, y` so that `a*x + b*y = gcd(a, b)`. Comes in handy for finding inverses when your modulus isn't prime.

**`modular_arithmetic_1()`** — just a demo that "x ≡ y (mod n)" is really just a remainder. Computes `11 % 6` and `8146798528947 % 17` and returns the smaller one (which is `4`).

**`modular_arithmetic_2(a, b, c)`** — Fermat's little theorem in action: if `c` is prime, then `a^c − a` is always a multiple of `c`. The code does `pow(a, b) % c` — works fine, though for big numbers you'd usually use the 3-argument form `pow(a, b, c)` (see [gotchas](#heads-up)).

**`modular_inverting(a, p)`** — finds `a^(-1) mod p` for prime `p`. Uses the trick `a^(p-2) ≡ a^(-1) (mod p)`, which falls straight out of Fermat. Implemented as `pow(a, p-2, p)`.

**`quadratic_residues(p, ints)`** — for each `a` in `ints`, finds every `x` in `0..p-1` whose square is `a mod p`. With `p=29, ints=[14,6,11]` it returns `[8, 21]` because `8² ≡ 21² ≡ 6 (mod 29)`, while `14` and `11` don't have roots mod 29.

**`modular_math_legendre(p, ints)`** — uses Euler's criterion (`a^((p-1)/2) mod p == 1` means `a` is a quadratic residue) and then takes the square root as `a^((p+1)/4) mod p`. The square-root trick only works when `p ≡ 3 (mod 4)` — see [gotchas](#heads-up).

---

## Examples

Each example in [`examples/`](./examples) is a standalone script that re-implements the algorithm inline (so it runs on its own) and prints the computation step by step.

| Script | What it shows | Sample output |
| --- | --- | --- |
| `01_gcd.py` | GCD | `gcd(48, 18) = 6` |
| `02_gcd_extended.py` | Extended GCD + Bézout check | `egcd(240, 46) = (2, -9, 47)`, with `240·(-9) + 46·47 = 2` |
| `03_modular_arithmetic_1.py` | The congruence-as-remainder demo | `min(5, 4) = 4` |
| `04_modular_arithmetic_2_fermat.py` | Fermat reduction | `pow(5, 100, 13) = 1` |
| `05_modular_inverting.py` | Modular inverse + verification | `3^(-1) mod 11 = 4`, and `3·4 ≡ 1 (mod 11)` |
| `06_quadratic_residues.py` | QR roots for `p=29` | `[8, 21]` for `a=6`; `14` and `11` are non-residues |
| `07_modular_math_legendre.py` | Correct case `p=23` vs broken case `p=29` | shows the shortcut failing when `p ≡ 1 (mod 4)` |

---

## Heads up

A few things worth knowing — I didn't change the code, just flagging them here.

- **Option 7 in `main()` is unfinished.** It literally says `p = ` with nothing after it, which is a Python syntax error, so the file as a whole won't import or run until you fill that in. To try it, replace `p = ` with something like `p = 23` and give `ints` a few values.
- **The Legendre shortcut needs `p ≡ 3 (mod 4)`.** The square-root trick `a^((p+1)/4) mod p` only works for primes that are 3 mod 4. The menu's own `p = 29` is `1 mod 4`, so the shortcut gives the wrong root there. Try `p = 23` instead — that's what example 07 uses. For `p ≡ 1 (mod 4)` you'd need the full Tonelli–Shanks algorithm.
- **`modular_arithmetic_2` computes the full `a^b` first.** `pow(a, b) % c` works but materialises a huge number before reducing. The idiomatic form `pow(a, b, c)` does modular exponentiation internally and is way friendlier to memory. Fine for teaching, not for big inputs.
- **Small comment typo.** In `greatest_common_divisor` the comment says "returns 0" but the function actually returns `b`, which is the right answer (`gcd(0, b) = |b|`). Just a typo in the comment, the code is correct.

---

## License

MIT — see [`LICENSE`](./LICENSE).
