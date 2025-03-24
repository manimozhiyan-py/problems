#Find all repeating element in an array

arr = [54, 65, 75, 81, 21, 75]

def repeating_element(arr):
    dic = {}
    for element in arr:
        if element not in dic.keys():
            dic[element] = 1
        else:
            dic[element] += 1
    for element in arr:
        if dic[element] == 1:
            print(element, dic[element])

repeating_element(arr)