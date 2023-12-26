from algorithms.times import time_execution
from algorithms._numbers import gcd

@time_execution
def f():
    numers = 1
    denoms = 1
    for numer in range(10,100):
        for denom in range(10,100):
            a = numer // 10
            b = numer % 10
            c = denom // 10
            d = denom % 10

            if 0 not in [a,b,c,d] and numer / denom < 1:
                if a == c and b /d == numer / denom:
                    numers *= numer
                    denoms *= denom
                    print((numer, denom), (b, d))
                if a == d and b / c == numer / denom:
                    numers *= numer
                    denoms *= denom
                    print((numer, denom), (b, c))
                if b == c and a / d == numer / denom:
                    numers *= numer
                    denoms *= denom
                    print((numer, denom), (a, d))
                if b == d and a / c == numer / denom:
                    numers *= numer
                    denoms *= denom
                    print((numer, denom), (a, c))

            
    
    common = gcd(numers, denoms)
    print(denoms / common)

f()