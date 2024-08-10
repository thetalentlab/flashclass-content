def reverse_string(s):
    return ''.join(map(lambda i: s[-i], range(1, len(s)+1)))
