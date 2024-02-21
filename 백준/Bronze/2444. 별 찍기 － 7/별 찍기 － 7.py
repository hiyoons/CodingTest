n = int(input())

for i in range(0, n):
    for j in range(0, n - i - 1):
        print(" ", end="")
    for k in range(2 * (i + 1) - 1):
        print("*", end="")

    print("")

for i in range(0, n - 1):
    for j in range(0, i + 1):
        print(" ", end="")
    for k in range(2 * (n - 1) - 2, 1 + i * 2 - 2, -1):
        print("*", end="")
    
    print("")
 