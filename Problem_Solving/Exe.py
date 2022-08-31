
str1 = "dcba"
y = sorted(str1)
print(y)

str = "abir yusuf"
print(str.split())

def anagram_1(str1, str2):
    x = sorted(str1)
    y = sorted(str2)

    if x == y:
        return True
    else:
        return False
str1 = "abcdef"
str2 = "efcdab"
print(anagram_1(str1, str2))

def anagram_2(x, y):
    str_1 = x.replace(" ", "").lower()
    string_1 = sorted(str_1)
    str_2 = y.replace(" ", "").lower()
    string_2 = sorted(str_2)

    if string_1 == string_2:
        return True
    else:
        return False
x_1 = "I am abir"
y_2 = "abir am i"
print(anagram_2("I an abir", "I am abir"))

def anagram_3(x, y):
    x_1 = x.replace(" ", "").lower()
    y_2 = y.replace(" ", "").lower()

    if x_1 != y_2:
        return False

    count = {}

    for letter in x_1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    for letter in y_2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] == 0: # check count doesn't have any value
            return True
        return False

def palindrom(str):
    str_1 = str.lower()
    new = ""
    rev = ""
    for i in str_1:
        new = new + i
        rev = i + rev
    if new == rev:
        return "It is palindrom"
    return "It is not"
print(palindrom("Madam"))

def reverse(str):
    res = ""
    for i in str:
        res = i + res
    return res
print(reverse("I am abir yusuf "))