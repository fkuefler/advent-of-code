import os
import math

file_path = os.path.join(os.path.dirname(__file__), "input_day_8.txt")
with open(file_path, "r") as file:
    input_ = file.read()


# Custom Disjoint Set Union implementation
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.max_size = 1

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def merge(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        if irep != jrep:
            self.parent[irep] = jrep
            self.size[jrep] += self.size[irep]
            self.size[irep] = 1
            self.max_size = max(self.max_size, self.size[jrep])


# Returns the distance between two 3D points
def dist(c1, c2) -> float:
    return ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2 + (c1[2] - c2[2]) ** 2) ** 0.5


coords = [tuple(int(x) for x in line.split(",")) for line in input_.split("\n")]
edges = [(i, j) for i in range(len(coords)) for j in range(i + 1, len(coords))]

dsu = DSU(len(coords))
for i, edge in enumerate(sorted(edges, key=lambda e: dist(coords[e[0]], coords[e[1]]))):
    dsu.merge(edge[0], edge[1])
    if i == 999:
        print("Part 1 Answer:", math.prod(sorted(dsu.size, reverse=True)[:3]))
    if dsu.max_size == len(coords):
        print("Part 2 Answer:", coords[edge[0]][0] * coords[edge[1]][0])
        break
