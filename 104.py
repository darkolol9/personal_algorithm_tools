from algorithms.times import time_execution

# get the first 9 digits of a numbers fast
def get_first_9_digits(n):

    while n >= 1_000_000_000:
        n = n // 10

    return n


def check_pandigitality_start(n):
    
    first_9 = get_first_9_digits(n)

    for i in range(1,10):
        if str(i) not in str(first_9):
            return False
        
    return True

def check_pandigitality_end(n):
    last_9 = n % 10**9

    for i in range(1,10):
        if str(i) not in str(last_9):
            return False
        
    return True

    

    

@time_execution
def f():
    f1, f2 = 1, 2
    last_9 = 3
    idx = 3

    while not check_pandigitality_end(f2) or not check_pandigitality_start(f2):
        if idx % 1_000 == 0:
            print('1k done', idx)

        f1, f2 = f2, f1 + f2
        idx += 1
      
    print("answer" , idx)



f()