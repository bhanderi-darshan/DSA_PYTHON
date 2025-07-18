# Day 13: Doubly Linked List Implementation in Python

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            last = current
            current = current.next
        print("None")
    
    def display_backward(self):
        current = self.head
        while current and current.next:
            current = current.next
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# Test the DoublyLinkedList
dll = DoublyLinkedList()
dll.append(100)
dll.append(200)
dll.append(300)

print("Doubly Linked List (Forward):")
dll.display_forward()

print("Doubly Linked List (Backward):")
dll.display_backward()
