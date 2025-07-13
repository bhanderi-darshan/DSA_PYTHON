# Day 9: Quick Sort Algorithm in Python

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # Choosing the first element as pivot
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Sample unsorted array
arr = [10, 7, 8, 9, 1, 5]

print("Original array:", arr)
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
