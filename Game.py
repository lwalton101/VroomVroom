import pygame

class Game():

    VERSION = 0.1

    def __init__(self, screenWidth: int, screenHeight: int, frameRate: int, title:str) -> None:
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.frameRate = frameRate
        self.title = title

        self.running = True

        pygame.init()
        self.screen = pygame.display.set_mode((screenWidth, screenHeight))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

        print(f"Game made with VroomVroom version {self.VERSION}")
        pass

    def loop(self) -> None:
        self.clock.tick(self.frameRate)

        for event in pygame.event.get():       
            if event.type == pygame.QUIT:
                self.running = False

        self.screen.fill((255,255,255))
        pygame.display.flip()

    def quit(self):
        pygame.quit()