import os

import pygame


class ResourceManager:
    images: dict[str, pygame.Surface] = {}
    sounds: dict[str, pygame.mixer.Sound] = {}

    @staticmethod
    def registerAllFilesInFolder(folderName: str, debug: bool = False) -> None:
        for root, _, files in os.walk(folderName):
            for file in files:
                filePath: str = os.path.join(root, file)
                fileName: str = filePath.split("\\")[-1]
                fileEnding: str = filePath.split(".")[-1]

                if fileEnding in ResourceManager.fileEndingFunctions.keys():
                    # we supress warning because vs code doesnt like me using functions as variables
                    # it gives a function object not callable error, code still works tho
                    ResourceManager.fileEndingFunctions[fileEnding](filePath, fileName, fileEnding)  # type: ignore
                    if debug:
                        print(
                            f"Registered {fileName} using {ResourceManager.fileEndingFunctions[fileEnding].__name__}"
                        )
                else:
                    print(f"RESOURCE ERROR: Unrecognised file extension: {fileEnding}")

    @staticmethod
    def autoRegister(debug: bool = False) -> None:
        ResourceManager.fileEndingFunctions: dict[str, function] = {
            "png": ResourceManager.registerAlphaSprite,
            "jpg": ResourceManager.registerSprite,
            "jpeg": ResourceManager.registerSprite,
            "mp3": ResourceManager.registerSound,
        }

        ResourceManager.registerAllFilesInFolder("assets", debug)
        ResourceManager.registerAllFilesInFolder("vroom/builtinassets", debug)

    @staticmethod
    def registerSprite(filePath: str, fileName: str, fileEnding: str) -> None:
        """
        The registerSprite function takes in a file path, the name of the file, and its ending.
        It then creates a surface from the file path and stores it in ResourceManager's images dictionary.

        :param filePath: str: Specify the file path of the image
        :param fileName: str: Identify the image
        :param fileEnding: str: Determine the file ending of the image
        :return: Nothing, so the return type is none
        :doc-author: Trelent
        """
        img = pygame.image.load(filePath)
        ResourceManager.images[fileName.replace(fileEnding, "").replace(".", "")] = img

    @staticmethod
    def registerAlphaSprite(filePath: str, fileName: str, fileEnding: str) -> None:
        img = pygame.image.load(filePath).convert_alpha()
        ResourceManager.images[fileName.replace(fileEnding, "").replace(".", "")] = img

    @staticmethod
    def registerSound(filePath: str, fileName: str, fileEnding: str) -> None:
        sounds = pygame.mixer.Sound(filePath)
        ResourceManager.sounds[
            fileName.replace(fileEnding, "").replace(".", "")
        ] = sounds

    @staticmethod
    def getSprite(imgName: str) -> pygame.Surface:
        if imgName in ResourceManager.images.keys():
            return ResourceManager.images[imgName]
        else:
            print(f"Sprite {imgName} not found")
            return ResourceManager.images["missing_texture"]

    @staticmethod
    def getSound(audioName: str) -> pygame.mixer.Sound:
        if audioName in ResourceManager.sounds.keys():
            return ResourceManager.sounds[audioName]
        else:
            return ResourceManager.sounds["soundnotfound"]
