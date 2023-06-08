from Controller import Controller
from vroom.GameObject import GameObject
from vroom.Scene import Scene
from vroom.component.SpriteRenderer import SpriteRenderer

class Scene1(Scene):

    def __init__(self):
        super().__init__((255,0,0))

    def Start(self):
        super().Start()
        print("Starting Scene 1")

        go: GameObject = self.CreateGameObject("bedrock image")
        go.AddComponent(SpriteRenderer("bedrock.png"))
        go.AddComponent(Controller())

        go: GameObject = self.CreateGameObject("bedrock image 2")
        go.AddComponent(SpriteRenderer("grass.png"))
        go.pos = 100,100

    def Update(self):
        super().Update()

    def Exit(self):
        super().Exit()
        print("Exiting Scene 1")
        
