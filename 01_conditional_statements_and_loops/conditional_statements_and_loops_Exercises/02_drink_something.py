drink_type = ""
age = int(input())

if age <= 14:
    drink_type = "toddy"
elif 14 < age <= 18:
    drink_type = "coke"
elif 18 < age <= 21:
    drink_type = "beer"
elif age > 21:
    drink_type = "whisky"

print(f"drink {drink_type}")