import networkx as nx


def basic_numbers(g: nx.Graph):
    print(f"Number of Nodes (Order):  {g.number_of_nodes()}")
    print(f"Number of Edges (Size): {g.number_of_edges()}")
    print(f"Density {str(nx.density(g))}")


def clustering_coefficient(g: nx.Graph):
    if g.is_directed():
        print("clustering coefficient not implemented for directed graphs")
    else:
        print(f"clustering coefficient: {str(nx.average_clustering(g))}")


def average_shortest_path_length(g):
    if not g.is_directed() and nx.is_connected(g):
        print(f"Average shortest path length: {str(nx.average_shortest_path_length(g))}")
    else:
        print("cant compute average shortest path length, graph directed or graph not connected")


def diameter(g: nx.Graph):
    if not g.is_directed() and nx.is_connected(g):
        print(f"Diameter: {nx.diameter(g)}")
    else:
        print("Diameter not computable, graph not connected or is directed")


def connectivity(g: nx.Graph):
    print(f"Connectivity: {nx.node_connectivity(g)}")
