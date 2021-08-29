# not included in final score
#
budget = float(input())
price_flour_kg = float(input())

price_eggs_pack = price_flour_kg * 0.75
price_milk_liter = price_flour_kg * 1.25

price_one_kozunak = price_eggs_pack + price_flour_kg + (price_milk_liter / 4)

remaining_budget = budget
colored_eggs = 0
total_kozunaks = 0

while remaining_budget >= price_one_kozunak:
    colored_eggs += 3
    total_kozunaks += 1
    remaining_budget -= price_one_kozunak
    if total_kozunaks % 3 == 0:
        colored_eggs -= (total_kozunaks - 2)

print(f"You made {total_kozunaks} cozonacs! Now you have {colored_eggs} eggs and {remaining_budget:.2f}BGN "
      f"left.")