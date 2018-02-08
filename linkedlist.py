class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    # O(1)
    def insertStart(self, data):
        self.size += 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    # O(1)
    def get_size(self):
        return self.size

    # O(N)
    def insertEnd(self, data):
        self.size += 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print("%d" % actualNode.data)
            actualNode = actualNode.nextNode

    # O(N)
    def remove(self, data):
        if self.head is None:
            return

        self.size -= 1

        currentNode = self.head
        previousNode = None

        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode


### tests ###
linkedListTest = LinkedList()
linkedListTest.insertStart(12)
linkedListTest.insertStart(122)
linkedListTest.insertStart(3)
linkedListTest.insertEnd(31)

linkedListTest.traverseList()
print(linkedListTest.get_size())

linkedListTest.remove(31)
linkedListTest.remove(12)

print(linkedListTest.get_size())
