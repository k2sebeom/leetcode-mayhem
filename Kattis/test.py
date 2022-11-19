class Tree:
    def __init__(self, idx, gate, changeable, val=None):
        self.idx = idx
        self.gate = gate
        self.changeable = True if changeable > 0 else False
        self.val = val
        self.left = None
        self.right = None


def findMinimumGates(nodes, target):
    dp = [[-1, -1] for _ in range(len(nodes))]
    cases = [
        [[(0, 0)], [(1, 1), (1, 0), (0, 1)]],
        [[(0, 0), (1, 0), (0, 1)], [(1, 1)]]
    ]

    for i in range(len(nodes) -1, -1, -1):
        node = nodes[i]
        if node.gate < 0:
            for v in range(2):
                dp[i][v] = 0 if node.val == v else -1
        else:
            for v in range(2):
                cand = []
                ldx, rdx = 2 * node.idx - 1, 2 * node.idx
                for c in cases[node.gate][v]:
                    L, R = c                    
                    if dp[ldx][L] >= 0 and dp[rdx][R] >= 0:
                        cand.append(dp[ldx][L] + dp[rdx][R])
                
                if node.changeable:
                    for c in cases[(node.gate + 1) % 2][v]:
                        L, R = c
                        if dp[ldx][L] >= 0 and dp[rdx][R] >= 0:
                            cand.append(dp[ldx][L] + dp[rdx][R] + 1)
                dp[i][v] = min(cand) if cand else -1
    return dp[0][target]

n = eval(input())

for k in range(n):
    total, val = input().split()
    total, val = eval(total), eval(val)
    nodes = []
    for i in range((total - 1) // 2):
        G, C = input().split()
        G, C = eval(G), eval(C)
        t = Tree(i + 1, G, C)
        nodes.append(t)
    for i in range((total + 1) // 2):
        leaf = eval(input())
        t = Tree(i + 1, -1, -1, leaf)
        nodes.append(t)

    for i in range(1, (total - 1) // 2 + 1):
        parent = nodes[i - 1]
        parent.left = nodes[2 * i - 1]
        parent.right = nodes[2 * i]

    ans = findMinimumGates(nodes, val)
    print(f'Case #{k + 1}: {ans if ans >= 0 else "IMPOSSIBLE"}')
