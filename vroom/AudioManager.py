import pygame

from vroom.resource_manager import ResourceManager


class AudioManager:
    totalChannels: int = 0
    categories: dict[str, list[pygame.mixer.Channel]] = {}

    @staticmethod
    def Init():
        """
        The Init function initializes the pygame mixer module.
            It is called by the AudioManager constructor.

        :return: A dictionary of all the sounds in the game
        :doc-author: Trelent
        """
        pygame.mixer.pre_init(channels=AudioManager.totalChannels)
        pygame.mixer.init()

    @staticmethod
    def AddCategory(name: str, numOfChannels: int):
        """
        The AddCategory function adds a new category of channels to the AudioManager.
            The name parameter is used as the key for accessing this category in the future.
            The numOfChannels parameter specifies how many channels should be allocated to this category.

        :param name: str: Identify the category
        :param numOfChannels: int: Determine how many channels are allocated to the category
        :return: A list of channels
        :doc-author: Trelent
        """
        allocatedChannels: int = AudioManager.totalChannels
        AudioManager.totalChannels += numOfChannels
        pygame.mixer.set_num_channels(AudioManager.totalChannels)

        channels: list[pygame.mixer.Channel] = []
        for x in range(numOfChannels):
            channels.append(pygame.mixer.Channel(allocatedChannels))
            allocatedChannels += 1
        AudioManager.categories[name] = channels

    @staticmethod
    def PlaySound(categoryName: str, soundName: str) -> None:
        """
        The PlaySound function takes in a category name and sound name,
        and plays the sound on an available channel. If no channels are available,
        it prints out an error message.

        :param categoryName: str: Specify which category of audio channels the sound should be played on
        :param soundName: str: Get the sound from the resourcemanager
        :return: None
        :doc-author: Trelent
        """
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
