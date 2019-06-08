k = 0
for i in range(1, 5):
    d = k
    for j in range(1, 6):
        if j <= 5-i:
            print(end=" ")
        else:
            x = str(k)
            print(end=x)
            k -= 1
    k = d+i+1
    print()
