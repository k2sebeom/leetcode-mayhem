'''

Title: Kth Smallest Element in a BST
Source: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Comment: Inorder traversal of BST is a sorted list

'''

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            result = []
            if node.left:
                result = inorder(node.left) + result
            result.append(node.val)
            if node.right:
                result = result + inorder(node.right)
            return result
        return inorder(root)[k - 1]