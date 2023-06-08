import pygame
from vroom.GameObject import GameObject
from uuid import UUID

class Scene:
    def __init__(self, color: tuple[int,int,int]):
        self.color: tuple[int,int,int] = color
        self.gameObjects: dict[UUID,GameObject] = {}
        pass

    def Start(self):
        pass

    def Update(self):
        for uuid in self.gameObjects:
            self.gameObjects[uuid].Update()

    def Exit(self):
        pass

    def Render(self, screen: pygame.Surface):
        screen.fill(self.color)
        for uuid in self.gameObjects:
            self.gameObjects[uuid].Render(screen)

    def AddGameObject(self, gameobject: GameObject) -> None:
        self.gameObjects[gameobject.id] = (gameobject)

    def CreateGameObject(self, name: str, xPos: int = 0, yPos: int = 0) -> GameObject:
        go: GameObject = GameObject(name, xPos, yPos)
        self.AddGameObject(go)
        return go
    
    def GetGameObject(self, name:str) -> GameObject | None:
        for uuid in self.gameObjects:
            go: GameObject = self.gameObjects[uuid]
            if go.name == name:
                return go
            
        return None
