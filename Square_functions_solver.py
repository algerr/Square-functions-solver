# Copyright by algerr on GitHub 2020
# Private usage and commercial only with permission by the owner

import os
import math

# finding roots
def equationroots( a, b, c):

    # calculating discriminant
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))

    # checking condition for discriminant
    if dis > 0:
        print("real and different roots ")
        print((-b + sqrt_val)/(2 * a))
        print((-b - sqrt_val)/(2 * a))

    elif dis == 0:
        print("real and same roots")
        print(-b / (2 * a))

    # discriminat less than 0
    else:
        print("Complex Roots")
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)

# values
a = int(input("a: "))
b = int(input("p/b: "))
c = int(input("q/c: "))

# If a = 0, incorrect
if a == 0:
        print("Input correct quadratic equation")

else:
    equationroots(a, b, c)

os.system("pause")
