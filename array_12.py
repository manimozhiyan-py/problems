# Removing duplicate from unsorted array

arr = [54, 65, 75, 81, 21, 75]


def using_array(arr):
    unique = []
    for element in arr:
        if element not in unique:
            unique.append(element)
    return unique


def using_dic(arr):
    dic = {}
    unique = []
    for element in arr:
        if element not in dic.keys():
            dic[element] = 1
        else:
            dic[element] += 1
    for element in dic.keys():
        unique.append(element)

    return unique


print(using_dic(arr))
