
def my_Function(a, b):
    print( a * 2, b * 5)

my_Function(3, 6)

c = lambda x: x * 10

print(c(4))


def my_function_6(n):
    return lambda a: a * n
x = my_function_6(2)
print(x(3))