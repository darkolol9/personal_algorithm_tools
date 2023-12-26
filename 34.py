
from algorithms.times import time_execution
solved_factorials = {}


def factorial(n):
    
    if n in solved_factorials:
        return solved_factorials[n]
    
    res = 1
    for i in range(1, n + 1):
        res *= i

    solved_factorials[n] = res

    return res

    


@time_execution
def f():
    total = 0
    for i in range(100000):
        if len(str(i)) > 1 and sum([factorial(int(x)) for x in str(i)]) == i:
            total += i

    
    print(total)

f()
