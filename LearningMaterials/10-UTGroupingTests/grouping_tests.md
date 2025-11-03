# Unit Testing: Grouping Tests

Sometimes we want to group tests to run specific subsets of our test suite, whether it's based on certain criteria or characteristics. Pytest provides various mechanisms to accomplish this, such as substring matching of test names and using markers.

Before going into these mechanisms, let's make the following changes to our maths project.

In `project.src.math_operations` add the following functions:

```Python
def power(arg1: float, arg2: float):
    return arg1 ** arg2

def modulo(arg1: int, arg2: int):
    return arg1 % arg2

def absolute_value(arg):
    return abs(arg)
```

In `project.tests.test_math_operations`:

- change the beginning imports to look like this:

```Python
import pytest
from src.math_operations import add, subtract, multiply, divide, power, modulo, absolute_value
```

- add `_basic` in the names for the first four tests (i.e `test_add` becomes `test_basic_add`)
- add the following functions:
  
```Python
def test_advanced_power():
    # Arrange
    input_value1 = 2
    input_value2 = 3
    expected_value = 8

    # Act
    actual_value = power(input_value1, input_value2)

    # Assert
    assert actual_value == expected_value


def test_advanced_modulo():
    # Arrange
    input_value1 = 10
    input_value2 = 3
    expected_value = 1

    # Act
    actual_value = modulo(input_value1, input_value2)

    # Assert
    assert actual_value == expected_value


def test_advanced_absolute():
    # Arrange
    input_value = -10
    expected_value = 10

    # Act
    actual_value = absolute_value(input_value)

    # Assert
    assert actual_value == expected_value

```

## Substring Matching of Test Names

To run specific tests containing a particular string in their names, you can use the following syntax:

``` text
python -m pytest -k <substring>
```

In this command, `-k <substring>` denotes the substring to search for within the test names.

For instance, to run tests featuring the term 'basic' in their names, execute:

``` text
python -m pytest -k basic
```

Every test which contains the substring `basic` will be run, i.e in the collection phase it will only collect the tests:

- `test_basic_add`
- `test_basic_subtract`
- `test_basic_multiply`
- `test_basic_divide`

## Using Markers

A more sophisticated way to group tests is to use pytest's markers.  
In pytest, markers allow you to add metadata to your tests, and we will see here that this can make it easy to run group tests depending on their marker.
We will see later that markers have extra functionality on top of just being able to group tests together.

Markers can be applied at the test function level using the `@pytest.mark` decorator. This allows you to assign one or more markers to individual test functions, indicating their characteristics or properties. For example, you might use markers to denote the priority level of tests, the environment in which they should run (such as "development" or "production"), the speed it would take to run the test, or any other relevant categorisation. Once tests have these markers you can make sure you only run the tests which are labelled as highest priority for example.

The syntax to apply a marker to test function is as follows:

```Python
import pytest
@pytest.mark.marker_name
def test_function_name():
    # Test code goes here
    pass
```

You can replace `marker_name` with the name of the marker you want to apply, and `test_function_name` with the name of your test function.
This decorator adds metadata to the test function, enabling you to categorise and group tests based on different criteria.

(Note: we have to import `pytest` in the module so that we can access the `pytest.mark` module for applying markers to test functions.)

Then, to execute tests associated with a certain marker, you can use the following syntax:

``` text
pytest -m <marker_name>
```

**Note**: if you ever want to see further information from running pytest you can add the `-v` (verbose) option (or `-vv` for further details).

``` text
pytest -v
```

In our current case you could do the follows:

``` text
pytest -m <marker_name> -v
```

### Concept Check

- remove the `_basic` in the first four test functions
- remove the `_advanced` in the final three test functions
- mark the appropriate tests as `basic` and `advanced`
- using the markers run pytest on test functions categorised as basic, and then again on advanced - run it with the -vv flag

Above we created our own custom markers. It is recommended to register markers for your test suite and to do this it's as simple as creating a file `pytest.ini` in your root directory with the following contents:

``` text
[pytest]
markers =
    basic: mark a test as testing a basic math function.
    advanced: mark a test as testing a basic math function.
```

Whilst you do not have to register markers, the reasons it'ss recommended is so that:

- It provides clarity and documentation as to what the markers are  
- Typos in function markers are treated as an error if you use the --strict-markers flag from the command line or add `addopts = "--strict-markers"` to the `pytest.ini` file.

Pytest also provides several built-in markers that offer additional functionalities. To see the markers available in your test suits run the following:

``` text
pytest --markers
```

You will see our custom markers which we registered, (note: had we not reistered them, they would not be available in this output), as well as all the built in markers, including `xfail`, `skip` and `parametrize`. We will discuss `parametrize` in greater detail in the next unit.

### xfail

`xfail`: This marker stands for "expected failure". It marks a test that is expected to fail. If the test passes, it is reported as an unexpected success.

```Python
import pytest

@pytest.mark.xfail
def test_something():
    assert 1 == 2
```

### skip

`skip`: This marker skips the test without executing it. It is useful when a test is not ready or applicable under certain conditions.

```Python
import pytest

@pytest.mark.skip(reason="Test is not implemented yet")
def test_my_feature():
    assert 1 == 2
```
