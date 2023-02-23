from typing import List

def move_to_end(moved_list: List[int], tuple_list: List[int]) -> List:
    last_value = moved_list.index(tuple_list)
    moved_list[-1], moved_list[last_value] = moved_list[last_value], moved_list[-1]
    return moved_list

print(move_to_end([2,3,4,6,7],3))