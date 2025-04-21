import heapq

# Graph with edge costs
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('E', 2)],
    'C': [('F', 1)],
    'D': [],
    'E': [('G', 5)],
    'F': [('G', 1)],
    'G': []
}

# Heuristic values (straight-line distance to goal 'G')
heuristic = {
    'A': 6,
    'B': 5,
    'C': 2,
    'D': 4,
    'E': 3,
    'F': 1,
    'G': 0
}

# A* Search function
def a_star_search(start, goal):
    # Priority queue: (total_cost, path_cost, node, path)
    pq = [(heuristic[start], 0, start, [start])]
    visited = set()

    while pq:
        total_cost, cost_so_far, current, path = heapq.heappop(pq)

        if current == goal:
            print("Path found:", path)
            print("Total cost:", cost_so_far)
            return path

        if current in visited:
            continue
        visited.add(current)

        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                g = cost_so_far + weight
                f = g + heuristic[neighbor]
                heapq.heappush(pq, (f, g, neighbor, path + [neighbor]))

    print("No path found.")
    return None

# Example usage
a_star_search('A', 'G')
