from collections import deque, defaultdict

# Graph representation using adjacency list
g = defaultdict(list, {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
})

# Breadth-First Search
def bfs(s):
    print("BFS Traversal:")
    q = deque([s])
    visited = {s}

    while q:
        n = q.popleft()
        print(n, end=" ")

        for x in g[n]:
            if x not in visited:
                visited.add(x)
                q.append(x)
    print()

# Depth-First Search
def dfs(n, visited=set()):
    if n in visited:
        return
    print(n, end=" ")
    visited.add(n)

    for x in g[n]:
        dfs(x, visited)

# Main Execution
bfs(0)
print("DFS Traversal:")
dfs(0)
print()
