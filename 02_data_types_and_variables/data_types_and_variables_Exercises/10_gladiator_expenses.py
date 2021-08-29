# (not included in final score)
#
fights_lost = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_expenses = 0.0
shield_brakes = 0

for fight in range(1, fights_lost + 1):
    if fight % 2 == 0:  # broken helmet
        total_expenses += helmet_price
    if fight % 3 == 0:  # broken sword
        total_expenses += sword_price
    if fight % 2 == 0 and fight % 3 == 0:   # broken shield
        total_expenses += shield_price
        shield_brakes += 1
        if shield_brakes % 2 == 0:  # broken armor
            total_expenses += armor_price

print(f"Gladiator expenses: {total_expenses:.2f} aureus")