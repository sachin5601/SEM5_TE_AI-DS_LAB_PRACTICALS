# Simple Depth-First Search (DFS) Implementation (Uninformed Search) with Path
def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set() 
    if path is None:
        path = []  

    visited.add(start)  
    path.append(start)

    if start == goal:  
        return True, path  

    # Explore each neighbor of the current node
    for neighbor in graph.get(start, []):
        if neighbor not in visited:  
            found, result_path = dfs(graph, neighbor, goal, visited, path)
            if found:
                return True, result_path  

    path.pop()  
    return False, [] 

# Example usage
if __name__ == "__main__":
    
    graph = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['e'],
        'd': [],
        'e': ['f'],
        'f': []
    }

    start_node = 'a'
    goal_node = 'f'

    
    found, path = dfs(graph, start_node, goal_node)

    if found:
        print(f"Path found from {start_node} to {goal_node}: {' -> '.join(path)}")
    else:
        print(f"No path found from {start_node} to {goal_node}.")
