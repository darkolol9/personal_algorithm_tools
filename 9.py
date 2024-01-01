from algorithms.times import time_execution


@time_execution
def f():
    for a in range(800):
        for b in range(800):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                print(a*b*c)
            


f()