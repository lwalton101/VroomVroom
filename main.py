from vroom.Game import Game
from Scene1 import Scene1
import pygame
from vroom.InputManager import InputManager

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FRAME_RATE = 60
TITLE = "Basic Window"

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, FRAME_RATE, TITLE, Scene1())

while game.running:
    game.loop()

    if InputManager.IsKeyDown(pygame.K_SPACE):
        game.SetScene(Scene1())

game.quit()

