import timeit

start = timeit.default_timer() # Start timer


def merge(arr1,arr2): # Function for merging and sorting 2 arrays
    merged = [] # Create empty array to store sorted values
    i,j=0,0 # Set 2 pointers for iterating through both arrays

    while i < len(arr1) and j < len(arr2): # Iterate through both arrays until one reaches the end
        if arr1[i] <= arr2[j]: # If current index in arr1 is less than or equal to current index in arr2
            merged.append(arr1[i]) # Append value to merged
            i+=1 # Iterate to next value
        else: # If current index in arr2 is more than current index in arr2
            merged.append(arr2[j]) # Append value to merged
            j+=1 # Iterate to next value
    
    # Stores any remaining value that was not iterated through
    arr1_tail = arr1[i:]
    arr2_tail = arr2[j:]

    # Return merged array and tails
    return merged + arr1_tail + arr2_tail

def merge_sort(arr):
    if len(arr) <= 1: # Base case
        return arr
    
    # Seperate array to 2 halves
    mid = len(arr)//2 # Set mid-point
    left = arr[:mid] # Left half
    right = arr[mid:] # Right half

    # Using recursion to sort both halves
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Merge both halves using merge function
    return merge(left_sorted,right_sorted)


end = timeit.default_timer() # Stop timer

array = [100,-23,56,12,59,67,-3,-1,0,999]
print('Unsorted Array:', array)
print('Sorted Array:', merge_sort(array)) # Print Sorted Array
print('Runtime:', (end - start) * 1000, 'ms')  # Runtime in milliseconds
print('Time Complexity: O(n log n)')
print('Space Complexity: O(n)')
'''

Time Complexity:
Merge sort is a divide-and-conquer algorithm with the following time complexity:

Best Case: O(n log n)
Average Case: O(n log n)
Worst Case: O(n log n)

Space Complexity: O(n)

'''