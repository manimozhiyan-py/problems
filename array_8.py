# Rotate array by k

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3

'''while k > 0:
    arr.insert((len(arr)-1), arr.pop(0))
    k -= 1

print(arr)'''

rotated_arr = arr[-(len(arr) - k):] + arr[:k]
print(rotated_arr)
