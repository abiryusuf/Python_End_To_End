# List comprehension allow to create a
# new list from a sequence
info = ["Abir", "Mim", "jim"]

newMember = []

for i in info:
    if "i" in i:
        newMember.append(i)
print(newMember)
f = [i.upper() for i in info if "i" in i]
print(f)

num = []

for i in range(10):
    x = num.append(i * 2)
print(x)

y = [i * 2 for i in range(1, 5)]
print("New", y)



# range and condition
newList = [x * 2 for x in range(10)]
print(newList)

listA = [2, 4, 6, 7]
newList = []
for i in listA:
    if 7 < 3:
        newList.append(i)
print(newList)
