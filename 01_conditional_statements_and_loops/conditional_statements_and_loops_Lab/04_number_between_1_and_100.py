# ВАРИАНТ 1:
number = float(input())

while True:
    if 1 <= number <= 100:
        print(f"The number {number} is between 1 and 100")
        break
    else:
        number = float(input())
# -----------------------------------------------------------------
# ВАРИАНТ 2:
# number = float(input())
#
# while True:
#     if number < 1 or number > 100:
#         number = float(input())
#     else:
#         print(f"The number {number} is between 1 and 100")
#         break