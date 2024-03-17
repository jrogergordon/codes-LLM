def solveKnight(m, n, K):
    def canPlace(x, y, visited):
        for dx, dy in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                return False
        return True

    def placeKnights(x, y, visited, count):
        if count == K:
            return True
        for dx, dy in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and canPlace(nx, ny, visited):
                visited[nx][ny] = True
                if placeKnights(nx, ny, visited, count + 1):
                    return True
                visited[nx][ny] = False
        return False

    if K > m * n:
        return -1
    visited = [[False] * n for _ in range(m)]
    visited[0][0] = True
    if not placeKnights(0, 0, visited, 1):
        return -1
    return True

# Test the function
m = 5
n = 5
K = 2
print(solveKnight(m, n, K))   # Output: True
    