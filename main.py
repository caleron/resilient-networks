import networkx as nx
import functions


# used graphs:
# gnutella (directed, not connected)
#   http://snap.stanford.edu/data/p2p-Gnutella31.txt.gz

# sality
#   https://raw.githubusercontent.com/iBigQ/botnet-graphs/master/individual_snapshots/sality_v3_core_min.graphml.gz

# facebook combined (undirected, connected)
#   http://snap.stanford.edu/data/facebook_combined.txt.gz

# facebook (undirected, connected)
#   http://snap.stanford.edu/data/facebook.tar.gz

# zero access (directed)
#   https://github.com/iBigQ/botnet-graphs/blob/master/individual_snapshots/za_16464_core_min.graphml.gz

def analyze_net(g: nx.Graph, name: str):
    print(f"Analyzing {name}")
    # https://networkx.github.io/documentation/stable/reference/classes/generated/networkx.Graph.to_undirected.html
    g = nx.to_undirected(g)

    # https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.components.is_connected.html
    print(f"Graph is connected: {str(nx.is_connected(g))}")

    functions.basic_numbers(g)
    functions.average_shortest_path_length(g)
    functions.clustering_coefficient(g)
    functions.clustering_distribution(g)
    functions.diameter(g)
    functions.connectivity(g)

    print(f"Done analyzing {name}")


def gnutella():
    name = "gnutella"
    print(f"Loading {name}")
    # gnutella network
    g = nx.read_edgelist("graphs/p2p-Gnutella31.txt")
    analyze_net(g, name)


def sality():
    name = "sality"
    print(f"Loading {name}")
    g = nx.read_graphml("graphs/GraphSality_SuperpeersAt2016-02-24_02-34-02_anonym.graphml")
    analyze_net(g, name)


def facebook_combined():
    name = "facebook"
    print(f"Loading {name}")
    g = nx.read_edgelist("graphs/facebook_combined.txt")
    analyze_net(g, name)


def zero_access():
    name = "zero access core min"
    print(f"loading {name}")
    g = nx.read_graphml("graphs/GraphZeroAccess_SuperpeersAt2016-02-23_03-19-30_anonym.graphml")
    analyze_net(g, name)


def facebook_0():
    name = "facebook"
    print(f"Loading {name}")
    g = nx.read_edgelist("graphs/facebook/686.edges")
    analyze_net(g, name)


# facebook_0()
# zero_access()
# facebook_combined()
# sality()
gnutella()
