from algorithms.times import time_execution
from algorithms.primes import *
from itertools import permutations

def get_artithmitic_subseq_of_len_3(arr):
    """
    Returns a list of all the arithmetic subsequence of length 3 in the given array.

    Parameters:
        arr (list): A list of integers.

    Returns:
        list: A list of all the arithmetic subsequence of length 3 in the given array.
    """
    res = []
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                if arr[k] - arr[j] == arr[j] - arr[i]:
                    res.append([arr[i], arr[j], arr[k]])


    return res


def get_number_perms(n):
    """
    Generates a list of unique permutations of the given number.

    Parameters:
        n (int): The number to generate permutations for.

    Returns:
        list: A list of unique permutations of the given number.
    """
    return list(set([int(''.join([str(x) for x in p])) for p in permutations([int(x) for x in str(n)])]))

@time_execution
def f():
    cands = []
    for num in range(1000, 10000):
        if is_prime(num):
            perms = get_number_perms(num)

            prime_perms = list(filter(lambda x: is_prime(x) and len(str(x)) == 4, perms))
            if len(prime_perms) >= 3:
                cands.append(sorted(prime_perms))

    for t in cands:
        subs = get_artithmitic_subseq_of_len_3(t)
        if len(subs):
            print(subs)
    
f()



