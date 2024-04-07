from collections import defaultdict

def findOrder(numCourses, prerequisites):
    # Create a graph and in-degree dictionary
    graph = defaultdict(list)
    in_degree = [0] * numCourses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # DFS function to visit nodes
    def dfs(node, visited, result):
        if visited[node] == 1:  # Cycle detected
            return False
        if visited[node] == 2:  # Already visited
            return True
        
        visited[node] = 1  # Mark as visiting
        
        for neighbor in graph[node]:
            if not dfs(neighbor, visited, result):
                return False
        
        visited[node] = 2  # Mark as visited
        result.append(node)  # Add to the result
        
        return True
    
    # Initialize visited and result list
    visited = [0] * numCourses
    result = []
    
    # Perform DFS on each node
    for i in range(numCourses):
        if not dfs(i, visited, result):
            return []
    
    return result[::-1]  # Reverse the result to get the correct order

# Test the function
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(findOrder(numCourses, prerequisites))  # Output: [0, 1, 2, 3]
