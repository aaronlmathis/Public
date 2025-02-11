from abc import ABCMeta, abstractmethod
"""
Factory Design Pattern
----------------------
The Factory Design Pattern is a creational design pattern that provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created. 
It encapsulates the object creation logic, promoting loose coupling between client code and concrete classes.

Instead of directly instantiating objects using the new keyword (or calling the class constructor), the factory method is used to create and return instances dynamically. 
This improves code maintainability, enhances flexibility, and allows the addition of new object types with minimal changes to existing code.

Key Characteristics:
--------------------
    - Defines a common interface for creating objects.
    - Uses a factory method to instantiate and return objects based on input parameters.
    - Encapsulates object creation logic, reducing direct dependencies on concrete classes.
    - Promotes scalability and maintainability, making it easy to introduce new object types.

Use Cases:
---------
    - When object creation is complex or requires multiple steps.
    - When the exact type of object is determined at runtime.
    - When managing a large hierarchy of related classes.

    
metaclass
    - defines the behavior of other classes (controls how classes are constructed)
    - type is the default.

ABCMeta
    - prevents direct instatiation of class that has @abstractmethod's
    - enforces subclass implementation of abstract methods

@abstractmethod means:
    - object can't be created directly. So no calling IPerson(). 
    - @abstractmethod ensures that every subclass MUST define a person_method()

@staticmethod means 
    - the method doesn't need to pass 'self'
    - also, calling static method doesn't require creating instance of class. You can call it without.
"""
class IPerson(metaclass=ABCMeta):
    @abstractmethod
    def person_method(self):
        """ Interface Method """
        pass
class Student(IPerson):
    
    def __init__(self):
        self.name = "Basic Student Name"
    
    def person_method(self):
        print("I am a student")

class Teacher(IPerson):

    def __init__(self):
        self.name = "Basic Teacher Name"
    
    def person_method(self):
        print("I am a teacher")

class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("Invalid Type")
        return None

if __name__ == "__main__":
    choice = input("What type of person do you want to create?\n")
    person = PersonFactory.build_person(choice)
    person.person_method()