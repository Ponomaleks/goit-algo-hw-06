import networkx as nx
import matplotlib.pyplot as plt
from graph_data import edges, nodes, nodes_positions


def shifted_labels(pos, dx=0.3, dy=0.3):
    return {node: (x + dx, y + dy) for node, (x, y) in pos.items()}


def build_graph(nodes, edges):
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(edges)
    return G


def analyze_graph(G):
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    is_connected = nx.is_connected(G)

    print(f"Number of nodes: {num_nodes}")
    print(f"Number of edges: {num_edges}")
    print("Is the graph connected?", is_connected)


def analyze_node(G, node):
    degree = G.degree(node)
    neighbors = list(G.neighbors(node))
    print(f"Node: {node}")
    print(f"Degree: {degree}")
    print(f"Neighbors: {neighbors}")


def analyze_edge(G, node1, node2):
    if G.has_edge(node1, node2):
        weight = G[node1][node2]["weight"]
        print(f"Edge between {node1} and {node2} has weight: {weight}")
    else:
        print(f"No edge exists between {node1} and {node2}")
        print(
            f"Shortest path between {node1} and {node2}: {nx.shortest_path(G, node1, node2, weight='weight')}"
        )


def draw_graph(G, positions):
    plt.figure(figsize=(14, 10))
    pos = positions
    distances = nx.get_edge_attributes(G, "weight")

    nx.draw(
        G, pos, with_labels=False, node_color="lightblue", node_size=200, font_size=8
    )
    nx.draw_networkx_edge_labels(G, pos, edge_labels=distances, font_size=6)

    label_pos = shifted_labels(pos, dx=0.2, dy=0.2)
    nx.draw_networkx_labels(G, label_pos, font_size=8)

    plt.title("Graph of Ukrainian Cities and Distances")
    plt.savefig("ukraine_transport_graph.png", dpi=300, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    graph = build_graph(nodes, edges)
    print("Graph Analysis:")
    analyze_graph(graph)
    print("\n\nNode Analysis:")
    analyze_node(graph, "Kyiv")
    print("\n\nEdge Analysis:")
    analyze_edge(graph, "Kyiv", "Lviv")
    draw_graph(graph, nodes_positions)
