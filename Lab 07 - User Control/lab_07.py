""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


class Bird:
    def __init__(self, position_x, position_y, radius, color):

        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)


class Ball:

    def __init__(self, position_x, position_y, change_y, change_x, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_y = change_y
        self.change_x = change_x
        self.radius = radius
        self.color = color
        self.hit_wall_sound = arcade.load_sound(":resources:sounds/fall2.wav")

    def draw(self):
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius
            arcade.play_sound(self.hit_wall_sound)

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            arcade.play_sound(self.hit_wall_sound)

        if self.position_y < self.radius:
            self.position_y = self.radius
            arcade.play_sound(self.hit_wall_sound)

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            arcade.play_sound(self.hit_wall_sound)



class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.bird = Bird(50, 50, 15, arcade.color.RED)
        self.set_mouse_visible(False)
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.RED)

    def update(self, delta_time: float):
        self.ball.update()

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.ORANGE)

        arcade.draw_lrtb_rectangle_filled(0, 600, 550, 450, arcade.color.ORANGE_PEEL)
        arcade.draw_lrtb_rectangle_filled(0, 600, 450, 400, arcade.color.DARK_ORANGE)
        arcade.draw_lrtb_rectangle_filled(0, 600, 400, 340, arcade.color.PUMPKIN)
        arcade.draw_lrtb_rectangle_filled(0, 600, 340, 150, arcade.color.ORANGE_RED)

        # Draw the grass with STL design
        arcade.draw_lrtb_rectangle_filled(0, 600, 250, 0, arcade.color.APPLE_GREEN)
        arcade.draw_text("S T L",
                         150, 100,
                         arcade.color.GREEN_YELLOW, 100)

        # Draw the arch
        arcade.draw_arc_filled(300, 250, 400, 600, arcade.color.DARK_GRAY, 0, 180)
        arcade.draw_arc_filled(300, 250, 350, 550, arcade.color.ORANGE_PEEL, 0, 180)
        arcade.draw_arc_filled(300, 250, 350, 450, arcade.color.DARK_ORANGE, 0, 180)
        arcade.draw_arc_filled(300, 250, 350, 400, arcade.color.PUMPKIN, 0, 180)
        arcade.draw_arc_filled(300, 250, 350, 350, arcade.color.ORANGE_RED, 0, 180)

        # Draw buildings with windows
        arcade.draw_lrtb_rectangle_filled(0, 50, 400, 250, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(10, 20, 390, 380, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(10, 20, 370, 360, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(10, 20, 350, 340, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(30, 40, 390, 380, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(30, 40, 370, 360, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(30, 40, 350, 340, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(50, 80, 350, 250, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(60, 70, 340, 330, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(60, 70, 320, 310, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(550, 600, 400, 250, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(580, 590, 390, 380, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(580, 590, 370, 360, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(580, 590, 350, 340, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(560, 570, 390, 380, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(560, 570, 370, 360, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(560, 570, 350, 340, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(520, 550, 350, 250, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(530, 540, 340, 330, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(530, 540, 320, 310, arcade.color.WHITE)

        # Draw the sun
        arcade.draw_arc_filled(300, 250, 200, 200, arcade.color.SAE, 0, 180)

        self.bird.draw()
        self.ball.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.bird.position_x = x
        self.bird.position_y = y

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED


    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0


def main():
    window = MyGame()
    arcade.run()


main()
