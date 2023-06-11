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
    def __init__(self) -> None:
        super().__init__((255, 0, 0))

    def Start(self) -> None:
        super().Start()
        print("Starting Scene 1")

        debugObject: GameObject = self.CreateGameObject("Debug Manager")
        debugObject.AddComponent(Debug())
        debugObject.z_index = 999999999999

        bedrockObject: GameObject = self.CreateGameObject("Bedrock Square")
        bedrockObject.AddComponent(SpriteRenderer("bedrock"))
        bedrockObject.AddComponent(Controller())
        bedrockObject.z_index = 1

        circleObject: GameObject = self.CreateGameObject("Circle")
        circleObject.AddComponent(
            Circle(
                radius=random.randint(25, 50),
                color=(
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                ),
            )
        )
        circleObject.pos = (50, 50)
        circleObject.z_index = 2

        lineObject: GameObject = self.CreateGameObject("Line")
        lineObject.AddComponent(Line((-100, 0), (100, 0), (0, 255, 0)))
        lineObject.pos = 100, 50
        lineObject.static = True

        disabledLineObject: GameObject = self.CreateGameObject("Disabled Line")
        disabledLineObject.AddComponent(Line((-100, 0), (100, 0), (0, 255, 0)))
        disabledLineObject.pos = 0, 0
        disabledLineObject.enabled = False

    def Update(self) -> None:
        super().Update()

    def Exit(self):
        super().Exit()
        print("Exiting Scene 1")
