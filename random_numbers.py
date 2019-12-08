#!/usr/bin/env python3

# Created by: Dylan Hanna
# Created on: Nov 2019
# This program creates random numbers and finds the average


import random


def main():

    random_number = []

    for loop_counter in range(0, 10):
        random_numbers = (random.randint(0, 100))
        random_number.append(random_numbers)
    print("")

    print("Your 10 random numbers:")

    for loop_counter in range(0, 10):
        print("{0}, ".format(random_number[loop_counter]), end="")

    lst = [loop_counter]
    average = (random_number[loop_counter])
    print("")
    print("Average of the numbers: ", round(average))

    print("")


if __name__ == "__main__":
    main()
