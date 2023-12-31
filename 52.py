from algorithms.times import time_execution


def compare_digit_counts(a, b):
    digs_a = {x: 0 for x in range(10)}
    digs_b = {x: 0 for x in range(10)}


    for x in str(a):
        digs_a[int(x)] += 1

    for x in str(b):
        digs_b[int(x)] += 1


    for key in digs_a:
        if digs_a[key] != digs_b[key]:
            return False
        
    return True


@time_execution
def f():
    for i in range(1,100000000000000):
        if compare_digit_counts(i, 2 * i):
            if compare_digit_counts(i, 3 * i):
                if compare_digit_counts(i, 4 * i):
                    if compare_digit_counts(i, 5 * i):
                        if compare_digit_counts(i, 6 * i):
                            print(i)
                            break


f()