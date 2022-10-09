import networkx as nx
import matplotlib.pyplot as plt


# class Cell:
#     def __init__(self, ID):
#         self.ID = ID
#         self.condition = 0 # Состояние
#         self.annoyed = False # Раздражение
#
#
# class Network:
#     def __init__(self, n: int):
#         self.n = n # Период Рефрактерности
#         self.Cells = [] # список всех ячеек


def show(graph: nx.Graph, color_map):
    nx.draw_spectral(graph, with_labels=True, node_color=color_map)
    plt.pause(2)
    plt.clf()


def assign_colors(graph: nx.Graph):
    color_map = []
    for i in range(graph.size()):
        if graph.nodes[i]['annoyed']:
            color_map.append('red')
        elif not graph.nodes[i]['annoyed'] and graph.nodes[i]['condition'] > 0:
            color_map.append('blue')
        else:
            color_map.append('darkgrey')
    return color_map


def disturb_cells(graph: nx.Graph):
    line = input('Введите номера клеток ктр хотите побеспокоить через пробел: ')
    nums = [int(i) for i in line.split(' ')]
    for i in nums:
        graph.nodes.data()[i]['annoyed'] = True

    
