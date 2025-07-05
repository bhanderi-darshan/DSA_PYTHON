# Day 1: Basic Array Operations in Python

# Define an array (list in Python)
arr = [10, 20, 30, 40, 50]

# Print the array
print("Original array:", arr)

# Append an element
arr.append(60)
print("After appending 60:", arr)

# Insert an element at a specific position
arr.insert(2, 25)
print("After inserting 25 at index 2:", arr)

# Remove an element by value
arr.remove(40)
print("After removing 40:", arr)

# Pop an element (last by default)
popped = arr.pop()
print("Popped element:", popped)
print("Array after pop:", arr)

# Accessing elements
print("Element at index 1:", arr[1])

# Updating element
arr[1] = 22
print("After updating index 1 to 22:", arr)

# Traversing array using loop
print("Traversing array:")
for i in arr:
    print(i)
