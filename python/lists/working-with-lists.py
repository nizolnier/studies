display = ["mango", "filet mignon", "chocolate milk"]

print(display)

# insert(index, item) 
display.insert(0, "pineapple")

print(display)

##########
data_science_topics = ["machine learning", "sql", "pandas", "algorithms", "statistics", "python 3"]

print(data_science_topics)

# pop(index)
data_science_topics.pop(2)

print(data_science_topics)

#########
# range creates consecutive list
number_list = range(3)

print(list(number_list)) # [0, 1, 2]

range_five_three = range(5, 15, 2)

print(list(range_five_three)) # [5, 7, 9, 11, 13]

range_diff_five = range(0, 40, 5)

print(list(range_diff_five))

#########
big_range = range(2, 3000, 10)

big_list = list(big_range)

# len(list) returns length
big_list_len = len(big_list)

print(big_list_len)

#########
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# slice list[index:index] save a few items from a list
beginning = suitcase[0:2]
print(beginning)

middle = suitcase[2:4]
print(middle)

end = suitcase[-2:]
print(end)

#########
votes = ["jake", "jake", "jake", "jake", "laurie", "laurie", "cassie", "cassie", "jake", "jake"]

# count(item)
jakes_votes = votes.count("jake")
print(jakes_votes)

#########
names = ["ron", "hermione", "harry", "albus", "sirius"]

names.sort()

print(names)

cities = ["london", "paris", "rome", "los angeles", "new york"]

cities.sort(reverse=True)

print(cities)

games = ["portal", "minecraft", "pacman", "tetris", "the sims", "pokemon"]

games_sorted = sorted(games)

print(games)
print(games_sorted)