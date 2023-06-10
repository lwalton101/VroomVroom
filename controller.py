import pygame
from vroom.AudioManager import AudioManager
from vroom.camera import Camera
from vroom.component import Component
from vroom.input_manager import InputManager
from vroom.time import Time


class Controller(Component):
    def Start(self):
        super().Start()
        self.speed: float = 0.5

    def Update(self) -> None:
        super().Update()
        if InputManager.IsKeyPressed(pygame.K_w):
            self.gameObject.pos = (
                self.gameObject.pos[0],
                self.gameObject.pos[1] + (self.speed * Time.dt),
            )
        if InputManager.IsKeyPressed(pygame.K_a):
            self.gameObject.pos = (
                self.gameObject.pos[0] - (self.speed * Time.dt),
                self.gameObject.pos[1],
            )
        if InputManager.IsKeyPressed(pygame.K_s):
            self.gameObject.pos = (
                self.gameObject.pos[0],
                self.gameObject.pos[1] - (self.speed * Time.dt),
            )
        if InputManager.IsKeyPressed(pygame.K_d):
            self.gameObject.pos = (
                self.gameObject.pos[0] + (self.speed * Time.dt),
                self.gameObject.pos[1],
            )

        if InputManager.IsKeyDown(pygame.K_o):
            AudioManager.PlaySound("test", "vine_om")

        Camera.offset = self.gameObject.pos
