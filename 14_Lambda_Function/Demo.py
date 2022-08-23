"""
A lambda function is small anonymous function that a function
doesn't have name

A lambda function can take any number of arguments, but it can
only have single expression
"""
def my_Function(a, b):
    print(a * 2, b * 5)


def my_function_6(n):
    return lambda a: a * n


x = my_function_6(2)
print(x(3))

# syntax lambda arguments : expression
y = lambda a, b: a + b
print(y(3, 5))

"""
Why use lambda functions ?
The power of lambda is better shown when you use them as an
anonymous function inside another function 
Lets say I have function that takes one argument and that
argument will be multiplied with an unknown number
"""

def lambda_function(n):
    return lambda a: a * n
x = lambda_function(3)
y = x(2)
print(y)

g = lambda h, t: y - t
print(g(6, 3))


