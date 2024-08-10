# Binary Search Using Lambda Functions

This variant of binary search is implemented using lambda functions for a more compact and functional approach. The `search` lambda recursively calls itself, making decisions about the search space in a more succinct way. The use of the walrus operator (`:=`) in the lambda function allows the midpoint to be calculated and used within the same expression.

### Characteristics:
- **Time Complexity:** O(log n)
- **Space Complexity:** O(log n) due to recursive stack
- **Style:** Functional, concise lambda expressions
