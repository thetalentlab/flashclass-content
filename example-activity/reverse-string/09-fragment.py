from collections import deque

def reverse_string(s):
    d = deque(s)
    reversed_s = ''
    while d:
        reversed_s += d.pop()
    return reversed_s
