# ----- A* Algorithm -----

# Define the graph with neighbors and their costs
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 1, 'E': 5},
    'C': {'F': 2},
    'D': {'G': 3},
    'E': {'G': 1},
    'F': {'G': 5},
    'G': {}
}

# Heuristic values (estimated distance to goal)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 4,
    'G': 0
}

def astar(start, goal):
    open_list = {start: 0}   
    closed_list = []        
    parent = {}              

    g_cost = {start: 0}      

    while open_list:
        # Find node with lowest f = g + h
        current = min(open_list, key=lambda node: g_cost[node] + heuristic[node])
        print(f"Visiting Node: {current}")

        # If goal reached
        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            print("\nPath Found:", " → ".join(path))
            return path
        open_list.pop(current)
        closed_list.append(current)
        for neighbor, cost in graph[current].items():
            if neighbor in closed_list:
                continue
            tentative_g = g_cost[current] + cost
            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                parent[neighbor] = current
                open_list[neighbor] = tentative_g

    print("No Path Found!")
    return None

# Run A*
start = 'A'
goal = 'G'
astar(start, goal)
