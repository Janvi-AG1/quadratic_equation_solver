#finding roots of the quadratic equation ax^2 + bx + c=0

import math
import cmath

#to round up every result
def round_up(x, digits):
    """to round up a real number"""
    factor = 10 ** digits
    return math.ceil(x * factor) / factor

def round_up_c(z, digits):
    """to round up a complex numebr"""
    factor = 10 ** digits
    real = math.ceil(z.real * factor) / factor
    imag = math.ceil(z.imag * factor) / factor
    return complex(real, imag)

#calculating roots
def find_roots(a, b, c):
    #calculation of discriminant
    d = (b ** 2 - 4 * a * c)
    print('discriminant is', d)

    """conditions based on value of d"""
    if d < 0:
        print('imaginary roots')
        # to calculate imaginary roots
        r1 = round_up_c(((-b + cmath.sqrt(d)) / (2 * a)), 2)
        r2 = round_up_c(((-b - cmath.sqrt(d)) / (2 * a)), 2)
        return r1, r2
    elif d == 0:
        print('only one root')
        r = -b / (2 * a)
        return r
    else:
        print('two unique roots')
        #to calculate real roots
        r1 = round_up(((-b + math.sqrt(d)) / (2 * a)), 2)
        r2 = round_up(((-b - math.sqrt(d)) / (2 * a)), 2)
        return r1, r2

def main():
    print('Qudratic equation solver : ax^2 + bx + c =0')
    #to validate the values using try except block
    try:
        a = float(input("Enter coeff of x^2: "))
        b = float(input("Enter coeff of x: "))
        c = float(input("Enter constant: "))
    except ValueError:
        print("invalid input")
        return

    #coefficient of x^2 should not be 0
    if a==0:
        print('this is not a quadratic equation')
        return

    print(f"your quadratic equation is: {a}x² + {b}x + {c} = 0")
    roots = find_roots(a, b, c)
    print('root: ', roots)

#to guard the main() function
if __name__ == "__main__":
    main()
