from collections import deque

def bubble_sort(arr):
    q = deque(arr)
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if q[j] > q[j+1]:
                q[j], q[j+1] = q[j+1], q[j]
    return list(q)
