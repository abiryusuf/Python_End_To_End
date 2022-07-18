"""
Dictionaries are used to store data values in key: value pairs
Dictionary is collection which is ordered, changeable, and don't
allow duplicates

Dictionaries are written with curly brackets and have keys
and values
"""

thisCar = {
    "brand": "kia",
    "model": "sportage x",
    "year": 2020
}
print(thisCar["brand"])
print(thisCar.get("brand"))

# keys() method will return a list of all the keys
x = thisCar.keys()
y = thisCar.values()
z = thisCar.items()
thisCar["color"] = "matt"
thisCar["year"] = "2023"
thisCar.update({"model": "sportage pro"})
print(x)
print(y)
print(z)

for x, y in thisCar.items():
    print(x,y)