"""This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""
# Import the "arcade" library
import arcade
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def draw_grass():
    """ Draw grass"""
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 2.4, 0, arcade.color.APPLE_GREEN)


def draw_st_louis_logo(x, y):
    """Draw a point at x, y fo reference"""
    arcade.draw_point(x, y, arcade.color.RED, 5)
    """Draw STL logo"""
    arcade.draw_text("S T L",
                     x, y,
                     arcade.color.GREEN_YELLOW, 100)


def draw_sun_set():
    """ Draw sun set"""
    arcade.draw_lrtb_rectangle_filled(0, 600, 550, 450, arcade.color.ORANGE_PEEL)
    arcade.draw_lrtb_rectangle_filled(0, 600, 450, 400, arcade.color.DARK_ORANGE)
    arcade.draw_lrtb_rectangle_filled(0, 600, 400, 340, arcade.color.PUMPKIN)
    arcade.draw_lrtb_rectangle_filled(0, 600, 340, 150, arcade.color.ORANGE_RED)

def draw_arch():
    """ Draw arch with sunset"""
    arcade.draw_arc_filled(300, 250, 400, 600, arcade.color.DARK_GRAY, 0, 180)
    arcade.draw_arc_filled(300, 250, 350, 550, arcade.color.ORANGE_PEEL, 0, 180)
    arcade.draw_arc_filled(300, 250, 350, 450, arcade.color.DARK_ORANGE, 0, 180)
    arcade.draw_arc_filled(300, 250, 350, 400, arcade.color.PUMPKIN, 0, 180)
    arcade.draw_arc_filled(300, 250, 350, 350, arcade.color.ORANGE_RED, 0, 180)


def draw_buildings():
    """ Draw buildings with windows"""
    arcade.draw_lrtb_rectangle_filled(0, 50, 400, 250, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(50, 80, 350, 250, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(550, 600, 400, 250, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(520, 550, 350, 250, arcade.color.BLACK)


def draw_windows(x, y):
    """Draw a point at x, y fo reference"""
    arcade.draw_point(x, y, arcade.color.RED, 5)
    """ Draw windows"""
    arcade.draw_rectangle_filled(x, y, 10, 10, arcade.color.WHITE)
    arcade.draw_rectangle_filled(x, y - 20, 10, 10, arcade.color.WHITE)


def draw_sun(x, y):
    """Draw a point at x, y fo reference"""
    arcade.draw_point(x, y, arcade.color.BLUE, 5)
    "Draw sun"
    """Rise and lower sun with sunset"""
    arcade.draw_circle_filled(x, y, 100, arcade.color.SAE)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with functions")
    arcade.set_background_color(arcade.color.ORANGE)
    arcade.start_render()

    draw_sun_set()

    draw_arch()

    draw_buildings()

    draw_sun(300, 400)

    draw_grass()

    draw_st_louis_logo(100, 100)

    draw_windows(10, 380)
    draw_windows(30, 380)
    draw_windows(590, 380)
    draw_windows(570, 380)
    draw_windows(540, 340)
    draw_windows(70, 340)

    # Finish and run
    arcade.finish_render()
    arcade.run()

# Call the main function to get the program started.
main()