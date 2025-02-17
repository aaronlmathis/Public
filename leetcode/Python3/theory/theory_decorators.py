def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = function.__name__
            f.write(f"{fname} returned value {value}\n")
            print(f"{fname} returned value {value}")
        return value
    return wrapper

@logged
def add(x, y):
    return x+y

#print(add(10, 20))

import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.perf_counter()  # High-precision timing
        value = function(*args, **kwargs)
        after = time.perf_counter()
        fname = function.__name__
        print(f"{fname} took {after - before:.8f} seconds to execute!")  # Format for better precision
        return value
    return wrapper

@timed
def myfunction(x):
    result = 1
    for i in range(1, x):
        result*=i
    return result

myfunction(90000)
