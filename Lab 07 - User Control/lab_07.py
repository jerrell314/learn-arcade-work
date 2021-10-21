""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
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

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


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
