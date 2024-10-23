__author__: str = "730736088"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import add_at_index
import pytest


def test_edge_case_only_evens() -> None:
    a = [
        -1,
        1,
        -3,
    ]
    assert only_evens(a) == []


def test_use_case1_only_evens() -> None:
    a = [2, 3, 7, 8]
    assert only_evens(a) == [2, 8]


def test_use_case2_only_evens() -> None:
    a = [1, 6, 8, 10, 12, 13, 14]
    assert only_evens(a) == [6, 8, 10, 12, 14]


def test_edge_case_sub() -> None:
    a = [1]
    b = 5
    c = 10
    assert sub(a, b, c) == []


def test_use_case1_sub() -> None:
    a = [3, 5, 6, 7, 8]
    b = 1
    c = 3
    assert sub(a, b, c) == [5, 6]


def test_use_case2_sub() -> None:
    a = [10, 2, 4, 12, 17, 19]
    b = 0
    c = 4
    assert sub(a, b, c) == [10, 2, 4, 12]


def test_edge_case_add_at_index() -> None:
    a = [1, 3, 5]
    b = 2
    c = 7
    with pytest.raises(IndexError):
        add_at_index(a, b, c)


def test_use_case1_add_at_index() -> None:
    a = [7, 9, 2, 3]
    b = 1
    c = 0
    add_at_index(a, b, c)
    assert a == [1, 7, 9, 2, 3]


def test_use_case2_add_at_index() -> None:
    a = [10, 2, 3, 6, 7]
    b = 89
    c = 3
    add_at_index(a, b, c)
    assert a == [10, 2, 3, 89, 6, 7]
