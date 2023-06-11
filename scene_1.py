from controller import Controller
from vroom.components.circle import Circle
from vroom.components.debug import Debug
from vroom.components.line import Line
from vroom.components.rectangle import Rectangle
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
        go.AddComponent(SpriteRenderer("bedrock"))
        go.AddComponent(Controller())
        go.z_index = 5

        go: GameObject = self.CreateGameObject(str("x"))
        go.AddComponent(
            Circle(
                radius=random.randint(1, 25),
                color=(
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                ),
            )
        )
        go.pos = (0, 0)

        lineObject: GameObject = self.CreateGameObject("Line")
        lineObject.AddComponent(Line((-100, 0), (100, 0), (0, 255, 0)))
        lineObject.pos = 100, 50

        lineObject: GameObject = self.CreateGameObject("Line2")
        lineObject.AddComponent(Line((-100, 0), (100, 0), (0, 255, 0)))
        lineObject.pos = 0, 0

    def Update(self):
        super().Update()

    def Exit(self):
        super().Exit()
        print("Exiting Scene 1")
