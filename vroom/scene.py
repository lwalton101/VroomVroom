import pygame
from vroom.camera import Camera
from vroom.components.debug import Debug
from vroom.game_object import GameObject
from uuid import UUID


class Scene:
    def __init__(self, color: tuple[int, int, int]):
        self.color: tuple[int, int, int] = color
        self.gameObjects: dict[UUID, GameObject] = {}

    def Start(self):
        Camera.offset = (0, 0)
        pass

    def Update(self):
        """
        The Update function is called every frame.
        It calls the Update function of each game object in the scene.

        :param self: Represent the instance of the class
        :return: Nothing
        :doc-author: Trelent
        """
        for go in self.gameObjects.values():
            if go.enabled:
                go.Update()

    def Exit(self):
        pass

    def Render(self, screen: pygame.Surface):
        """
        The Render function is responsible for drawing the game objects to the screen.
        It does this by first filling the screen with a color, then iterating through all of
        the game objects and calling their Render function.

        :param self: Refer to the object itself
        :param screen: pygame.Surface: Draw the game objects on the screen
        :return: The screen
        :doc-author: Trelent
        """
        screen.fill(self.color)

        goByZIndex = sorted(
            self.gameObjects.values(),
            key=lambda gameobject: gameobject.z_index,
        )

        for go in goByZIndex:
            if go.enabled:
                go.Render(screen)

    def AddGameObject(self, gameobject: GameObject) -> None:
        """
        The AddGameObject function adds a gameobject to the list of gameobjects.


        :param self: Represent the instance of the class
        :param gameobject: GameObject: Pass in the gameobject to be added
        :return: Nothing, so it should be:
        :doc-author: Trelent
        """
        self.gameObjects[gameobject.id] = gameobject
        self.gameObjects[gameobject.id].Start()

    def CreateGameObject(self, name: str, xPos: int = 0, yPos: int = 0) -> GameObject:
        """
        The CreateGameObject function creates a new GameObject and calls AddGameObject().


        :param self: Refer to the current instance of a class
        :param name: str: Name the game object
        :param xPos: int: Set the x position of the game object
        :param yPos: int: Set the y position of the gameobject
        :return: A gameobject
        :doc-author: Trelent
        """
        go: GameObject = GameObject(name, xPos, yPos)
        self.AddGameObject(go)
        return go

    def GetGameObject(self, name: str) -> GameObject | None:
        """
        The GetGameObject function returns a GameObject with the given name.
            If no such GameObject exists, it returns None.

        :param self: Represent the instance of the class
        :param name: str: Specify the name of the game object that we want to get
        :return: A gameobject or none
        :doc-author: Trelent
        """
        for uuid in self.gameObjects:
            go: GameObject = self.gameObjects[uuid]
            if go.name == name:
                return go

        return None
