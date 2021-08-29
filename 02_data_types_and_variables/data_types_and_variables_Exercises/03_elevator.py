from math import ceil

number_of_people_n = int(input())
elevator_capacity_p = int(input())

courses = ceil(number_of_people_n / elevator_capacity_p)

print(courses)