__author__: str = "730736088"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_for_when_list_none() -> None:
    a = []
    assert find_and_remove_max(a) == -1


def test_find_and_remove_max_return_exp() -> None:
    b = [1, 2, 4, 2, 1, 4]
    assert find_and_remove_max(b) == 4


def test_find_and_remove_max_muate_right() -> None:
    b = [1, 4, 4, 2, 1, 4]
    find_and_remove_max(b)
    assert b == [1, 2, 1]
