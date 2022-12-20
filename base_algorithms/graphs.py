from functools import cmp_to_key
from heapq import heappush, heappop


def dijkstra(s, V, E):
    weights = dict()
    for v in V:
        weights[v] = 0 if v == s else float('inf')
    q = []

    heappush(q, (0, s))

    while q:
        w, d = heappop(q)
        for e in E:
            if d in e[:2]:
                d2 = e[0] if d == e[1] else e[1]
                w2 = w + e[2]
                if w2 < weights[d2]:
                    weights[d2] = w2
                    heappush(q, (w2, d2))
    print(weights)


def kruskal(V, E):
    cmp = set()
    tree = []

    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]
    
    def union(parent, a, b):
        a = find(parent, a)
        b = find(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    parent = dict()
    for v in V:
        parent[v]  = v

    E.sort(key=lambda e: e[2])
    
    while len(cmp) < len(V):
        e = E.pop(0)

        if find(parent, e[0]) != find(parent, e[1]):
            cmp.add(e[0])
            cmp.add(e[1])
            union(parent, e[0], e[1])
            tree.append(e)
    print(tree)
    return tree


if __name__ == "__main__":
    V = [1, 2, 3, 4, 5]
    E = [
        (2, 3, 2), (3, 4, 6), (2, 1, 5), (1, 4, 9), (4, 5, 2), (1, 5, 1)
    ]
    dijkstra(1, V, E)

    V = [1, 2, 3, 4, 5, 6]
    E = [
        (5, 6, 2), (1, 2, 3), (3, 6, 3), (1, 5, 5), (2, 3, 5), (2, 5, 6), (4, 6, 7), (3, 4, 9)
    ]

    kruskal(V, E)
