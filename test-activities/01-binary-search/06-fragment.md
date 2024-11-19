# an implementation of binary search
*this is one of many possible implementations of binary search*

<br>

```python
def binary_search(phonebook, name):

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
