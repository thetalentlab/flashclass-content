# Variant 10: Binary Search Using the `reduce` Function

In this variant, the binary search algorithm is implemented using Python's `reduce` function from the `functools` module. The `reducer` function calculates the mid-point and adjusts the search boundaries. The `reduce` function iterates over a range object, simulating the search process. The final boundaries are used to determine if the `target` was found. This approach demonstrates a functional programming style, applying the `reduce` function to a problem typically solved with loops or recursion.

### Characteristics:
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Functional programming using `reduce`
