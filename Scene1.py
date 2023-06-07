from vroom.Scene import Scene

class Scene1(Scene):
    def Start(self):
        super().Start()
        print("Starting Scene 1")

    def Update(self):
        super().Update()

    def Exit(self):
        super().Exit()
        print("Exiting Scene 1")
        
