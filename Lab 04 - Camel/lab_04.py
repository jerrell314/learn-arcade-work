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
    distance_of_natives_behind = -20
    done = False

    while not done:
        print()
        print("a.Drink from your canteen.")
        print("a.Drink from your canteen.")
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
            print("Natives are", miles_traveled - distance_of_natives_behind, "miles behind you")

        elif user_choice.lower() == "d":
            my_number = random.randrange(7, 14)
            print("camel is happy")
            print("Natives are", my_number, " miles behind you")

        elif user_choice.lower() == "c":
            ahead = random.randrange(10, 20)
            fatigue = random.randrange(1, 3)
            native_advancing = random.randrange(7, 14)
            print("Ahead full speed. You have traveled", miles_traveled + ahead, "miles")
            thirst += 1
            camel_tiredness += fatigue
            print("Natives are", distance_of_natives_behind + native_advancing, "behind you")
            if random.randrange(25) == 0:
                print("You have found an oasis!")
                thirst = 0
                camel_tiredness = 0
                drinks_in_canteen = 3

        elif user_choice.lower() == "a":
            thirst = 0
            print("That was good!")
            print(drinks_in_canteen - 1, "drinks from canteen left")

        elif user_choice.lower() == "b":
            print("Ahead moderate speed")
            onward = random.randrange(5, 12)
            camel_tiredness += 1
            forward = distance_of_natives_behind + random.randrange(7, 14)
            print("You have traveled", onward, "miles ")
            print("Natives are", forward, "behind you")
            if random.randrange(25) == 0:
                print("You have found an oasis!")
                thirst = 0
                camel_tiredness = 0
                drinks_in_canteen = 3

        if thirst >= 6:
            print("You died of thirst")
            done = True
        elif thirst >= 4:
            print("You are thirsty")

        if not done:
            if camel_tiredness >= 8:
                print("Your camel is dead and the natives have caught you")
                done = True
            elif camel_tiredness >= 5:
                print("Your camel is getting tired")

        if not done:
            if distance_of_natives_behind >= miles_traveled:
                print("Natives have caught you GAME OVER!!")
                done = True
            elif distance_of_natives_behind <= 15 - miles_traveled:
                print("Natives are getting close")

        if not done:
            if miles_traveled >= 200:
                print("YOU WON")
                done = True


main()
