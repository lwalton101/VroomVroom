import pygame

from vroom.resource_manager import ResourceManager


class AudioManager:
    totalChannels: int = 0
    categories: dict[str, list[pygame.mixer.Channel]] = {}

    @staticmethod
    def Init():
        pygame.mixer.pre_init(channels=AudioManager.totalChannels)
        pygame.mixer.init()

    @staticmethod
    def AddCategory(name: str, numOfChannels: int):
        allocatedChannels: int = AudioManager.totalChannels
        AudioManager.totalChannels += numOfChannels
        pygame.mixer.set_num_channels(AudioManager.totalChannels)
        print(pygame.mixer.get_num_channels())

        channels: list[pygame.mixer.Channel] = []
        for x in range(numOfChannels):
            channels.append(pygame.mixer.Channel(allocatedChannels))
            allocatedChannels += 1
        AudioManager.categories[name] = channels

    @staticmethod
    def PlaySound(categoryName: str, soundName: str) -> None:
        sound: pygame.mixer.Sound = ResourceManager.getSound(soundName)

        if categoryName not in AudioManager.categories.keys():
            print(f"ERROR: Category {categoryName} not found")
            return

        playedAudio: bool = False

        for channel in AudioManager.categories[categoryName]:
            if not channel.get_busy():
                channel.play(sound)
                playedAudio = True
                break

        if not playedAudio:
            print(f"All channels in category {categoryName} used up")
