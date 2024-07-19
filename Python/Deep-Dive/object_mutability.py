"""
def process(s):
    print(f'Initial s # = {id(s)}')
    s = s + ' world'
    print(f'Final s # = {id(s)}')

my_var = 'hello'
print(f'my_var # = {id(my_var)}')
process(my_var)

print(id(my_var))

def modify_list(lst):
    print(f'Initial lst # = {id(lst)}')
    lst.append(100)
    print(f'Final lst # = {id(lst)}')   

my_list = [1, 2, 3]
print(id(my_list))
modify_list(my_list)
print(id(my_list))

def modify_tuple(t):
    print(f'Initial t # = {id(t)}')
    t[0].append(100)
    print(f'Final t # = {id(t)}')   

my_tuple = ([1, 2], 'a')
print(id(my_tuple))
modify_tuple(my_tuple)
print(id(my_tuple))


def my_func(e):
    if e in [1, 2, 3]:
        pass
my_func(3)
print(my_func.__code__.co_consts)

"""
import string
import time

char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)

def membership_test(n, container):
    for i in range(n):
        if 'z' in container:
            pass

start = time.perf_counter()
membership_test(10000000, char_set)
end = time.perf_counter()
print('list ', end-start)