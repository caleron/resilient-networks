import networkx as nx

g: nx.Graph = nx.read_edgelist("graphs/facebook_combined.txt")
print(f"connected: {nx.is_connected(g)}")
