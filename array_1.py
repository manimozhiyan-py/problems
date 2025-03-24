#find the smallest number in the array

arr = [54, 65, 75, 81, 21, 46]


def small(arr):
    smallest = arr[0]
    for element in arr:
        if element < smallest:
            smallest = element

    return smallest


print(small(arr))