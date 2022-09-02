# Study Note

## Add Two Numbers
- Source: https://leetcode.com/problems/add-two-numbers/
- Comment:



```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        node = ListNode(0)
        head = node
        # While at least one of the lists has not ended
        while l1 is not None or l2 is not None:
            # if both not ended -> do calculation and leave carry
            if l1 is not None and l2 is not None:
                val = l1.val + l2.val + carry
                carry = val // 10
                head.next = ListNode(val % 10)

                head = head.next
                l1 = l1.next
                l2 = l2.next
            # if one ended -> add carry and do calculation
            elif l1 is None:
                val = l2.val + carry
                carry = val // 10
                head.next = ListNode(val % 10)

                head = head.next
                l2 = l2.next
            elif l2 is None:
                val = l1.val + carry
                carry = val // 10
                head.next = ListNode(val % 10)

                head = head.next
                l1 = l1.next
        if carry > 0:
            head.next = ListNode(carry)
        return node.next
```


## Two Sum
- Source: https://leetcode.com/problems/two-sum/
- Comment:



```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = dict()
        for i, value in enumerate(nums):
            indices[value] = i
        for i, value in enumerate(nums):
            remaining = target - value
            if remaining in indices and indices[remaining] != i:
                return [i, indices[remaining]]
        return [-1, -1]

```
