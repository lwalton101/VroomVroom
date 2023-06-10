from vroom.camera import Camera
from vroom.game import Game
from scene_1 import Scene1
import pygame, tkinter
from vroom.input_manager import InputManager

root = tkinter.Tk()

SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()
FRAME_RATE = 60
TITLE = "Bananas Beans"


game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, FRAME_RATE, TITLE, Scene1())

while game.running:
    game.loop()

    if InputManager.IsKeyDown(pygame.K_SPACE):
        game.SetScene(Scene1())

game.quit()
