from vroom.GameObject import GameObject
from uuid import UUID

class Scene:

    gameObjects: dict[UUID,GameObject] = {}
    
    def __init__(self):
        pass

    def Start(self):
        pass

    def Update(self):
        for uuid in self.gameObjects:
            self.gameObjects[uuid].Update()

    def Exit(self):
        pass

    def Render(self):
        for uuid in self.gameObjects:
            self.gameObjects[uuid].Render()

    def AddGameObject(self, gameobject: GameObject) -> None:
        self.gameObjects[gameobject.id] = (gameobject)

    def CreateGameObject(self, name: str) -> GameObject:
        go: GameObject = GameObject(name)
        self.AddGameObject(go)
        return go
    
    def GetGameObject(self, name:str) -> GameObject | None:
        for uuid in self.gameObjects:
            go: GameObject = self.gameObjects[uuid]
            if go.name == name:
                return go
            
        return None
