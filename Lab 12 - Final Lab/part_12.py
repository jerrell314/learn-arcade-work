import arcade
import os

SPRITE_SCALING = 0.3
BRICK_SCALING = 0.5
BALL_SCALING = 0.3
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Walls Example"

MOVEMENT_SPEED = 5
BALL_SPEED = 5



class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.coin_list = None
        self.wall_list = None
        self.player_list = None
        self.ball_list = None

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None
        self.ball_sprite = None
        self.set_mouse_visible(False)
        self.ball_on_paddle = True

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.ball_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:gui_basic_assets/red_button_normal.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        # Image is from Brunswickbowling.com
        self.ball_sprite = arcade.Sprite(":resources:images/pinball/pool_cue_ball.png", BALL_SCALING)
        self.ball.center_x = self.player_sprite.center_x
        self.ball.bottom = self.player_sprite.top
        self.ball_list.append(self.ball_sprite)




        # -- Set up the walls
        # Create a row of boxes

        for x in range(30, 790, 64):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 BRICK_SCALING)
            wall.center_x = x
            wall.center_y = 570
            self.wall_list.append(wall)

        # Create a column of boxes
        for y in range(30, 700, 64):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 BRICK_SCALING)
            wall.center_x = 766
            wall.center_y = y
            self.wall_list.append(wall)
        for y in range(30, 700, 64):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 BRICK_SCALING)
            wall.center_x = 30
            wall.center_y = y
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.wall_list.draw()
        self.ball_list.draw()
        self.player_list.draw()



    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):

        self.player_sprite.center_x = x
        if self.ball_on_paddle:
            self.ball_list = self.player_sprite


    def on_mouse_press(self, x, y, button, modifiers):
        pass




    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()
        self.ball_list.update()


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()