# find median in array
# lets learn lambda

arr = [54, 65, 75,  21, 46]

median = lambda x: (arr[int(len(arr)/2)] + arr[int(len(arr)/2)-1])/2 if len(arr)%2 == 0 else arr[int(len(arr)/2)]

print(median(arr))