def binary_search(haystack, needle):
    left = 0
    right = len(haystack) - 1

    """
    Binary Search works by splitting the array in half.

    The midpoint is the center element between the left and right pointers, calculated as:
    """

    # repeat as long as LEFT is less than or equal to RIGHT
    while left <= right:
        # Calculate the midpoint
        mid = left + (right - left) // 2

    """
    LEFT is 0  (the first position, value 2 in this example)
    RIGHT is 8 (the last position, value 23 in this example)

    MID is (0 + 8) // 2 = 4 (the middle position, value 11 in this example)

    [2, 3, 5, 7, 11, 13, 17, 19, 23]
                 ^
                mid
    """