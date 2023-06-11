import pygame
from util.MathUtil import MathUtil
from vroom.camera import Camera
from vroom.component import Component


class Rectangle(Component):
    def __init__(
        self,
        width: int = 20,
        height: int = 20,
        color: tuple[int, int, int] = (255, 255, 255),
    ):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color

    def Render(self, screen):
        super().Render(screen)
        rect: pygame.Rect = pygame.Rect(0, 0, self.width, self.height)
        if self.gameObject.static:
            rect.center = MathUtil.RoundFloatPosToIntPos(self.gameObject.pos)
        else:
            rect.center = Camera.WorldPosToScreenPos(self.gameObject.pos)
        pygame.draw.rect(screen, self.color, rect)
