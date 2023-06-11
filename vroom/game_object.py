from vroom.component import Component
import uuid, pygame


class GameObject:
    def __init__(self, name: str, xPos: float = 0, yPos: float = 0):
        self.name: str = name
        self.components: list[Component] = []
        self.id = uuid.uuid4()
        self.pos: tuple[float, float] = 0, 0
        self.rotation: float = 0
        self.scale: float = 1
        self.z_index = 0
        self.enabled: bool = True

    def Start(self) -> None:
        pass

    def Render(self, screen) -> None:
        """
        The Render function is a function that renders all of the components attatched to the game object.
        It does this by iterating through each component and calling its Render() method.

        :param self: Represent the instance of the class
        :return: Nothing
        :doc-author: Trelent
        """
        for component in self.components:
            component.Render(screen)

    def Update(self):
        """
        The Update function is called once per frame. It updates the state of all components attatched to the game object.

        :param self: Represent the instance of the class
        :return: Nothing
        :doc-author: Trelent
        """
        for component in self.components:
            component.Update()

    def GetComponent(self, componentType: type) -> Component | None:
        """
        The GetComponent function returns the first component of a given type that it finds.
        If no such component is found, None is returned.

        :param self: Represent the instance of the class
        :param componentType: type: Specify the type of component that is being searched for
        :return: A component of the specified type
        :doc-author: Trelent
        """
        for component in self.components:
            if type(component) == componentType:
                return component

        return None

    def AddComponent(self, component: Component) -> Component | None:
        """
        The AddComponent function adds a component to the gameobject's list of components.
            If the component already exists, it will not be added and instead print an error message.

        :param self: Refer to the current instance of the class
        :param component: Component: Pass in a component object to the function
        :return: A component or none
        :doc-author: Trelent
        """
        if not self.HasComponent(type(component)):
            component.gameObject = self
            self.components.append(component)
            component.Start()
        else:
            print(
                f"Tried adding duplicate component {type(component)} on gameobject {self.name}"
            )

    def HasComponent(self, componentType: type):
        """
        The HasComponent function checks if the game object has a component of the specified type.


        :param self: Refer to the current instance of a class
        :param componentType: type: Specify the type of component that you want to check for
        :return: A boolean value
        :doc-author: Trelent
        """
        hasComponent = False

        for component in self.components:
            if type(component) == componentType:
                hasComponent = True

        return hasComponent

    def RemoveComponent(self, componentType):
        """
        The RemoveComponent function removes a component from the gameobject.

        :param self: Reference the object itself
        :param componentType: Determine which component to remove from the gameobject
        :return: A string
        :doc-author: Trelent
        """
        removed = False

        for component in self.components:
            if type(component) == componentType:
                self.components.remove(component)
                removed = True

        if not removed:
            print(
                f"Tried removing nonexistant component {componentType} on gameobject {self.name}"
            )

    def SetEnabled(self, state: bool) -> None:
        self.enabled = state
