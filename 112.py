from algorithms.times import time_execution




def is_bouncy(n):
    n = str(n)
    return n != "".join(sorted(n)) and n != "".join(sorted(n, reverse=True))


@time_execution
def f():
    bouncy_numbers = 19602
    numbers_seen = 21780

    while bouncy_numbers / numbers_seen < 0.99:
        if (numbers_seen % 1000) == 0:
            print(bouncy_numbers / numbers_seen)
        if is_bouncy(numbers_seen):
            bouncy_numbers += 1
        numbers_seen += 1

    print(numbers_seen)



f()