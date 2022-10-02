'''

Title: Copy List with Random Pointer
Source: https://leetcode.com/problems/copy-list-with-random-pointer/
Comment: O(n) algorithm by saving in python array

'''

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        indices = dict()
        new_indices = dict()
        node = head
        i = 0
        new_head = Node(head.val)
        new_node = new_head
        while node is not None:
            indices[node] = i
            new_indices[i] = new_node
            node = node.next
            if node is not None:
                new_node.next = Node(node.val)
            new_node = new_node.next
            i += 1
        
        node = head
        new_node = new_head
        
        while node is not None:
            if node.random is not None:
                random_idx = indices[node.random]
                random_node = new_indices[random_idx]
                new_node.random = random_node
            node = node.next
            new_node = new_node.next
        
        return new_head
