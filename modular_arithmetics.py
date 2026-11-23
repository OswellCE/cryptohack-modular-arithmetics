#Cryptohack Modular Arithmetics Course Program
#Version 00
#First and simple functions

import math

def greatest_common_divisor(a,b): #Function with 2 input values
    if a == 0:#Verify a is equal to 0
        return b# In that case returns 0
    return greatest_common_divisor(b%a,a)#Bieng recursive means use of it until its 0

def greatest_common_divisor_extended(a,b):
    if a == 0:
        return b,0,1
    else:
        gcd,x,y = greatest_common_divisor_extended(b%a,a)
        return gcd , y - (b // a) * x,x

def modular_arithmetic_1():
    #The Congruence modulo relation can be transformed to a modulo operation
    a = 11 % 6
    b = 8146798528947 % 17
    return min(a,b)

def modular_arithmetic_2(a,b,c):
    #states that if c is a prime number, then for any integer a, the number a c – a is an integer multiple of c
    return pow(a,b) % c

def modular_inverting(a,p):
    # a^(p-1) ≡ 1 mod p
    # a^(p-1) * a^(-1) ≡ a^(-1) mod p
    # a^(p-2) * a * a^(-1) ≡ a^(-1) mod p
    # a^(p-2) ≡ a^(-1) mod p
    # <=>
    # a^(p-2) % p = a^(-1)
    #In Python code we can use the pow() function that can do the base**exp % mod
    return pow(a,p-2,p)

def quadratic_residues(p,ints):
    #qr = [min(pow(x,2,p) for x in ints)]
    # x ^ 2 = a mod p
    #Take for instance the number of times p take to equals x ^ 2,there are 2 possibilities like square roots
    #if the number calculated a = x ^ 2 % p its a quadratic residue this results in two numbers
    qr = [x for x in range(p) if pow(x,2,p) in ints]
    return qr

def modular_math_legendre(p,ints):
    #Calculate the quadratic root if int in ints calculated pow(a,(p-1)//2,p) == 1 returns true
    # https://math.stackexchange.com/questions/1273690/when-p-3-pmod-4-show-that-ap1-4-pmod-p-is-a-square-root-of-a
    # This follows from Euler's criterion which is similar to Legendre Symbol which states:
    # a^((p - 1) / 2)  ≡ 1 (mod p)
    # multipy through by a:
    # a^((p + 1) / 2) ≡ a (mod p)
    # (a^((p + 1) /4)) ^ 2 = a (mod p)
    # Since a^2 = x mod p means a is the root of x mod p then:
    # root is: (a^((p + 1) /4))
    an = []
    an = [pow(a,(p+1)//4,p) for a in ints if pow(a,(p-1)//2,p) == 1]
    return an

def main():
    print('Menu Options')
    print('1.-Greatest Common Divisor')
    print('2.-Greatest Common Divisor Extended')
    print('3.-Modular Arithmetic 1')
    print('4.-Modular Arithmetic 2: Fermats Theorem')
    print('5.-Modular Inverting: Fermats Theorem')
    print('6.-Quadratic Residues')
    print('7.-Modular Math Legendre Symbol')
    op = int(input(': '))
    if op == 1:
        print('Insert Numbers')
        num1 = int(input('a: '))
        num2 = int(input('b: '))
        print('The gcd is :',greatest_common_divisor(num1, num2))
    elif op == 2:
        print('Insert Numbers')
        num1 = int(input('a: '))
        num2 = int(input('b: '))
        print('The extended gcd is:',greatest_common_divisor_extended(num1,num2))
    elif op == 3:
        print('The minimun is:',modular_arithmetic_1())
    elif op == 4:
        print('Insert Numbers')
        num1 = int(input('a: '))
        num2 = int(input('b: '))
        num3 = int(input('c: '))
        print(modular_arithmetic_2(num1,num2,num3))
    elif op == 5:
        print('Insert Numbers')
        num1 = int(input('a: '))
        num2 = int(input('p: '))
        print(modular_inverting(num1,num2))
    elif op == 6:
        p = 29
        ints = [14,6,11]
        print(quadratic_residues(p,ints))
    elif op == 7:
            ints = []

            p = 

            print(modular_math_legendre(p,ints))
    else:
        print('This option doesnt exist')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Quiting......')
        exit()
