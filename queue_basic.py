from collections import deque

# Create a queue
queue = deque()

# Enqueue elements
queue.append(10)
queue.append(20)
queue.append(30)

print("Initial Queue:", list(queue))

# Dequeue elements
print("Dequeued:", queue.popleft())
print("Queue after dequeue:", list(queue))

# Peek front element
print("Front element:", queue[0])

# Check if queue is empty
if not queue:
    print("Queue is empty")
else:
    print("Queue is not empty")
  
