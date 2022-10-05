
num = [2, 4, 4, 5, 15, 5, 6, 6]

max = num[0]
min = num[0]
secMax = num[0]
print(max)
for i in range(len(num)):
    x = num[i]
    if x > max:
        max = x
    if x < min:
        min = x
    if x < secMax and x != max:
        secMax = x
print("Max number", max, "\n Min number", min)
print("2nd max ", secMax)


