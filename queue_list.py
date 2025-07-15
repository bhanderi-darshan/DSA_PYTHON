# Day 11: Queue Implementation using Python List

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Test the Queue
q = Queue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)

print("Front element is:", q.peek())
print("Dequeued element is:", q.dequeue())
print("Queue size is:", q.size())
print("Is queue empty?", q.is_empty())
