import pygame
from InputManager import InputManager

class Game:

    VERSION = 0.1
    def __init__(self, screenWidth: int, screenHeight: int, frameRate: int, title:str):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.frameRate = frameRate
        self.title = title

        self.inputManger = InputManager()
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode((screenWidth, screenHeight))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

        print(f"Game made with VroomVroom version {self.VERSION}")

    def loop(self) -> None:
        self.clock.tick(self.frameRate)
        self.inputManger.update()
        for event in pygame.event.get():       
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.inputManger.handleKeydownEvent(event.key)
            if event.type == pygame.KEYUP:
                self.inputManger.handleKeyupEvent(event.key)

        print(self.inputManger.IsKeyPressed(pygame.K_SPACE))
        self.screen.fill((255,255,255))
        pygame.display.flip()

    def quit(self) -> None:
        pygame.quit()