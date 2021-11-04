""" Sprite Sample Program """
import math
import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.2
SPRITE_SCALING_CLARINET = 0.2
SPRITE_SCALING_KRABBY_PATTY = 0.2
CLARINET_COUNT = 50
KRABBY_PATTY_COUNT = 25
CLARINET_COLLECT = arcade.load_sound("coin4.wav")
KRABBY_PATTY_COLLECT = arcade.load_sound("error1.wav")
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Krabbypatty(arcade.Sprite):
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


class Clarinet(arcade.Sprite):
    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.center_y -= 1
        if self.top < 0:
            self.reset_pos()



class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        self.player_list = None
        self.clarinet_list = None
        self.krabby_patty_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.SKY_BLUE)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.clarinet_list = arcade.SpriteList()
        self.krabby_patty_list = arcade.SpriteList()
        self.score = 0
        # Squidward is from Elan Arad for WhatsApp
        self.player_sprite = arcade.Sprite("sticker_1.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(CLARINET_COUNT):
            # Clarinet is from The Parody Wiki
            clarinet = Clarinet("Squidward%27s_Clarinet.png", SPRITE_SCALING_CLARINET)


            clarinet.center_x = random.randrange(SCREEN_WIDTH)
            clarinet.center_y = random.randrange(SCREEN_HEIGHT)
            self.clarinet_list.append(clarinet)

        for i in range(KRABBY_PATTY_COUNT):

            krabby_patty = Krabbypatty("Krabby_Patty_transparentpng.png", SPRITE_SCALING_KRABBY_PATTY)
            krabby_patty.circle_center_x = random.randrange(SCREEN_WIDTH)
            krabby_patty.circle_center_y = random.randrange(SCREEN_HEIGHT)
            krabby_patty.circle_radius = random.randrange(12, 200)
            krabby_patty.circle_angle = random.random() * 2 * math.pi
            self.krabby_patty_list.append(krabby_patty)




    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.clarinet_list.draw()
        self.krabby_patty_list.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        if len(self.krabby_patty_list) == 0:
            game = "GAME OVER"
            arcade.draw_text(game, 325, 300, arcade.color.WHITE, 20)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        if len(self.krabby_patty_list) > 0:
            self.krabby_patty_list.update()
            self.clarinet_list.update()
            good_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.clarinet_list)
            bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.krabby_patty_list)

            for clarinet in good_hit_list:
                clarinet.remove_from_sprite_lists()
                clarinet.reset_pos()
                self.score += 1
                arcade.play_sound(CLARINET_COLLECT)


            for krabby_patty in bad_hit_list:
                krabby_patty.remove_from_sprite_lists()
                self.score -= 1
                arcade.play_sound(KRABBY_PATTY_COLLECT)



def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()