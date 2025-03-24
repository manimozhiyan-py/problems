#find the largest element in the array

arr = [54, 65, 75, 81, 21, 46]


def largest(arr):
    large = arr[0]
    for element in arr:
        if large < element:
            large = element
    return large


print(largest(arr))