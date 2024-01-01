from algorithms.times import time_execution
from algorithms._numbers import *



limit = 80_000

prefix_sums = [1]

for i in range(1,limit):
     prefix_sums.append(prefix_sums[i - 1] + i)


print('finished calcing prefix_sums')


@time_execution
def sol():

    tirangle = 1
    pivot = 2
    divs = num_of_divisors(tirangle)
    while divs <= 500:
        print(tirangle, divs)
        tirangle += pivot
        divs = num_of_divisors(tirangle)
        pivot += 1

    
    print(tirangle)

sol()
    




