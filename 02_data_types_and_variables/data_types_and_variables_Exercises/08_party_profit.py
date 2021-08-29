# (not included in final score)
#
from math import floor

party_size = int(input())
days = int(input())

total_coins_earned = 0

new_party_size = party_size

for day in range(1, days + 1):

    if day % 10 == 0:
        new_party_size -= 2
    if day % 15 == 0:
        new_party_size += 5

    COINS_PER_DAY = 50 - (2 * new_party_size)
    total_coins_earned += COINS_PER_DAY

    THIRD_DAY_COSTS = 3 * new_party_size
    FIFTH_DAY_INCOME = 20 * new_party_size
    THIRD_AND_FIFTH_DAY_COSTS = 2 * new_party_size

    if day % 3 == 0:
        total_coins_earned -= THIRD_DAY_COSTS
    if day % 5 == 0:
        total_coins_earned += FIFTH_DAY_INCOME
        if day % 3 == 0:
            total_coins_earned -= THIRD_AND_FIFTH_DAY_COSTS

coins_per_companion = floor(total_coins_earned / new_party_size)

print(f"{new_party_size} companions received {coins_per_companion} coins each.")