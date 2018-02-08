class Queue:

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        return self.queue[0]

    def get_size(self):
        return len(self.queue)

### test ###


queue_test = Queue()
queue_test.enqueue(10)
queue_test.enqueue(20)
queue_test.enqueue(30)
print("Size: ", queue_test.get_size())
print("Dequeue: ", queue_test.dequeue())
print("Dequeue: ", queue_test.dequeue())
print("Size: ", queue_test.get_size())
