#Rearrange element of array in increasing and decreasing order
arr = [54, 65, 75, 81, 21, 46]

def increase(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

def decrease(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr
