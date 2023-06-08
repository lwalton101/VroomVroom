from vroom.GameObject import GameObject

class Scene:

    gameObjects: list[GameObject] = []
    
    def __init__(self):
        pass

    def Start(self):
        pass

    def Update(self):
        for gameObject in self.gameObjects:
            gameObject.Update()

    def Exit(self):
        pass

    def Render(self):
        pass

    def AddGameObject(self, gameobject: GameObject) -> None:
        self.gameObjects.append(gameobject)

    def CreateGameObject(self, name: str) -> GameObject:
        go: GameObject = GameObject(name)
        self.gameObjects.append(go)
        return go