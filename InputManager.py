class InputManager:
    def __init__(self) -> None:
        self.keysDown = []
        self.keysPressed = []
        self.keysUp = []

    def handleKeydownEvent(self, keyIndex: int) -> None:
        self.keysDown.append(keyIndex)
        self.keysPressed.append(keyIndex)

    def handleKeyupEvent(self, keyIndex: int) -> None:
        self.keysUp.append(keyIndex)
        self.keysPressed.remove(keyIndex)

    def update(self) -> None:
        self.keysDown = []
        self.keysUp = []

    def debug(self) -> None:
        print(f"Keys Down: {self.keysDown}")
        print(f"Keys Pressed: {self.keysPressed}")
        print(f"Keys Up: {self.keysUp}")

    def IsKeyDown(self, key: int):
        return key in self.keysDown
    
    def IsKeyPressed(self, key: int):
        return key in self.keysPressed
    
    def IsKeyUp(self, key: int):
        return key in self.keysUp

        