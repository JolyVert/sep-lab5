"""Binary conversion utilities."""


def decimal_to_binary(number: int) -> str:
    """Convert natural number from 0-100 to binary."""

    if not isinstance(number, int):
        raise TypeError("Number must be an integer")

    if number < 0 or number > 100:
        raise ValueError("Number must be between 0 and 100")

    return bin(number)[2:]
