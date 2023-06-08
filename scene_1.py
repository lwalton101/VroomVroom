from controller import Controller
from vroom.game_object import GameObject
from vroom.scene import Scene
from vroom.components.sprite_renderer import SpriteRenderer


class Scene1(Scene):
    def __init__(self):
        super().__init__((255, 0, 0))

    def Start(self):
        super().Start()
        print("Starting Scene 1")

        go: GameObject = self.CreateGameObject("rotate")
        go.AddComponent(SpriteRenderer("bedrock.png"))
        go.AddComponent(Controller())

        go: GameObject = self.CreateGameObject("")
        go.AddComponent(SpriteRenderer("grass.png"))
        go.pos = 100, 100

    def Update(self):
        super().Update()

    def Exit(self):
        super().Exit()
        print("Exiting Scene 1")
