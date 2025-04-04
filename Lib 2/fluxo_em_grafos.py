def ford_fulkerson(capacity, s, t):
    n = len(capacity)
    flow = 0
    residual = [row[:] for row in capacity] 

    def dfs(u, t, visited, f):
        if u == t:
            return f
        visited[u] = True
        for v in range(n):
            if not visited[v] and residual[u][v] > 0:
                next_flow = dfs(v, t, visited, min(f, residual[u][v]))
                if next_flow > 0:
                    residual[u][v] -= next_flow
                    residual[v][u] += next_flow
                    return next_flow
        return 0

    while True:
        visited = [False] * n
        pushed = dfs(s, t, visited, float('inf'))
        if pushed == 0:
            break
        flow += pushed

    return flow


from collections import deque

def edmonds_karp(capacity, s, t):
    n = len(capacity)
    flow = 0
    residual = [row[:] for row in capacity]

    def bfs():
        parent = [-1] * n
        q = deque()
        q.append(s)
        while q:
            u = q.popleft()
            for v in range(n):
                if parent[v] == -1 and residual[u][v] > 0 and v != s:
                    parent[v] = u
                    if v == t:
                        return parent
                    q.append(v)
        return None

    while True:
        parent = bfs()
        if parent is None:
            break

        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, residual[u][v])
            v = u

        v = t
        while v != s:
            u = parent[v]
            residual[u][v] -= path_flow
            residual[v][u] += path_flow
            v = u

        flow += path_flow

    return flow


def dinic(capacity, s, t):
    from collections import deque
    n = len(capacity)
    flow = 0
    residual = [row[:] for row in capacity]
    level = [0] * n

    def bfs():
        nonlocal level
        level = [-1] * n
        q = deque()
        q.append(s)
        level[s] = 0
        while q:
            u = q.popleft()
            for v in range(n):
                if residual[u][v] > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[t] != -1

    def dfs(u, pushed):
        if u == t:
            return pushed
        for v in range(n):
            if residual[u][v] > 0 and level[v] == level[u] + 1:
                tr = dfs(v, min(pushed, residual[u][v]))
                if tr > 0:
                    residual[u][v] -= tr
                    residual[v][u] += tr
                    return tr
        return 0

    while bfs():
        pushed = dfs(s, float('inf'))
        while pushed:
            flow += pushed
            pushed = dfs(s, float('inf'))

    return flow
