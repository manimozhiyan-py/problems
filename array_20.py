#Sorting elements of an array by frequency

arr = [54, 75, 75, 81, 21, 46, 21, 21]
out_arr = []

dic = {}
for i in arr:
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1

const = max(dic.values())
while len(out_arr) != len(arr):
    for element in arr:
        if dic[element] == const:
            out_arr.append(element)
    const -= 1


print(out_arr)