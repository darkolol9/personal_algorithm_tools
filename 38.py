from algorithms.times import time_execution




def is_pandigital(word):
    if len(word) != 9:
        return False
    for i in range(1, 10):
        if str(i) not in word:
            return False
    return True





@time_execution
def f():
    max_pan_digital = 1
    for i in range(1,10_000):
        s = str(i)
        for j in range(2, i*i):
            s += str(i * j)
            if is_pandigital(s):
                max_pan_digital = max(max_pan_digital, int(s))
            if len(s) > 9:
                break;


    print(max_pan_digital)
            
    
    


f()


