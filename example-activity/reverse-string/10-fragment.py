def reverse_string(s):
    return ''.join(map(lambda x: s[-x-1], range(len(s))))
