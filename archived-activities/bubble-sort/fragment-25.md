# Variant 25: Bubble Sort with a Rolling Window of Comparisons

This variant of bubble sort compares elements within a rolling window of a fixed size (default is 3) and sorts them in-place. The window moves along the array, performing local sorts. This approach introduces a localized sorting mechanism within the broader bubble sort process, though it doesn't change the overall time complexity.

### Characteristics:
- **Time Complexity:** O(n^2)
- **Space Complexity:** O(1)
- **Style:** Iterative, uses rolling window for local sorting
