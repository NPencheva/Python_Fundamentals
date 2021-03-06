# (not included in final score)
#
number_of_snowballs = int(input())

max_snowball_value = 0
max_snowball_snow = 0
max_snowball_time = 0
max_snowball_quality = 0

for snowball in range(1, number_of_snowballs + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    current_snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    if current_snowball_value > max_snowball_value:
        max_snowball_value = current_snowball_value
        max_snowball_snow = snowball_snow
        max_snowball_time = snowball_time
        max_snowball_quality = snowball_quality

print(f"{max_snowball_snow} : {max_snowball_time} = {int(max_snowball_value)} ({max_snowball_quality})")