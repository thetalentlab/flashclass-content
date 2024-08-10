# Binary Search with a Lookup Table for Midpoints

In this variant, a lookup table is created for the midpoint calculations. The table is indexed by the sum of `left` and `right` indices, precomputing the midpoints to avoid recalculating them during the search. This approach is a bit unconventional and adds some overhead in terms of space but can illustrate the concept of trading off space for potentially faster lookup times.

### Characteristics:
- **Time Complexity:** O(log n)
- **Space Complexity:** O(n) due to the lookup table
- **Style:** Iterative, uses a precomputed lookup table
