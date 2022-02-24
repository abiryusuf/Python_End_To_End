"""
Tuple are used to store multiple items in a single variable
A tuple is a collection which is ordered and unchangeable
"""
x = (1,)
print (x)

a = ("Abir", 27, "NY")  # packing
(name, age, place) = a  # unpacking
print(name, age, place)

# tuple comparison starts with a first element of each tuple
x = (5, 6)
y = (6, 8)

if x > y:
    print("X is bigger")
else:
    print("Y is bigger")
