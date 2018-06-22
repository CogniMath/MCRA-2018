import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist("higgs_retweet.txt",nodetype=int) 

plt.figure(figsize=(10,8))
nx.draw_circular(G,node_size=150)
plt.show()