# Parameterized Tests

Parameterized tests in pytest allow you to run the same test function with multiple sets of input parameters, which is great for reducing code duplication.

We introduced the pytest decorator `@pytest.mark` in the previous unit and saw that it had an in-built marker `@pytest.mark.parametrize`. This marker allows us to dynamically generate multiple test cases by providing different input parameter values.

When testing functions, it is best practice to test the function with a variety of test cases in order to to ensure their robustness and reliability.

In our project however, each function is only tested against one set of input arguments. For example, we only test the `add` function with the inputs `10` and `20` ensuring that the output is `30`. This is not a very comprhensive test of our `add` function and may overlook potential edge cases or bugs.

To address this limitation, one might consider defining multiple test functions, each testing the function with different inputs against their respective expected outputs. However, this approach would lead to significant code duplication and maintenance overhead.

This is where parameterized testing comes into play.  

## Using `@pytest.mark.parametrize`

In order to parametrize a test, we use the `@pytest.mark.parametrize` decorator above the test function. A simple use case of a the decorator typically takes the following arguments:

- **Parameter and Return Names String**: A string containing parameter names and the expected value separated by commas. It serves as a placeholder for the input parameters and the expected result in each test case. This string is used to specify the names of the parameters that will be passed to the test function. For example, `"param1, param2, ..., expected_result"`.
- **Parameter and Return Values List**: This is a list of tuples, where each tuple represents a set of input parameters and the corresponding expected result for one test case. Each tuple should contain values corresponding to the parameter names specified in the parameter names string. For example, `[(value1_1, value1_2, ..., expected_result1), (value2_1, value2_2, ..., expected_result2), ...]`. The number of elements in each tuple must match the number of parameters specified in the parameter names string. Additionally, the number of tuples in the list determines the number of test cases that will be generated.

Parametrizing the `test_add` function would look something like this (we have left the marker of `@pytest.mark.basic` in this example, but a parametrized test fuction does not need another marker):

```Python
@pytest.mark.parametrize("input_value1, input_value2, expected_value", [
    (10, 20, 30),
    (-5, -2, -7),
    (0, 0, 0),
    (-10, 10, 0),
])
@pytest.mark.basic
def test_add(input_value1, input_value2, expected_value):
    # Act
    actual_value = add(input_value1, input_value2)

    # Assert
    assert actual_value == expected_value
```

If you now run:

``` text
pytest -vv
```

You will see the that pytest executed the `test_add` function four times, once for each test case defined in the parameter values list. The more verbose output displays detailed information about each test case execution, confirming that the `test_add` function has been successfully parameterized and executed for all specified input/output cases.

## Concept Check

- Parametrize the other tests.

## Test IDs in Parameterized Tests

In pytest, when you use parametrized tests, pytest constructs a unique string known as the test ID for each set of values provided. These test IDs are useful for identifying the specific case when a test fails. If you run pytest with the `--collect-only` flag, it will display the generated test IDs.

For numbers, strings, booleans, and None, pytest utilises their standard string representations in the test ID. However, for other objects, pytest generates a string based on the argument name.

However, it may be more useful to give each test in the parameterized test its own ID. We can either do this by passing a third argument in the decorator `ids` which will be a list of the different IDs for each test function:

```Python
@pytest.mark.parametrize("input_value1, input_value2, expected_value", [
    (10, 20, 30),
    (-5, -2, -7),
    (0, 0, 0),
    (-10, 10, 0)], 
ids=["Addition of positive numbers", 
    "Addition of negative numbers", 
    "Addition of zeros", 
    "Addition of positive and negative numbers"])
@pytest.mark.basic
def test_add(input_value1, input_value2, expected_value):
    # Act
    actual_value = add(input_value1, input_value2)

    # Assert
    assert actual_value == expected_value
```

A neater way to do this is by using `pytest.param(..., id = "...")`. This is a way to define individual test cases within the `@pytest.mark.parametrize` decorator. It allows you to specify the input values for each parameter and the expected output value, along with a custom ID for the test case. For example:

```Python
@pytest.mark.parametrize(
    "a,b,expected",
    [pytest.param(10, 20, 30, 
                id="Addition of positive numbers"),
    pytest.param(-5, -2, -7, 
                id="Addition of negative numbers"),
    pytest.param(0, 0, 0, 
                id="Addition of zeros"),
    pytest.param(-10, 10, 0, 
                id="Addition of positive and negative numbers")])
@pytest.mark.basic
def test_add(a, b, expected):
    # Act
    actual_value = add(a, b)

    # Assert
    assert actual_value == expected
```

## Custom Test IDs Concept Check

- Give IDs to all other parametrized tests.
