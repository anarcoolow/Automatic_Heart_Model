import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class Automaton:
    def __init__(self, matrix: np.ndarray, size, n):
        if 1 in matrix.diagonal():
            raise 'Есть петли!'
        self.n = n
        self.size = size
        self.graph = nx.Graph(matrix)
        for i in range(size):
            self.graph.nodes[i]['condition'] = 0
            self.graph.nodes[i]['annoyed'] = False
        self.color_map = self.assign_colors()

    def assign_colors(self):
        color_map = []
        for i in range(self.size):
            if self.graph.nodes[i]['annoyed']:
                color_map.append('red')
            elif not self.graph.nodes[i]['annoyed'] and self.graph.nodes[i]['condition'] > 0:
                color_map.append('blue')
            else:
                color_map.append('darkgrey')
        return color_map

    def show(self):
        nx.draw_spectral(self.graph, with_labels=True, node_color=self.color_map)
        plt.pause(2)
        plt.clf()

    def disturb_cells(self, irritants: str = None): # 1 2, 5 5, 2 1
        if not irritants:
            irritants = {x: 0 for x in range(self.size)}
        else:
            irritants = [i.strip() for i in irritants.split(',')]
            irritants = {i.split(' ')[0]: i.split(' ')[1] for i in irritants}
        for i, level in enumerate(irritants):
            if level > self.graph.nodes.data()[i]['condition']:
                self.graph.nodes.data()[i]['annoyed'] = True

    def process(self, irritants: str = None):
        pass
