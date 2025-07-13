import random
import time

def partition(arr, pivot):
    """Partition arr into elements less than, equal to, and greater than pivot."""
    low, equal, high = [], [], []
    for x in arr:
        if x < pivot:
            low.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            high.append(x)
    return low, equal, high

def randomized_select(arr, k):
    if not arr or k < 1 or k > len(arr):
        raise ValueError("k is out of bounds for the input array.")

    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    low, equal, high = partition(arr, pivot)

    if k <= len(low):
        return randomized_select(low, k)
    elif k <= len(low) + len(equal):
        return pivot
    else:
        return randomized_select(high, k - len(low) - len(equal))

def test_performance():
    sizes = [10, 20, 40]
    for n in sizes:
        print(f"\nArray size: {n}")
        k = n // 2

        # Random array
        arr_random = [random.randint(1, n) for _ in range(n)]
        start = time.perf_counter()
        randomized_select(arr_random, k)
        print(f"Random array: {time.perf_counter() - start:.6f} seconds")

        # Sorted array
        arr_sorted = list(range(1, n + 1))
        start = time.perf_counter()
        randomized_select(arr_sorted, k)
        print(f"Sorted array: {time.perf_counter() - start:.6f} seconds")

        # Reverse-sorted array
        arr_reverse = list(range(n, 0, -1))
        start = time.perf_counter()
        randomized_select(arr_reverse, k)
        print(f"Reverse-sorted array: {time.perf_counter() - start:.6f} seconds")

if __name__ == "__main__":
    array = [12, 3, 5, 7, 4, 19, 26, 23, 2, 11, 6, 13, 5, 5, 7]
    k = 5
    try:
        result = randomized_select(array, k)
        print(f"The {k}-th smallest element is {result}")
    except ValueError as e:
        print(e)

    # Performance testing
    test_performance()