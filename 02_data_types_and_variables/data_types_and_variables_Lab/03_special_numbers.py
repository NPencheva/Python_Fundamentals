# ВАРИАНТ 1:
#
# number = int(input())
#
# for n in range(1, number + 1):
#     sum_of_digits = 0
#     digits = n
#
#     while digits > 0:
#         sum_of_digits += digits % 10
#         digits = int(digits / 10)
#     if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
#         print(f"{n} -> True")
#     else:
#         print(f"{n} -> False")
#
# ------------------------------------------------------------
# ВАРИАНТ 2:

number = int(input())

for n in range(1, number + 1):
    sum_of_digits = 0
    n_str = str(n)

    for index in range(len(n_str)):
        sum_of_digits += int(n_str[index])

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{n} -> True")
    else:
        print(f"{n} -> False")
