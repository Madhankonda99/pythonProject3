def d1(n):
    def d2(func):
        global i
        for i in range(n):
            func()
    return d2

@d1 (5*5)
def d3():
    print(i)

