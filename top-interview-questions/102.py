'''

Title: Binary Tree Level Order Traversal
Source: https://leetcode.com/problems/binary-tree-level-order-traversal/
Comment: Use the traversal, but simplify if you can

'''

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result, level = [], [root]
        if not root:
            return []
        add = result.append
        while level:
            add(list(map(lambda n: n.val, level)))

            next_level = []
            log = next_level.append
            for node in level:
                if node.left:
                    log(node.left)
                if node.right:
                    log(node.right)
            level = next_level
        return result