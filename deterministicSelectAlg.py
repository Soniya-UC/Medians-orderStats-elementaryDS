import time
import random

def deterministic_select(arr, k):

    if not arr or k < 1 or k > len(arr):
        raise ValueError("k is out of bounds for the input array.")
    
    if len(arr) <= 5:
        return sorted(arr)[k - 1]

    # divide the input array, arr, into smaller sublists 
    chunks = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    # process each chunk to find its median, create a list of medians
    medians = [sorted(chunk)[len(chunk) // 2] for chunk in chunks]
    # Recursively find the median of medians
    pivot = deterministic_select(medians, len(medians) // 2 + 1)

    # Partition the array into < pivot, == pivot, > pivot
    low = [el for el in arr if el < pivot]
    high = [el for el in arr if el > pivot]
    # Count for duplicates of pivot
    count = arr.count(pivot)  

    # Recurse in the appropriate partition
    if k <= len(low):
        return deterministic_select(low, k)
    elif k > len(low) + count:
        return deterministic_select(high, k - len(low) - count)
    else:
        return pivot 

def test_performance():
    sizes = [10, 20, 40]
    for n in sizes:
        print(f"\nArray size: {n}")
        k = n // 2

        # Random array
        arr_random = [random.randint(1, n) for _ in range(n)]
        start = time.perf_counter()
        deterministic_select(arr_random, k)
        print(f"Random array: {time.perf_counter() - start:.6f} seconds")

        # Sorted array
        arr_sorted = list(range(1, n + 1))
        start = time.perf_counter()
        deterministic_select(arr_sorted, k)
        print(f"Sorted array: {time.perf_counter() - start:.6f} seconds")

        # Reverse-sorted array
        arr_reverse = list(range(n, 0, -1))
        start = time.perf_counter()
        deterministic_select(arr_reverse, k)
        print(f"Reverse-sorted array: {time.perf_counter() - start:.6f} seconds")

if __name__ == "__main__":
    array = [12, 3, 5, 7, 4, 19, 26, 23, 2, 11, 6, 13, 5, 5, 7]
    k = 5
    try:
        result = deterministic_select(array, k)
        print(f"The {k}-th smallest element is {result}")
    except ValueError as e:
        print(e)

    # Performance testing
    test_performance()