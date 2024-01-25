import sys
import struct
import logging


def print_help():
    """Prints the usage instructions."""
    logging.info(f'Usage: {sys.argv[0]} (create | offset) <value> <buflen>')


def pattern_create(length=8192):
    """Creates a cyclic pattern of a given length.

    Args:
        length (int): The length of the pattern to be created.

    Returns:
        str: The generated cyclic pattern.
    """
    pattern = ''
    parts = ['A', 'a', '0']

    try:
        length = int(length, 0)  # Handles both hex and decimal
    except ValueError:
        print_help()
        sys.exit(254)

    while len(pattern) < length:
        pattern += parts[len(pattern) % 3]
        if len(pattern) % 3 == 0:
            parts = update_parts(parts)

    return pattern


def update_parts(parts):
    """Updates the parts used in pattern creation.

    Args:
        parts (list): The current parts of the pattern.

    Returns:
        list: The updated parts of the pattern.
    """
    parts[2] = chr(ord(parts[2]) + 1)
    if parts[2] > '9':
        parts[2] = '0'
        parts[1] = chr(ord(parts[1]) + 1)
        if parts[1] > 'z':
            parts[1] = 'a'
            parts[0] = chr(ord(parts[0]) + 1)
            if parts[0] > 'Z':
                parts[0] = 'A'
    return parts


def pattern_offset(value, length=8192):
    """Finds the offset of a value in a cyclic pattern.

    Args:
        value (str): The value to find.
        length (int): The length of the pattern.

    Returns:
        int or str: The offset of the value in the pattern or 'Not found'.
    """
    try:
        if isinstance(value, str) and value.startswith('0x'):
            value = struct.pack('<I', int(value, 16)).strip(b'\x00').decode()
    except ValueError:
        print_help()
        sys.exit(254)

    pattern = pattern_create(length)

    try:
        return pattern.index(value)
    except ValueError:
        return 'Not found'


def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) < 3 or sys.argv[1].lower() not in ['create', 'offset']:
        print_help()
        sys.exit(255)

    command = sys.argv[1].lower()
    num_value = sys.argv[2]

    if command == 'create':
        print(pattern_create(num_value))
    elif len(sys.argv) == 4:
        print(pattern_offset(num_value, sys.argv[3]))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
