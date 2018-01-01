import networkx as nx
import matplotlib.pyplot as plt

# generate a graph which has n=20 nodes, probablity p = 0.2.
ER = nx.random_graphs.dense_gnm_random_graph(20, 190)
# the shell layout
pos = nx.shell_layout(ER)
nx.draw(ER, pos, with_labels=False, node_size=30)
plt.show()