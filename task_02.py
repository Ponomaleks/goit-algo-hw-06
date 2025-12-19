from collections import deque
from task_01 import build_graph
from graph_data import edges, nodes


def dfs_path_recursive(G, start, goal, path=None):
    if path is None:
        path = set()
    path.add(start)
    if start == goal:
        return [start]
    for neighbor in G.neighbors(start):
        if neighbor not in path:
            result = dfs_path_recursive(G, neighbor, goal, path)
            if result is not None:
                return [start] + result
    return None


def bfs_path_iterative(G, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current_node, path = queue.popleft()
        if current_node == goal:
            return path
        visited.add(current_node)
        for neighbor in G.neighbors(current_node):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None


def compare(graph, start, end):
    dfs_result = dfs_path_recursive(graph, start, end)
    bfs_result = bfs_path_iterative(graph, start, end)

    print(f"\nComparing paths from {start} to {end}:")

    print(
        f"DFS path from {start} to {end}: {' -> '.join(dfs_result) if dfs_result else 'No path found'}"
    )
    print(
        f"BFS path from {start} to {end}: {' -> '.join(bfs_result) if bfs_result else 'No path found'}"
    )

    if dfs_result == bfs_result:
        print("Both algorithms found the same path.")
    else:
        print("The algorithms found different paths.")
        print(f"DFS path length: {len(dfs_result) if dfs_result else 'N/A'}")
        print(f"BFS path length: {len(bfs_result) if bfs_result else 'N/A'}")


if __name__ == "__main__":
    graph = build_graph(nodes, edges)
    start_node = "Kyiv"
    goal_node = "Lviv"
    compare(graph, start_node, goal_node)

    start_node = "Odesa"
    goal_node = "Luhansk"
    compare(graph, start_node, goal_node)
