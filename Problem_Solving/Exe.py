
list_A = [1, 3, 10, 9, 11, 60, 5, 16]

def linearSearch(n, target):

    for i in range(len(n)):
        x = n[i]
        if x == target:
            return True
    return False
print(linearSearch(list_A, 11))



