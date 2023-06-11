import pygame
from util.MathUtil import MathUtil
from vroom.camera import Camera
from vroom.component import Component
from vroom.resource_manager import ResourceManager


class SpriteRenderer(Component):
    def __init__(self, assetName: str) -> None:
        super().__init__()
        self.img: pygame.Surface = ResourceManager.getSprite(assetName)
        self.spareImg: pygame.Surface = self.img

    def Render(self, screen: pygame.Surface) -> None:
        super().Render(screen)
        self.img = self.spareImg

        if self.gameObject.rotation != 0 or self.gameObject.scale != 1:
            self.img = pygame.transform.rotozoom(
                self.img, self.gameObject.rotation, self.gameObject.scale
            )

        rect: pygame.Rect = self.img.get_rect()
        if self.gameObject.static:
            rect.center = MathUtil.RoundFloatPosToIntPos(self.gameObject.pos)
        else:
            rect.center = Camera.WorldPosToScreenPos(self.gameObject.pos)
        screen.blit(self.img, rect)

    def Update(self) -> None:
        super().Update()
