x = 2.9
print(round(x))  # print: 3
x = -2.9
print(abs(x))  # print: 2.9

# module import for math
import math

x = 1.5
print(math.floor(x))     # print : 1
print(math.ceil(x))     # print: 2
print(math.fabs(x))     # Return the absolute value of x
x = 5
print(math.factorial(x))  # if x is not integer then raises valueError
print(math.gcd(10, 5))  # gcd return

# Trigonometric functions
print(math.cos(30))  # Return the cosine of x radians.
print(math.sin(30))  # Return the sin of x radians.

# Angular conversion
print(math.degrees(30))  # Convert angle x from radians to degrees
print(math.radians(30))  # Convert angle x from degrees to radians.

# Constant
print(math.pi)
print(math.e)

