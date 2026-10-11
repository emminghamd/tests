# python doesn't have alot of inbuilt mathematical options, to use more complex mathematical methods we have to usea a math module which is like a separate file, with python code
# because math is a object we can use the . notation to see all the possible functions
# before using any complex mathematical method we have to write the following:
import math

# print(math.comb(n, k)) - returns the ways to choose k items from n items without repetitions and without order
# n evaluates to n! / * (n - k)! when k <= n and evaluates to zero when k > n
print("COMB - returns the ways to chose k items from n items with repetition and without order")
print(math.comb(7, 2))
# 7! / ( 2! * (7-2)!)
# 7! = 7*6*5*4*3*2*1 = 5040 - 2! = 2*1 = 2 - 7-2 = 5! = 5*4*3*2*1 = 120
# 5040 - 2 * 120 = 21
print(math.comb(5, 3))
# 5! / (3! * (5-3)!) = 120 / (6 * 2) = 10
print(math.comb(3, 6))
# while if k is bigger than n it returns 0 as shown
# 6 / (30 * -6) = 6 / -180 = 0,333 technically but it returns 0 here

# raises typeerror if either of the arguments (n,k) are not integers
# print(math.comb(a, b))
# and the same goes for if the arguments are negatives
# print(math.comb(-1, -4))

# FACTORIAL returns factorial of the non-negative integer n we multiply each number for the number before it
print("FACTORIAL = x! for example 4! = 4*3*2*1 = 24")
# 4 * 3 * 2 * 1 = 24
print(math.factorial(4))
# 5 * 4 * 3 * 2 * 1 = 120
print(math.factorial(5))
# 6 * 5 * 4 * 3 * 2 * 1 = 720
print(math.factorial(6))

# GCD = greatest common divisor of the specific integer arguments
# if any of the arguments is a nonzero then the returned value is the largest positive integer that is a divisor of all arguments
# if all arguments are zero or gcd(0) then the value is 0
print("GCD = greatest common divisor")
print(math.gcd(400, 1230, 4280))

# ISQRT - return the integer square root of the nonnegative integer n
print("ISQRT = integer square root")
print(math.isqrt(40))
# square root of a number x is a number y such as y * y = x
# in the example above the square root would be 6.324 but we get 6 because we are getting back a integer (whole number)and not a float

# LCM = LEAST COMMON MULTIPLIER of the specific integer arguments or the smallest number that is evenly divisible by all integers in the set
# if all arguments are nonzero then the returned value is the smallest positive integer that is a multiple of all arguments
# if any argument is zero the returned value is 0, without arguments returns 1
print("LCM = LEAST COMMON MULTIPLIER")
print(math.lcm(12, 15, 30))
print(math.lcm(10, 15))

# PERM = math.perm(n, k=none)
# return the number of ways to choose k items from n items without repetition and with order
# math.perm(n, k=none) - n! / (n - k)! evaluates zero when k > n
# if k is not specified or is none then k defaults to n and the function returns n!
# raises typeerror if either arguments are not integers or if either arguments are negative
print("PERM")
print(math.perm(99, 7))
# practical example: how many different initial 7 cards hands do i have in a 99 card deck?
# 99! / (99-7)! = 93326215444e+15 / 124384140546e+142 = 75030638981760

# FLOATING POINT ARITHMETIC
print("FLOATING POINT ARITHMETIC")

# CEIL - math.ceil(x)
# this shows the ceiling outcome for the number
print("CEIL = ceiling outcome for the value x")
print(math.ceil(2.2))

# FABS - math.fabs(x)
# returns the absolute value of x
# so the non-negative value of x measured without regard to it's sign
print("FABS 0 absolute value of x")
print(math.fabs(-5))
# in the case of a number, even if negative it gives it's positive counterpart so -5 absolute value is 5 for example or -3's absolute value would be 3
print(math.fabs(0))
# the other possible outcome is 0, the absolute value of 0 is 0

# FLOOR - math.floor(x)
# return the floor of x, the largest integer less than or equal to x, if x is not a float delegates to x._floor_.
print("FLOOR = floor of the value x")
print(math.floor(2.4))
# example of x being a float returning the closest number (opposite to ceil essentially which searches the biggest)
print(math.floor(43))
# example of x being a integer

