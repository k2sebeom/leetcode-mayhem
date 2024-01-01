'''

Title: Roads and Libraries
Source: https://www.hackerrank.com/challenges/torque-and-development/problem
Comment: Think of examples like DFS, and think of the fact that min number of edges to fully connect a graph with n nodes is n - 1


'''

def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        return n * c_lib
    
    visited = dict()
    edges = dict()

    for c in range(1, n + 1):
        visited[c] = False
        edges[c] = []
    
    for s, d in cities:
        edges[s].append(d)
        edges[d].append(s)
    

    def dfs(s, sofar): # visit all the connected nodes and return partition
        visited[s] = True
        sofar.add(s)
        for d in edges[s]:
            if not visited[d]:
                visited[d] = True
                dfs(d, sofar)
    
    partitions = []
    
    for c in range(1, n + 1):
        if not visited[c]:
            sofar = set()
            dfs(c, sofar)
            partitions.append(len(sofar))
    
    cost = 0
    for p in partitions:
        cost += c_lib + (p - 1) * c_road
    return cost
            