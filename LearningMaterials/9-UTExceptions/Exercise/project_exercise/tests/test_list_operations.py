import pytest
from src.list_operations import get_element_by_index


def test_get_element_by_index_input1_not_list():
    # Arrange
    input_val1 = 123
    input_val2 = 0

    # Act and assert 
    with pytest.raises(TypeError):
        get_element_by_index(input_val1, input_val2)



def test_get_element_by_index_input2_not_valid_type():
    # Arrange
    input_val1 = [123, 456]
    input_val2 = {1}

    # Act and assert 
    with pytest.raises(TypeError):
        get_element_by_index(input_val1, input_val2)


def test_get_element_by_index_not_valid_index_value():
    # Arrange
    input_val1 = [123, 456]
    input_val2 = "hello"

    # Act and assert 
    with pytest.raises(ValueError):
        get_element_by_index(input_val1, input_val2)

def test_get_element_by_index_index_error_out_of_range():
    # Arrange
    input_val1 = [123, 456]
    input_val2 = 3

    # Act and assert 
    with pytest.raises(IndexError):
        get_element_by_index(input_val1, input_val2)


    

