"""Seeing how many instances of a letter in a string"""

__author__ = "730736088"


def num_instances(phrase: str, search_char: str) -> int:
    i = 0
    x = 0
    # a loop function that runs for the length of the phrase
    while i < len(phrase):
        if phrase[i] == search_char:
            # x serves as my counting variable so everytime it sees that a letter in
            # the word matches the desired letter it adds one to the count
            x = x + 1
        # my iteration counter
        i = i + 1
    return x
