
num = [2, 4, 4, 5, 15, 5, 6, 6]

def sum(n):

    count = 0
    for i in n:
        count += i
    return count

print(sum(num))

def maxNumber(n):
    max = n[0]
    min = n[0]
    secondMax = n[0]
    thirdMax = n[0]
    for i in range(len(n)):
        if n[i] > max:
            max = n[i]
        if n[i] < min:
            min = n[i]
        if n[i] > secondMax and n[i] != max:
            secondMax = n[i]
        if n[i] > thirdMax and n[i] != secondMax and n[i] != max:
            thirdMax = n[i]

    return max, min, secondMax, thirdMax
print(maxNumber(num))

def dup(m):
    m = sorted(m)
    count = []
    for i in m:
        if i not in count:
            count.append(i)
    return count
print(dup(num))

