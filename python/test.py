def find_missing_number(lst):
    n = len(lst)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum


numbers = [0,1, 2, 3, 5, 6, 7, 8, 9]
print(find_missing_number(numbers))  # Output: 4