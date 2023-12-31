from algorithms.times import time_execution


memo = {}


def factorial(n):
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = n * factorial(n - 1)
    return memo[n]

@time_execution
def f():
    million = 1_000_000

    count = 0

    for i in range(1,101): 
        for j in range(i):
            if factorial(i) / (factorial(j) * factorial(i - j)) > million:
                count += 1
    print(count)


f()