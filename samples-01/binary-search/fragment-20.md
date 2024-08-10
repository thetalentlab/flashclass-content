# Binary Search Using a Dictionary for Index Lookup

In this variant, a dictionary is used to map each value in the array to its index, enabling O(1) index lookup. The binary search itself remains the same, but instead of returning the index directly from the array, it is fetched from the dictionary. This approach is more of a hybrid technique, showcasing how dictionaries can be integrated into traditional search algorithms for quick lookups.

### Characteristics:
- **Time Complexity:** O(log n) for the search, O(1) for the lookup
- **Space Complexity:** O(n) due to the dictionary
- **Style:** Iterative, hybrid with dictionary-based lookup
