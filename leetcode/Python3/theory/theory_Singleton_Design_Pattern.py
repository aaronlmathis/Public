"""
Singleton Design Pattern
------------------------

"""
from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):
    @abstractmethod
    def print_data():
        """ Implement in Child Class """
        pass

class PersonSingleton(IPerson):

    __instance = None   # Single instance that can be created

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance 
    
    def __init__(self, name, age):
        if PersonSingleton.__instance != None:
            raise Exception("Singleton cannot be instantiated more than once.")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self
    
    @staticmethod
    def print_data():
        instance = PersonSingleton.get_instance()
        print(f"Name is {instance.name}. Age is: {instance.age}")


p = PersonSingleton("Mike", 30)
print(p)
p.print_data()
