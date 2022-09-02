def reverse(str):
    res = ""

    for i in str.lower():
        res = i + res
    return res

print(reverse("abir"))

def palindrom(str):
    new = ""
    rev = ""
    for i in str.lower():
        new = new + i
        rev = i + rev
    if new == rev:
        return True
    return False
print(palindrom("mtdam"))


def countVowels(str):
    count = 0

    for i in str.lower():
        if i in "aieou":
            count += 1
    return count
print(countVowels("abir"))
count = {i: 0 for i in "aeiou"}
def count_V(str):
 for i in str.lower():
       if i in count:
           count[i] += 1
