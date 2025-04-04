import heapq

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        else:
            self.parent[root_v] = root_u
            if self.rank[root_u] == self.rank[root_v]:
                self.rank[root_u] += 1
        return True


def kruskal(n, edges):
    edges.sort()
    uf = UnionFind(n)
    mst = []
    total_weight = 0

    for weight, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight


def prim(graph, start=0):
    visited = set()
    min_heap = [(0, start, -1)]  
    mst = []
    total_weight = 0

    while min_heap and len(visited) < len(graph):
        weight, u, prev = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        total_weight += weight
        if prev != -1:
            mst.append((prev, u, weight))

        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (w, v, u))

    return mst, total_weight
