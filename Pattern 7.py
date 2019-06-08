k = 0
for i in range(1, 5):
    for j in range(5-i, 0, -1):
        print(end=" ")
    s = k
    for j in range(1, i+1):
        if k >= 0:
            x = str(k)
            print(end=x)
            k -= 1
    k = s+i+1
    print()
