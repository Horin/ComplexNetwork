import networkx as nx
import matplotlib.pyplot as plt

# generate a graph which has n=20 nodes, probablity p = 0.2.
ER = nx.random_graphs.fast_gnp_random_graph(20, 0.2)
print(ER.degree())
# the shell layout
pos = nx.shell_layout(ER)
nx.draw(ER, pos, with_labels=True, node_size=30)
plt.show()

