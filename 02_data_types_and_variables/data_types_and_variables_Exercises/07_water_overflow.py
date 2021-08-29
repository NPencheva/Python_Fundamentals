number_of_inputs = int(input())

tank_capacity = 255
filled_capacity = 0

for liters in range(1, number_of_inputs + 1):
    current_liters = int(input())
    if filled_capacity + current_liters > tank_capacity:
        print(f"Insufficient capacity!")
        continue
    else:
        filled_capacity += current_liters

print(filled_capacity)