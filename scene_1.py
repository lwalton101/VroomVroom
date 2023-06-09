from controller import Controller
from vroom.components.debug import Debug
from vroom.game_object import GameObject
from vroom.scene import Scene
from vroom.components.sprite_renderer import SpriteRenderer


class Scene1(Scene):
    def __init__(self):
        super().__init__((255, 0, 0))

    def Start(self):
        super().Start()
        print("Starting Scene 1")

        debugObject: GameObject = self.CreateGameObject("Debug Manager")
        debugObject.AddComponent(Debug())

        go: GameObject = self.CreateGameObject("rotate")
        go.AddComponent(SpriteRenderer("bedrock.png"))
        go.AddComponent(Controller())

    def Update(self):
        super().Update()

    def Exit(self):
        super().Exit()
        print("Exiting Scene 1")
