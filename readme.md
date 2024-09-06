# Code Samples for flashclass

this repo is used as input to load flashclass content with a script that is run manually

> the script is here:
> https://github.com/thetalentlab/flashclass/blob/main/scripts/extractFragmentsFromDirectory.ts
>
> and depends on these utilities for a single method `runFragmentSyncScript`:
> https://github.com/thetalentlab/flashclass/blob/main/src/utils/scriptsUtils.ts

- there is 1 important folder in this repo called `activities`
- there is also an `archived-activities` folder to keep working files from previous iterations

# Activity Format

`manifest.yaml`

```yaml
title: Binary Search
description: Binary Search is a search algorithm that finds the position of a target value within a sorted array.
instructions:
  - pages:
    - text: "In this activity we will show you a lot of code"
    - text: "Relax and just look at the code; let your brain do the work."
random: true
```

`##-fragment.py`

```py
def binary_search(arr, target):
    # Initialize the left and right pointers
    left, right = 0, len(arr) - 1
    # ... rest of code here
```

`##-metadata.yaml`

```yaml
description: Binary Search is a search algorithm that finds the position of a target value within a sorted array.
language: Python
```
