
# list comprehension
x = [lambda x=i: x * 10 for i in range(1, 3)]

for i in x:
    print(i())

d = lambda a, b: a if a > b else b

print(d(2, 3))
