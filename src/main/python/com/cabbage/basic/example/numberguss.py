"""
Play a game of guss the number with the user
"""

import random

str1 = 1

def main():
    # Inputs this bounds of the range of numbers and lets the user guss the computer's number until the guss is correct.
    smaller = int(input("Enter the larger number: "))
    lager = int(input("Enter the larger number: "))
    myNumber = random.randint(smaller,lager)
    count = 0
    while True:
        count += 1
        userNumber = int(input("Enter your guss: "))
        if userNumber < myNumber:
            print("Too small")
        elif userNumber > myNumber:
            print("Too larger")
        else:
            print("You've got it in",count,"tries")
            break


if __name__ == '__main__':
    main()