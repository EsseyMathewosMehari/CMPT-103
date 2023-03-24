#This function compress compresses a given string into a new string by counting consecutive occurrences of the same character and representing each character and its count as a single character followed by its count. If the count is 1, then only the character is included in the compressed string. The compressed string is returned as the result of the function.
def compress(string):
    compressed_str = ""
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            compressed_str += string[i-1] + str(count) if count > 1 else string[i-1]
            count = 1
    compressed_str += string[-1] + str(count) if count > 1 else string[-1]
    return compressed_str

#This function expand(string) expands a compressed string into its original form. It does this by iterating over the input string string using a while loop, and checking if the current character is a digit. If it is, the function multiplies the previous character by the digit, effectively repeating it in the output string expanded_str. If the current character is not a digit, it is simply added to the expanded_str. The expanded_str is returned as the result of the function.
def expand(string):
    expanded_str = ""
    i = 0
    while i < len(string):
        if string[i].isdigit():
            expanded_str += string[i-1] * int(string[i])
        else:
            expanded_str += string[i]
        i += 1
    return expanded_str

#This function is_basic_expr(string) checks if the input string string is a valid basic mathematical expression. The expression must start and end with a digit, contain only digits, spaces, and the operators +, -, *, and /, and satisfy certain conditions regarding the placement of spaces.
def is_basic_expr(string):
    if not string[0].isdigit() or not string[-1].isdigit():
        return False
    i = 0
    while i < len(string):
        if string[i].isdigit():
            if (i > 0 and not string[i-1].isspace()) or (i < len(string) - 1 and not string[i+1].isspace()):
                return False
        elif string[i] in ['+', '-', '*', '/']:
            if (i == 0 or i == len(string) - 1) or not string[i-1].isspace() or not string[i+1].isspace():
                return False
        elif string[i].isspace():
            if (i == 0 or i == len(string) - 1) or (not string[i-1].isdigit() and not string[i+1].isdigit()):
                return False
        else:
            return False
        i += 1
    return True