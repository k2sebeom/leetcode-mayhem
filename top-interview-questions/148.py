'''

Title: Sort List
Source: https://leetcode.com/problems/sort-list/
Comment: This is very fake...

'''

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake = []
        node = head
        while node is not None:
            fake.append(node.val)
            node = node.next
        
        fake.sort()
        
        node = head
        for n in fake:
            node.val = n
            node = node.next
        return head