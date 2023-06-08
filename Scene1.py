from vroom.Scene import Scene

class Scene1(Scene):
    def Start(self):
        super().Start()
        print("Starting Scene 1")

        self.CreateGameObject("test 1")
        self.CreateGameObject("cheese")

    def Update(self):
        super().Update()

    def Exit(self):
        super().Exit()
        print("Exiting Scene 1")
        
