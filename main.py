import time
import random

import pyRetroGame
from pyRetroGame.assets import *
from pyRetroGame.mathematics.vector import Vector2


class Background:
    def __str__(self):
        return TextAssets.FilledBlock


class Player(pyRetroGame.objects.gameEntity):
    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self) -> str:
        return TextAssets.BlankSpace


class Wall(pyRetroGame.objects.gameObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.solid = True

    def __str__(self):
        return "x"


game = pyRetroGame.game.Game(background=Background, size=Vector2(30, 30))
player = Player(Vector2(20, 3), game)
start = time.time()


@game.inputHandler(["w", "a", "s", "d"])
def movement(key):
    direction = Vector2(0, 0)
    if key == "s":
        direction.y += 1
    if key == "a":
        direction.x -= 1
    if key == "d":
        direction.x += 1

    player.move(direction)


@player.gameLimitCollisionHandler()
def colesion(side):
    if not side == "down":
        game.quit()

    game.printText(f"You win in {int(time.time() - start)} seconds")
    time.sleep(2)
    game.quit()
    

def main():
    for x in range(12):
        game.spawn(Wall(position=Vector2(11 + x, 4)))

    for _ in range(110):
        game.spawn(Wall(position=Vector2(
            random.randint(0, 28), 
            random.randint(6, 27)
        )))

    game.spawn(player)
    game.start(60)

if __name__ == "__main__":
    main()
