def mygenerator(n):
    for x in range(n):
        yield x ** 3

values = mygenerator(100)

#print(next(values))

def infinite_sequence():
    result = 1
    while True:
        yield result
        result *=5

values = infinite_sequence()
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))