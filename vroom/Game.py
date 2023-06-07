import pygame
from vroom.InputManager import InputManager
from vroom.Scene import Scene

class Game:

    VERSION = 0.1
    def __init__(self, screenWidth: int, screenHeight: int, frameRate: int, title:str, mainScene: Scene):
        print(f"Game made with VroomVroom version {self.VERSION}")
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.frameRate = frameRate
        self.title = title
        self.currentScene = mainScene

        self.inputManger = InputManager()
        self.running = True

        pygame.init()
        self.screen = pygame.display.set_mode((screenWidth, screenHeight))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

        self.currentScene.Start()

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

        self.currentScene.Render()
        self.screen.fill((255,255,255))
        pygame.display.flip()

    def quit(self) -> None:
        pygame.quit()

    def SetScene(self, scene: Scene):
        self.currentScene.Exit()
        self.currentScene = scene
        self.currentScene.Start()
