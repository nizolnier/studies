grades = [90, 88, 62, 76, 74, 89, 48, 57]

scaled_grades = [temp + 10 for temp in grades]

print(scaled_grades)

heights = [161, 164, 156, 144, 158, 170, 163]

can_ride_coaster = [temp for temp in heights if temp > 161]

print(can_ride_coaster)