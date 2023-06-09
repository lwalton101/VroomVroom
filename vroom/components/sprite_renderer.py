import pygame
from vroom.camera import Camera
from vroom.component import Component


class SpriteRenderer(Component):
    def __init__(self, assetName: str) -> None:
        super().__init__()
        self.img: pygame.Surface = pygame.image.load(assetName).convert_alpha()
        self.spareImg: pygame.Surface = self.img

    def Render(self, screen: pygame.Surface) -> None:
        """
        The Render function is called every frame.
        It takes the screen surface as an argument and blits the image to it.
        The image is rotated, scaled, and adjusted for camera offset before being blit.

        :param self: Access the class variables and methods
        :param screen: pygame.Surface: Draw the image on the screen
        :return: None, but the pygame
        :doc-author: Trelent
        """
        super().Render(screen)
        self.img = self.spareImg
        self.img = pygame.transform.rotozoom(
            self.img, self.gameObject.rotation, self.gameObject.scale
        )

        rect: pygame.Rect = self.img.get_rect()
        rect.center = self.gameObject.pos
        rect = Camera.AdjustRectForOffset(rect)

        screen.blit(self.img, rect)