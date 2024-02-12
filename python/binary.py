def binary_search(array, target):
    low = 0
    high = len(array) - 1
    count = 0

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            # Find the first occurrence of the target value
            while mid > 0 and array[mid-1] == target:
                mid -= 1
            first_idx = mid
            # Count the number of occurrences of the target value
            count = 1
            while mid < len(array) - 1 and array[mid+1] == target:
                mid += 1
                count += 1
            break
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return first_idx, count

array = [1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 6]
index, count = binary_search(array, 5)
print(index)  # Output: 8
print(count)  # Output: 3