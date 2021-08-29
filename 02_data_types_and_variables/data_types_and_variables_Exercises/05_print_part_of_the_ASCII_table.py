start_ascii = int(input())
end_ascii = int(input())

for chars in range(start_ascii, end_ascii + 1):
    print(f"{chr(chars)} ", end="")