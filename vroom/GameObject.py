from vroom.Component import Component

class GameObject:
    name: str = ""
    components: list[Component] = []

    def __init__(self, name: str):
        self.name = name

    def Update(self):
        """
        The Update function is called once per frame. It updates the state of all components in the entity.
        
        :param self: Represent the instance of the class
        :return: Nothing
        :doc-author: Trelent
        """
        for component in self.components:
            component.Update()

        print(f"update from gameobject {self.name}")

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

    def AddComponent(self, componentType: type):
        """
        The AddComponent function adds a component to the gameobject.
            If the component already exists, it will not be added again.
        
        :param self: Represent the instance of the class
        :param componentType: type: Specify the type of component that is being added to the gameobject
        :return: The component it just added to the gameobject
        :doc-author: Trelent
        """
        if not self.HasComponent(componentType):
            self.components.append(componentType())
        else:
            print(f"Tried adding duplicate component {componentType} on gameobject {self.name}")

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


    def RemoveComponent(self,componentType):
        """
        The RemoveComponent function removes a component from the gameobject. 
        
        :param self: Reference the object itself
        :param componentType: Determine which component to remove from the gameobject
        :return: A string
        :doc-author: Trelent
        """
        if self.HasComponent(componentType):
            self.components.append(componentType())
        else:
            print(f"Tried removing nonexistant component {componentType} on gameobject {self.name}")

    
            

