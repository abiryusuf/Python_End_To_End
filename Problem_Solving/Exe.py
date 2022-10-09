list_A = [1, 3, 10, 9, 11]
list_B = [20, 8, 40, 50, 80]

def merge(listA, listB):

    new_list = []
    a = 0
    b = 0
    for i in range(len(listA)):
        if a < listA[i]:
            new_list.append(listA[i])
    for j in range(len(listB)):
        if b < listB[j]:
            new_list.append(list_B[j])

    return new_list


print(merge(list_A, list_B))

