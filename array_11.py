#remove dupllicates from the sorted array

arr = [54, 65, 75, 81, 21, 75]

def sorting(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
arr = sorting(arr)
for i in range(len(arr)-2):
    if arr[i] == arr[i+1]:
        arr.pop(i)


print(arr)

