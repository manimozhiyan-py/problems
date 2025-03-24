#Finding all symmetric
arr = [(1, 2), (2, 1), (3, 4), (5, 6), (4, 3)]

def symmetric(arr):
    dic = {}
    symmetric_arr = []
    for element in arr:
        if element[::-1] not in dic.keys():
            dic[element] = element[::-1]
        else:
            symmetric_arr.append(element)
            symmetric_arr.append(dic[element[::-1]])


    return symmetric_arr

print(symmetric(arr))