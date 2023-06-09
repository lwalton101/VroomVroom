import pygame
from vroom.component import Component


class Debug(Component):
    lines: list[str] = []

    def Start(self) -> None:
        # super().Start()
        self.font: pygame.font.Font = pygame.font.SysFont("comicsansms", 12)
        print("font init")

    def Update(self):
        super().Update()
        Debug.lines = []

    def Render(self, screen: pygame.Surface):
        index = 0
        for x in Debug.lines:
            screen.blit(self.font.render(x, True, (0, 0, 0)), (0, 0))
            pass

    @staticmethod
    def Push(text: str):
        Debug.lines.append(text)
