# Day 7: Insertion Sort Algorithm in Python

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Sample unsorted array
arr = [12, 11, 13, 5, 6]

print("Original array:", arr)
insertion_sort(arr)
print("Sorted array:", arr)
