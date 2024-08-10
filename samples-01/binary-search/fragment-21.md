# Binary Search Using a Generator

This variant of binary search uses a generator function to perform the search. The generator `search_gen` yields the index of the target if found, or `-1` if not. Using a generator allows for a more flexible control flow, especially useful if you want to extend this search to handle more complex cases or to integrate with other generator-based workflows.

### Characteristics:
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Iterative, uses a generator for flow control
