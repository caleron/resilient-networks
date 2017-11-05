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
    print(f"TODO clustering: {str(clustering)}")


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


# uses node_connectivity function as above
# node_connectivity is the number of nodes that must be removed to disconnect the graph
def cohesiveness(g: nx.Graph, v):
    before = nx.node_connectivity(g)
    copy = g.copy()
    copy.remove_node(v)
    after = nx.node_connectivity(copy)
    # print(f"before: {before} after: {after}, cohesiveness of node {v}: {before - after}")
    return before - after


def power_law_properties(g: nx.Graph):
    print("TODO")


def cohesiveness_distribution(g: nx.Graph):
    arr = dict()
    for node in g.nodes:
        arr[node] = cohesiveness(g, node)

    print(f"Cohesiveness distribution: {str(arr)}")


def edge_persistence_greedy_attack(g: nx.Graph):
    copy = g.copy()
    # initialize the vars
    removed_nodes_to_zero_degree_dict = dict()
    zero_degree_count = 0
    removed_nodes_count = 0

    # repeat this until all nodes are isolated
    while zero_degree_count < copy.number_of_nodes():
        highest_tuple = None
        zero_degree_count = 0
        # find node with highest degree and count nodes with zero degree at the same time
        # means zero_degree_count stores the number of isolated nodes after the last removal
        # therefore save this before removing a new node and once after the while loop to get all values
        for entry in nx.degree(copy):
            # entry[0] is the node, entry[1] its degree
            if highest_tuple is None:
                highest_tuple = entry
            elif highest_tuple[1] < entry[1]:
                highest_tuple = entry

            if entry[1] == 0:
                zero_degree_count += 1

        # store the current number of isolated nodes mapped to the removed nodes and total nodes
        removed_nodes_to_zero_degree_dict[removed_nodes_count] = zero_degree_count, copy.number_of_nodes()
        # now remove the node with the highest degree and increase the counter
        # if highest_tuple[1] == 0, then the while loop stops
        if highest_tuple[1] > 0:
            # print(f"removing node {highest_tuple[0]}")  # for debugging
            copy.remove_node(highest_tuple[0])
            removed_nodes_count += 1

    # add for the last removal
    removed_nodes_to_zero_degree_dict[removed_nodes_count] = zero_degree_count, copy.number_of_nodes()
    print(f"TODO{str(highest_tuple)}")


def resilience_against_attacks(g: nx.Graph):
    print("TODO")
