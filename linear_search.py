# Linear search algorithm will search each item in a list in order to find a match.
from typing import List


def linear_search(haystack: List, needle: int) -> int:
    for i in range(len(haystack)):
        if haystack[i] == needle:
            return i
    return -1


