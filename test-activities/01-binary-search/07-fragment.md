# an implementation of binary search
*the function signature specifies the name and inputs of the "machine"*

<br>

```python {1}
def binary_search(phonebook, name):    # function signature

    left = 0
    right = len(phonebook) - 1

    while left <= right:

        mid = (left + right) // 2

        if phonebook[mid] == name:
            return mid
        elif phonebook[mid] < name:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```
