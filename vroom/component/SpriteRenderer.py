import pygame
from vroom.Camera import Camera
from vroom.Component import Component

class SpriteRenderer(Component):
    
    def __init__(self, assetName: str) -> None:
        super().__init__()
        self.img: pygame.Surface = pygame.image.load(assetName).convert()

    def Render(self, screen: pygame.Surface) -> None:
        super().Render(screen)
        rect: pygame.Rect = self.img.get_rect()
        rect.center = self.gameObject.pos
        rect = Camera.AdjustRectForOffset(rect)
        
        screen.blit(self.img, rect)

    def Update(self):
        super().Update()
