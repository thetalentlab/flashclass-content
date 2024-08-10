def reverse_string(s):
    stack = list(s)
    reversed_s = []
    while stack:
        reversed_s.append(stack.pop())
    return ''.join(reversed_s)
