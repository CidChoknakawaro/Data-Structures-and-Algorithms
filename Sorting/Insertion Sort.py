import timeit

start = timeit.default_timer()  # Start timer


def insertion_sort(arr):
    for i in range(1, len(arr)): # Start from the second element
        key = arr[i] # Key to be inserted
        j = i - 1 # Start comparing with the previous element

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j] # Move elements greater than key one position ahead
            j -= 1

        arr[j + 1] = key # Insert key into its correct position

    return arr


end = timeit.default_timer()  # Stop timer

array = [100, -23, 56, 12, 59, 67, -3, -1, 0, 999]
print('Unsorted Array:', array)
print('Sorted Array:', insertion_sort(array))  # Print Sorted Array
print('Runtime:', (end - start) * 1000, 'ms')  # Runtime in milliseconds
print('Time Complexity: O(n^2)')
print('Space Complexity: O(1)')
'''

Time Complexity:
Insertion sort is a simple sorting algorithm with the following time complexity:

Best Case: O(n) - When the array is already sorted.
Average Case: O(n^2)
Worst Case: O(n^2) - When the array is sorted in reverse order.

Space Complexity: O(1) - It sorts the array in-place, hence constant space complexity.

'''
