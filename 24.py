from algorithms.times import time_execution
import sys


sys.setrecursionlimit(10_000_000)




def g(word, seen, words):

    if len(word) == 10:
        words.append(word)

    for i in range(10):
        if seen[i] == False:
            seen[i] = True
            g(word + str(i), seen, words)
            seen[i] = False

    



@time_execution
def sol():
    seen_digits  = {i : False for i in range(10)}

    word = ''
    words = []

    g(word, seen_digits, words)


    print(words[999_999])






sol()



