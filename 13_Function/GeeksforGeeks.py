num3 = 0


def add(num1, num2):
    num3 = num1 + num2
    return num3


num1 = 5
num2 = 6
print(add(3, 5))
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}")


def prime(num):
    if num in [2, 3]:
        return True
    if (num == 1) or (num % 2 == 0):
        return False
    r = 3
    while r * r <= num:
        if num % r == 0:
            return False
        r += 2
        return True
print(prime(78), prime(79))


def even_odd(x):
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")
even_odd(4)

def my_function(x, y =40):
    print("x: ", x)
    print("y: ", y)
my_function(10)

def myFun(*argv):
    for arg in argv:
        print(arg)
myFun(1, 3, 5, "abir")

def myFun_One(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

myFun_One(name="abir", live="NY")
