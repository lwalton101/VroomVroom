import pygame
from vroom.camera import Camera
from vroom.component import Component
from vroom.components.debug import Debug


class Circle(Component):
    def __init__(self, radius: int = 15, color: tuple[int, int, int] = (255, 255, 255)):
        super().__init__()
        self.radius: int = radius
        self.color: tuple[int, int, int] = color

    def Render(self, screen):
        super().Render(screen)
        rect: pygame.Rect = pygame.Rect(0, 0, self.radius, self.radius)
        rect.center = Camera.WorldPosToScreenPos(self.gameObject.pos)
        pygame.draw.circle(screen, self.color, rect.center, self.radius)

    def Update(self):
        super().Update()
        Debug.Push(f"Circle World Pos: {self.gameObject.pos}")
        Debug.Push(
            f"Circle Screen Pos: {Camera.WorldPosToScreenPos(self.gameObject.pos)}"
        )
