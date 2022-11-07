'''

Title: Delete Node in a Linked List
Source: https://leetcode.com/problems/delete-node-in-a-linked-list/
Comment: Is this medium level?

'''

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        slow, fast = node, node.next
        while fast is not None:
            slow.val = fast.val # Shifting values of nodes to left
            if fast.next is None:
                slow.next = None
            slow, fast = slow.next, fast.next