def reverse_string(s):
    return ''.join(x for x, _ in zip(s[::-1], s))
