from functools import reduce

def reverse_string(s):
    return reduce(lambda x, y: y + x, s)
