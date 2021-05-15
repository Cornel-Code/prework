# Cornel Duhaney
# Knowledge House Prework
# 2021 Innovation Fellowship

def longest_name(names):
    temp_name = ""
    for name in names:
        if len(name) > len(temp_name):
            temp_name = name
    return temp_name


names_list = ["bob", "jimmy", "max b", "bernie", "jordan", "future hendrix"]

big_name = longest_name(names_list)
print(big_name)