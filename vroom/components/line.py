import pygame
from vroom.camera import Camera
from vroom.component import Component


class Line(Component):
    def __init__(
        self,
        startPoint: tuple[float, float],
        endPoint: tuple[float, float],
        color: tuple[int, int, int],
        width: int = 5,
    ):
        super().__init__()
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.color = color
        self.width = width

    def Start(self):
        super().Start()

    def Render(self, screen):
        super().Render(screen)
        screenStartPos = (
            self.startPoint[0] + self.gameObject.pos[0],
            self.startPoint[1] + self.gameObject.pos[1],
        )

        screenEndPos = (
            self.endPoint[0] + self.gameObject.pos[0],
            self.endPoint[1] + self.gameObject.pos[1],
        )

        if not self.gameObject.static:
            screenStartPos = Camera.WorldPosToScreenPos(screenStartPos)
            screenEndPos = Camera.WorldPosToScreenPos(screenEndPos)

        pygame.draw.line(
            screen,
            self.color,
            screenStartPos,
            screenEndPos,
            self.width,
        )

    def OnEnable(self):
        super().OnEnable()
        print("Enabled crimes")
