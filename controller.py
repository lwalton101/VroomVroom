import pygame
from vroom.camera import Camera
from vroom.component import Component
from vroom.input_manager import InputManager


class Controller(Component):
    def Update(self) -> None:
        super().Update()
        if InputManager.IsKeyPressed(pygame.K_w):
            self.gameObject.pos = self.gameObject.pos[0], self.gameObject.pos[1] + 1
        if InputManager.IsKeyPressed(pygame.K_a):
            self.gameObject.pos = self.gameObject.pos[0] - 1, self.gameObject.pos[1]
        if InputManager.IsKeyPressed(pygame.K_s):
            self.gameObject.pos = self.gameObject.pos[0], self.gameObject.pos[1] - 1
        if InputManager.IsKeyPressed(pygame.K_d):
            self.gameObject.pos = self.gameObject.pos[0] + 1, self.gameObject.pos[1]

        Camera.offset = self.gameObject.pos