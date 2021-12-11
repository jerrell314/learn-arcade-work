import arcade
import os
import random

SPRITE_SCALING = 0.3
WALL_SCALING = 0.5
BRICK_SCALING = 0.3
BALL_SCALING = 0.25
PADDLE_SCALING = 0.4
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = "BRICK BREAKER 0.5"
SOUND = arcade.load_sound(":resources:sounds/hit4.wav")


MOVEMENT_SPEED = 5
BALL_SPEED = 10



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
        self.top_wall_list = None
        self.player_list = None
        self.ball_list = None
        self.green_brick_list = None
        self.diamonds_brick_list = None
        self.clubs_brick_list = None
        self.blue_brick_list = None

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None

        # Set up ball
        self.ball_sprite = None
        self.set_mouse_visible(False)

        # Set up the ball on paddle
        self.ball_on_paddle = True

        # Set up score and lives
        self.score = 0
        self.lives = 4

        # Set up the Bricks
        self.green_brick_sprite = None
        self.diamonds_brick_sprite = None
        self.clubs_brick_sprite = None
        self.blue_brick_sprite = None


    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.top_wall_list = arcade.SpriteList()
        self.ball_list = arcade.SpriteList()
        self.green_brick_list = arcade.SpriteList()
        self.diamonds_brick_list = arcade.SpriteList()
        self.clubs_brick_list = arcade.SpriteList()
        self.blue_brick_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:gui_basic_assets/red_button_normal.png",
                                           PADDLE_SCALING)
        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = SCREEN_HEIGHT - 600
        self.player_list.append(self.player_sprite)
        self.score = 0
        self.lives = 5

        # Set the score and lives
        self.score = 0
        self.lives = 4

        # Image is from Brunswickbowling.com
        ball = arcade.Sprite(":resources:images/pinball/pool_cue_ball.png", BALL_SCALING)
        ball.center_x = self.player_sprite.center_x
        ball.bottom = self.player_sprite.top
        self.ball_list.append(ball)
        self.ball_sprite = ball





        # -- Set up the walls
        # Create a row of boxes

        for x in range(90, 1000, 64):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 WALL_SCALING)
            wall.center_x = x
            wall.center_y = 670
            self.top_wall_list.append(wall)

        # Create a column of boxes
        for y in range(30, 700, 64):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 WALL_SCALING)
            wall.center_x = 970
            wall.center_y = y
            self.wall_list.append(wall)
        for y in range(30, 700, 64):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 WALL_SCALING)
            wall.center_x = 30
            wall.center_y = y
            self.wall_list.append(wall)
        for x in range(150, 900, 55):
            brick = arcade.Sprite(":resources:images/cards/cardBack_green5.png",
                                 BRICK_SCALING)
            brick.center_x = x
            brick.center_y = 550
            brick.angle = 90
            self.green_brick_list.append(brick)
        for x in range(150, 900, 55):
            brick = arcade.Sprite(":resources:images/cards/cardDiamonds9.png",
                                  BRICK_SCALING)
            brick.center_x = x
            brick.center_y = 510
            brick.angle = 90
            self.diamonds_brick_list.append(brick)
        for x in range(150, 900, 55):
            brick = arcade.Sprite(":resources:images/cards/cardClubsK.png",
                                  BRICK_SCALING)
            brick.center_x = x
            brick.center_y = 470
            brick.angle = 90
            self.clubs_brick_list.append(brick)
        for x in range(150, 900, 55):
            brick = arcade.Sprite(":resources:images/cards/cardBack_blue3.png",
                                  BRICK_SCALING)
            brick.center_x = x
            brick.center_y = 440
            brick.angle = 90
            self.blue_brick_list.append(brick)

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
        self.top_wall_list.draw()
        self.ball_list.draw()
        self.player_list.draw()
        self.green_brick_list.draw()
        self.diamonds_brick_list.draw()
        self.clubs_brick_list.draw()
        self.blue_brick_list.draw()

        arcade.draw_text(f"Score: {self.score}", SCREEN_WIDTH - 990, SCREEN_HEIGHT - 40, arcade.color.WHITE, 14)
        arcade.draw_text(f"Lives: {self.lives}", SCREEN_WIDTH - 90, SCREEN_HEIGHT - 40, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):

        self.player_sprite.center_x = x
        self.player_sprite.center_y = SCREEN_HEIGHT - 600
        if self.player_sprite.center_x < 100:
            self.player_sprite.center_x = 100
        if self.player_sprite.center_x > 900:
            self.player_sprite.center_x = 900


        if self.ball_on_paddle:
            self.ball_sprite.center_x = x
            self.ball_sprite.bottom = self.player_sprite.top






    def on_mouse_press(self, x, y, button, modifiers):
        self.ball_on_paddle = False
        self.ball_sprite.change_y = 5
        self.ball_sprite.change_x = random.randrange(-3, 4)





    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)

        self.ball_list.update()

        self.green_brick_list.update()
        self.ball_list.change_y = 0


        green_brick_hit_list = arcade.check_for_collision_with_list(self.ball_sprite, self.green_brick_list)
        if len(green_brick_hit_list):
            self.ball_sprite.change_y *= -1
        for brick in green_brick_hit_list:
            brick.remove_from_sprite_lists()
            self.score += 4
            arcade.play_sound(SOUND)

        self.diamonds_brick_list.update()

        diamonds_brick_hit_list = arcade.check_for_collision_with_list(self.ball_sprite, self.diamonds_brick_list)
        if len(diamonds_brick_hit_list):
            self.ball_sprite.change_y *= -1
        for brick in diamonds_brick_hit_list:
            brick.remove_from_sprite_lists()
            self.score += 3
            arcade.play_sound(SOUND)

        self.clubs_brick_list.update()

        clubs_brick_hit_list = arcade.check_for_collision_with_list(self.ball_sprite, self.clubs_brick_list)
        if len(clubs_brick_hit_list):
            self.ball_sprite.change_y *= -1
        for brick in clubs_brick_hit_list:
            brick.remove_from_sprite_lists()
            self.score += 2
            arcade.play_sound(SOUND)

        self.blue_brick_list.update()

        blue_brick_hit_list = arcade.check_for_collision_with_list(self.ball_sprite, self.blue_brick_list)
        if len(blue_brick_hit_list):
            self.ball_sprite.change_y *= -1

        for brick in blue_brick_hit_list:
            brick.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(SOUND)


        self.player_list.update()

        player_hit_list = arcade.check_for_collision_with_list(self.ball_sprite, self.player_list)
        for player in player_hit_list:
            if self.ball_sprite.change_y < 0:
                self.ball_sprite.change_y *= -1



        wall_hit_list = arcade.check_for_collision_with_list(self.ball_sprite, self.wall_list)
        for wall in wall_hit_list:
            self.ball_sprite.change_x *= -1

        top_wall_hit_list = arcade.check_for_collision_with_list(self.ball_sprite, self.top_wall_list)
        for wall in top_wall_hit_list:
            self.ball_sprite.change_y *= -1

        if self.ball_sprite.center_y < 0:
            self.ball_on_paddle = True
            self.ball_sprite.change_y = 0
            self.ball_sprite.change_x = 0

        if self.ball_sprite.center_y <= 0:
            self.lives -= 1








def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()