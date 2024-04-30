import timeit

start = timeit.default_timer() # Start timer


def binary_search(arr, target): # Binary Search Function
    low = 0 # Set low value
    high = len(arr) - 1 # Set high value
    
    while low <= high:
        mid = low+((high-low)//2) # Use low and high value to find middle index
        if arr[mid] == target: # If target is found
            return mid 
        elif arr[mid] < target: # If target is higher than mid-index
            low = mid + 1 # Set low pointer to middle index + 1
        else: # If target is low than mid-index
            high = mid - 1 # Set high pointer to middle index - 1
    
    return -1 # If the target is not found


end = timeit.default_timer() # Stop timer

sorted_array = [-23, -3, -1, 0, 12, 56, 59, 67, 100, 999]
target = 59

print('Sorted Array:', sorted_array)
print('Target:', target)

index = binary_search(sorted_array, target) # Call binary search function
if index != -1:
    print('Target found at index:', index) # Print target index
else:
    print('Target not found in the array') # Target not found in the array

print('Runtime:', (end - start) * 1000, 'ms') # Runtime in milliseconds
print('Time Complexity: O(log n)')
print('Space Complexity: O(1)')

'''

Time Complexity:
Best Case: O(1) - The target element is found at the middle of the array in the first comparison.
Average Case: O(log n) - In each step, the search space is halved.
Worst Case: O(log n) - When the target is not present in the array, and the search continues until the search space becomes empty.

Space Complexity: O(n) O(1) - Binary search is an iterative algorithm that doesn't require any extra space proportional to the input size.

'''