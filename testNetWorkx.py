import networkx as nx
import matplotlib.pyplot as plt
# create a empty graph
g = nx.Graph()

g.add_node("quoc")
g.add_node("Nhi")

g.add_edge("quoc","Nhi")

g.add_edge(4,1)

g.add_edges_from([(2,5),(1,3)], color = 'red')

print (type(g.edges()))
print (nx.info(g))

nx.draw(g, with_labels = 1)

plt.show()