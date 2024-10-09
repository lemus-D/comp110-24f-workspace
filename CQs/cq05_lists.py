"""Mutating functions."""

__author__ = "730736088"


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


def manual_append(get_list: list[int], num: int) -> None:
    get_list.append(num)


def double(get_list: list[int]) -> None:
    i: int = 0
    while i < len(get_list):
        get_list[i] = get_list[i] * 2
        i += 1


double(list_2)
print(list_1)
print(list_2)
