class Node():
def __init__(self, data):
    self.data = data
    self.next = None


class Queue():

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        return self.first

    def enque(self, value):
        newNode = Node(value)
        if self.first is None:
            self.first = newNode
            self.last = self.first
        else:
            self.last.next = newNode
            self.last = self.last.next
            self.length += 1
            return self

    def deque(self):
        cur = self.first
        if cur is None:
            return None
        else:
            self.first = self.first.next
            self.length -= 1
            return self

    def printt(self):
        cur = self.first
        while cur != None:
            print(cur.data , end = '->')
            cur = cur.next
        print()
        print(self.length)

myQueue = Queue()
myQueue.enque('Google')
myQueue.enque('Udemy')
myQueue.enque('discord')
myQueue.peek()
myQueue.deque()
myQueue.printt()