# Variant 8: Binary Search Using a For Loop

This variant utilizes a `for` loop instead of the more common `while` loop. The `for` loop iterates a fixed number of times (equal to the length of the array), which is somewhat unconventional for binary search. The loop breaks early if the search space is exhausted (`left > right`). This variant highlights an alternative way to structure the iteration process.

### Characteristics:
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Iterative, unconventional use of `for` loop
