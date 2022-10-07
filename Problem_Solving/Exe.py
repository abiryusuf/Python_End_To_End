
list_A = [1, 3, 10, 9, 11, 60, 5, 16]

def binarySearch(n, target):
    low = 0
    high = len(n) - 1

    while low < high:
        mid = (low + high) // 2
        if n[mid] == target:
            return True
        if n[mid] < target:
            low = mid
        else:
            high = mid
    return False
target = 3
x = binarySearch(list_A, target)

if x == -1:
    print("Item is not found")
else:
    print("Found", x)
print(binarySearch(list_A, 10))
