class Stack():

    def __init__(self):
        self.array = []

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        return self.array[len(self.array)-1]

    def push(self, value):
        self.array.append(value)
        return self

    def pop(self):
        self.array.pop()
        return self.array

myNewStack = Stack()
myNewStack.push('Google')
myNewStack.push('Toyota')
myNewStack.push('Github')
myNewStack.peek()
myNewStack.pop()
print(myNewStack)