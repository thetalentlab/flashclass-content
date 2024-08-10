def reverse_string(s):
    reversed_s = ""
    for i in range(len(s)):
        reversed_s = s[i:i+1] + reversed_s
    return reversed_s
