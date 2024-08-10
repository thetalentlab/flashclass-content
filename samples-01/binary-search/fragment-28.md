# Variant 28: Binary Search with Early Exit if Mid is Not Promising

This variant introduces an early exit condition if the `mid` value is at the boundaries (`left` or `right`) and doesn't match the target. This slight optimization helps to cut the search short in cases where it's clear that further searching won't yield the target, particularly in edge cases.

### Characteristics:
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Iterative, early exit optimization
