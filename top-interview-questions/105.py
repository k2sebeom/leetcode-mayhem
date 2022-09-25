'''

Title: Construct Binary Tree from Preorder and Inorder Traversal
Source: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Comment: Distinguish inorder and preorder

'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        root = preorder[0]
        idx = inorder.index(root)
        
        left_in, right_in = inorder[:idx], inorder[idx + 1:]
        
        idx = len(left_in)
        
        left_pre, right_pre = preorder[1: idx + 1], preorder[idx + 1:]
        
        left_tree = self.buildTree(left_pre, left_in)
        right_tree = self.buildTree(right_pre, right_in)
        
        return TreeNode(root, left_tree, right_tree)
