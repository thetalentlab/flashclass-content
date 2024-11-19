# an implementation of binary search
*code manipulates DATA*

<br>

```python {1|3|4|6|11,17}
def binary_search(phonebook, name):    # data being "received" by the machine

    left = 0                           # data being assigned
    right = len(phonebook) - 1         # data being discovered, calculated and assigned

    while left <= right:               # data being compared

        mid = (left + right) // 2

        if phonebook[mid] == name:
            return mid                 # data being "sent back" from the machine (on success)
        elif phonebook[mid] < name:
            left = mid + 1
        else:
            right = mid - 1

    return -1                          # data being "sent back" from the machine (on failure)
```
