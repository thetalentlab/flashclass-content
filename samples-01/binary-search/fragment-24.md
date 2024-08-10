# Binary Search with Simulated Tail Call Optimization

This variant mimics tail call optimization (TCO) by converting the recursive calls into a loop. Instead of a true recursive function, the loop updates the parameters (`left` and `right`) until the base case is met. This approach avoids the potential pitfalls of deep recursion, like stack overflow, and keeps the code more efficient in terms of space.

### Characteristics:
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Iterative, mimics tail call optimization
