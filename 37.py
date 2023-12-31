from algorithms.times import *
from algorithms.primes import *


seen = {}

def truncable_from_left(i):
    word = str(i)[1:]
    while word:
        if int(word) in seen or not is_prime(int(word)):
            return False
        seen[int(word)] = 1
        word = word[1:]

    return True

def truncable_from_right(i):
    word = str(i)[:-1]
    while word:
        if int(word) in seen or not is_prime(int(word)):
            return False
        seen[int(word)] = 1
        word = word[:-1]

    return True

@time_execution
def f():
    s = 0
    count = 0
    i = 0
    while count < 12:
        if is_prime(i):
            if truncable_from_left(i) and truncable_from_right(i):
                count += 1
                print('got one!', count, i)
                s += i
        i += 1
            

         
            
    print("sum" ,s)



f()