#Reverse a given array

arr = [54, 65, 75, 81, 21, 46]


def reverse_array(arr):
    reverse_arr = []
    for i in range(len(arr)-1,-1,-1):
        reverse_arr.append(arr[i])

    return reverse_arr

print(reverse_array(arr))