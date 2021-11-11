"""
Scroll around a large screen.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_scrolling
"""

import random
import arcade

SPRITE_SCALING = 0.5
SPRITE_SCALING_COIN = 0.2
DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"
NUMBER_OF_COINS = 25

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 7


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None

        # Set up the player
        self.player_sprite = None
        self.score = 0

        # Physics engine so we don't run into walls.
        self.physics_engine = None
        self.coin_list = None


        # Create the cameras. One for the GUI, one for the sprites.

        # We scroll the 'sprite world' but not the GUI.

        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)


    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           scale=0.4)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 512
        self.player_list.append(self.player_sprite)

        # card boundary
        for x in range(173, 1010, 64):
            wall = arcade.Sprite("cardClubsQ.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 350
            self.wall_list.append(wall)
        for x in range(230, 1010, 64):
            wall = arcade.Sprite("cardClubsQ.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 987
            self.wall_list.append(wall)
        for y in range(410, 1010, 64):
            wall = arcade.Sprite("cardHeartsK.png", SPRITE_SCALING)
            wall.center_x = 170
            wall.center_y = y
            self.wall_list.append(wall)
        for y in range(410, 1010, 64):
            wall = arcade.Sprite("cardHeartsK.png", SPRITE_SCALING)
            wall.center_x = 1005
            wall.center_y = y
            self.wall_list.append(wall)

        coordinate_list = [[400, 600],
                           [464, 600],
                           [528, 600],
                           [592, 600]]
        # place bricks
        for coordinate in coordinate_list:
            wall = arcade.Sprite("brickGrey.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        coordinate_list = [[400, 600],
                           [464, 600],
                           [528, 600],
                           [592, 600]]
        # place bricks
        for coordinate in coordinate_list:
            wall = arcade.Sprite("brickGrey.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        wall = arcade.Sprite("brickGrey.png", SPRITE_SCALING)
        wall.center_x = 700
        wall.center_y = 850
        self.wall_list.append(wall)

        wall = arcade.Sprite("brickGrey.png", SPRITE_SCALING)
        wall.center_x = 250
        wall.center_y = 455
        self.wall_list.append(wall)

        wall = arcade.Sprite("brickGrey.png", SPRITE_SCALING)
        wall.center_x = 950
        wall.center_y = 855
        self.wall_list.append(wall)
        coordinate_list = [[588, 688],
                           [716, 795],
                           [668, 566],
                           [741, 634]]
        for coordinate in coordinate_list:
            wall = arcade.Sprite("brickGrey.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)
        coordinate_list = [[414, 416],
                           [274, 703],
                           [850, 532],
                           [535, 512]]
        for coordinate in coordinate_list:
            wall = arcade.Sprite("brickGrey.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)
        for x in range(230, 550, 64):
            wall = arcade.Sprite("brickGrey.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 850
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)
        # Place coin
        for coin in range(NUMBER_OF_COINS):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)
            coin_placed_successfully = False

            while not coin_placed_successfully:
                coin.center_x = random.randrange(DEFAULT_SCREEN_WIDTH)
                coin.center_y = random.randrange(DEFAULT_SCREEN_HEIGHT)
                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    coin_placed_successfully = True
            self.coin_list.append(coin)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()


        # Select the camera we'll use to draw all our sprites

        self.camera_sprites.use()


        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()


        # Select the (unscrolled) camera for our GUI

        self.camera_gui.use()


        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 14)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """



        # Call update on all sprites (The sprites don't do much in this

        # example though.)

        self.physics_engine.update()



        # Scroll the screen to the player

        self.scroll_to_player()
        self.coin_list.update()
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.coin_list)
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1



    def scroll_to_player(self):

        """

        Scroll the window to the player.



        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.

        Anything between 0 and 1 will have the camera move to the location with a smoother

        pan.

        """



        position = self.player_sprite.center_x - self.width / 2, \
                self.player_sprite.center_y - self.height / 2

        self.camera_sprites.move_to(position, CAMERA_SPEED)



    def on_resize(self, width, height):

        """

        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()