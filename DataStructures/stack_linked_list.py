class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        if self.bottom is None:
            return None
        return self.top.data

    def push(self, value):
        newNode = Node(value)
        if self.bottom is None:
            self.top = self.bottom = newNode
        else:
            holdingPointer = self.top
            self.top = newNode
            self.top.next = holdingPointer

        self.length += 1
        return self

    def pop(self):
        if self.bottom is None:
            return None
        elif self.top is self.bottom:
            self.bottom = None
            return None
        else:
            self.top = self.top.next
            self.length -= 1
            return self

    def printt(self):
        temp = self.top
        while temp != None:
            print(temp.data , end = ' -> ')
            temp = temp.next


myNewStack = Stack()
myNewStack.push('Google')
myNewStack.push('Toyota')
myNewStack.push('Github')
myNewStack.peek()
myNewStack.pop()
myNewStack.printt()