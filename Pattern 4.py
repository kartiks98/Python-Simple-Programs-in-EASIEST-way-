for i in range(1, 6):
    for j in range(1, i):
        print(end=" ")
    print(end="*")
    if i < 3:
        for j in range(1, 6-(2*i)):
            print(end=" ")
        print(end="*")
    elif i > 3:
        for j in range(6-(2*i), -1):
            print(end=" ")
        print(end="*")
    print()
