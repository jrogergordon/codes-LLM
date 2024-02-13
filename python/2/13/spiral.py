def spiral_order(lists):
    rows = len(lists)
    cols = len(lists[0])
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    i, j, direction = 0, 0, 0  # Initial position and direction
    result = []
    visited = [[False] * cols for _ in range(rows)]  # Initialize visited array

    for _ in range(rows * cols):  # Loop until all elements are visited
        if visited[i][j]:  # If current element has been visited, change direction
            direction = (direction + 1) % 4  # Cycle through directions
            i, j = get_next_location(i, j, direction, visited)
        else:
            result.append(lists[i][j])  # Append unvisited element
            visited[i][j] = True  # Mark element as visited

        # Update position and direction based on current corner
        if i == 0 and j == 0:  # Top-left corner
            direction = 1  # Change direction to right
        elif i == 0 and j == cols - 1:  # Top-right corner
            direction = 2  # Change direction to down
        elif i == rows - 1 and j == cols - 1:  # Bottom-right corner
            direction = 3  # Change direction to left
        elif i == rows - 1 and j == 0:  # Bottom-left corner
            direction = 0  # Change direction to up

    return result

def get_next_location(i, j, direction, visited):
    if direction == 0:  # Up
        if visited[i - 1][j]:  # If upcoming element has been visited, change direction
            direction = (direction + 1) % 4
            i, j = get_next_location(i, j, direction, visited)
        else:
            i -= 1
    elif direction == 1:  # Right
        if visited[i][j + 1]:  # If upcoming element has been visited, change direction
            direction = (direction + 1) % 4
            i, j = get_next_location(i, j, direction, visited)
        else:
            j += 1
    elif direction == 2:  # Down
        if visited[i + 1][j]:  # If upcoming element has been visited, change direction
            direction = (direction + 1) % 4
            i, j = get_next_location(i, j, direction, visited)
        else:
            i += 1
    elif direction == 3:  # Left
        if visited[i][j - 1]:  # If upcoming element has been visited, change direction
            direction = (direction + 1) % 4
            i, j = get_next_location(i, j, direction, visited)
        else:
            j -= 1
    return i, j


ans = spiral_order([[1,2,3],[12,13,6],[11,14,7]])
print(ans)