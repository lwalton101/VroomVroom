from controller import Controller
from vroom.components.debug import Debug
from vroom.game_object import GameObject
from vroom.scene import Scene
from vroom.components.sprite_renderer import SpriteRenderer
import random


class Scene1(Scene):
    def __init__(self):
        super().__init__((255, 0, 0))

    def Start(self):
        super().Start()
        print("Starting Scene 1")

        debugObject: GameObject = self.CreateGameObject("Debug Manager")
        debugObject.AddComponent(Debug())

        go: GameObject = self.CreateGameObject("Bedrock Square")
        go.AddComponent(SpriteRenderer("bedrock.png"))
        go.AddComponent(Controller())

        for x in range(100):
            go: GameObject = self.CreateGameObject(str(x))
            go.AddComponent(SpriteRenderer("bedrock.png"))
            go.pos = (random.randint(-250,250), random.randint(-250,250))

    def Update(self):
        super().Update()

    def Exit(self):
        super().Exit()
        print("Exiting Scene 1")
