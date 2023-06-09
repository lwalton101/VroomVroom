class Component:
    def __init__(self):
        import vroom.game_object

        self.gameObject: vroom.game_object.GameObject
        pass

    def Start(self):
        pass

    def Render(self, screen):
        """
        The Render function is called by the main game loop to draw all of the
            bits in a sprite. It takes one argument, screen, which is a pygame
            Surface object that represents the display window. The Render function
            should be overridden by each Component subclass to draw its own objects.

        :param self: Represent the instance of the class
        :param screen: Draw the object
        :return: The screen
        :doc-author: Trelent
        """
        pass

    def Update(self):
        pass
