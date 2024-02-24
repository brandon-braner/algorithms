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

