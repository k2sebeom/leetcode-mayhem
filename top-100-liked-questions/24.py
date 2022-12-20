'''

Title: Swap Nodes in Pairs
Source: https://leetcode.com/problems/swap-nodes-in-pairs/
Comment: Node traversal

'''


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n) O(1)
        fast, slow = head, None
        if head is None:
            return None

        if head.next is not None:
            head = head.next

        while fast is not None and fast.next is not None:
            node = fast.next
            node.next, fast.next = fast, node.next
            if slow is not None:
                slow.next = node
            fast, slow = fast.next, fast
        return head
        