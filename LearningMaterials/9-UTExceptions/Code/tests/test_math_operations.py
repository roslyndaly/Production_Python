from src.math_operations import add, subtract, multiply, divide

def test_add():
    # Arrange
    input_value1 = 10
    input_value2 = 20
    expected_value = 30

    # Act
    actual_value = add(input_value1, input_value2)

    # Assert
    assert actual_value == expected_value


def test_subtract():
    # Arrange
    input_value1 = 10
    input_value2 = 20
    expected_value = -10

    # Act
    actual_value = subtract(input_value1, input_value2)

    # Assert
    assert actual_value == expected_value


def test_multiply():
    # Arrange
    input_value1 = 2
    input_value2 = 2
    expected_value = 4

    # Act
    actual_value = multiply(input_value1, input_value2)

    # Assert
    assert actual_value == expected_value


def test_divide():
    # Arrange
    input_value1 = 20
    input_value2 = 10
    expected_value = 2

    # Act
    actual_value = divide(input_value1, input_value2)

    # Assert
    assert actual_value == expected_value




