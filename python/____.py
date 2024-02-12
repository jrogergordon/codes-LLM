def find_unique(dupeNums):
    unique_element = None

    for i, num in enumerate(dupeNums):
        if i == 0 or num != dupeNums[i-1]:
            unique_element = num
        elif num == unique_element:
            break

    return unique_element

ans = find_unique([1,1,2,2,3,3,4,4,5])
print(ans)