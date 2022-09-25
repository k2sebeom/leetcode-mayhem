'''

Title: Binary Tree Zigzag Level Order Traversal
Source: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Comment: Just the same as 102, but with zigzag indicator

'''

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []   
        result, level = [], [root]
        add = result.append
        counter = 1
        while level:
            add(list(map(lambda n: n.val, level[::counter])))
            counter *= -1
            next_level = []
            log = next_level.append
            for node in level:
                if node.left:
                    log(node.left)
                if node.right:
                    log(node.right)
            level = next_level
        return result