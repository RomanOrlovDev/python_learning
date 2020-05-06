import math


def get_triangle_square(a, b, c):
    half_p = (a + b + c) / 2
    return math.sqrt(
        half_p * (half_p - a) * (half_p - b) * (half_p - c)
    )


print(get_triangle_square(5, 3, 4))
