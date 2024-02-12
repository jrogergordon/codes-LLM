def find_unique(dupeNums):
    unique_elements = {}

    for num in dupeNums:
        if num not in unique_elements:
            unique_elements[num] = 1
        else:
            unique_elements[num] += 1

    for num, count in unique_elements.items():
        if count == 1:
            return num

    return None

ans = find_unique([1,1,2,2,3,3,4,5,4])
print(ans)