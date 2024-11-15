import heapq

class Node:
    def __init__(self, name, heuristic=0):
        self.name = name
        self.heuristic = heuristic
        self.cost = float('inf')
        self.parent = None

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def a_star(graph, start, goal, heuristics):
    open_list = []
    closed_list = set()

    start_node = Node(start, heuristics[start])
    start_node.cost = 0
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.name == goal:
            return reconstruct_path(current_node)

        closed_list.add(current_node.name)

        for neighbor in graph.get(current_node.name, []):
            if neighbor in closed_list:
                continue
            
            neighbor_node = Node(neighbor, heuristics[neighbor])
            tentative_cost = current_node.cost + 1
            
            if tentative_cost < neighbor_node.cost:
                neighbor_node.cost = tentative_cost
                neighbor_node.parent = current_node

                if neighbor_node not in open_list:
                    heapq.heappush(open_list, neighbor_node)

    return None

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.name)
        node = node.parent
    return path[::-1]

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    heuristics = {
        'A': 5,
        'B': 4,
        'C': 2,
        'D': 1,
        'E': 0,
        'F': 0
    }

    start_node = 'A'
    goal_node = 'F'

    path = a_star(graph, start_node, goal_node, heuristics)

    if path:
        print(f"Path found from {start_node} to {goal_node}: {' -> '.join(path)}")
    else:
        print(f"No path found from {start_node} to {goal_node}.")
