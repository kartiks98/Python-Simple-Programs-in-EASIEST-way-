for i in range(1, 6):
    for j in range(5-i, 0, -1):
        print(end=" ")
    for j in range(1, i+1):
        x = str(j)
        print(end=x)
    print()
