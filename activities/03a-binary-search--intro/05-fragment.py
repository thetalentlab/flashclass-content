"""

Once we have the midpoint, we compare it to the target value:

- If the midpoint value matches the target, we have found the element.
- If the midpoint value is less than the target, the target must be in the right half.
- If the midpoint value is greater than the target, the target must be in the left half.

"""
def binary_search(haystack, needle):
    left = 0
    right = len(haystack) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # if the needle is in the middle of the haystack
        if haystack[mid] == needle:
            return mid  # we found the target! here is the location of the needle in the haystack.

        # if the needle is smaller than the value at the middle of the haystack
        elif haystack[mid] < needle:
            left = mid + 1  # then we need to search in the right half

        # otherwise (the needle is bigger than the value at the middle of the haystack)
        else:
            right = mid - 1  # then we need to search in the left half
