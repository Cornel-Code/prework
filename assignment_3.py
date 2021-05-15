# Cornel Duhaney
# Knowledge House Prework
# 2021 Innovation Fellowship

names_list = ["bob", "jimmy", "max b", "bernie", "jordan", "future hendrix"]

longest_name = ''

for name in names_list:
    if len(name) > len(longest_name):
        longest_name = name
    else:
        continue

print(longest_name)
