#Count frequency of each element in the array

arr = [54, 65, 75, 81, 21, 46, 46]

def frequency_dictionary(arr):
    dic = {}
    for i in arr:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    return dic

def frequency_array(arr):
    frequency_arr = [False] * len(arr)

    for i in range(len(arr)):
        if frequency_arr[i]:
            continue

        count =1
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                count += 1
                frequency_arr[j] = True
        print(f'{arr[i]} : {count}')



frequency_array(arr)


