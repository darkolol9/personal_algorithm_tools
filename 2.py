from algorithms.times import time_execution




@time_execution
def f():
    total = 0
    a, b = 1, 2

    while b < 4 * 1e6:

        if b % 2 == 0:
            total += b

        a, b = b, a + b
  
    print(total)

    

f()



