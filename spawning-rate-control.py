import arcade
import random
import math
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_RADIUS = 15
OBJECT_RADIUS = 10
NUM_OBJECTS = 10
MAX_SPEED = 1
SPAWN_DELAY = 2  # Adjust the spawn delay (in seconds) as needed
MAX_OBJECTS = 10

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)

        self.player_x = SCREEN_WIDTH // 2
        self.player_y = PLAYER_RADIUS + 10

        self.objects = []
        self.last_spawn_time = time.time()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.player_x, self.player_y, PLAYER_RADIUS, arcade.color.BLUE)

        for obj in self.objects:
            x, y = obj
            arcade.draw_circle_filled(x, y, OBJECT_RADIUS, arcade.color.RED)

    def update(self, delta_time):
        if time.time() - self.last_spawn_time > SPAWN_DELAY:
            if len(self.objects) < MAX_OBJECTS:
                self.objects.append((random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)))
                self.last_spawn_time = time.time()

        for i in range(len(self.objects)):
            x, y = self.objects[i]
            dx = self.player_x - x
            dy = self.player_y - y
            distance = math.sqrt(dx ** 2 + dy ** 2)

            if distance < PLAYER_RADIUS + OBJECT_RADIUS:
                # Collision occurred, handle it here
                self.objects.pop(i)
                self.objects.append((random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)))
            elif distance < 100:
                dx /= distance
                dy /= distance

                x += dx * 3
                y += dy * 3
                self.objects[i] = (x, y)





    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_x -= 15
        elif key == arcade.key.RIGHT:
            self.player_x += 15
        elif key == arcade.key.UP:
            self.player_y += 15
        elif key == arcade.key.DOWN:
            self.player_y -= 15

if __name__ == "__main__":
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