# FMA - math.fma(x, y, z)
# fused multiply-add operation returns (x * y) + z this operator provides better accuracy than the expression (x * y) + z
print("FMA = fused multiply-add operation")
print(math.fma(3, 2, 5.5))
# in the case of fma(0, inf, nan) and fma (inf, 0, nan) the return is NaN and does not raise exceptions

# FMOD - math.fmod(x, y)
# returns the floating-point remainder of x/ y
# if working with integers use x % y on python
print("FMOD = floating remainder of x/ y")
print(math.fmod(10.5, 2))

# MODF - mat.fmod(x)
# returns the fractional and integer parts of x. both results carry the sign of x and are floats
print("MODF - fractional and integer parts of x")
print(math.modf(13.4))

# REMAINDER - math.remainder(x, y)
# returns the iEEE 754-style remainder of x with respect to y
# for finite and finite x non zero y this is the difference x - n+y where n is the closest integer to the exact value of the quotient x / y.
# if x / y is exactly halfway bethween two consecutive integers
print(" REMAINDER - ")
print(math.remainder(13, 4))
# 13 / 4 would return 3,25 the remainder would be 1

# TRUNC - math.trunc(x)
# returns x with the fractional part removed, leaving the integer part, this rounds towards 0
# if x is not a float delegates to x._trunc_. which should return an integral value
print("trunc - returns x with the fractional part removed, leaving the integer part")
# trunc() is equivalent to floor() for positive x
print(math.trunc(10.9))
# equivalent to ceil() for negative x
print(math.trunc(-5.3))
# for cell(), floor() and modf() functions, all floating-point numbers that are sufficiently large magnitude are integers since python floats typically carry no more than 53 bits of precision
# in those cases any float x with abs(x) >= 2**52 necessarily has no fractional bits


# FLOATING POINT MANIPULATION FUNCTIONS
print("FLOATING POINT MANIPULATION FUNCTIONS")

# math.copysign(x, y) - returns a float with magnitude (absolute value) of x but the sign of y
print("copysign - returns the value of the first parameter(x) and the sign of the second (y)")
print(math.copysign(4, -1))
# x absolute value is 4, the sign of y is - = -4
print(math.copysign(-8, 97.21))
# x absolute value is 8, y sign is + = 8
print(math.copysign(-43, -76))
# x absolute value is 43, y sign is - = 43

# math.frexp(x) - returns mantissa and exponent of number/s as a pair
# if the value is not a number it returns typeerror
# the matissa is returned as a float, the exponent as a integer
print("frexp - returns mantissa and exponent of numbers")
print(math.frexp(4))
print(math.frexp(-4))
print(math.frexp(7))

# math.isclose(a, b, rel_tol, abs_tol) - checks wether two values are close to each other or not, the result is a boolean
# rel_tol is optional and sets the maximum allowed difference bethween values a and b
# abs_tol is optional and sets the minimum absolute tolerance, bethween values a and b, used to compare values near 0, the value must be at least 0
print("itclose - checks wether two values are close to each other or not the result is a boolean")
print(math.isclose(1.233, 1.4566))
print(math.isclose(1.233, 1.233))
print(math.isclose(1.233, 1.24))
print(math.isclose(1.233, 1.233000001))
# rel_tol=0,05 sets a relative tolerance of 5%
# in this case it turns true because we are within that margin
print(math.isclose(40, 38, rel_tol=0.05))
# in this case it turns false because we are not within that margin
print(math.isclose(40, 37, rel_tol=0.05))
# abs_tol= sets the absolute tolerance, defaults to 0.0 and must be nonnegative
# in this case we set the absolute tolerance to 2 returning the boolean true since the distance bethween a and b is equale or less than our abs
print(math.isclose(5, 3, abs_tol=2))
# in this case we set it to 1 returning the boolean false since the distance bethween a and b is too great
print(math.isclose(5, 3, abs_tol=1))

# math.isfinite(x)
# return true if x is a positive or negative infinity, false otherwise
print("isfinite - checks wether a number is finite or not returns a boolean")
print(math.isfinite(2000))
print(math.isfinite(-45.34))
print(math.isfinite(+45.34))
print(math.isfinite(math.inf))
print(math.isfinite(float("nan")))
print(math.isfinite(float("inf")))
print(math.isfinite(float("-inf")))
print(math.isfinite(-math.inf))
print(math.isfinite(0.0))

