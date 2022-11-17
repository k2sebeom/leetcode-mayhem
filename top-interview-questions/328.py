'''

Title: Odd Even Linked List
Source: https://leetcode.com/problems/odd-even-linked-list/
Comment: This is a crappy solution, but basically it uses two pointers.

'''


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        tail = head.next
        if not tail:
            return head
        slow, fast = head, head.next
        while fast.next:
            slow.next, fast.next = fast.next, fast.next.next
            fast = fast.next
            if slow.next:
                slow = slow.next
            if not fast:
                break
        slow.next = tail
        return head