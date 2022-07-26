num = [7, 9, 8, 3]

num.sort(reverse=True)
print(num)
num.reverse()
print(num)
x = sorted(num)
print(x)


def reverseStr(str):
    newStr = ""
    for i in str:
        newStr = i + newStr
    return newStr.upper()
print(reverseStr("Abir"))
