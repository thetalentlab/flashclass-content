# Variant 17: Bubble Sort Using Bidirectional Scanning

This variant of bubble sort scans the array in both directions during each iteration, first bubbling the largest element to the end and then bubbling the smallest element to the beginning. This "cocktail shaker" approach can reduce the number of passes needed for nearly sorted arrays, though it does not improve the worst-case time complexity.

### Characteristics:
- **Time Complexity:** O(n^2)
- **Space Complexity:** O(1)
- **Style:** Iterative, bidirectional scanning (cocktail shaker sort)
