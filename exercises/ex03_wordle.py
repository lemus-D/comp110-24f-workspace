"""Wordle"""

__author__: str = "730736088"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns_taken = 1
    turn_won = 0
    while turns_taken <= 6:
        print(f"=== Turn {turns_taken}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            # serves as a marker on what turn someone won
            turn_won = turns_taken
            turns_taken = 7
        turns_taken = turns_taken + 1
    if turn_won == 0:
        print("X/6 - Sorry, try again tomorrow!")
    else:
        print(f"You won in {turn_won}/6 turns!")


def input_guess(secret_word_len: int) -> str:
    guess = input(f"Enter a {secret_word_len} character word:")
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again:")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    # this thing gon search the word and check if it has the certain char in it
    assert len(char_guess) == 1
    i = 0
    while i < len(secret_word):
        if secret_word[i] == char_guess:
            return True
        i = i + 1
    return False


def emojified(guess: str, secret: str) -> str:
    # uses emojis to describe how close two strings are in relation top each other
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i = 0
    output = ""
    while i < len(guess):
        if contains_char(secret, guess[i]):
            if guess[i] == secret[i]:
                output = output + GREEN_BOX
            else:
                output = output + YELLOW_BOX
        else:
            output = output + WHITE_BOX
        i = i + 1
    return str(output)


if __name__ == "__main__":
    main(secret="codes")
