import arcade
import random

WINDOW_WIDTH = 1400

def make_road():
    road_list = arcade.SpriteList()

    for xLoc in range(0, WINDOW_WIDTH):
        road_tile = arcade.Sprite(":resources:images/tiles/dirtCenter.png")
        road_tile.center_y = 300
        road_tile.center_x = xLoc
        road_list.append(road_tile)
    return road_list
#makes 1st road

def make_road_2():
    road_2_list = arcade.SpriteList()

    for xLoc in range(0, WINDOW_WIDTH):

        road_tile_2 = arcade.Sprite(":resources:images/tiles/dirtCenter.png")
        road_tile_2.center_y = 236
        road_tile_2.center_x = xLoc
        road_2_list.append(road_tile_2)
    return road_2_list
#makes 2nd road


def make_river():
    river_list = arcade.SpriteList()

    for xLoc in range(0,WINDOW_WIDTH):
        river_tile = arcade.Sprite(":resources:images/tiles/waterTop_low.png")
        river_tile.center_y = 600
        river_tile.center_x = xLoc
        river_list.append(river_tile)
    return river_list
#makes first river

def make_river_2():
    river_list_2 = arcade.SpriteList()

    for xLoc in range(0, WINDOW_WIDTH):
        river_tile_2 = arcade.Sprite(":resources:images/tiles/waterTop_low.png")
        river_tile_2.center_y = 690
        river_tile_2.center_x = xLoc
        river_list_2.append(river_tile_2)
    return river_list_2
#makes 2nd river

def make_cars():
    car_sprite_list = arcade.SpriteList()
    distance = 100
    for car_number in range(3):
        car_sprite = arcade.Sprite("car.png",-0.5)
        car_sprite.center_y = 330
        car_sprite.center_x = random.randint(0, WINDOW_WIDTH)
        car_overlap = arcade.check_for_collision_with_list(car_sprite, car_sprite_list)
        if car_overlap:
            distance = distance + 100
            car_sprite.center_x = random.randint(0, 150)+ distance
            #creates cars going to the left, if overlap happens, car will move to a new position

        else:
            car_sprite_list.append(car_sprite)
    return car_sprite_list

def make_cars_2():
    car_sprite_list_2 = arcade.SpriteList()
    distance = 100
    for car_number in range(3):
        car_sprite = arcade.Sprite("car.png",0.5)
        car_sprite.center_y = 230
        car_sprite.center_x = random.randint(0, WINDOW_WIDTH)
        car_overlap = arcade.check_for_collision_with_list(car_sprite, car_sprite_list_2)
        if car_overlap:
            distance = distance + 100
            car_sprite.center_x = random.randint(0, 150)+ distance

        else:
            car_sprite_list_2.append(car_sprite)
    return car_sprite_list_2
#creates cars going to the right, if overlap happens, car will move to a new position




def make_turtles():
    turtle_sprite_list = arcade.SpriteList()
    distance = 100
    for turtle_number in range(4):
        turtle_sprite = arcade.Sprite(":resources:images/enemies/slimeBlock.png",)
        turtle_sprite.center_y= 600
        turtle_sprite.center_x = random.randint(0, WINDOW_WIDTH)
        turtle_overlap = arcade.check_for_collision_with_list(turtle_sprite, turtle_sprite_list)
        if turtle_overlap:
            distance = distance + 100
            turtle_sprite.center_x = random.randint(0, 150)+distance


        else:
            turtle_sprite_list.append(turtle_sprite)
    return turtle_sprite_list
#creates turtles going to the right, if overlap happens, turtle will move to a new position
def make_turtles_2():
    turtle_sprite_list_2 = arcade.SpriteList()
    distance = 100
    for turtle_number_2 in range(3):
        turtle_sprite_2 = arcade.Sprite(":resources:images/enemies/slimeBlock.png",) #turtle sprite
        turtle_sprite_2.center_y= 690
        turtle_sprite_2.center_x = random.randint(0, WINDOW_WIDTH)
        turtle_overlap = arcade.check_for_collision_with_list(turtle_sprite_2, turtle_sprite_list_2)
        if turtle_overlap:
            distance = distance + 100
            turtle_sprite_2.center_x = random.randint(0, 150)+distance

        else:
            turtle_sprite_list_2.append(turtle_sprite_2)
    return turtle_sprite_list_2
#creates turtles going to the left , if overlap happens, turtle will move to a new position









