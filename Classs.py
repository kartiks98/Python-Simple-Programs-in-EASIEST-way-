class St:
    x = 10
    c = 0

    def __init__(self, y):
        print(self.x)
        print(y)
        self.c += 1
        St.c += 1
        print(self.c)
        print(St.c)
        print("\n")
        self.c += 1
        print(self.c)
        print("\n")


s = St(20)
s2 = St(30)
