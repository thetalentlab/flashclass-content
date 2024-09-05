def reverse_string(s, acc=""):
    if not s:
        return acc
    return reverse_string(s[:-1], acc + s[-1])
