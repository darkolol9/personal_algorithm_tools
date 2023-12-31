from algorithms.times import time_execution


def get_nth_pentagonal(n):
    return n * (3 * n - 1) // 2

pentagonalD = {}



for i in range(1,100000):
    pentagonalD[get_nth_pentagonal(i)] = 1



@time_execution
def f():
    minD = int(1e6)

    for i in range(2, 10000):
        for j in range(1,i):
            a = get_nth_pentagonal(j)
            b = get_nth_pentagonal(i)

            if a + b in pentagonalD:
                if a - b in pentagonalD:
                    print('yay')
                    if abs(a - b) < minD:
                        minD = a - b
                        print(a, b, minD)



f()