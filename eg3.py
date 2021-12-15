def d1(func):
    def d2():
        result = func()
        return result + 'python learners'
    return d2

def d3():
    return 'hello'

r = d1(d3)
print(r())

