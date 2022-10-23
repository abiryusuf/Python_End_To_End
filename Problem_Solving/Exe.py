
arr = [12, 3, 6, 10]

def bubbleSort(num):
    arr = len(num)
    for i in range(arr):
        for j in range(0, arr - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


bubbleSort(arr)

for i in range(len(arr)):
    print(arr[i])