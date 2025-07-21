# Day 16: Implement Queue Using Two Stacks

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if self.empty():
            return "Queue is empty"
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if self.empty():
            return "Queue is empty"
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self):
        return not self.stack1 and not self.stack2

# Test the QueueUsingStacks
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Front element:", queue.peek())
print("Dequeued:", queue.dequeue())
print("Front after dequeue:", queue.peek())
