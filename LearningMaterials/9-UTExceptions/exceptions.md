# Testing for Exceptions

In unit 5, we wrote several simple unit tests for the functions in `src.math_operations`.

We used `assert` statements to check that the actual output to the expected output. We saw that a test fails if the test function runs into an exception during execution, and passes if the test function makes it way to the end of the function logic. However, what if the behavior we're testing is whether a function raises an exception under certain conditions? We cannot just call the function in our test function with those conditions as we have seen before, as this would raise an exception (if the source function has been witeen correctly). Luckily, pytest provides robust mechanisms to facilitate this.

## Understanding Exception Testing

In our `src.math_operations` module, we have defined various mathematical operations, including `divide()` which should raise a `ZeroDivisionError` if `arg2 == 0`.  

If we were to define a test function as follows:

```Python
def test_divide_zero_division():
    # Arrange 
    input_value_1 = 10
    input_value_2 = 0
    expected_value = ZeroDivisionError('arg2 cannot be 0, since you cannot divide by 0')

    # Act
    actual_output = divide(input_value_1, input_value_2)
    
    # Assert
    assert actual_output == expected_output
```

Then whenever this test executed, this line `actual_output = divide(input_value_1, input_value_2)`, specifically the function call, will raise a `ZeroDivisionError`. Which will mean the test function will not make it's way to the end of the function call and fail the test.

To properly handle testing for exceptions in pytest, you can use the `pytest.raises()` context manager, passing through the brackets the specifc type of Exception you are expecting. The general syntax of using `pytest.raises()` is as follows:

```Python
import pytest

def test_function_name():
    with pytest.raises(ExpectedException):
        # Code block expected to raise ExpectedException
```

Here `pytest.raises(ExpectedException)` is a context manager provided by pytest specifically for testing exceptions. Inside the with block, you execute the code that is expected to raise the specified exception.
If the expected exception is raised during the execution of the code block, `pytest.raises` does not raise an `AssertionError`, and the test passes. If the expected exception is not raised, `pytest.raises` raises an `AssertionError` and the test will fail.

In our project, we can use the abpve syntax to check whether calling `divide` raises a `ZeroDivisionError` as follows:

```Python
def test_divide_zero_division():
    # Arrange 
    input_value_1 = 10
    input_value_2 = 0
    
    # Act & Assert
    with pytest.raises(ZeroDivisionError):
        divide(input_value_1, input_value_2)
```

In this updated version, the with `pytest.raises(ZeroDivisionError):` block encapsulates the function call `divide(input_value_1, input_value_2)`. If this function call raises a `ZeroDivisionError`, the test will pass. If the exception is not raised, the test will fail. This ensures that your test function properly handles the expected exception without prematurely failing due to the exception being raised.
