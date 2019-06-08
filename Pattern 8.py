k = 0
for i in range(1, 5):
    for j in range(1, i+1):
        x = str(k)
        print(end=x)
        k += 1
    for j in range(4-i, 0, -1):
        print(end=" ")
    print()
