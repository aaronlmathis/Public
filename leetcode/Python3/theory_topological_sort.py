def topological_sort_dfs(graph):
    def dfs(node):
        visited.add(node)
        for next_node in graph[node]:
            if next_node not in visited:
                dfs(next_node)
        
        # This is the end of the recursion for DFS..
        stack.append(node)
    
    visited = set()
    stack = []

    for node in graph:    
        if node not in visited:
            dfs(node)
    # Items were added at the end of DFS's, so reverse the stack to get the item with no dependencies first
    return stack[::-1]

from collections import defaultdict, deque

def topological_sort_bfs(graph):
    # Step 1: Compute in-degrees of all nodes
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Step 2: Collect all nodes with in-degree 0
    queue = deque([node for node in in_degree if in_degree[node] == 0])

    # Step 3: Process the nodes
    topo_order = []
    while queue:
        node = queue.popleft()
        topo_order.append(node)

        # Decrease the in-degree of neighbors
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if there was a cycle (if topo_order doesn't contain all nodes)
    if len(topo_order) == len(graph):
        return topo_order
    else:
        raise ValueError("Graph is not a DAG (contains a cycle)")

#dependent: [dependencies]
graph = {
    5: [0, 2],
    4: [],
    3: [],
    2: [3, 1],
    1: [],
    0: [4]
}
print(topological_sort_dfs(graph))


