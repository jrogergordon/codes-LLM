def numIslands(grid):
    if not grid:
        return 0, 0, 0

    count = 0
    max_size = 0
    distinct_islands = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                shape = dfs(grid, i, j)
                count += 1
                max_size = max(max_size, len(shape))
                distinct_islands.add(shape)
    return count, max_size, len(distinct_islands)

def dfs(grid, i, j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
        return ''
    grid[i][j] = '#'
    shape = f'{i},{j}'
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        shape += dfs(grid, i+dx, j+dy)
    return shape

ans = numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","1"],
  ["0","0","1","0","0"]
])
print(ans)