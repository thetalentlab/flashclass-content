def reverse_string(s):
    reversed_list = []
    for char in s:
        reversed_list.insert(0, char)
    return ''.join(reversed_list)
