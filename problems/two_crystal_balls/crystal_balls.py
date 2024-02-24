import math
from typing import List


# def crystal_balls(floors: List[int]) -> int:
#     return math.ceil((math.sqrt(1 + 8 * floors) - 1) / 2)


def crystal_balls(floors: List[bool]) -> int:
    num_of_floors = len(floors) - 1
    jump_distance = math.floor(math.sqrt(len(floors)))

    breaking_point = 0
    # find the floor where the first ball breaks
    for i in range(jump_distance, num_of_floors, jump_distance):
        if floors[i]:
            breaking_point = i
            break

    # go back to the previous point we knew the ball didn't break and drop it till we find where it breaks
    # since the endpoint is exclusive we need to add one to make sure we check the floor it broke on just incase
    # that is the first floor it breaks on
    for i in range(breaking_point - jump_distance, breaking_point+1):
        if floors[i]:
            return i

    return -1


