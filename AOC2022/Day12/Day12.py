import numpy as np, networkx as nx

grid = np.array([[*x] for x in open('input.txt').read().split()])

S = tuple(*np.argwhere(grid=='S')); grid[S] = 'a'
E = tuple(*np.argwhere(grid=='E')); grid[E] = 'z'

N = nx.grid_2d_graph(*grid.shape)

G = nx.DiGraph()
for a in np.ndindex(grid.shape):
    for b in N.neighbors(a):
        if ord(grid[b]) <= ord(grid[a]) + 1:
            G.add_edge(a, b)

ls = nx.shortest_path_length(G, target=E)

print(ls[S], min(ls[a] for a in ls if grid[a]=='a'))