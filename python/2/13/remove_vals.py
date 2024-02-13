def remove_val(nums, val):
    if isinstance(val, list):
        # val is a list, remove all occurrences of each element in the list
        for v in val:
            nums = [x for x in nums if x != v]
    else:
        # val is a single value, remove all occurrences of it
        nums = [x for x in nums if x != val]
    return nums

ans = [7,6,7,8,7,8,9,7,7,7]
ans = remove_val(ans, 7)
print(ans)