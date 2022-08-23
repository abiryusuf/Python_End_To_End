
def myFun(e):
    return len(e)
cars = ["g", "c", "d"]

cars.sort()

print(cars)

def myFunc(x):
    return x["year"]
names = [
    {"name": "mim", "year": 6},
    {"name": "Jim", "year": 3}
]
names.sort(key=myFun)
print(names)