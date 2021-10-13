import arcade


class Room:
    def __init__(self, description, north, east, west, south):
        self.description = description
        self.north = north
        self.east = east
        self.west = west
        self.south = south


def main():
    room_list = []
    room = Room("You are in the master bed room, " 
                "you have a door to the west and south of you.",
                None,
                None,
                2,
                1)
    room_list.append(room)
    room = Room("You are in the bed room 2,"
                "you have a door to the north and west of you.",
                0,
                None,
                3,
                None)
    room_list.append(room)
    room = Room("You are in the north hall, "
                "you have a door to the north, east, west, and south of you.",
                8,
                0,
                4,
                3)
    room_list.append(room)
    room = Room("You are in the south hall, "
                "you have a door to the north, east, west, and south of you.",
                2,
                1,
                5,
                7)
    room_list.append(room)
    room = Room("You are in the kitchen, "
                "you have a door to the east and the west of you.",
                None,
                2,
                None,
                5)
    room_list.append(room)
    room = Room("You are in the living room, "
                "you have a door to the north, east, and west pf you.",
                4,
                3,
                6,
                None)
    room_list.append(room)
    room = Room("You are at the pool, "
                "you have a door to the east of you.",
                None,
                5,
                None,
                None)
    room_list.append(room)
    room = Room("You are in the game room, "
                "you have a door to the north of you.",
                3,
                None,
                None,
                None)
    room_list.append(room)
    room = Room("You are in the movie theater, "
                "you have a door to the south of you.",
                None,
                None,
                None,
                2)
    room_list.append(room)
    current_room = 0
    done = False
    while not done:
        print()
        print(room_list[current_room].description)
        user_input = input("Which door would you like to go through? ")
        if user_input.lower() == "n" or user_input.lower() == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input.lower() == "e" or user_input.lower() == "east":
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input.lower() == "s" or user_input.lower() == "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input.lower() == "w" or user_input.lower() == "west":
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room
        elif user_input.lower() == "q" or user_input.lower() == "quit":
            print("Goodbye!")
            done = True

        else:
            print("Can't go that way choose another direction.")





main()
