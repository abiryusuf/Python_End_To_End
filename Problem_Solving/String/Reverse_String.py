
name = "abir" # out put irba


def reverse_string(str):

    res = {}  # store the data
    for i in str:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    return res
print(reverse_string("uuuyyyttt"))

# count vowels
def count_vowels(str):
    str = str.lower()
    count = 0

    for i in str:
        if i in "aieou":
            count += 1
    return count
print(count_vowels("abir"))

count_1 = {i : 0 for i in "aieou"}

for i in "abir".lower():
    if i in count_1:
        count_1[i] += 1
print(count_1)

def palindrom(str):
    new = ""
    reverse = ""
    for i in str.lower():
        new = new + i
        reverse = i + reverse
    if new == reverse:
        return True
    else:
        return False
print(palindrom("Cadam"))

