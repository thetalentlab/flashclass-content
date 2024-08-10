# Binary Search Using Deque for Stack-Like Behavior

This variant of binary search uses a `deque` from the `collections` module to simulate stack behavior. The `deque` is used to store the left and right indices during the search process, mimicking recursion but in an iterative manner. This approach highlights the flexibility of Python's `collections` module in implementing different data structures for algorithmic purposes.

### Characteristics:
- **Time Complexity:** O(log n)
- **Space Complexity:** O(log n) due to the deque
- **Style:** Iterative, stack simulation using deque
