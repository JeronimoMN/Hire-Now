class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SingledList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, value):
        newNode = Node(value)

        if not self.head:
            self.head = newNode
            self.size +=1
        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            temp.next = newNode
            self.size += 1

        return