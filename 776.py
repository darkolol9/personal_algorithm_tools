from algorithms.times import time_execution


def d(n):
    return sum(int(digit) for digit in str(n))




@time_execution
def f(n):
    s  = 0
    for i in range(1, n + 1):
        s += i / d(i)

    print(f'{s / 1e6}e6')


# f(1234567890123456789)
    

for i in range(200, 211):
    print(d(i))