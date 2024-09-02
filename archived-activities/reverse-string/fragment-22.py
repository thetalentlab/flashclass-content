from functools import reduce

def reverse_string(s):
    return reduce(lambda acc, char: char + acc, s, "")
