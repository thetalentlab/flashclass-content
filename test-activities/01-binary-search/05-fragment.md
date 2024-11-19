# the structure of binary search
*any implementation is likely to have the same basic structure*

<br>

```python {all|1|3|4|8|10-11,17|all}
def binary_search(phonebook, name):    # a machine that accepts the phonebook and the name to search for

    left = 0                           # remember the start of the phonebook
    right = len(phonebook) - 1         # remember the end of the phonebook



        mid = (left + right) // 2      # remember the middle of the phonebook

        if phonebook[mid] == name:     # if the middle of the phonebook has the name we're looking for ...
            return mid                 #   return the middle position if we found the name





    return -1                          #   return -1 if we didn't find the name
```
<br>

<div style="position: absolute" v-click="[1]">a function is a named collection of individual lines of code</div>
<div style="position: absolute" v-click="[2,5]">variables capture the basic structure of the phonebook</div>
<div style="position: absolute" v-click="[5]">logic is used to make decisions</div>
