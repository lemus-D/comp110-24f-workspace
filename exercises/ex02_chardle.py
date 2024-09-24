"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730736088"


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    user_word = input("Enter a 5-character word:")
    # checks if the word is not 5 letters if so then it will spit out
    # the error message
    if len(user_word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return user_word


def input_letter() -> str:
    user_char = input("Enter a single character:")
    # checks if the character is not 1 char if so then it will spit out
    # the error message
    if len(user_char) != 1:
        print("Error: Character must be a single character.")
        # placed the exit here so no value would return
        exit()
    return user_char


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    # I used the x varriable as a counting var
    x = 0
    # all the ifs were used to check different indexs of the word
    if word[0] == letter:
        print(letter + " found at index 0")
        x = x + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        x = x + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        x = x + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        x = x + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        x = x + 1
    # Checked the x value to see if the value actually increased or not then just did
    # print statements to reflect that
    if x == 0:
        print("No instances of " + letter + " found in " + word)
    elif x == 1:
        print(str(x) + " instance of " + letter + " found in " + word)
    elif x > 1:
        print(str(x) + " instances of " + letter + " found in " + word)


if __name__ == "__main__":
    main()
