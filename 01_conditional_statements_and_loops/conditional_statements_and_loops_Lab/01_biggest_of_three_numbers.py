# https://judge.softuni.bg/Contests/1718

# 1. Biggest of Three Numbers

a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)
# -----------------------------------------------
# a = int(input())
# b = int(input())
# c = int(input())
#
# highest = max(a, b, c)
# print(highest)