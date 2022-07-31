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
x = [1, 2,  3, 4, 5, 6, 7, 8]
y = [1, 2, 3, 4, 5, 6]
for i in x:
    for j in y:
        print(i, end="")
    print()

