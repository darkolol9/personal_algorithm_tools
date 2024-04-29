from algorithms.times import time_execution
from algorithms._numbers import get_divisors
from math import sqrt

LIMIT = 1_000_000

def is_square(n):
    return int(sqrt(n)) ** 2 == n


@time_execution
def sol():
    best_x_and_d = 1, 1
    found = False
    x = 2

    while not found:
        if is_square(x):
            best_x_and_d = sqrt(x), x - 1


sol()
