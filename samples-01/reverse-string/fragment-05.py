def reverse_string(s):
    s_list = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1
    return ''.join(s_list)
