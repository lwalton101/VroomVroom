import pygame
from vroom.component import Component
from vroom.input_manager import InputManager


class Debug(Component):
    lines: list[str] = []

    def Start(self) -> None:
        # super().Start()
        self.font: pygame.font.Font = pygame.font.SysFont("comicsansms", 12)
        self.enabled: bool = False

    def Update(self):
        super().Update()
        Debug.lines = []
        if InputManager.IsKeyDown(pygame.K_BACKSPACE):
            self.enabled = not self.enabled

    def Render(self, screen: pygame.Surface):
        yPos = 0
        if self.enabled:
            for x in Debug.lines:
                screen.blit(self.font.render(x, True, (0, 0, 0)), (0, yPos))
                yPos += 15

    @staticmethod
    def Push(text: str):
        Debug.lines.append(text)
