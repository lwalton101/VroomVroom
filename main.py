from Game import Game

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FRAME_RATE = 60
TITLE = "Basic Window"

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, FRAME_RATE, TITLE)

while game.running:
    game.loop()

game.quit()

