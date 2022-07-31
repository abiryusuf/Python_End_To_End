

def fac(n):
    s = 1
    for i in range(1, n):
        s += i * 2
    print(s)

fac(5)