import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from automaton import *

size = 6
n = 3
END_TIME = 10

# matrix = np.zeros(shape=(size, size), dtype=int)
# df = pd.DataFrame(matrix)
# df.to_csv('matrix.csv', index=False, header=False)
#
# input('Заполните матрицу смежности')

matrix = np.genfromtxt('matrix.csv', delimiter=',', dtype=int)
if 1 in matrix.diagonal():
    raise 'Есть петли!'

graph = nx.Graph(matrix)
for i in range(size):
    graph.nodes[i]['condition'] = 0
    graph.nodes[i]['annoyed'] = False

colo_map = assign_colors(graph)
show(graph, colo_map)

for _ in range(END_TIME):
    disturb_cells
