
size = int(input())
arr = list(map(int, input().split(' ')))

def subarray(arr, size):
    #high_subarray = []
    high_sum = 0
    while size:
        end = size
        start = 0
        for i in range(len(arr)-size+1):
            if high_sum < sum(arr[start:end]):
                high_sum = sum(arr[start:end])
                #high_subarray = arr[start:end]
            if end == len(arr)-1:
                break
            start += 1
            end += 1
        size -= 1
    return high_sum


def o_of_n(arr, size):
        max_sum = float('-inf')  # Initialize to a very small value
        current_sum = 0

        for num in arr:
            current_sum = max(num, current_sum * num)  # Either take current element or extend subarray
            max_sum = max(max_sum, current_sum)  # Update max sum if current sum is greater

        return max_sum


def max_subarray(arr, size):
    max_sum = float('-inf')
    current_sum = 0
    start = end = temp = 0
    for i in range(size):
        if current_sum * arr[i] > arr[i]:
            current_sum *= arr[i]
        else:
            current_sum = arr[i]
            temp = i
        if current_sum > max_sum:
            max_sum = current_sum
            start, end = temp, i

    return max_sum, arr[start:end+1]




print(max_subarray(arr,size))