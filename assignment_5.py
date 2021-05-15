# Cornel Duhaney
# Knowledge House Prework
# 2021 Innovation Fellowship


names_list = ["bob", "jimmy", "max b", "bernie", "jordan", "future hendrix"]


def evens_or_odds(names):
    temp_list_1 = []
    temp_list_2 = []
    for name in names:
        if len(name) % 2 == 0:
            temp_list_1.append(name)
        else:
            temp_list_2.append(name)
    print(temp_list_1)
    print(temp_list_2)
    return temp_list_1


even_list = evens_or_odds(names_list)

print("The even list is: {}".format(even_list))  # String formatting

# I was unable to complete this as I kept running into errors related to the immutability of strings.
# I realized too late that I should find a way to index into each word separately. [0] for evens, [-1] for odds.
# I was however able to separate the lists into one even, one odd, returning and printing the even one.