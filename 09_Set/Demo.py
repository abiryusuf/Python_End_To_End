"""
Set items are unchangeable, unordered, and unindexed and
doesn't allow duplicate value

But I can add items and remove where tuple can not
set use curly brackets
"""

thisSet = {"a", "b", "c", "d", "d"}
x = ["r", "t"]

thisSet.update(x)

print(thisSet)
print(type(thisSet))