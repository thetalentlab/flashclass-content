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

There should be only one file named manifest.yaml in one activity. There can be sevaral activities though.

`manifest.yaml`

```yaml
title: Binary Search
random: true
```
There can be multiple pairs of fragment.py and metadata.yaml files in one activity folder.
Other than .py some other file extensions are also supported that includes .ts .js and .md

But the pair should be like this. Example.
- 01-fragment.py and 01-metadata.yaml
- 01-fragment.md and 01-metadata.yaml
- 01-fragment.ts and 01-metadata.yaml

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
```
