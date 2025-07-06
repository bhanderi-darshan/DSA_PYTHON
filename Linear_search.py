# Day 2: Linear Search Algorithm in Python

# Function to perform linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target
    return -1  # Target not found

# Sample array
arr = [5, 12, 7, 9, 20, 33, 45]

# Element to search for
target = 20

# Calling the linear search function
result = linear_search(arr, target)

# Output result
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")
