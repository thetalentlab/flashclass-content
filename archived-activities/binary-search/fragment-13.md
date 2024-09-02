# Binary Search Using Object-Oriented Programming (OOP)

## Summary

This OOP-based approach demonstrates how binary search functionality can be encapsulated within a class, promoting reusability and extensibility. The structure allows the binary search to be easily integrated into larger systems, adhering to principles of object-oriented programming such as encapsulation and abstraction.

## Description

This variant implements binary search using an object-oriented approach. The `BinarySearch` class encapsulates the array and provides a `search` method to perform the binary search. This structure allows for the binary search functionality to be reused and extended, demonstrating the principles of encapsulation and abstraction in OOP.

## Explanation

1. **Class Definition**:
   - The `BinarySearch` class encapsulates the array (`arr`) as an instance variable, making it accessible within the class methods.

2. **Constructor (`__init__`)**:
   - The constructor method initializes the class with the array and stores it as an instance variable (`self.arr`).

3. **Search Method**:
   - The `search` method implements the binary search algorithm, using the instance variable `self.arr` to access the array.
   - The method initializes the `left` and `right` pointers to define the search boundaries.

4. **Midpoint Calculation and Target Comparison**:
   - The midpoint is calculated with `mid = left + (right - left) // 2`.
   - If `self.arr[mid]` matches the `target`, the method returns the index `mid`.
   - If `target` is greater than `self.arr[mid]`, the search continues in the right half by adjusting the `left` pointer.
   - If `target` is smaller, the search continues in the left half by adjusting the `right` pointer.

5. **Return Value**:
   - If the loop completes without finding the `target`, the method returns `-1`, indicating that the target is not present in the array.

6. **Example Usage**:
   - An instance of `BinarySearch` is created with an array, and the `search` method is called to find the index of the `target`.

## Characteristics

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Style:** Object-oriented programming, reusable and extensible
