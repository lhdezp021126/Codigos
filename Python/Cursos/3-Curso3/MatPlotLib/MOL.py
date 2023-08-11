from matplotlib import pyplot as plt;

height = [174.3, 153.5, 162.1, 157.9, 174.8, 169.2, 172.0, 160.4, 152.8, 163.3] 
weight = [ 65.7,  59.2,  57.3,  61.5,  77.3,  90.7,  85.4,  63.1,  73.2, 105.5]

plt.title("Alturas vs. pesos")
plt.xlabel("Alturas (cm)")
plt.ylabel("Pesos (kg)")
plt.scatter(x = height, y = weight, 
            c = "black", edgecolors = "red", alpha = 1,
            marker = "X", s = 200, linewidths = 2)
plt.show()

import networkx as nx;

g=nx.Graph();

g.add_nodes_from('abcd');
g.add_edge('a','b')
g.add_edge('b','c')
g.add_edge('c','a')

nx.draw(g);

plt.show();