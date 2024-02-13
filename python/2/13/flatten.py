import math

def is_element_in_half_of_lists(list_of_lists, k):
    num_lists = len(list_of_lists)
    target_count = math.floor(num_lists / 2)
    count = 0
    for sublist in list_of_lists:
        if k in sublist:
            count += 1
    return count == target_count


ans = is_element_in_half_of_lists([[1,23],[45,6,8],[7,9,8,8,8]], 8)
print(ans)