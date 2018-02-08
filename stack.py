class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]  # return the last item
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def get_size(self):
        return len(self.stack)


stack_test = Stack()
stack_test.push(3)
stack_test.push(4)
stack_test.push(423)
stack_test.push(12)

print("Size: ", stack_test.get_size())
print("Popped: ", stack_test.pop())
print("Popped: ", stack_test.pop())
print("Size: ", stack_test.get_size())
print("Peek: ", stack_test.peek())
print("Size ", stack_test.get_size())
