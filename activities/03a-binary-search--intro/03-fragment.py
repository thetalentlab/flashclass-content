"""

A sorted array is the required input to the binary search algorithm.

Sorted array: [2, 3, 5, 7, 11, 13, 17, 19, 23]

Search target: 13  <-- this is the number we want to find



Binary search machine at the very beginning of the algorithm:

   [2, 3, 5, 7, 11, 13, 17, 19, 23]
    ^                           ^
  left                        right



In Binary Search, we maintain two pointers, left and right, to define the current bounds of the search. \\

Initially, left starts at the beginning of the array, and right starts at the end.

These pointers help narrow down the search space.

"""

def binary_search(haystack, needle):
    # Initialize the left and right pointers

    # left is at the first position and we usually start counting at 0
    left = 0

    # right is the last position, then length minus 1 since we started at 0
    right = len(haystack) - 1
