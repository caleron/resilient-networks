import networkx as nx


def basic_numbers(g: nx.Graph):
    print(f"Number of Nodes (Order):  {g.number_of_nodes()}")
    print(f"Number of Edges (Size): {g.number_of_edges()}")
    # https://networkx.github.io/documentation/stable/reference/generated/networkx.classes.function.density.html
    print(f"Density {str(nx.density(g))}")


# https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.approximation.clustering_coefficient.average_clustering.html
def clustering_coefficient(g: nx.Graph):
    if g.is_directed():
        print("clustering coefficient not implemented for directed graphs")
    else:
        print(f"clustering coefficient: {str(nx.average_clustering(g))}")


# https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.cluster.clustering.html
def clustering_distribution(g: nx.Graph):
    # computes clustering coefficient for each node
    # result is a map: node -> coefficient
    clustering: dict = nx.clustering(g)
    print(f"clustering: {str(clustering)}")


# https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.generic.average_shortest_path_length.html
def average_shortest_path_length(g):
    if not g.is_directed() and nx.is_connected(g):
        print(f"Average shortest path length: {str(nx.average_shortest_path_length(g))}")
    else:
        print("cant compute average shortest path length, graph directed or graph not connected")


# https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.distance_measures.diameter.html
def diameter(g: nx.Graph):
    if not g.is_directed() and nx.is_connected(g):
        print(f"Diameter: {nx.diameter(g)}")
    else:
        print("Diameter not computable, graph not connected or is directed")


# https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.approximation.connectivity.node_connectivity.html
def connectivity(g: nx.Graph):
    print(f"Connectivity: {nx.node_connectivity(g)}")
