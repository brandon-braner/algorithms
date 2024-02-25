from typing import List


def bubble_sort(arr: List[int]) -> List[int]: from typing import List


def bubble_sort(arr: List[int], direction='asc') -> List[int]:
    n = len(arr)
    if direction == 'asc':
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    else:
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
