# List comprehension allow to create a new list from a sequence
info = ["Abir", "Mim", "jim"]

newMember = []

for i in info:
    if "i" in i:
        newMember.append(i)
print(newMember)
f = [i.upper() for i in info if "i" in i]
print(f)
mul = []
for num in range(1, 10):
    mul.append(num * 2)
print(mul)

y = {i * 2 for i in range(1, 5)}
print(y)


# range and condition
newList = [x * 2 for x in range(10)]
print(newList)

listA = [2, 4, 6, 7]
newList = []
for i in listA:
    if 7 < 3:
        newList.append(i)
print(newList)
