__author__ = "730736088"


def get_coords(xs: str, ys: str) -> None:
    i = 0
    j = 0
    while i < len(xs):
        while j < len(ys):
            print("(" + xs[i] + "," + ys[j] + ")")
            j = j + 1
        i = i + 1
        j = 0


get_coords("12", "34")
