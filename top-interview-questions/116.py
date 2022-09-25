'''

Title: Populating Next Right Pointers in Each Node
Source: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
Comment: Think of the known traversals when dealing with trees. (Also related to Leetcode #102)

'''

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        levels = []
        
        def preorder(tree, depth):
            if tree is None:
                return
            if depth >= len(levels):
                levels.append([])
            levels[depth].append(tree)
            preorder(tree.left, depth + 1)
            preorder(tree.right, depth + 1)
        
        preorder(root, 0)
        
        for level in levels:
            for i in range(len(level)):
                if i < len(level) - 1:
                    level[i].next = level[i + 1]
                else:
                    level[i].next = None
        return root