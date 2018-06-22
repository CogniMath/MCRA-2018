import networkx          as nx
import matplotlib.pyplot as plt

# GENERADORES DE GRAFOS:

N = 30 # NUMERO DE NODOS

# GRAFO ERDOS-RENYI
G1 = nx.erdos_renyi_graph(N,0.5) 

# GRAFO WATTS-STROGATZ
G2 = nx.watts_strogatz_graph(N,4,0.1) 

# GRAFO BARABASI-ALBERT
G3 = nx.barabasi_albert_graph(N,1) 

# GRAFO TOTALMENTE CONECTADO O COMPLETO
G4 = nx.complete_graph(10) 

# GRAFO CIRCULAR EN ESCALERA
G5 = nx.circular_ladder_graph(N) 

# GRAFO ESTRELLA
G6 = nx.star_graph(N) 

plt.figure(figsize=(14,14))

plt.subplot(231) 
plt.title('Grafo Erdos-Renyi',fontsize=20)
nx.draw_random(G1,node_color='blue',node_size=200,with_labels=False,alpha=0.8)

plt.subplot(232)
plt.title('Grafo Watts-Strogatz',fontsize=20)
nx.draw_circular(G2,node_color='green',node_size=200,with_labels=False,alpha=0.8)

plt.subplot(233)
plt.title('Grafo Barabasi-Albert',fontsize=20)
nx.draw_spring(G3,node_color='orange',node_size=200,with_labels=False,alpha=0.8)

plt.subplot(234)
plt.title('Grafo Completo',fontsize=20)
nx.draw_shell(G4,node_color='deeppink',node_size=300,with_labels=False,alpha=0.8)

plt.subplot(235)
plt.title('Grafo Circular',fontsize=20)
nx.draw_spring(G5,node_color='tomato',node_size=100,with_labels=False,alpha=0.8)

plt.subplot(236)
plt.title('Grafo Estrella',fontsize=20)
nx.draw_spring(G6,node_color='purple',node_size=200,with_labels=False,alpha=0.8)

plt.show()
