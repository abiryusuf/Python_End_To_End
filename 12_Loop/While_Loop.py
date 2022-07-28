
"""
The while loop we can execute a set of statements as long a
condition is true.
"""

# Break statement we can stop the loop even if the while condition in true
i = 0
while i < 10:
    i += 1
    if i == 4:
        break
    #print(i)
# Continue statement not execute current iteration and continue the next
y = 1
while y < 10:
    y = y + 2
    if y == 8:
        continue
   # print(y)

i = 1
while i < 10:
    i *= 2
    if i == 4:
        continue
    print(i)