"""This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""
# Import the "arcade" library
import arcade

# Open a window.
# From the "arcade" library use a function called "open_window"
# Set the dimensions (width and height)
# Set the window title to "Drawing Example"
arcade.open_window(600, 600, "Drawing Example")

# Set background color
arcade.set_background_color(arcade.color.ORANGE)

# Get ready to draw
arcade.start_render()

# Draw sun set
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


# Finish Drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()