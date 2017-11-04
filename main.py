import networkx as nx
import functions


# used graphs:
# gnutella (directed, not connected)
#   http://snap.stanford.edu/data/p2p-Gnutella31.txt.gz

# sality
#   https://raw.githubusercontent.com/iBigQ/botnet-graphs/master/individual_snapshots/sality_v3_core_min.graphml.gz

# facebook combined (undirected, connected)
#   http://snap.stanford.edu/data/facebook_combined.txt.gz
##
# facebook (undirected, connected)
#   http://snap.stanford.edu/data/facebook.tar.gz


def analyze_net(g: nx.Graph, name: str):
    print(f"Analyzing {name}")

    functions.basic_numbers(g)
    functions.average_shortest_path_length(g)
    functions.clustering_coefficient(g)
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


def facebook_0():
    name = "facebook"
    print(f"Loading {name}")
    g = nx.read_edgelist("graphs/facebook/686.edges")
    analyze_net(g, name)


facebook_combined()
# sality()
# gnutella()
