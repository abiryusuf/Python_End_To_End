import array as arr

# creating an array
a = arr.array("i", [1, 2, 3])

print("The new created array is : ", end=" ")
a.insert(1, 4)
a.append(6)
print("After Add", a)
a.pop()
for i in range(len(a)):
    print(a[i], end=" ")
print()


print(a[0])

b = arr.array("d", [1, 2, 3, 4])
for i in range(len(b)):
    print(b[i], end =" ")

# slice: range of array
print("\n")
listTwo = [10, 30, 40, 50]
x = arr.array("i", listTwo)
for i in range(len(x)):
    print(x[i], end=" ")


