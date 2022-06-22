"""
I can combine number and string by using format()
method

--> The format method takes the passed argument, formats them and place them in the string where
the placeholders {} are
"""

age = 28
phone = 45422
info = "I am Abir, and I am {}, Cell {}"
print(info.format(age, phone))

quantity = 3
item = 676
price = 45.7

myOrder = "I want {} pices of item {} for {} dollars."
print(myOrder.format(quantity, item, price))


print("****Index number****")
t = "Mim"
age = 5
ing = "Name is {1} and age is {0}"
print(ing.format(t, age))