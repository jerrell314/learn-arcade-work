""" Sprite Sample Program """
import math
import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.2
SPRITE_SCALING_CLARANET = 0.2
SPRITE_SCALING_KRABBY_PATTY = 0.2
CLARANET_COUNT = 50
KRABBY_PATTY_COUNT = 60

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class KRABBYPATTY(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.circle_angle = 0
        self.circle_radius = 0
        self.circle_speed = 0.008
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):
        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
                        + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
                        + self.circle_center_y
        self.circle_angle += self.circle_speed



class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        self.player_list = None
        self.claranet_list = None
        self.krabby_patty_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.SKY_BLUE)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.claranet_list = arcade.SpriteList()
        self.krabby_patty_list = arcade.SpriteList()
        self.score = 0
        # Squidward is from Elan Arad for WhatsApp
        self.player_sprite = arcade.Sprite("sticker_1.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(CLARANET_COUNT):
            # Claranet is from The Parody Wiki
            claranet = arcade.Sprite("Squidward%27s_Clarinet.png", SPRITE_SCALING_CLARANET)

            claranet.center_x = random.randrange(SCREEN_WIDTH)
            claranet.center_y = random.randrange(SCREEN_HEIGHT)
            self.claranet_list.append(claranet)

        for i in range(KRABBY_PATTY_COUNT):

            krabby_patty = KRABBYPATTY("Krabby_Patty_transparentpng.png", SPRITE_SCALING_KRABBY_PATTY)
            krabby_patty.circle_center_x = random.randrange(SCREEN_WIDTH)
            krabby_patty.circle_center_y = random.randrange(SCREEN_HEIGHT)
            krabby_patty.circle_radius = random.randrange(12, 200)
            krabby_patty.circle_angle = random.random() * 2 * math.pi
            self.krabby_patty_list.append(krabby_patty)




    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.claranet_list.draw()
        self.krabby_patty_list.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        self.claranet_list.update()
        self.krabby_patty_list.update()
        good_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.claranet_list)
        bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.krabby_patty_list)

        for claranet in good_hit_list:
            claranet.remove_from_sprite_lists()
            self.score += 1

        for krabby_patty in bad_hit_list:
            krabby_patty.remove_from_sprite_lists()
            self.score -= 1



def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()