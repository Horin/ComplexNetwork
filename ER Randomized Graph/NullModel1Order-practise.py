import networkx as nx
import matplotlib.pyplot as plt

# # generate a graph which has n=20 nodes, probablity p = 0.2.
# ER = nx.random_graphs.fast_gnp_random_graph(5, 0.2)
# print(ER.degree())
# print(nx.degree_histogram(ER))
#
# # the shell layout
# pos = nx.shell_layout(ER)
# nx.draw(ER, pos, with_labels=True, node_size=30)
# plt.show()

sequence = nx.random_powerlaw_tree_sequence(10, tries=500)
G = nx.configuration_model(sequence)
print(len(G))
actual_degrees = [d for v, d in G.degree()]
print(actual_degrees == sequence)
print(sequence)
print(G.degree())
print(nx.degree_histogram(G))


pos = nx.shell_layout(G)
nx.draw(G, pos, with_labels=True, node_size=30)
plt.show()