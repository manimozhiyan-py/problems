#Adding element in an array

arr = [54, 65, 75, 81, 21, 46]

def inbuilt(arr, element):
    return arr.append(element)

def manual(arr, element):
    arr += [element]
    return arr


print(manual(arr,5))