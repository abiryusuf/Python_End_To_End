"""
Tuple is a collection which is ordered and unchangeable
and tuples are written with round brackets.

Tuples are unchangeable, meaning that we cannot change, add or remove items after the
tuple has been created
"""
thisTuple = ("Apple",)  # need a comma for a tuple or it will be string
print(type(thisTuple))
x = ("abir")
print(type(x))

thisT = ("a", "b", "c", "d")
x = thisT.count("b")
print(x)

# update
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

print(fruits)