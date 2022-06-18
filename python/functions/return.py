current_budget = 3500.75

def print_remaining_budget(budget):
    print("your remaining budget is $" + str(budget))

print_remaining_budget(current_budget)

def deduct_expense(budget, expense):
    return budget - expense

shirt_expense = 9 
new_budget = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget)

def top_tourist_locations_italy():
    first = "rome"
    second = "venice"
    third = "florence"
    return first, second, third

most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)




