'''
Binary Search
O(log n)
'''
from typing import List

def search(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums)

    while lo <= hi:
        mid = (lo + hi) // 2

        if nums[mid] < target:
            lo = mid + 1
        elif nums[mid] > target:
            hi = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    L = [1, 3, 5, 7, 10, 15, 27]

    print(search(L, 1))
    print(search(L, 7))
    print(search(L, 10))
    print(search(L, 18))
