from algorithms.times import time_execution


@time_execution
def sol():

    longest_streak = 0
    max_num = 1
    for i in range(2,1001):
        for t in range(2, 10):
            word = str(1/i)[t:]
            for j in range(len(word)):
                subword = word[:j]
                if (word.count(subword) > 1):
                    if (len(subword) > longest_streak):
                        print("word" , word, "subword", subword)
                        longest_streak = len(subword)
                        max_num = i

    print(longest_streak, max_num)

    

sol()