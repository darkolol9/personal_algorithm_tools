from algorithms.times import time_execution



def factorial(n):
    m = 1
    for i in range(1, n+1):
        m *= i

    return m

def factorialize(num):
    return sum([factorial(int(x)) for x in str(num)])



def dfs(num, length = 1, seen = {}):

    if num in seen:
        return length - 1

    seen[num] = 1
    return dfs(factorialize(num), length + 1, seen)

@time_execution
def f():
    t = 0
    for i in range(1, 1000000):
        if dfs(i, 1 , {}) == 60:
            print(f'found one {i}')
            t += 1


    print(t)




f()


