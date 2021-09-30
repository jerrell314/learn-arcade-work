# Camel Lab

import random


def main():
    # Instructions
    print("Welcome to Camel!")
    print("You have stolen a camel to make you way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")

    # Variables for miles traveled, thirst , drinks in canteen, camel tiredness, how far are the natives
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    drinks_in_canteen = 3
    distance_of_natives_behind = miles_traveled - 20


    done = False
    while not done:
        print("\na.Drink from your canteen.")
        print("b.Ahead moderate speed.")
        print("c.Ahead full speed.")
        print("d.Stop for the night.")
        print("e.Status check.")
        print("q.Quit.")

        # What is said after choice is made

        user_choice = input("What is your choice? ")

        if user_choice.lower() == "q":
            print("See ya next time")
            done = True
        elif user_choice.lower() == "e":
            print("You traveled", miles_traveled)
            print("You have", drinks_in_canteen, "drinks in canteen")
            print("Natives are", distance_of_natives_behind, "miles behind you")

        elif user_choice.lower() == "d":
            my_number = random.randrange(7, 14)
            print("camel is happy")
            print("Natives are", my_number, " miles behind you")


main()