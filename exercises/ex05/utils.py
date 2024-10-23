__author__: str = "730736088"

a_list = [10, 20, 30, 40]
list2 = []
list_1 = [1, 2, 3, 5]


def only_evens(ints: list[int]) -> list[int]:
    """takes a list and returns only the even values"""
    return_list = []
    for x in ints:
        if x % 2 == 0:
            return_list.append(x)
    return return_list


def sub(List: list[int], start: int, end: int) -> list[int]:
    """makes a subset of a list depending on start and end indexs"""
    return_list = []
    if len(List) == 0 or end <= 0 or start > len(List) - 1:
        return return_list
    if start < 0:
        start = 0
    if end > len(List) - 1:
        end = len(List)
    for x in range(start, end):
        return_list.append(List[x])
    return return_list


def add_at_index(list_of_ints: list[int], num: int, index: int) -> None:
    modded_list = []
    if index < 0 or index > len(list_of_ints):
        raise IndexError("Index is out of bounds for the input list")
    for x in range(0, len(list_of_ints)):
        if index == x:
            modded_list.append(num)
        modded_list.append(list_of_ints[x])
    for x in range(0, len(list_of_ints)):
        list_of_ints.pop(len(list_of_ints) - 1)
    for x in range(0, len(modded_list)):
        list_of_ints.append(modded_list[x])
    if index == len(list_of_ints):
        list_of_ints.append(num)
