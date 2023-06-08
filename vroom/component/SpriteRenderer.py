import pygame
from vroom.Camera import Camera
from vroom.Component import Component

class SpriteRenderer(Component):
    
    def __init__(self, assetName: str) -> None:
        super().__init__()
        self.img: pygame.Surface = pygame.image.load(assetName).convert_alpha()
        self.spareImg: pygame.Surface = self.img

    def Render(self, screen: pygame.Surface) -> None:
        super().Render(screen)
        self.img = self.spareImg
        self.img = pygame.transform.rotozoom(self.img, self.gameObject.rotation ,self.gameObject.scale)

        rect: pygame.Rect = self.img.get_rect()
        rect.center = self.gameObject.pos
        rect = Camera.AdjustRectForOffset(rect)
        
        screen.blit(self.img, rect)

    def Update(self):
        super().Update()
