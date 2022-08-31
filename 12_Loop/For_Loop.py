"""
For loop: execute the set of statement
"""

x = ["a", "b", "c", "d"]

for i in x:
    # print("Break comes after the print", i)
    if i == "c":
        break
    # print("** Break comes before the print", i)


for t in x:
    if t == "c":
        continue
   # print(t)

# for h in range(6):
#     print(h)
# else:
#    print("Done")

adj = ["ab", "bc", "gt"]
x = ["a", "b", "c", "d"]

for a in adj:
    for b in x:
        pass

# Print with range
for i in range(10):
    print(i, end=" ")
sum = 0
for i in range(1, 10):
    sum += i
    print("\nSum of first 10 numbers :", sum)


x = [1, 2,  3, 4, 5, 6, 7, 8]
sum = 0
for i in x:
    sum += i
    if sum % 2 == 0:
        print("THIS IS EVEN", sum)
    else:
        print("This is Odd", sum)
print(sum)
# y = [1, 2, 3, 4, 5, 6]
# for i in x:
#     for j in y:
#         print(i, end="")
#     print()

