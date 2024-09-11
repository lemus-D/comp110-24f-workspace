"""The purpose of this program is to calculate the cost of a tea party depending on
things like number of guests, it would also look at number of tea bags and treats"""

__author__: str = "730736088"


def main_planner(guests: int) -> None:
    """Main entrypoint of the program"""
    # gotta make everything into strings or else you will get an error learned that the
    # hard way
    print("A Cozy Tea Party For " + str(guests) + " people!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    # I was going to make variables for each value from the function but just calling
    # each function in the print statement was just as easy
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """assume people have two cups of tea"""
    return people * 2


def treats(people: int) -> int:
    """assume people have 1.5 treats per person"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calcs cost of party"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
