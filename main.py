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
G = Automaton(matrix, size, n)

G.process()
G.process()
G.process('1 1')
G.process()
G.process()
G.process()
G.process()
