def get_rotations(l1, l2):
    if sorted(l1) != sorted(l2):
        return -1
    else:
        for i in range(len(l1)):
            if all(l1[j] == l2[(i+j)%len(l1)] for j in range(len(l1))):
                return i
        return -1

l1 = [1, 2, 3, 4, 5, 1, 1]
l2 = [2, 3, 4,5,1,1,1]

print(get_rotations(l1, l2))  # output: 2uts: (2, 3)