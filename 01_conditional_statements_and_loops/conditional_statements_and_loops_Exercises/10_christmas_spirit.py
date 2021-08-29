# (not included in final score)

allowed_quantity = int(input())
days_until_christmas = int(input())

ornament_set_price = 2
tree_skirt_price = 5
garlands_price = 3
tree_lights_price = 15

total_costs = 0
christmas_spirit = 0

for day in range(1, days_until_christmas + 1):
    if day % 11 == 0:
        allowed_quantity += 2
    if day % 2 == 0:    # ornament set
        total_costs += allowed_quantity * ornament_set_price
        christmas_spirit += 5
    if day % 3 == 0:    # tree skirt AND garlands
        total_costs += allowed_quantity * (tree_skirt_price + garlands_price)
        christmas_spirit += 13
    if day % 5 == 0:    # tree lights
        total_costs += allowed_quantity * tree_lights_price
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        total_costs += tree_skirt_price + garlands_price + tree_lights_price
        if day == days_until_christmas:
            christmas_spirit -= 30

print(f"Total cost: {total_costs}")
print(f"Total spirit: {christmas_spirit}")