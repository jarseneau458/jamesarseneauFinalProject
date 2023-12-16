import random

import ProjectHelper
import arcade
import time

WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 800



class FroggerGameWindow (arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "Frogger")
        self.player = None
        self.dx= 0
        self.dy = 0
        self.road_list_ = None
        self.road_2_list = None
        self.river_list = None
        self.river_list_2 = None
        self.cars = None
        self.cars_2 = None
        self.turtles = None
        self.turtles_2 = None
        self.ouch_sound = None
        self.move_sound = None
        self.win_sound = None
        self.lose = False
        self.lose_time = None
        #creates the variables




    def setup(self):
        self.player = arcade.Sprite(":resources:images/enemies/frog.png")
        self.player.center_x = 700
        self.player.center_y = 150
        self.ouch_sound = arcade.load_sound(":resources:sounds/hurt3.wav")
        self.move_sound = arcade.load_sound(":resources:sounds/jump4.wav")
        self.win_sound = arcade.load_sound(":resources:sounds/coin5.wav")
        self.cars = ProjectHelper.make_cars()
        self.cars_2 = ProjectHelper.make_cars_2()

        self.road_list = ProjectHelper.make_road()
        self.road_2_list = ProjectHelper.make_road_2()
        self.river_list = ProjectHelper.make_river()
        self.river_list_2 = ProjectHelper.make_river_2()
        self.turtles = ProjectHelper.make_turtles()
        self.turtles_2 = ProjectHelper.make_turtles_2()
        #sets up the variables

    def on_update(self,delta_time: float):
        if self.lose:

            return

        self.move_player()
        for car in self.cars:

            car.center_x -= 2
            if car.center_x <= 0:
                car.center_x = WINDOW_WIDTH + 63
        for car in self.cars_2:
            car.center_x += 2
            if car.center_x >= WINDOW_WIDTH:
                car.center_x = 63
                #moves cars, one set left, the other right
        self.car_collision()
        self.turtle_collision()
        #adds turtle and car collisons to on_update function


        for turtle in self.turtles:
            turtle.center_x -= 3
            if turtle.center_x <= 0:
                turtle.center_x = WINDOW_WIDTH
        for turtle in self.turtles_2:
            turtle.center_x += 3
            if turtle.center_x >= WINDOW_WIDTH:
                turtle.center_x = 64
            #moves turtles left and right
    def car_collision(self):
        if arcade.check_for_collision_with_list(self.player, self.cars):
            self.ouch = True
            arcade.play_sound(self.ouch_sound)

            self.player.center_y = 150
            self.lose = True
        elif arcade.check_for_collision_with_list(self.player, self.cars_2):

            self.ouch = True
            arcade.play_sound(self.ouch_sound)
            self.player.center_x = 700
            self.player.center_y = 150
            self.lose = True
            #checks for collison with frog and cars and plays lose sound and resets frog to starting point
    def turtle_collision(self):
        if arcade.check_for_collision_with_list(self.player, self.turtles):
            self.player.center_x -= 3
        elif arcade.check_for_collision_with_list(self.player, self.turtles_2):
            self.player.center_x += 3
        else:
            if self.player.center_y > 550 and self.player.center_y < 695 :

                self.ouch = True
                arcade.play_sound(self.ouch_sound)

                self.reset()
                self.lose = True
        #checks fro collison with turtles, if player collides with turtles, movement spped of turtle will be same as player
        # if player hits the water, lose sound will play and player will reset







    def reset(self):
        self.player.center_x = 700
        self.player.center_y = 150
        #resets player to starting point
    def move_player(self):
        self.player.center_y += self.dy
        self.player.center_x += self.dx





        if self.player.center_y >= WINDOW_HEIGHT:
            self.player.center_y = WINDOW_HEIGHT
            # prevents frog from moving off screen in regards to the height

        elif self.player.center_y <= 150:
            self.player.center_y = 150

        if self.player.center_x >= WINDOW_WIDTH:
            self.player.center_x = WINDOW_WIDTH
        elif self.player.center_x <= 0:
            self.player.center_x = 0
            # prevents frog from moving off screen in regards to the width
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.DOWN:
            self.dy= -2
        elif symbol == arcade.key.UP:
            self.dy = 2
        elif symbol == arcade.key.RIGHT:
            self.dx = 2
        elif symbol == arcade.key.LEFT:
            self.dx = -2
            #moves player with up down left and right keys


    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.DOWN or symbol == arcade.key.UP:
            self.dy = 0
            arcade.play_sound(self.move_sound)
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.dx = 0
            arcade.play_sound(self.move_sound)
            #stops frog when key is released, plays movement sound





    def on_draw(self):
        arcade.start_render()
        arcade.draw_xywh_rectangle_filled(0,0, WINDOW_WIDTH, WINDOW_HEIGHT,
                                          arcade.color.DARK_GREEN)
        #sets the background

        self.road_list.draw()
        self.road_2_list.draw()
        self.cars.draw()
        self.cars_2.draw()
        self.river_list.draw()
        self.river_list_2.draw()
        self.turtles.draw()
        self.turtles_2.draw()
        self.player.draw()
        #draws everything
        if self.player.center_y > 770:
            arcade.draw_text("You Win!", 200, 700, arcade.color.YELLOW, 100)
            arcade.play_sound(self.win_sound)
            #If the play makes it to the end, the text and win sound will play
        if self.lose:
            arcade.draw_text("You Lose", 200, 100, arcade.color.BLACK, 100)
            #if player loses, text will appear




        arcade.finish_render()