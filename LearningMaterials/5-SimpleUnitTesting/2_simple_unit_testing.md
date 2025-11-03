# Writing Simple Tests Using pytest

Pytest is a widely-used Python testing framework that simplifies the process of writing and executing automated tests. It offers a straightforward syntax and powerful features for testing Python code, making it a popular choice among developers.

## Getting Started with pytest

1. **Install pytest**

    Before you can start writing tests with pytest, you'll need to install the pytest package

    ``` shell
    pip install pytest
    ```

2. **Create First Test**

    Begin by creating a new Python file called `test_math_operations.py`. In this file, define a function and a corresponding test function using pytest's syntax (we will explain this syntax momentarily):

    ```Python
    # test_math_operations.py
    def add(arg1, arg2):
        return arg1 + arg2


    def test_add():
        assert add(10, 20) == 30
        
    ```

3. **Running Tests with pytest**

    Once you've written your test, you can execute it using the pytest command. Simply navigate to the directory containing your test file (`test_math_operations.py` in this case) and run pytest:

    ``` shell
    pytest
    ```

    Pytest will automatically discover and execute any test functions defined within your project directory and its subdirectories. It will then provide feedback on the test results, indicating whether each test passed, failed, or was skipped.

### Running `pytest`

When `pytest` is run, there are three stages:

1. **Discovery**. The tests scheduled to be run are discovered, and then collected. The default discovery behaviour will include:
    - All functions with a name that starts with `test_`, that are located in files with a filename that starts with `test_` or ends with `_test`
    - All methods that meet the above conditions, provided that their containing class does not have an `__init__` method and the class name begins with `Test`.
2. **Execution**. The tests are then executed, which includes setting up any test resources (if needed) and 'tearing down' these resources afterwards.
3. **Reporting**. Once all tests are executed, `pytest` generates a report. This report includes information such as the number of tests executed, the number of failures, and any errors encountered during testing.

### Understanding Test Success and Failure in pytest

In pytest, a test is deemed to have passed successfully if the test function reaches the end of its code or encounters a `return` statement without raising an `Exception`.

Conversely, if an `Exception` is raised during the execution of the test function, pytest considers the test as having failed. This typically happens when the observed behavior of the code being tested does not align with the expected behavior defined within the test.

As authors of a test function, we need to consider **when** we want the code to deliberatey raise an exception during test execution and also **how** to do this:

- **When**: We intentionally raise an `Exception` when the behavior of the code under test deviates from the expected outcome.
- **How**: In pytest the standard approach for signalling test failures is through the `assert` statement. If the expression following the `assert` statement evaluates to `True`, the test function continues execution without raising an `Exception`.
If the expression evaluates to `False`, an `AssertionError` is raised, indicating a test failure.

Therefore, the expression after the assert statement in our test functions should be checking the equality between the observed behavior of the code and the expected outcome.

### A Pattern For Writing Tests

With the above in mind, a good pattern to follow when writing these unit tests is known as the `Arrange-Act-Assert` pattern.
This pattern describes an order of operations to follow in a test function:

- **Arrange** inputs and targets. First, prepare everything you need for your test. This might mean creating objects.

- **Act** on the target behavior. Next, do the thing you want to test. This could be calling the function or method you're testing.

- **Assert** expected outcomes. Finally, see if what happened matches what you expected. For example, this is where you check if your function did the behaviour you are expecting of it when you called it in the `Act` stage.'

Let's change our above test to explicitly follow this pattern:

```Python
def test_add():
    # Arrange 
    input_value_1 = 10
    input_value_2 = 20
    expected_output = 30

    # Act
    actual_output = add(input_value_1, input_value_2)
    
    # Assert
    assert actual_output == expected_output
```

## Expanding on pytest Testing

When we ran `pytest` above, we demonstrated a simple test within the same module as the function being tested. This is not how tests are laid out in projects.

In projects, it's common practice to separate tests into their own dedicated package, typically named `tests`, to keep them organised and distinct from the source code. This separation helps maintain a clean project structure and makes it easier to manage and run tests as the project grows.

In this `tests` package, you can then organise your test files within it. Each test file can contain multiple test functions, test classes and test methods, and you can use Pytest's built-in capabilities to run all tests within the tests package or specific tests.

Let's now build out the following project structure, which contains two packages: `src`, containing the source code and `tests`, containing the tests which will be executed when we run `pytest` on our project.

Note: we are keeping the actual Python source code simple here to focus on how pytest works.

``` text
project/
│
├── src/
│   ├── __init__.py
│   └── math_operations.py
│
└── tests/
    ├── __init__.py
    └── test_math_operations.py
```

Now, let's populate these files with some content:

In `math_operations.py`, we define some basic mathematical operations:

```Python
# math_operations.py
def add(arg1, arg2):
    return arg1 + arg2


def subtract(arg1, arg2):
    return arg1 - arg2


def multiply(arg1, arg2):
    return arg1 * arg2


def divide(arg1, arg2):
    if arg2 == 0:
        raise ZeroDivisionError('arg2 cannot be 0, since you cannot divide by 0')
    else:
        return arg1 / arg2

```

In `test_math_operations.py`, we write test cases to validate these operations:

```Python
# test_math_operations.py
from src.math_operations import add, subtract, multiply, divide

def test_add():
    # Arrange 
    input_value_1 = 10
    input_value_2 = 20
    expected_output = 30

    # Act
    actual_output = add(input_value_1, input_value_2)
    
    # Assert
    assert actual_output == expected_output
```

**Note**: Both `__init__.py` files can be left empty.

### Concept Check

Add a test fuction for the remaining operations in `src.math_operations`.

**Note**: For now, ignore testing `divide` with arg2 == 0, we will come on to this.

With this structure and these test cases, you can now run `pytest` in your project directory, and it will discover and execute the tests in the tests package, providing you with detailed feedback on the success or failure of each test.
