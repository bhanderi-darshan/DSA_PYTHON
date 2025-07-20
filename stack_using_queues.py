# Day 15: Implement Stack Using Two Queues

from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.empty():
            return "Stack is empty"
        return self.q1.popleft()

    def top(self):
        if self.empty():
            return "Stack is empty"
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0

# Test the StackUsingQueues
stack = StackUsingQueues()
stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.top())
print("Popped element:", stack.pop())
print("Top element after pop:", stack.top())
