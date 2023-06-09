import os

import pygame


class ResourceManager:

    images: dict[str, pygame.Surface] = {}
    
    @staticmethod
    def autoRegister(debug: bool = False) -> None:
        fileEndingFunctions: dict[str, function] = {
            "png": ResourceManager.registerAlphaSprite,
            "jpg": ResourceManager.registerSprite,
            "jpeg": ResourceManager.registerSprite
        }

        for root, _, files in os.walk("assets"):
            for file in files:
                filePath: str = os.path.join(root, file)
                fileName: str = filePath.split("\\")[-1]
                fileEnding: str = filePath.split(".")[-1]

                if fileEnding in fileEndingFunctions.keys():
                    fileEndingFunctions[fileEnding](filePath, fileName, fileEnding)
                    if debug:
                        print(f"Registered {fileName} using {fileEndingFunctions[fileEnding]}")
                else:
                    print(f"RESOURCE ERROR: Unrecognised file extension: {fileEnding}")


    @staticmethod
    def registerSprite(filePath: str, fileName: str, fileEnding: str):
        img = pygame.image.load(filePath)
        ResourceManager.images[fileName.replace(fileEnding, "").replace(".", "")] = img

    @staticmethod
    def registerAlphaSprite(filePath: str, fileName: str, fileEnding: str):
        img = pygame.image.load(filePath).convert_alpha()
        ResourceManager.images[fileName.replace(fileEnding, "").replace(".", "")] = img


    @staticmethod
    def getSprite(imgName: str) -> pygame.Surface:
        if imgName in ResourceManager.images.keys():
            return ResourceManager.images[imgName]
