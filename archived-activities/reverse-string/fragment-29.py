def reverse_string(s):
    def gen():
        for i in range(len(s)-1, -1, -1):
            yield s[i]
    return ''.join(gen())
