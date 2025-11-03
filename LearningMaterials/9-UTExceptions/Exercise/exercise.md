# Unit Testing Exceptions Exercise

## Exercise: List Operations

Create a project of this structure:

``` text
project/
│
├── src/
│   ├── __init__.py
│   └── list_operations.py
│
└── tests/
    ├── __init__.py
    └── test_list_operations.py
```

Suppose you have a function `get_element_by_index()` in the `src.list_operations` module. This function takes a list and an index as arguments and returns the element at the specified index. The function should have the functionality to accept the index as an integer, float, bool, or string (as long as it represents a valid index, i.e the string `"1"` would represent a valid index, but `"hello"` would not, or the float `1.0` would represent a valid index, but `1.5` would not.). However, the function should raise different exceptions for different scenarios:

- It should raise a `TypeError` if the input is not a list.
- It should raise a `TypeError` if the index is not an integer, float, bool, or string.
- It should raise a `ValueError` if the index value does not correspond to a valid index.
- It should raise an `IndexError` if the index is out of range.

Your task is to write test functions in the `tests.test_list_operations` module to verify that `get_element_by_index()` correctly raises the appropriate exceptions for each scenario.
