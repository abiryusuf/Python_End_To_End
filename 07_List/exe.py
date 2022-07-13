""" List are used to store multiple items in single variable
# List items are ordered, changeable, and allow duplicate values"""

x = [4, 6, 7, 8]
# x.append(9)
# x.insert(1, 10)
# x.pop(0)
# del x[1]
# y = len(x)
# for i in range(y):
#     print(i, end=" ")

newList = []
for i in x:
    if i < 10:
        newList.append(i)
print(newList)

for i in range(1, 10):
    newList.append(i * 2)
print(newList)

listCom = [i * 2 for i in range(1, 10)]
print(listCom)

