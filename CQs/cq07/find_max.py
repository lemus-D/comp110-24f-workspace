__author__: str = "730736088"


def find_and_remove_max(list_of_ints: list[int]) -> int:
    if len(list_of_ints) == 0:
        return -1
    i = 0
    max_int = 0
    while i < len(list_of_ints):
        if list_of_ints[i] > list_of_ints[i - 1]:
            max_int = list_of_ints[i]
        i += 1
    c = list_of_ints.count(max_int)
    for i in range(c):
        list_of_ints.remove(max_int)
    return max_int
