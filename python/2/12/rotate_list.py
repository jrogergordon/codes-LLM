def rotate_list(lst, rotations):
    """
    Rotate the list in the opposite direction by the given number of rotations.

    :param lst: The list to rotate
    :param rotations: The number of rotations to perform
    :return: The count of "real" rotations performed
    """
    actual_rotations = 0
    for i in range(rotations % len(lst)):
        lst.insert(0, lst.pop())
        actual_rotations += 1
    return actual_rotations

ans = [1,1,2,3,4,5,6,7]
ans2 = rotate_list(ans, 18)
print(ans, ans2)