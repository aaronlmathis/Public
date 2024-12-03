"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""
class MinStack:

    def __init__(self):
        self.items = []
        self.minStack = []


    def push(self, val: int) -> None:
        self.items.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
          if self.items.pop() == self.minStack[-1]:
            self.minStack.pop()


    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
def execute_operations(operations, values):
    obj = None
    results = []
    for op, val in zip(operations, values):
        if op == "MinStack":
            obj = MinStack()  # This will call your MinStack implementation
            results.append(None)
        elif op == "push":
            obj.push(val[0])
            results.append(None)
        elif op == "pop":
            obj.pop()
            results.append(None)
        elif op == "top":
            results.append(obj.top())
        elif op == "getMin":
            results.append(obj.getMin())
    return results

operations = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
values = [[], [-2], [0], [-3], [], [], [], []]

print(execute_operations(operations, values))
