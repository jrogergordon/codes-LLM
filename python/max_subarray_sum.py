def old_max_subarray_sum(arr):
    max_sum = -float('inf')
    current_sum = 0
    for i in range(len(arr)):
        current_sum = max(current_sum + arr[i], 0)
        max_sum = max(max_sum, current_sum)
    return max_sum


def new_max_subarray_sum(arr):
    max_sum = -float('inf')
    current_sum = 0
    for i in range(len(arr)):
        current_sum += arr[i]
        max_sum = max(max_sum, current_sum)
    return max_sum


def max_subarray_sum(arr):
    if arr[0] > 0:  # Check if the first element is positive
        return old_max_subarray_sum(arr)  # Use the old implementation for positive arrays
    else:
        return new_max_subarray_sum(arr)  # Use the new implementation for negative arrays


ans = max_subarray_sum([1, -2, 3, -4, 5])
ans2 = max_subarray_sum([-1, -2, -3, -4, -5])
print(ans)
print(ans2)