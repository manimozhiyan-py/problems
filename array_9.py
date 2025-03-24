# Average of all elements in an array

arr = [54, 65, 75, 81, 21, 46]

def average(arr):
    sum = 0
    for element in arr:
        sum += element
    return f"{sum/len(arr):.2f}".rstrip("0").rstrip(".")

print(average(arr))