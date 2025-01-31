class Person:

    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender
    
    @property
    def Name(self):
        return self.__name
    
    @Name.setter
    def Name(self, value):
        if value != 'Bob':
            self.__name = value
    
    @staticmethod
    def my_method():
        print("This is a static method call")

# No need to initialize object to call static method
Person.my_method()

p1 = Person("Aaron", 30, "m")
print(p1.Name)
p1.Name = 'Bobb'
print(p1.Name)

# But you can def call it from object.
p1.my_method()