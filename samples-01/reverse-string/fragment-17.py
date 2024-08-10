from collections import deque

def reverse_string(s):
    d = deque(s)
    return ''.join([d.pop() for _ in range(len(d))])
