import pytest
import binary_utils


@pytest.mark.parametrize(
    "number, expected",
    [
        (0, "0"),
        (1, "1"),
        (2, "10"),
        (5, "101"),
        (10, "1010"),
        (100, "1100100"),
    ],
)
def test_decimal_to_binary(number, expected):
    result = binary_utils.decimal_to_binary(number)
    assert result == expected


@pytest.mark.parametrize(
    "number",
    [-1, 101, 200],
)
def test_range_validation(number):
    with pytest.raises(ValueError):
        binary_utils.decimal_to_binary(number)


@pytest.mark.parametrize(
    "number",
    [1.5, 2.7, "abc"],
)
def test_integer_validation(number):
    with pytest.raises(TypeError):
        binary_utils.decimal_to_binary(number)
