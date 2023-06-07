class Game():

    VERSION = 0.1

    def __init__(self, screenWidth: int, screenHeight: int, frameRate: int) -> None:
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.frameRate = frameRate
        print(f"Game made with VroomVroom version {self.VERSION}")
        pass

    def run(self) -> None:
        pass

    def loop(self) -> None:
        pass