# math.isinf(x)
# returns true if the specified number is positive or negative infinitly, otherwise it returns false
print("isinf - returns the boolean true if the number is positive/negative infinitly otherwise returns false")
print(math.isinf(56))
print(math.isinf(-45.34))
print(math.isinf(+45.34))
print(math.isinf(math.inf))
print(math.isinf(float("nan")))
print(math.isinf(float("inf")))
print(math.isinf(float("-inf")))
print(math.isinf(-math.inf))

# math.isnan(x)
# returns true if x is a NaN (not a number) and false otherwise
print("isnan - returns the boolean true if x is NaN (not a number)")
print(math.isnan(56))
print(math.isnan(-45.34))
print(math.isnan(+45.34))
print(math.isnan(math.inf))
print(math.isnan(float("nan")))
print(math.isnan(float("inf")))
print(math.isnan(float("-inf")))
print(math.isnan(math.nan))

# math,idexp(x, i)
# returns x * (2**i) this is essentially the inverse of function frexp()
print(" inverse of a function - x * (2^i) - ( 2^i = 2 elevated at i)")
print(math.ldexp(9, 3))
# for example 9 x 2^3 (2) elevated at 3) = 9 x 2x2x2 = 9 x 8 = 72
print(math.ldexp(-5, 2))
# -5 * 2^2 = -5 * 2*2 = -20
print(math.ldexp(15, 5))
# 15 * 2^5 = 15 * 2*2*2*2*2 = 15 + 32 = 480

# math.nextafter(x, y steps=1)
# returns the floating-point value steps steps after x towards y - if x is equal to y returns y unless steps is zero
print("nextafter - returns the floating-point value steps steps after x towards y")
print(math.nextafter(1, math.inf))  # goes up: towards positive infinity.
print(math.nextafter(1, -math.inf))  # goes down: towards minus infinity.
print(math.nextafter(1, 0.0))  # goes towards zero.
print(math.nextafter(1, math.copysign(math.inf, 2)))  # goes away from zero.

# math.ulp(x)
# returns the value of the least significant bit of the float x
# If x is a NaN (not a number), return x.
# If x is negative, return ulp(-x).
# If x is a positive infinity, return x.
# If x is equal to zero, return the smallest positive denormalized representable float (smaller than the minimum positive normalized float, sys.float_info.min).
# If x is equal to the largest positive representable float, return the value of the least significant bit of x, such that the first float smaller than x is x - ulp(x).
# Otherwise (x is a positive finite number), return the value of the least significant bit of x, such that the first float bigger than x is x + ulp(x).
print("ulp - returns the value of the least significant bit of the float")
print(math.ulp(1.1))

# POWER, EXPONENTIAL and LOGARITHMIC FUNCTIONS

# math.cbrt(x)
# returns the cube root of x aka the value that, when multiplied by itself three times equals the original number
print(" CBRT - return the cube root of x")
print(math.cbrt(8))
# 2*2*2 = 8
print(math.cbrt(125))
# 5*5*5 = 125

# math,exp(x) - method returns E raised to the power of x (Ex)
# return "E" raised to the power of different numbers
# E is = 2.718282 x is the number passed to it
# function used to model situations where quantity grows or shrinks by a fixed percentage over equal intervals, such as population growth, radioactive decay, interest calculations, spread of diseases
print("EXP - find the exponential(growth) of the specified value")
print(math.exp(4))
print(math.exp(-2.89))

# math.exp2(x) - returns 2 raised to the power x
print("EXP2 - returns 2 raised to the power x")
print(math.exp2(3))
# 2*2*2 = 8
print(math.exp2(8))
# 2*2*2*2*2*2*2*2 = 256

# math.exp1(x) - find the exponential value of a number - 1
# Ex - 1 - E = 2.718282
# used over the math.exp function due to it being more precise for small floats x
print("exp1 - exponential value of a number -1")
print(math.exp(32))
# example of exp used on a big float
print(math.expm1(32))
# example of expm1 on a big float
print(math.exp(1e-5))
# less accuracy of the exp function when using small floats
print(math.expm1(1e-5))
# accuracy of the exp1 function when using small floats

