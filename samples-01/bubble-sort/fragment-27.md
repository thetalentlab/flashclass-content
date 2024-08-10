# Variant 27: Bubble Sort with Probabilistic Swaps

This variant introduces randomness into the bubble sort process by making swaps probabilistic. A swap occurs only if the elements are out of order and a randomly generated number is below a certain threshold. This approach makes the sorting process less deterministic, which can be interesting for experimentation, though it generally doesn't improve performance.

### Characteristics:
- **Time Complexity:** O(n^2)
- **Space Complexity:** O(1)
- **Style:** Iterative, probabilistic swaps
