from functools import partial

def reverse_string(s):
    return ''.join(map(partial(str.__getitem__, s[::-1]), range(len(s))))
