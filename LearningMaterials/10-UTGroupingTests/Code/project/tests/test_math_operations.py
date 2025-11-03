from src.math_operations import add, subtract, multiply, divide, power, modulo, absolute_value

def test_basic_add():
    # Arrange
    input_value1 = 10
    input_value2 = 20
    expected_value = 30

    # Act
    actual_value = add(input_value1, input_value2)

    # Assert
    assert actual_value == expected_value


def test_basic_subtract():
    # Arrange
    input_value1 = 10
    input_value2 = 20
    expected_value = -10

    # Act
    actual_value = subtract(input_value1, input_value2)

    # Assert
    assert actual_value == expected_value

def test_basic_multiply():
    # Arrange
    input_value1 = 2
    input_value2 = 2
    expected_value = 4

    # Act
    actual_value = multiply(input_value1, input_value2)

    # Assert
    assert actual_value == expected_value


def test_basic_divide():
    # Arrange
    input_value1 = 20
    input_value2 = 10
    expected_value = 2

    # Act
    actual_value = divide(input_value1, input_value2)

    # Assert
    assert actual_value == expected_value


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
