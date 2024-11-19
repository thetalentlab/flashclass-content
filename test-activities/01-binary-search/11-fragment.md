# an implementation of binary search
*code makes DECISIONS*

<br>

```python {10|12|14}
def binary_search(phonebook, name):

    left = 0
    right = len(phonebook) - 1

    while left <= right:

        mid = (left + right) // 2

        if phonebook[mid] == name:     # a decision, "if the value in the middle of the phonebook is equal to the name"
            return mid
        elif phonebook[mid] < name:    # a decision, "if the value at mid is less than (ie. comes before) the name"
            left = mid + 1
        else:                          # a decision, "otherwise (ie. value at mid is neither equal nor less, but greater)"
            right = mid - 1

    return -1
```
