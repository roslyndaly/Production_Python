# Fixtures

Fixtures in `pytest` are a powerful feature for setting up preconditions or states needed for tests and cleaning up after them. They provide a way to organise and reuse common setup and teardown code across multiple test functions. They are defined using the `@pytest.fixture` decorator and can be used by test functions or other fixtures.

## Creating a Simple Fixture

In the `project` folder in this directory, our source code contains some functions which work with an address book. When testing each function we need to have a common set up of creating a dictionary address book. Rather than defining this each time, this has been defined as a simple fixture in the test file. This fixture provides the value of a large address book which then allows us to provide this as input into our test functions.

**Note**: when defining fixtures, because we make use of `@pytest.fixture`, we need to ensure we have imported `pytest` into the module where the fixture is defined.

When pytest collects tests, if a fixture is passed as an input parameter, it executes the fixture function, and the returned value is stored in the input parameter. Subsequently, this value can be utilised within the test.

Fixtures are great for extracting data or objects that you use across multiple tests. The address book fixture is a very simple fixture, since it only defines an object in Python, however, fixtures in pytest are capable of handling more complex scenarios. For example, a fixture can set up a temporary database for testing database-related functions and tear it down afterward. Pytest also come with some built in fixtures.

**Note**: a fixture function defined within a test file can only be used within that file. To make a fixture accessible across multiple test files, it must be defined in a file named `conftest.py`.

### Built in Fixtures

The list of built-in fixtures is [here](https://docs.pytest.org/en/6.2.x/fixture.html), and covers many common use-cases for test resources.
A few of these are highlighted below:

- `capsys`: Capture, as text, output to sys.stdout and sys.stderr from the process we are testing, i.e. output of `print` statements.
- `tmp_path`: Provide a `pathlib.Path` object to a temporary directory which is unique to each test function.
- `monkeypatch`: Temporarily modify classes, functions, dictionaries, `os.environ`, and other objects.

#### tmp_path

The production code function `greet_to_open_file` writes a greeting to a named individual, to an open file.

```Python
def greet_to_open_file(username, open_file):
    open_file.write(f'Hello {username}!')


# Example use case
with open('example_file.txt', 'w') as f:
    greet_to_open_file('Jemima', f)
```

We will now write a test function that checks the function is working as expected.

```Python
import os

def test_greet_to_open_file(tmp_path):
    # Arrange
    test_username = 'Alice'
    test_file_path = tmp_path / 'test_file.txt'

    # Act
    with open(test_file_path, 'w') as test_file:
        greet_to_open_file(test_username, test_file)

    # Assert
    with open(test_file_path, 'r') as test_file:
        first_line = test_file.readline().strip()  # Read the first line and remove whitespace
        expected_greeting = f'Hello {test_username}!'
        assert first_line == expected_greeting  # Check if the greeting is correct
```

#### capsys

- When you use capsys, pytest captures everything your test sends to standard output (stdout) and standard error (stderr) during its execution. In particular, it gives us the ability to track what is printed during test execution.

```Python
def test_my_function(capsys):
    # Call your function or code that prints to stdout
    print("Hello, world!")
    # Capture the printed output
    captured = capsys.readouterr()
    # Assertions to check the captured output
    assert captured.out == "Hello, world!\n"
```

#### monkeypatch

- The monkeypatch fixture can be used to replace functions or methods with mock implementations.
- This allows you to simulate the behavior of dependencies or external components without actually calling them.
- You can replace functions, methods, or even attributes of objects.

```Python
# production_code.py
import requests
def iss_current_location():
    url = r'http://api.open-notify.org/iss-now.json'
    response = requests.get(url)
    response_dict = response.json()
    return response_dict['iss_position']

# test_code.py
import pytest
def mock_get(url):
    class MockResponse:
        def json(self):
            return {"message": "success", "iss_position": {"latitude": "48.6674", "longitude": "34.4125"}, "timestamp": 1713768749}
    return MockResponse()

def test_process_data(monkeypatch):
    monkeypatch.setattr(requests, 'get', mock_get)
    assert iss_current_location() == {"latitude": "48.6674", "longitude": "34.4125"}
```
