year = int(input()) + 1

while True:
    if len(str(year)) == len(set(str(year))):
        break
    year += 1

print(year)