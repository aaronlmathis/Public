'''
a = 3
if a < 5:
    b = 'a < 5'
else:
    b = 'a >= 5'
print(b)
'''
## CAN ALSO BE WRITTEN AS
'''
b = 'a < 5' if a < 5 else 'a >= 5'
print(b)


from math import sqrta

print(sqrt(4))

import math

print(math.pi)
print(math.exp(1))
''' 
#LAMbDA
''' 

fn1 = lambda x: x**2

print(fn1(2))
''' 

#while loops
'''
min_length = 2
name = input("Please enter your name: ")

while not(len(name) >= min_length and name.isprintable() and name.isalpha()):
    name = input("Please enter your name: ")

print("Hello, {0}".format(name))

min_length = 2

while True:
    name = input("Please enter your name: ")
    if len(name) >= min_length and name.isprintable() and name.isalpha():
        break
print(f"Hello, {name}")

a = 0

while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)
''''''
l = [1, 2, 3]
val = 10

found = False
idx = 0
while idx < len(l):
    if l[idx] == val:
        found = True
        break
    idx += 1

if not found:
    l.append(val)

print(l)

l = [1, 2, 3]
val = 10
idx = 0
while idx < len(l):
    if l[idx] == val:
        break
    idx+=1
else:
    l.append(val)

print(l)

a = 10
b = 0
try:
    a/b
except ZeroDivisionError:
    print('division by 0')
finally:
    print('this is always executing')


s='hello'
print(len(s))

for i, c in enumerate(s):
    print(i, c)

    ''' 

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive")
        else:
             self._width = width   

    @property
    def height(self):
        return self._height             

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("Height must be positive")
        else:
             self._height = height  

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f'Rectangle: width={self.width}, height={self.height}'
    
    def __repr__(self):
        return 'Rectangle({self.width},{self.height})'
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False
        
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented
        
    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() > other.area()
        else:
            return NotImplemented        
                       
r1 = Rectangle(10, 20)
r2 = Rectangle(30, 20)
r3 = Rectangle(30, 20)
