#Maximum product subarray in an array
arr = [2, 3, -2, 4]
max_product = 1
max_count = 1

for i in range(len(arr)):
    max_count = max(arr[i], max_count *arr[i])
    max_product = max(max_count, max_product)

print(max_product)