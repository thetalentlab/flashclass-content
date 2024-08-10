from functools import reduce

def binary_search(arr, target):
    def reducer(acc, x):
        if acc[0] > acc[1]:
            return acc
        mid = (acc[0] + acc[1]) // 2
        if arr[mid] == target:
            return (mid, mid)
        elif arr[mid] < target:
            return (mid + 1, acc[1])
        else:
            return (acc[0], mid - 1)

    left, right = reduce(reducer, range(len(arr)), (0, len(arr) - 1))
    return left if left <= right and arr[left] == target else -1
