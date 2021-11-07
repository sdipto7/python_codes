def binary(n):
    if n == 0: return "0"
    if n == 1: return "1"

    return binary(n // 2) + str(n % 2)


print("")
for i in range(10):
    f = binary(i)
    print(f"{i} (decimal) = {f} (binary)")