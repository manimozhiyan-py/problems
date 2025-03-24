from orca.debug import printTokens

arr1 = [5, 3, 1, 2, 4, 9, 7, 6, 8]
arr2 = [3, 1, 4, 5]
n = len(arr2)

output = arr2

for element in arr1:
    if element not in arr2:
        output.append(element)
output = output[:n] + sorted((output[n:]))
print(output)