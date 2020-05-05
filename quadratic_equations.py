import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

print(type(a))


def get_quadratic_equations(a, b, c):
    discriminator = b * b - 4 * a * c
    print("Discriminator: " + str(discriminator))
    if discriminator < 0:
        return []
    elif discriminator == 0:
        return -b / 2 * a
    else:
        return [(-b + math.sqrt(discriminator)) / 2 * a,
                (-b - math.sqrt(discriminator)) / 2 * a]


print(get_quadratic_equations(a, b, c))
