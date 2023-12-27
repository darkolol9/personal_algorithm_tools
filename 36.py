

from algorithms.times import time_execution
from algorithms._numbers import get_in_binary
from algorithms.strings import is_palindrome






@time_execution
def f():
    total = 0
    for i in range(int(1e6)):
        if is_palindrome(str(i)) and is_palindrome(get_in_binary(i)):
            total += i


    print(total)

f()