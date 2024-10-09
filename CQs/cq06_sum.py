"""Summing the elements of a list using different loops"""

__author__ = "730736088"


def w_sum(vals: list[float]) -> float:
    i = 0
    sum = 0.0
    while i < len(vals):
        sum = vals[i] + sum
        i += 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum = 0.0
    for idx in vals:
        sum = idx + sum
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum = 0.0
    for idx in range(0, len(vals)):
        sum = sum + vals[idx]
    return sum
