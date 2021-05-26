class Node():
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1


    def insert(self,index,data):
        new_node = Node(data)
        i = 0
        temp = self.head
        if index>=self.length:
            self.append(data)
            return
        if index == 0:
            self.prepend(data)
            return
        while i<self.length:
            if i == index - 1:
                temp.next , new_node.next = new_node , temp.next
                self.length += 1
                break
            temp = temp.next
            i += 1

    def remove(self,index):
        temp = self.head
        i = 0
        if index>=self.length:
            print("Entered wrong index")
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        while i<self.length:
            if i == index - 1:
                temp.next = temp.next.next
                self.length -= 1
                break
            i+=1
            temp = temp.next

    def printl(self):
        temp = self.head
        while temp != None:
            print(temp.data , end = ' ')
            temp = temp.next
        print('length: {}'.format(str(self.length)))

    def reverse(self):
        prev = None
        self.tail = self.head
        while self.head != None:
            temp = self.head
            self.head = self.head.next
            temp.next = prev
            prev = temp
        self.head = temp
        self.printl()


if __name__ == '__main__':
    myLinkedList = LinkedList()
    # 5 ->
    myLinkedList.append(5)
    # 9 -> 5 ->
    myLinkedList.prepend(9)
    # 9 -> 5 -> 2 ->
    myLinkedList.append(2)
    # 9 -> 5 -> 2 -> 4 ->
    myLinkedList.append(4)
    # 9 -> 5 -> 23 -> 2 -> 4 ->
    myLinkedList.insert(2, 23)
    # 9 -> 5 -> 23 -> 4 ->
    myLinkedList.remove(3)
    myLinkedList.printl() # 9 -> 5 -> 23 -> 4 ->  lenght: 4
    myLinkedList.reverse() # 4 -> 23 -> 5 -> 9 ->  lenght: 4