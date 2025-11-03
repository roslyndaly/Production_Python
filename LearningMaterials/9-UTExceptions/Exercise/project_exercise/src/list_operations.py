from typing import Union, Any

def get_element_by_index(input_list: list, index: Union[int, float, bool, str]) -> Any:
    """
    Get the element from the input list at the specified index.

    Args:
    - input_list: A list containing elements.
    - index: An integer, float, bool, or string representing the index of the element to retrieve.

    Returns:
    - The element at the specified index.

    Raises:
    - TypeError: If the input_list is not a list or if the index is not an integer, float, bool, or string.
    - ValueError: If the index value is not a valid value.
    - IndexError: If the index is out of range.
    """
    if type(input_list) != list:
        raise TypeError("input_list must be a list")

    if type(index) not in [int, float, bool, str]:
        raise TypeError("index must be an integer, float, bool, or string")

    # Convert index to appropriate type if it's a string
    try:
        index_int = int(index)
        if type(index) == float and index_int != index:
                raise ValueError()
    except ValueError:
        raise ValueError("index must be a valid value")

    # Check if index is out of range
    if index_int < -len(input_list) or index_int >= len(input_list):
        raise IndexError("index is out of range")

    # Return the element at the specified index
    return input_list[index_int]
