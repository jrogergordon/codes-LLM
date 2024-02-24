def rotate(lst, k):
    n = len(lst)
    count = k % n
    lst = lst[-count:] + lst[:-count]
    return lst, count


ans = rotate([-7, 18, -21,10,-5,-7, 14], 8)
print(ans)