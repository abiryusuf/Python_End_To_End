import array as arr

# creating an array
a = arr.array("i", [1, 2, 3])

print("The new created array is : ", end=" ")
a.insert(1, 4)
a.append(6)
for i in range(len(a)):
    print(a[i], end=" ")
print()


print(a[0])

b = arr.array("i",[1, 2, 3, 4])

