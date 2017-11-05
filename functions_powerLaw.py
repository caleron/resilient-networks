import networkx as nx
import random
import matplotlib.pyplot as plt


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

    degree_sequence = sorted(nx.degree(g).valures(),reverse=True)
	dmax = max(degree_sequence)
	
	plt.loglog(degree_sequence)
	plt.title("Degree plot")
	plt.ylabel("Degree")
	plt.xlabel("rank")
	
	Gcc = sorted(nx.connected_component_subgraphs(g), key = len, reverse = True)[0]
	
	pos = nx.spring_layout(Gcc)
	plt.axis('off')
	nx.draw_networkx_nodes(Gcc,pos,node_size=200)
	nx.draw_networkx_edges(Gcc,pos,alpha=0.5)
	
	plt.show()


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


def resilience_against_targeted_attacks(g: nx.Graph):
    copy = g.copy()
    # initialize the vars
    removed_nodes_count = 0

    # repeat this until the graph is disconnected
    # finds nodes with the lowest degree and removes neighbor nodes to disconnect them
    while nx.is_connected(copy):
        lowest_tuple = None
        # find node with lowest degree
        for entry in nx.degree(copy):
            # entry[0] is the node, entry[1] its degree
            if lowest_tuple is None:
                lowest_tuple = entry
            elif lowest_tuple[1] > entry[1]:
                lowest_tuple = entry

        # get first neighbor node
        neighbor = next(nx.all_neighbors(copy, lowest_tuple[0]))
        # now remove the node with the highest degree and increase the counter
        print(f"removing node {neighbor}")  # for debugging
        copy.remove_node(neighbor)
        removed_nodes_count += 1

    # add for the last removal
    print(f"Resilience against targeted attack: {str(removed_nodes_count)} nodes removed until graph disconnect")


def resilience_against_random_attacks(g: nx.Graph):
    sum_removed_edges = 0
    iterations = 100
    # removes random edges until graph is disconnected
    for i in range(iterations):
        copy = g.copy()

        removed_edges = 0
        while nx.is_connected(copy):
            # remove a random edge
            edge = random_edge(copy)
            copy.remove_edge(edge[0], edge[1])
            removed_edges += 1
            # print(f"removing edge {str(edge)}")

        sum_removed_edges += removed_edges

    # calculate average
    avg = sum_removed_edges / iterations
    print(f"Resilience against random attacks: removed {str(avg)} edges in average over {str(iterations)} iterations")


# selects a random node
def random_edge(g: nx.Graph):
    edge_index = random.randrange(g.number_of_edges())
    index = 0
    for edge in g.edges:
        if index == edge_index:
            return edge
        index += 1
