
list_A = [1, 3, 10, 9, 11, 60, 5, 16]
#x = list(input("Enter the Number "))
def maxNumber(n):
    max = n[0]

    for i in range(len(n)):
        if n[i] > max:
            max = n[i]
    return max

print(maxNumber(list_A))



