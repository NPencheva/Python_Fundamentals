number = float(input())

if number == 0:
    print("zero")
elif number < -1000000:
    print("large negative")
elif -1000000 <= number <= -1:
    print("negative")
elif -1 < number < 0:
    print("small negative")

elif 0 < number < 1:
    print("small positive")
elif 1 <= number <= 1000000:
    print("positive")
elif number > 1000000:
    print("large positive")