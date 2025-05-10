"""
Encryption and decryption functionality for the application.
This module contains functions for encrypting and decrypting 6-digit numbers.
"""


def swap_digits(digits):
    """
    Swap digits according to the encryption/decryption algorithm.
    1. Swap the first digit with the third.
    2. Swap the second digit with the fourth.
    3. Swap the fifth digit with the sixth.

    Args:
        digits (list): A list of 6 digits to be swapped.

    Returns:
        list: The list with swapped digits.
    """
    # Create a copy of the list to avoid modifying the original
    result = digits.copy()

    # Swap digits
    result[0], result[2] = result[2], result[0]  # 1st with 3rd
    result[1], result[3] = result[3], result[1]  # 2nd with 4th
    result[4], result[5] = result[5], result[4]  # 5th with 6th

    return result


def encrypt_number(number_str):
    """
    Encrypts a 6-digit number.
    1. Add 7 to each digit and take the remainder when divided by 10.
    2. Swap the first digit with the third.
    3. Swap the second digit with the fourth.
    4. Swap the fifth digit with the sixth.

    Args:
        number_str (str): A 6-digit number as a string.

    Returns:
        str: The encrypted number as a string, or None if input is invalid.
    """
    if not (number_str.isdigit() and len(number_str) == 6):
        # The UI will handle an error message
        return None

    digits = [int(d) for d in number_str]

    # Step 1: Encrypt each digit
    encrypted_digits = [(d + 7) % 10 for d in digits]

    # Steps 2, 3, and 4: Swap digits using the helper function
    encrypted_digits = swap_digits(encrypted_digits)

    return "".join(map(str, encrypted_digits))

def decrypt_number(encrypted_str):
    """
    Decrypts a previously encrypted number.
    1. Reverse the digit swaps (by applying the same swaps).
    2. Subtract 7 from each digit (or add 3, which is equivalent to module 10) and take the remainder.
       (original_digit = (encrypted_digit - 7 + 10) % 10)

    Args:
        encrypted_str (str): A 6-digit encrypted number as a string.

    Returns:
        str: The decrypted number as a string, or None if input is invalid.
    """
    if not (encrypted_str.isdigit() and len(encrypted_str) == 6):
        # The UI will handle an error message
        return None

    digits = [int(d) for d in encrypted_str]

    # Step 1: Reverse the digit swaps
    # The swap is symmetric, applying it again reverses the operation.
    digits = swap_digits(digits)

    # Step 2: Decrypt each digit
    decrypted_digits = [(d - 7 + 10) % 10 for d in digits]

    return "".join(map(str, decrypted_digits))
