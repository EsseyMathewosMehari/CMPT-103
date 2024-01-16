# ID# 3130873
# Lab 2

# Define a function called number_to_letter
def number_to_letter(number):
    """
    Converts a number to the corresponding UPPERCASE letter or space based on the conversion table.

    Parameters:
    number (int): An integer in the range 0 to 26 inclusive.

    Returns:
    str: The UPPERCASE letter or space associated with the input number.
    """
    # Define a conversion table that maps numbers to uppercase letters from A to Z.
    conversion_table = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    # Return the letter corresponding to the input number.
    return conversion_table[number]

# Define a function called letter_to_number
def letter_to_number(letter):
    """
    Converts a letter to the corresponding UPPERCASE letter or space based on the conversion table.

    Parameters:
    letter (str): A single letter (uppercase or lowercase) or a space character.

    Returns:
    int: The numerical representation associated with the input letter, where 'A' or 'a' is 0, 'B' or 'b' is 1, and so on.
         The space character is represented as 26.
    """
    # Define a conversion table that maps numbers to uppercase letters from A to Z
    conversion_table = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    # Convert the input letter to uppercase to ensure it matches the conversion table.
    letter = letter.upper()
    # Return the index position of the set letter in the conversion table.
    return conversion_table.index(letter)

# Define a function called encode
def encode(plaintext_letter, code_letter):
    """
    Encodes two letters by converting them to numbers, adding them together, and wrapping the result within 0-25.

    Parameters:
    first (str): The first letter to encode.
    second (str): The second letter to encode.

    Returns:
    int: The encoded result as an integer between 0 and 25 (inclusive).

    This function takes two letters, 'first' and 'second', and converts them to numbers using the 'letter_to_number'
    function. It then adds these numbers together and ensures that the result remains within the range 0 to 25 by taking
    the modulo 26. The resulting encoded number is returned.
    """
    first = letter_to_number(plaintext_letter)
    second = letter_to_number(code_letter)
    math = (first + second) % 26
    return number_to_letter(math)

# Define a function called decode
def decode(encoded_letter, code_letter):
    """
    Decode an encoded letter using a codebook letter.

    Parameters:
    encoded_letter (str): The letter to be decoded.
    code_letter (str): The corresponding letter from the codebook.

    Returns:
    str: The decoded letter.

    This function takes an encoded letter and a codebook letter, both represented as strings. It converts
    these letters to numerical representations using the 'letter_to_number' function, then performs a decoding
    calculation by subtracting the codebook letter's numerical representation from the encoded letter's representation.
    The result is wrapped within the range 0 to 26 (inclusive) using modulo 27 and then converted back to a letter using
    the 'number_to_letter' function. The decoded letter is returned.
    """
    # Convert the encoded letter to a numerical representation using the 'letter_to_number' function
    first = letter_to_number(encoded_letter)
    # Convert the codebook letter to a numerical representation using the 'letter_to_number' function
    second = letter_to_number(code_letter)
    # Perform the decoding calculation: Subtract the codebook letter's numerical representation from the encoded letter's,
    # then take the modulo 27 to ensure the result remains within the range 0 to 26 (inclusive).
    math = (first - second) % 27
    return number_to_letter(math)

# Define a function called text_encode
def text_encode(text_to_encode: str, codebook: str) -> str:
    """
    Encode a text using a given codebook.

    Parameters:
    text_to_encode (str): The input text to be encoded, containing characters A-Z, a-z, and ' ' (space).
    codebook (str): The codebook used for encoding, which should be at least as long as the input text.

    Returns:
    str: The encoded text.

    This function takes an input text and a codebook. It encodes the input text character by character
    by matching each character with the corresponding character from the codebook. The result is appended
    to a string and returned. Both the input text and codebook should only contain valid characters (A-Z, a-z, and space).
    """
    encoded_text = ""
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Loop through each character in the input text
    for i in range(len(text_to_encode)):
        # Ensure that we wrap around the codebook if it's shorter than the input text
        if i >= len(codebook):
            # Calculate the position in the codebook by taking the remainder of 'i' divided by the codebook length
            codebook_index = i % len(codebook)
        else:
            # If the codebook is long enough, use the current position 'i'
            codebook_index = i

        # Get the current character from the codebook
        codebook_char = codebook[codebook_index].upper()

        # Get the current character from the input text
        input_char = text_to_encode[i].upper()

        # Check if the character is a space and preserve it
        if input_char == ' ':
            encoded_text += ' '
        else:
            # Calculate the indices for the characters in the alphabet
            codebook_idx = alphabet.index(codebook_char)
            input_idx = alphabet.index(input_char)
            encoded_idx = (codebook_idx + input_idx) % 26

            # Append the encoded character to the result
            encoded_text += alphabet[encoded_idx]

    return encoded_text

# Define a function called text_decode
def text_decode(text_to_decode, codebook):
    """
    Decode an encoded text using a given codebook.

    Parameters:
    text_to_decode (str): The encoded text to be decoded.
    codebook (str): The codebook used for decoding, which should be at least as long as the encoded text.

    Returns:
    str: The decoded text.

    This function takes an encoded text and a codebook. It decodes the encoded text character by character
    by matching each character with the corresponding character from the codebook. The result is appended
    to a string and returned. Both the encoded text and codebook should only contain valid characters (A-Z, a-z, and space).
    """
    decoded_text = ""
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


    # Loop through each character in the input text
    for i in range(len(text_to_decode)):
        # Check if we've reached the end of the codebook and need to wrap around
        if i >= len(codebook):
            # Calculate the position in the codebook by taking the remainder of 'i' divided by the codebook length
            codebook_index = i % len(codebook)
        else:
            # If the codebook is long enough, use the current position 'i'
            codebook_index = i

        # Get the current character from the codebook
        codebook_char = codebook[codebook_index].upper()
        encoded_char = text_to_decode[i].upper()

        if encoded_char == ' ':
            decoded_text += ' '  # Preserve spaces
        else:
            encoded_index = alphabet.index(encoded_char)
            codebook_index = alphabet.index(codebook_char)
            decoded_index = (encoded_index - codebook_index) % 26
            decoded_text += alphabet[decoded_index]

    return decoded_text

#Calls the above functions
print(number_to_letter(24))
print(letter_to_number('F'))  
print(encode('a', 'a')) 
print(decode('b', 'e')) 
print(text_encode('fish','tortoise'))
print(text_decode('foz', 'cat'))