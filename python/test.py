def num_islands(grid):
    """
    Returns the number of islands in the given grid and the size of each island in descending order.
    """
    if not grid:
        return 0, []

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    island_sizes = []

    def explore(i, j, size=0):
        if i < 0 or i >= rows or j < 0 or j >= cols or visited[i][j] or grid[i][j] == "0":
            return size

        visited[i][j] = True
        size += 1
        explore(i + 1, j, size)
        explore(i - 1, j, size)
        explore(i, j + 1, size)
        explore(i, j - 1, size)
        return size

    count = 0
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j] and grid[i][j] == "1":
                size = explore(i, j)
                island_sizes.append(size)
                count += 1

    return count, island_sizes
ans = num_islands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])
print(ans)