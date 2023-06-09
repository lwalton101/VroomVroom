import pygame
from vroom.camera import Camera
from vroom.component import Component
from vroom.components.debug import Debug


class SpriteRenderer(Component):
    def __init__(self, assetName: str, alpha: bool = False) -> None:
        super().__init__()
        if alpha:
            self.img: pygame.Surface = pygame.image.load(assetName).convert_alpha()
        else:
            self.img: pygame.Surface = pygame.image.load(assetName).convert()

        self.spareImg: pygame.Surface = self.img

    def Render(self, screen: pygame.Surface) -> None:
        super().Render(screen)
        self.img = self.spareImg

        if self.gameObject.rotation != 0 or self.gameObject.scale != 1:
            self.img = pygame.transform.rotozoom(
                self.img, self.gameObject.rotation, self.gameObject.scale
            )

        rect: pygame.Rect = self.img.get_rect()
        rect.center = self.gameObject.pos
        rect = Camera.AdjustRectForOffset(rect)
        screen.blit(self.img, rect)

    def Update(self) -> None:
        super().Update()
