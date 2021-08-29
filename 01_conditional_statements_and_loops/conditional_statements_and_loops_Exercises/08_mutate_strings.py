str1 = input()
str2 = input()

current_string = ""
previous_string = str1

for iteration in range(0, len(str1)):
    for index_str2 in range(0, iteration + 1):
        current_string += str2[index_str2]
    for index_str1 in range(iteration + 1, len(str1)):
        current_string += str1[index_str1]
    if not previous_string == current_string:
        print(current_string)
    # Подготовка на данните за следващата итерация:
    previous_string = current_string
    current_string = ""