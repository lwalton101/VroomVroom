class InputManager:
    keysDown: list[int] = []
    keysPressed: list[int] = []
    keysUp: list[int] = []

    @staticmethod
    def handleKeydownEvent(keyIndex: int) -> None:
        """
        The handleKeydownEvent function is called when a key is pressed.
        It adds the keyIndex to the keysDown list and also adds it to the keysPressed list.

        :param self: Refer to the object itself
        :param keyIndex: int: Determine which key is pressed
        :return: None
        :doc-author: Trelent
        """
        InputManager.keysDown.append(keyIndex)
        InputManager.keysPressed.append(keyIndex)

    @staticmethod
    def handleKeyupEvent(keyIndex: int) -> None:
        """
        The handleKeyupEvent function is called when a keyup event occurs.
        It adds the keyIndex to the keysUp list and removes it from the keysPressed list.

        :param self: Refer to the object itself
        :param keyIndex: int: Determine which key is being pressed
        :return: None
        :doc-author: Trelent
        """
        InputManager.keysUp.append(keyIndex)
        InputManager.keysPressed.remove(keyIndex)

    @staticmethod
    def update() -> None:
        """
        The update function is called every frame, and it updates the keysDown and keysUp lists.
            The update function should be called at the end of every game loop.

        :return: None
        :doc-author: Trelent
        """
        InputManager.keysDown = []
        InputManager.keysUp = []

    @staticmethod
    def debug() -> None:
        """
        The debug function prints out the current state of the InputManager's
        keysDown, keysPressed, and keysUp lists.

        :return: The following:
        :doc-author: Trelent
        """
        print(f"Keys Down: {InputManager.keysDown}")
        print(f"Keys Pressed: {InputManager.keysPressed}")
        print(f"Keys Up: {InputManager.keysUp}")

    @staticmethod
    def IsKeyDown(key: int):
        return key in InputManager.keysDown

    @staticmethod
    def IsKeyPressed(key: int):
        return key in InputManager.keysPressed

    @staticmethod
    def IsKeyUp(key: int):
        return key in InputManager.keysUp
