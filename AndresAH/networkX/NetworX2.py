import networkx          as nx
import matplotlib.pyplot as plt

# EL GRAFO CON ATRIBUTOS
G1 = nx.Graph(tipo='Amigos de Tweeter')

# AGREGAMOS 10 NODOS
G1.add_node(0, nombre='Andres',    oficio = 'Profesor',   edad = '?')
G1.add_node(1, nombre='Trump',     oficio = 'Presidente', edad = '70')
G1.add_node(2, nombre='Mesi',      oficio = 'Futbolista', edad = '30')
G1.add_node(3, nombre='Hawking',   oficio = 'Físico',     edad = '80')
G1.add_node(4, nombre='Milgram',   oficio = 'Psicologo',  edad = '50')
G1.add_node(5, nombre='Erdos',     oficio = 'Matemático', edad = '80')
G1.add_node(6, nombre='C.Fuentes', oficio = 'Escritor',   edad = '80')
G1.add_node(7, nombre='C.Slim',    oficio = 'Empresario', edad = '70')
G1.add_node(8, nombre='Aristegui', oficio = 'Periodista', edad = '50')
G1.add_node(9, nombre='Johansson', oficio = 'Actriz',     edad = '38')

# AGREGAMOS ENLACES DE FORMA ALEATORIA
G1.add_edges_from([(0, 5), (0, 6), (0, 7), (0, 9), (1, 2), (1, 3), (1, 4), (1, 7), (1, 8), (2, 3), (2, 4), (2, 5), (2, 6), (2, 8), (3, 4), (3, 5), (3, 6), (4, 8), (4, 9), (5, 6), (5, 7), (5, 8), (6, 7), (6, 8), (6, 9), (7, 8), (7, 9)])

# Definimos la posición de cada nodo en el plano coordenado
# Network incluye funciones que lo hacen siguiente distintas configuraciones 
# como: draw_circular; draw_random; draw_spectral; draw_spring; draw_shell
pos = nx.circular_layout(G1)

nombres = nx.get_node_attributes(G1,'nombre')

plt.figure(figsize=(10,10))
# Dibujamos la red completa i.e. nodos y enlaces
nx.draw(G1,pos,node_color='b',node_size=1500,width=3,alpha=0.5,
        font_size=25,linewidths=2.5,linecolor='grey',with_labels=True,
        labels=nombres) 

nx.draw_networkx_nodes(G1,pos,nodelist=[0,5],node_color='r',node_size=2000)
nx.draw_networkx_edges(G1,pos,edgelist=[(0,5)],width=8,edge_color='r') 
plt.show()