
a = 100
b = 40

if a < b:
    print("a is greater than b")
elif a > b:
    pass
elif a == b:
    print('a is equal b')
else:
    print("not equal")

# Pass statement
"""
If statement cannot be empty but if you for some reason have an if 
statement with no content, put the pass statement to avoid getting an error 
"""
x = 5
y = 10

if y > x:
    pass
