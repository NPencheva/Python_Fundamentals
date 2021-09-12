n = int(input())

even_list = []
odd_list = []
negative_list = []
positive_list = []

for num in range(1, n + 1):
    number = int(input())
    if number % 2 == 0:
        even_list.append(number)
    if not number % 2 == 0:
        odd_list.append(number)
    if number >= 0:
        positive_list.append(number)
    else:
        negative_list.append(number)

command = input()

if command == "even":
    print(even_list)
if command == "odd":
    print(odd_list)
if command == "positive":
    print(positive_list)
if command == "negative":
    print(negative_list)