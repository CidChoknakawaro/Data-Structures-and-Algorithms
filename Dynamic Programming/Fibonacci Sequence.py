import timeit

start = timeit.default_timer() # Start timer


# Using memoization
def fib(index,memo={}):

    if index < 2: # If index is less than 2, return index
        return index
    
    if index in memo: # Return already visied index
        return memo[index]
    
    else: # Index has not been visied
        res = fib(index-1,memo) + fib(index-2,memo)

    memo[index] = res # Set memo index to result

    return memo[index] # Return result


end = timeit.default_timer() # Stop timer

index = 10 # Specify index

print('Index:', index)
print('Fibonacci Value:', fib(index)) # Print corresponding fibonacci value
print('Runtime:', (end - start) * 1000, 'ms')  # Runtime in milliseconds
print('Time Complexity: O(n)')
print('Space Complexity: O(n)')
'''

Time Complexity:
Best Case: O(n) - In the best case scenario, each Fibonacci number is computed only once and stored in the memoization table. Hence, the time complexity reduces to linear.
Average Case: O(n) - Same as the best case scenario, each Fibonacci number is computed only once and stored.
Worst Case: O(n) - Even in the worst case scenario, where every Fibonacci number up to the given index needs to be computed, each number is computed only once and stored.

Space Complexity: O(n) - The space complexity is O(n) because the memoization table stores the result of each Fibonacci number up to the given index.

'''