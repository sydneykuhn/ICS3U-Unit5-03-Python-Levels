#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Oct 2020
# This program converts a percentage to a level mark


def calculate_mark(level):
    # calculate mark

    # process
    if level == "4+":
        mark = "98%"
    elif level == "4":
        mark = "91%"
    elif level == "4-":
        mark = "83%"
    elif level == "3+":
        mark = "78%"
    elif level == "3":
        mark = "75%"
    elif level == "3-":
        mark = "71%"
    elif level == "2+":
        mark = "68%"
    elif level == "2":
        mark = "65%"
    elif level == "2-":
        mark = "61%"
    elif level == "1+":
        mark = "58%"
    elif level == "1":
        mark = "55%"
    elif level == "1-":
        mark = "51%"
    elif level == "R":
        mark = "25%"
    else:
        mark = -1

    # output
    return mark


def main():
    # this function gets the user input

    # input
    level_from_user = input("Enter a level you want converted to a percentage : ")
    # call function
    calculated_mark = calculate_mark(level_from_user)
    print(
        "Level {0} has a middle percentage of {1}.".format(
            level_from_user, calculated_mark))

    print("\nDone.")


if __name__ == "__main__":
    main()
