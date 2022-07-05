List = ["a", "b", "c"]

myList = List.copy()
print(myList)

D = [6, 7, 9, 2]
t = sorted(D)
Y = [7, 5, 7, 9]

t.reverse()
print("Reverse", t)
final = D + Y
print(final)
f = sorted(final)
print(f)

for x in Y:
    D.append(x)
print(D)

g = D.count(7)
print(g)

