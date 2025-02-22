"""
Proxy Design Pattern
--------------------
The Proxy Design Pattern is a structural design pattern that provides an object (Proxy) that acts as a substitute or placeholder for another object (Real Subject). 
It is used to control access to the original object, adding additional functionality such as lazy initialization, access control, logging, or caching without modifying the actual object.

A proxy behaves like the original object but can add pre-processing or post-processing logic. This helps optimize performance, enhance security, or control expensive resource usage.

Key Characteristics:
--------------------
    - Encapsulates the real object and controls its access.
    - Can implement lazy instantiation (loading an object only when needed).
    - Can act as a security layer to restrict access.
    - Can log requests or perform additional actions before or after delegating to the real object.

Types of Proxies:
-----------------

    - Virtual Proxy - Used for lazy loading or on-demand instantiation of expensive objects.
    - Protection Proxy- Controls access based on authentication or permissions.
    - Logging Proxy - Logs operations performed on the object.
    - Caching Proxy - Caches results to improve performance.

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
from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):

    @abstractmethod
    def person_method(self):
        """ Interface Method """

class Person(IPerson):
    def person_method(self):
        print("I am a person")

# Proxy to create and handle person object
class ProxyPerson(IPerson):

    def __init__(self):
        self.person = None    # Lazy initialization method
    
    def person_method(self):
        if self.person == None:
            self.person = Person()

        print("I am the proxy functionality.")
        self.person.person_method()

if __name__ == "__main__":
    proxy = ProxyPerson()

    proxy.person_method()

"""

Example of Logging/Caching Proxy
--------------------------------

ABC:
    - Enforces Interface Compliance
    - Ensures subclass must implement compute(value) method
    - Prevents Incomplete implementations
"""
from abc import ABC, abstractmethod
import time

# Step 1: Define the Interface
class IService(ABC):
    @abstractmethod
    def compute(self, value):
        pass

# Step 2: Implement the Real Object (Expensive Computation)
class ExpensiveService(IService):
    def compute(self, value):
        print(f"RealSubject: Performing expensive computation for {value}...")
        time.sleep(2)  # Simulating a costly operation
        return value * value  # Example: Squaring the number

# Step 3: Implement the Proxy with Logging and Caching
class ProxyService(IService):
    def __init__(self):
        self._real_service = ExpensiveService()
        self._cache = {}

    def compute(self, value):
        # Logging the request
        print(f"Proxy: Logging call to compute({value})")

        # Checking cache first
        if value in self._cache:
            print(f"Proxy: Returning cached result for {value}")
            return self._cache[value]

        # If not cached, call the real service
        result = self._real_service.compute(value)

        # Cache the result for future requests
        self._cache[value] = result
        return result

# Step 4: Client Code
if __name__ == "__main__":
    proxy = ProxyService()

    # First call - actual computation
    print("Result:", proxy.compute(5))  
    print("\n")

    # Second call - retrieves cached result
    print("Result:", proxy.compute(5))  

    # New call with different input
    print("\n")
    print("Result:", proxy.compute(10))  
