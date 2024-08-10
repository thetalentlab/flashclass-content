# Variant 26: Bubble Sort with Dynamic Window Resizing

This variant builds on the rolling window approach by dynamically resizing the window with each pass. The window starts small and grows as the algorithm progresses, allowing for progressively larger portions of the array to be sorted locally. This approach introduces a different way of handling the sorting process, though it remains O(n^2) in time complexity.

### Characteristics:
- **Time Complexity:** O(n^2)
- **Space Complexity:** O(1)
- **Style:** Iterative, uses dynamic window resizing