# logarithms - a logarithm of a number is the exponent by which another fixed value, the base must be raised to produce that number
# for example the logarithm of 1000 to base 10 is 3 because 1000 is 10 to the 3rd power
# 1000 = 10^3 = 10 × 10 × 10

# math.log(x[, base]) - with one argument returns the natural logarithm of x (to base e)
# with two arguments return the logarithm of x to the given base calculated as log(x/log(base)
print("LOG - with one argument returns the natural logarithm of x to base e")
# another way to explain it is, 17 is the base and the result is the natural logarithm of 17
print("Natural logarithm of 17 is: ", end="")
print(math.log(17))
# here we already have the base
print("logarithm base 5 of 17 is: ", end="")
print(math.log(17, 5))
# if we paragon with the 1000 - 10 - 3 of earlier 1000 is the 17 10 is the 5 and 3 is whatever the log calculates

# math.log1p(x) - returns the natural logarithm of 1+x(base e)
# the result is calculated in a way which is accurate for x near zero
print("log1p - returns the natural logarithm of 1+x(base e)")
print("Natural logarithm of 17+1 is: ", end="")
print(math.log1p(1))

# math.log2(x) - returns the base -2 logarithm of x
# this is more accurate than log (x, 2)
print("log2 - return the base-2 logarithm of a number x")
print("logarythm of 17-2 is:", end="")
print(math.log2(17))

# math.log10(x) - returns the base -10 logarithm of x
# this is more accurate than log (x, 10)
print("log10 - return the base-10 logarithm of a number x")
print("logarythm of 17-10 is:", end="")
print(math.log10(17))

# math.pow(x, y) - return x raised to the power y
# pow(1.0, x) and pow(x, 0.0) allways return 1 even when x is zero or NaN
# if both x and y are finite, x is negative and y is not an integer then pow(x, y) is undefind and raises valueerror
print("pow - return x raised to the power y")
print("x raised to the power of y is:", end="")
print(math.pow(2, 3))
# this would be 2^3 = 8 or 2 x 2 x 2 = 8
print("x raised to the power of y is:", end="")
print(math.pow(2, -3))
print("x raised to the power of y is:", end="")
print(math.pow(2, 1/3))
print("pow(1.0, x) and pow(x, 0.0) allways return:", end="")
print(math.pow(0, 0))

# math.sqrt(x) - returns the square root of x as a float
# returns valueerror if x is a negative number because the square root number is not definined for negative numbers
print("sqrt returns the square root of x as a float:", end="")
print(math.sqrt(12))
# a square root of a number x is that positive number that multiplied for itself gives x

# math.isqrt(x) - returns the square root of x as a integer
# returns valueerror if x is a negative number because the square root number is not definined for negative numbers
print("isqrt returns the square root of x as a integer:", end="")
print(math.isqrt(12))
# a square root of a number x is that positive number that multiplied for itself gives x

print("Summation and product functions")

# math,dist - returns the euclidean distance bethween 2 points (p and q)
# the two points must be of the same dimensions
print("dist returns the euclidean distance bethween two points, p and q:", end="")
p = [3]
q = [1]
print(math.dist(p, q))
print("dist returns the euclidean distance bethween two points, p and q:", end="")
p = [3, 3]
q = [6, 12]
print(math.dist(p, q))

# math.fsum(iterable)
print("fsum returns the sum of all items:", end="")
print(math.fsum([1.7, 0.3, 1.5, 4.5]))

# math.hypot (*coordinates) -
print("hypot return the hypotenuse of a right-angled triangle where perpendicular and base are known and to calculate the euclidean norm:", end="")
# set perpendicular and base
perpendicular = 10
base = 5
# print the hypotenuse of a right-angled triangle
# print(math.hypot(parendicular, base))
print(math.hypot(10, 5))

# math.prod(iterable, *, start=1)
# when the iterable is empty return the start value, this function is intended specifically for use with numeric values
print("prod returns the product of the elements from the given iterable:", end="")
sequence = (2, 2, 2)
# return the product of the elements
print(math.prod(sequence))

# math.sumprod(p, q)
print("sumprod returns the sum of products of values from two iterables p and q:", end="")
p = [2]
q = [5]
print(math.sumprod(p, q))
# does p * q = 2 * 5 = 10
