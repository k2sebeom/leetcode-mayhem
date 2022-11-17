'''

Title: Insert Delete GetRandom O(1)
Source: https://leetcode.com/problems/insert-delete-getrandom-o1/
Comment: Just used python set

'''

class RandomizedSet:

    def __init__(self):
        self.data = set()

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        else:
            self.data.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.data:
            self.data.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        L = list(self.data)
        return L[int(random.random() * len(L))]

