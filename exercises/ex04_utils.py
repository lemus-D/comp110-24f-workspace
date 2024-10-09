"""Honestly dont know yet."""

__author__ = "730736088"


def all(list_of_ints: list[int], int: int) -> bool:
    if len(list_of_ints) == 0:
        return False
    # using i as a counter to see how many of the ints in the list matched
    i = 0
    while i < len(list_of_ints):
        if int != list_of_ints[i]:
            return False
        i += 1
    return True


def max(list_of_ints: list[int]) -> int:
    if len(list_of_ints) == 0:
        raise ValueError("max() arg is an empty List")
    # serves as my compairison variable
    i = 0
    max_int = list_of_ints[i]
    while i < len(list_of_ints):
        if list_of_ints[i] > max_int:
            max_int = list_of_ints[i]
        i += 1
    return max_int


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    if len(list_1) != len(list_2):
        return False

    i = 0
    while i < len(list_1):
        if list_1[i] != list_2[i]:
            return False
        i += 1
    return True


def extend(list_1: list[int], list_2: list[int]) -> None:
    i = 0
    while i < len(list_2):
        list_1.append(list_2[i])
        i += 1
