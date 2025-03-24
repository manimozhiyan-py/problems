#find the second smallest and second largest
#      element in the array


arr = [54, 65, 75, 81, 21, 46]

def second_smallest(arr):
    firstSmallest = arr[0]
    secondSmallest = arr[0]

    for element in arr:
        if element < firstSmallest:
            firstSmallest, secondSmallest = element, firstSmallest
        elif (element > firstSmallest) and (element <secondSmallest):
            secondSmallest = element

    return secondSmallest

def second_largest(arr):
    secondLargest = arr[0]
    firstLargest = arr[0]

    for element in arr:
        if element > firstLargest:
            firstLargest, secondLargest = element, firstLargest
        elif (element < firstLargest) and (element > secondLargest):
            secondLargest = element

    return secondLargest

