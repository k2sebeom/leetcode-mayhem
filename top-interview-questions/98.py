'''

Title: Validate Binary Search Tree
Source: https://leetcode.com/problems/validate-binary-search-tree/
Comment: Think of standard tree traversal (inorder, preorder, postorder)

'''

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        
        def inorder(root: TreeNode, add):
            if root.left:
                inorder(root.left, add)
            add(root.val)
            if root.right:
                inorder(root.right, add)

        inorder(root, stack.append)

        for i in range(1, len(stack)):
            if stack[i - 1] >= stack[i]:
                return False
        return True
