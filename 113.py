from algorithms.times import time_execution



def generate_increasing_until(n, curr = '1', ans = {"count": 0}):
    '''this function is bad'''
    if int(curr) >= n:
        return ans["count"]

    for i in range(0, 10):
        if (i >= int(curr[-1])):
            ans["count"] += 1
            generate_increasing_until(n, curr + str(i), ans)



@time_execution
def sol():
    LIMIT = 7

    total = 0

    for lens in range(3, LIMIT):
        for i in range(lens - 3 + 1):
            for dig in range(2, 10):
                if (i == 0): # first iteratin, first slot cant be the digit 0
                    total += ((9 ** (lens - 3))  * (dig - 1) * (dig) )
                else:
                    total += ((9 ** (lens - 3)) * (dig) * (dig))
        
    print((10 ** (LIMIT - 1)) - total)




sol()
