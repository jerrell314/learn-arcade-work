"""This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""
# Import the "arcade" library
import arcade
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
def draw_grass():
    """ Draw grass with STL design"""
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 2.4, 0, arcade.color.APPLE_GREEN)
    arcade.draw_text("S T L",
                     150, 100,
                     arcade.color.GREEN_YELLOW, 100)

def draw_sun_set(x,y):
    """ Draw sun set"""
    arcade.draw_lrtb_rectangle_filled(0, 600, 550 + x, 450 + y, arcade.color.ORANGE_PEEL)
    arcade.draw_lrtb_rectangle_filled(0, 600, 450 + x, 400 + y, arcade.color.DARK_ORANGE)
    arcade.draw_lrtb_rectangle_filled(0, 600, 400 + x, 340 + y, arcade.color.PUMPKIN)
    arcade.draw_lrtb_rectangle_filled(0, 600, 340 + x, 150 + y, arcade.color.ORANGE_RED)


def draw_arch(x,y):
    """ Draw arch with sunset"""
    arcade.draw_arc_filled(300, 250, 400 + x, 600 + y, arcade.color.DARK_GRAY, 0, 180)
    arcade.draw_arc_filled(300, 250, 350 + x, 550 + y, arcade.color.ORANGE_PEEL, 0, 180)
    arcade.draw_arc_filled(300, 250, 350 + x, 450 + y, arcade.color.DARK_ORANGE, 0, 180)
    arcade.draw_arc_filled(300, 250, 350 + x, 400 + y, arcade.color.PUMPKIN, 0, 180)
    arcade.draw_arc_filled(300, 250, 350 + x, 350 + y, arcade.color.ORANGE_RED, 0, 180)

def draw_buildings():
    """ Draw buildings with windows"""
    arcade.draw_lrtb_rectangle_filled(0, 50, 400, 250, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(50, 80, 350, 250, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(550, 600, 400, 250, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(520, 550, 350, 250, arcade.color.BLACK)

# def draw_windows(x, y):
#     """ Draw windows"""
#     arcade.draw_lrtb_rectangle_filled(10, 20, 390 - x, 380 - y, arcade.color.WHITE)
#     arcade.draw_lrtb_rectangle_filled(30, 40, 390 - x, 380 - y, arcade.color.WHITE)
#     arcade.draw_lrtb_rectangle_filled(60, 70, 340 - x, 330 - y, arcade.color.WHITE)
#     arcade.draw_lrtb_rectangle_filled(580, 590, 390 - x, 380 - y, arcade.color.WHITE)
#     arcade.draw_lrtb_rectangle_filled(560, 570, 390 - x, 380 - y, arcade.color.WHITE)
#     arcade.draw_lrtb_rectangle_filled(530, 540, 340 - x, 330 - y, arcade.color.WHITE)
def draw_windows(x, y):
    arcade.draw_rectangle_filled(x, y, 10, 10, arcade.color.WHITE)
    arcade.draw_rectangle_filled(x, y - 20, 10, 10, arcade.color.WHITE)
def draw_sun(x,y):
    arcade.draw_circle_filled(300, 400 - x, 50 + y, arcade.color.SAE)
def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with functions")
    arcade.set_background_color(arcade.color.ORANGE)
    arcade.start_render()

    draw_sun_set(30, 30)

    draw_arch(100, 70)

    draw_buildings()



    draw_sun(50, 60)

    draw_grass()
    draw_windows(10, 380)
    draw_windows(340, 50)
    draw_windows(590, 380)

    # Finish and run
    arcade.finish_render()
    arcade.run()

# Call the main function to get the program started.
main()