def rotate_matrix(matrix):
    n, m = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(m):  
            if i < m and j < n:
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][-i-1]
                matrix[j][-i-1] = temp
    return matrix
ans = rotate_matrix([[1,2,3, 4],[5,6,7,8],[9,10,11,12]])
print(ans)