import ctypes
import sys
import gc

"""my_string = 'Hello Darling!'
my_var = 10
my_list = [1, 2, 3]



print(f"Variable: {my_string} is referenced at: {hex(id(my_string))}")
print(f"Variable: {my_var} is referenced at: {hex(id(my_var))}")
print(f"Variable: {my_var} is referenced at: {hex(id(my_list))}")

#ref_count = sys.getrefcount(my_list)



print(ref_count(id(my_list)))
b = my_list

print(ref_count(id(b)))
"""

def ref_count(address):
    return ctypes.c_long.from_address(address).value

def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object Exists"
    return "Not Found"

class A:
    def __init__(self):
        self.b = B(self)
        print(f'A: self: {hex(id(self))}, B: {hex(id(self.b))}')

class B:
    def __init__(self, a):
        self.a = a 
        print(f'B: self: {hex(id(self))}, a: {hex(id(self.a))}')

gc.disable()

my_var = A()

print(hex(id(my_var.b)))
print(hex(id(my_var.b.a)))

a_id = id(my_var)
b_id = id(my_var.b)
print(ref_count(a_id))
print(ref_count(b_id))

print(object_by_id(a_id))
print(object_by_id(b_id))

my_var = None

print(ref_count(a_id))
print(ref_count(b_id))
