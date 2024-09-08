"""

The search process continues, adjusting the left and right pointers until

1. either the target is found, or
2. the search space becomes invalid (left exceeds right).

If the target is not found by the end of the loop, we return -1 to indicate failure.

"""

def binary_search(haystack, needle):
    left = 0
    right = len(haystack) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if haystack[mid] == needle:
            return mid
        elif haystack[mid] < needle:
            left = mid + 1
        else:
            right = mid - 1

    # if we got this far, the loop has terminated because the target was not found
    return -1  # it's common to return -1 to indicate "target not found"
