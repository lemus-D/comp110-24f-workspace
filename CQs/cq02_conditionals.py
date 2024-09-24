"""Guessing game"""

__author__ = "730736088"


def guess_a_number() -> None:
    x = input("Guess a number:")
    Secret: int = 7
    print("Your guess was " + x)
    if int(x) == Secret:
        print("You got it!")
    elif int(x) > Secret:
        print("Your guess was too high! The secret number is " + str(Secret))
    else:
        print("Your guess was too low! The secret number is " + str(Secret))
    return None


if __name__ == "__main__":
    guess_a_number()
