dog_breeds_available = ["french bulldog", "dalmatian", "shihtzu", "poodle"]

dog_breed_I_want = "dalmatian"

for temp in dog_breeds_available:
    if(temp == dog_breed_I_want):
        print('found the dalmatian!')
        break

ages = [12, 38, 34, 26, 21, 19, 67]


for age in ages:
    if age < 21:
        continue
    print(age)