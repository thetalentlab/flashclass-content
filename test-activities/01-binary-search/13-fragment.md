# an implementation of binary search
*code repeats in LOOPS*

<br>

```python {6|6-15|6}
def binary_search(phonebook, name):

    left = 0
    right = len(phonebook) - 1

    while left <= right:               # a loop, "while left is less than or equal to right"

        mid = (left + right) // 2

        if phonebook[mid] == name:
            return mid
        elif phonebook[mid] < name:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```
