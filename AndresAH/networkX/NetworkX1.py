
import networkx as nx

# Creando el objeto grafo
G = nx.Graph()

# Agregamos un nodo. 
G.add_node("andres")

# Al agregar un enlace automaticamente se agregan los nuevos nodos
G.add_edge(1,2)

# Ahora agregemos un enlace entre el nodo 1 y el nodo “andres”
G.add_edge(1,"andres")

# Podemos agregar una lista de nodos
G.add_nodes_from([3,4,5,6])

# Y agregar enlaces
G.add_edges_from([(3,4),(3,5),(3,6),(5,6)])

print()
print('Los nodos de la red son:',G.nodes())

print()
print('Y los encales son:', G.edges())

print()
print('Los enlaces con el node 3 son:', G.edges(3))

print()
print('Los vecinos del nodo 3 son:', list(G.neighbors(3)))

print()
print('El grado del nodo 3 es:', G.degree(3))

print()
print('El grado de todos los nodos es:', G.degree())

print()
print('La matriz de acoplamiento es')
print(nx.to_numpy_matrix(G))
print()

print()
print('El camino mas corto entre Andres y el nodo 2 es:', nx.shortest_path(G,source='andres',target=2))

print()
print('El coeficiente de agrupamiento del nodo 3 es:')
print('                                               ',
      nx.clustering(G,3)) 
