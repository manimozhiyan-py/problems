#Equillibrium index of an Array


arr = list(map(int, input().split(',')))

def equilibrium(arr, index):
    if sum(arr[:index]) == sum(arr[index+1:]):
        return True
    return False

def find_equilibrium(arr):
    total_sum = sum(arr)  # Step 1: Compute total sum
    left_sum = 0  # Step 2: Initialize left sum
    equilibrium_indices = []

    for i, num in enumerate(arr):
        right_sum = total_sum - left_sum - num  # Step 3: Compute right sum

        if left_sum == right_sum:  # Step 4: Check condition
            equilibrium_indices.append(i)

        left_sum += num  # Step 5: Update left sum for next index

    return equilibrium_indices if equilibrium_indices else [-1]

# Example usage
arr = [-7, 1, 5, 2, -4, 3, 0]
print(find_equilibrium(arr))  # Output: [3, 6]


index = int(input())
while index < 0 or index >= len(arr):
    print("enter valid index :")
    index = int(input())
