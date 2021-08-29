number = int(input())

for i in range(1, number + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()

for k in range(number - 1, 0, -1):
    for l in range(1, k + 1):
        print("*", end="")
    print()