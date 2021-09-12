n = int(input())
word = input()

full_list = []
short_list = []

for item in range(1, n + 1):
    string = input()
    full_list.append(string)

    if word in string:
        short_list.append(string)

print(full_list)
print(short_list)