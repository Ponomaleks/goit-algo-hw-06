from task_01 import build_graph
from graph_data import edges, nodes
import networkx as nx


def dijkstra(graph, start):
    # Ініціалізація відстаней та попередніх вершин
    distances = {vertex: float("infinity") for vertex in graph.nodes}
    previous = {vertex: None for vertex in graph.nodes}

    distances[start] = 0
    unvisited = list(graph.nodes)

    while unvisited:
        # Знаходимо вершину з мінімальною відстанню
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо мінімальна відстань — нескінченність, завершуємо
        if distances[current_vertex] == float("infinity"):
            break

        # Оновлюємо відстані до сусідів
        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]["weight"]
            distance = distances[current_vertex] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex

        # Видаляємо поточну вершину з невідвіданих
        unvisited.remove(current_vertex)

    return distances, previous


def get_shortest_path(previous, start, end):
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if path[0] == start:
        return path
    return []


if __name__ == "__main__":
    graph = build_graph(nodes, edges)
    start_node = "Kyiv"
    end_node = "Lviv"

    distances, previous = dijkstra(graph, start_node)
    shortest_path = get_shortest_path(previous, start_node, end_node)

    if shortest_path:
        print(
            f"Shortest path from {start_node} to {end_node}: {' -> '.join(shortest_path)} with total distance {distances[end_node]} km"
        )
    else:
        print(f"No path found from {start_node} to {end_node}")

    start_node = "Odesa"
    end_node = "Luhansk"
    distances, previous = dijkstra(graph, start_node)
    shortest_path = get_shortest_path(previous, start_node, end_node)

    if shortest_path:
        print(
            f"Shortest path from {start_node} to {end_node}: {' -> '.join(shortest_path)} with total distance {distances[end_node]} km"
        )
    else:
        print(f"No path found from {start_node} to {end_node}")

    nx_shortest_path = nx.dijkstra_path(graph, start_node, end_node, weight="weight")
    print(
        f"NetworkX Shortest path from {start_node} to {end_node}: {' -> '.join(nx_shortest_path)} with total distance {nx.dijkstra_path_length(graph, start_node, end_node, weight='weight')} km"
    )
