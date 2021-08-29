Divisor = int(input())
Bound = int(input())
maximum = 0

for N in range(1, Bound + 1):
    if N % Divisor == 0:    # Числото, което търсим
        maximum = N

print(maximum)