from operator import truediv


print((5*2) -1 == 8 +1) # true
print(13 - 6 != (3*2)+1) # false
print(3*(2-1) == 4-1) # true

bool_one = 5 != 7
bool_two = 1 + 1 != 2
bool_three = 3*3 == 9

print(bool_one) # true
print(bool_two) # false
print(bool_three) # true

my_baby_bool = "true"
print(type(my_baby_bool)) # str

my_baby_bool = True
print(type(my_baby_bool)) # bool