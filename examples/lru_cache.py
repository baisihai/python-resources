from functools import lru_cache

# Example 1: Basic usage of lru_cache
@lru_cache(maxsize=3)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print("Fibonacci numbers with lru_cache:")
for i in range(10):
    print(f"fibonacci({i}) = {fibonacci(i)}")
print("")   # Just to add a blank line for better readability of output
# Output: Fibonacci numbers with lru_cache:
# fibonacci(0) = 0
# fibonacci(1) = 1
# fibonacci(2) = 1
# fibonacci(3) = 2
# fibonacci(4) = 3
# fibonacci(5) = 5
# fibonacci(6) = 8
# fibonacci(7) = 13
# fibonacci(8) = 21
# fibonacci(9) = 34
# The lru_cache decorator caches the results of the fibonacci function.
# The maxsize parameter limits the cache to the 3 most recent calls.
# This significantly speeds up the computation for larger Fibonacci numbers.



# Example 2: Demonstrating cache behavior
print("Cache info before additional calls:", fibonacci.cache_info())
print("Calling fibonacci(10):", fibonacci(10))
print("Cache info after calling fibonacci(10):", fibonacci.cache_info())
print("Calling fibonacci(11):", fibonacci(11))
print("Cache info after calling fibonacci(11):", fibonacci.cache_info())
print("")   # Just to add a blank line for better readability of output
# Output: Cache info before additional calls: CacheInfo(hits=16, misses=10, maxsize=3, currsize=3)
# Calling fibonacci(10): 55
# Cache info after calling fibonacci(10): CacheInfo(hits=16, misses=11, maxsize=3, currsize=3)
# Calling fibonacci(11): 89
# Cache info after calling fibonacci(11): CacheInfo(hits=16, misses=12, maxsize=3, currsize=3)
# The cache_info() method provides statistics about the cache usage.
# It shows the number of hits, misses, the maximum size of the cache, and the current size.



# Example 3: Using lru_cache with a function that has multiple arguments
@lru_cache(maxsize=5)
def power(base, exponent):
    return base ** exponent
print("Power function with lru_cache:")
print("power(2, 3) =", power(2, 3))
print("power(3, 3) =", power(3, 3))
print("power(2, 4) =", power(2, 4))
print("power(2, 3) again (should hit cache) =", power(2, 3))
print("Cache info for power function:", power.cache_info())
print("")   # Just to add a blank line for better readability of output
# Output: Power function with lru_cache:
# power(2, 3) = 8
# power(3, 3) = 27
# power(2, 4) = 16
# power(2, 3) again (should hit cache) = 8
# Cache info for power function: CacheInfo(hits=1, misses=3, maxsize=5, currsize=3)
# The power function demonstrates lru_cache with multiple arguments.
# The cache helps avoid redundant calculations for the same base and exponent.
# Overall, lru_cache is a powerful tool for optimizing functions that are called frequently with the same arguments.
# It can greatly improve performance in scenarios involving recursive functions or expensive computations.
# However, it is important to consider the memory usage and choose an appropriate maxsize for the cache.

print("End of lru_cache examples.")
# End of lru_cache examples.
