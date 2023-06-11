import os
import psutil
import pygame
from vroom.AudioManager import AudioManager
from vroom.components.debug import Debug
from vroom.input_manager import InputManager
from vroom.resource_manager import ResourceManager
from vroom.scene import Scene
from vroom.camera import Camera
from vroom.time import Time


class Game:
    VERSION = 0.1
    currentScene: Scene

    def __init__(
        self,
        screenWidth: int,
        screenHeight: int,
        frameRate: int,
        title: str,
        mainScene: Scene,
    ) -> None:
        """
        The __init__ function is called when the class is instantiated.
        It sets up all of the variables that are needed for the game to run, inits some pygame stuff and then calls Start() on mainScene.

        :param self: Refer to the current instance of the class
        :param screenWidth: int: Set the width of the screen
        :param screenHeight: int: Set the height of the screen
        :param frameRate: int: Set the frame rate of the game
        :param title:str: Set the title of the window, and mainscene: scene is used to set what scene will be loaded first
        :param mainScene: Scene: Set the first scene that will be displayed when the game starts
        :return: Nothing, so it returns none
        :doc-author: Trelent
        """
        print(f"Game made with VroomVroom version {self.VERSION}")
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.frameRate = frameRate
        self.title = title
        Game.currentScene = mainScene

        Camera.screenWidth = screenWidth
        Camera.screenHeight = screenHeight

        self.running = True
        self.process = psutil.Process(os.getpid())
        self.flags = pygame.DOUBLEBUF | pygame.SCALED

        pygame.init()
        self.screen = pygame.display.set_mode(
            (screenWidth, screenHeight), self.flags, 16
        )
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        pygame.event.set_allowed(
            [pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP, pygame.VIDEORESIZE]
        )

        ResourceManager.autoRegister(debug=True)
        AudioManager.Init()

        Game.currentScene.Start()

    def loop(self) -> None:
        """
        The loop function is the main game loop. It handles all of the events,
        updates and rendering for each frame. The loop function also updates
        the input manager with any new key presses or releases.

        :param self: Access the class attributes and methods
        :return: Nothing, but the function is called in a while loop
        :doc-author: Trelent
        """
        Time.dt = self.clock.tick(self.frameRate) / 1000
        InputManager.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                InputManager.handleKeydownEvent(event.key)
            if event.type == pygame.KEYUP:
                InputManager.handleKeyupEvent(event.key)
            if event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode(
                    (event.w, event.h), self.flags, 16
                )

        Game.currentScene.Update()
        memUsage = self.process.memory_info().rss / 1024 / 1024
        Debug.Push(f"FPS: {int(self.clock.get_fps())} / {self.frameRate}")
        Debug.Push(f"Delta Time: {Time.dt} seconds")
        Debug.Push(f"Frame Time: {Time.dt * 1000} ms")
        Debug.Push(f"Memory Usage: {memUsage} MB")

        Game.currentScene.Render(self.screen)

        pygame.display.update()

    def quit(self) -> None:
        """
        The quit function quits the game.


        :param self: Refer to the object itself
        :return: Nothing
        :doc-author: Trelent
        """
        pygame.quit()

    def SetScene(self, scene: Scene) -> None:
        """
        The SetScene function is used to change the current scene.
            It takes a Scene object as an argument and sets it as the currentScene.
            The previous scene's Exit function is called, then the new scene's Start function.

        :param self: Represent the instance of the class
        :param scene: Scene: Set the current scene to a new one
        :return: None
        :doc-author: Trelent
        """
        Game.currentScene.Exit()
        Game.currentScene = scene
        Game.currentScene.Start()
