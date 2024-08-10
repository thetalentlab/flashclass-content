# Binary Search with a While-Else Loop

This variant introduces a slight modification to the iterative binary search by utilizing a `while-else` loop. The `else` block executes if the `while` loop completes without encountering a `break` statement. This is particularly useful here to return `-1` when the search completes without finding the target. The core logic remains the same, but this approach emphasizes the use of Python's unique `while-else` construct, which is less commonly used in basic binary search implementations.

### Characteristics:
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Iterative, procedural with a Pythonic twist
