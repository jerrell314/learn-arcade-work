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
    print(room_list[current_room].description)
    done = False
    while not done:
        print()
        user_input = input("Which door would you like to go through? ")
        if user_input == "n":
            next_room = room_list[current_room].north
        if user_input == None:
            print("You can't go that way.")
        else:
            current_room = next_room







main()