"""
Runtime: O(log n)
For binary search, the input array must be sorted.
You do a log n search, you divide the array in half and check if the number is in the first or second half.

If the size of a list is 4096, it will take 12 steps to find the number.
log 4096 = 12
2048 (1)
1024 (2)
512 (3)
256 (4)
128 (5)
64  (6)
32 (7)
16 (8)
8 (9)
4 (10)
2 (11)
1 (12)
"""
from typing import List


def binary_search(haystack: List[int], needle: int) -> bool:
    lo = 0
    hi = len(haystack) - 1

    while lo <= hi:
        mid = (hi + lo) // 2
        value = haystack[mid]
        # If the number is found, return the index
        if value == needle:
            return mid
        # if the needle is greater then the value, search the right half
        elif needle > value:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1




