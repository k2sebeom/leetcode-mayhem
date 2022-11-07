'''

Title: Lowest Common Ancestor of a Binary Tree
Source: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
Comment: Basically a search in tree, if node appears in both child tress, than the node is potential LCA

'''

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        if root.val in (p.val, q.val):
            return root
        
        left, right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
        
        return root if left and right else left or right