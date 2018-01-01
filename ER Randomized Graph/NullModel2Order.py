import networkx as nx
import matplotlib.pyplot as plt

# # generate a graph which has n=20 nodes, probablity p = 0.2.
import networkx as nx
joint_degrees = {1: {4: 3}, 2: {2: 2, 3: 2, 4: 2}, 3: {2: 2, 4: 1}, 4: {1: 1, 2: 2, 3: 1}}
G = nx.joint_degree_graph(joint_degrees)
pos = nx.shell_layout(G)
nx.draw(G, pos, with_labels=True, node_size=30)
plt.show()