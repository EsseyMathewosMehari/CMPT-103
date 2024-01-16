# ID# 3130873
# Lab 3
# The ord value is something I had to look up online and learn
# to find an alternative for giving the letters a number placeholder

def is_valid_coordinate(coordinate):
    """
    Check if a coordinate is a valid chessboard coordinate.

    Parameters:
    coordinat: The coordinate to check.

    Returns:
    bool:True if the coordinate is valid, if not then false.
    """
    if len(coordinate) != 2:
        return False

    col = coordinate[0].lower()
    row = coordinate[1]
    if 'a' <= col <= 'h' and '1' <= row <= '8':
        return True

    return False

def is_king_move_valid(current_location, destination):
    """
    Verify the moves of a king's and see if it is valid.
    Parameters:
    current_location: The king's place at the moment.
    destination: The place where you want to go.

    Returns:
    If the motion is legal
    bool:True; if not False

    I had to research the ord value online to come up with a different way to assign a number to the letter.
    
    """
    if not is_valid_coordinate(current_location) or not is_valid_coordinate(destination):
        return False

    current_col = current_location[0].lower()
    current_row = int(current_location[1])
    dest_col = destination[0].lower()
    dest_row =  int(destination[1])

    col_diff = (ord(current_col) - ord(dest_col))
    row_diff = (current_row - dest_row)

    return col_diff <= 1 and row_diff <= 1

def is_queen_move_valid(current_location, destination):
    """
    Check if a queen's move is valid.

    Parameters:
    current_location: The current coordinate of the queen.
    destination: The destination coordinate.

    Returns:
    bool:True if the move is valid, False otherwise.
    """
    if not is_valid_coordinate(current_location) or not is_valid_coordinate(destination):
        return False

    current_col = current_location[0].lower()
    current_row = int(current_location[1])
    dest_col= destination[0].lower()
    dest_row = int(destination[1])

    col_diff = ord(current_col) - ord(dest_col)
    row_diff = current_row - dest_row

    return (col_diff == 0 and row_diff > 0) or (col_diff > 0 and row_diff == 0) or (col_diff == row_diff)

def is_bishop_move_valid(current_location, destination):
    """
    Check if a bishop's move is valid.

    Parameters:
    current_location: The current coordinate of the bishop.
    destination: The destination coordinate.

    Returns:
    bool: True if the move is valid, False otherwise.
    """
    if not is_valid_coordinate(current_location) or not is_valid_coordinate(destination):
        return False

    current_col = current_location[0].lower()
    current_row= int(current_location[1])
    dest_col = destination[0].lower() 
    dest_row =  int(destination[1])

    col_diff = abs(ord(current_col) - ord(dest_col))
    row_diff = abs(current_row - dest_row)

    return col_diff == row_diff

def is_rook_move_valid(current_location, destination):
    """
    Check if a rook's move is valid.

    Parameters:
    current_location: The current coordinate of the rook.
    destination: The destination coordinate.

    Returns:
    bool: True if the move is valid, False otherwise.
    """
    if not is_valid_coordinate(current_location) or not is_valid_coordinate(destination):
        return False

    current_col = current_location[0].lower()
    current_row = int(current_location[1])
    dest_col, dest_row = destination[0].lower()
    dest_row = int(destination[1])

    return current_col == dest_col or current_row == dest_row

def is_knight_move_valid(current_location, destination):
    """
    Check if a knight's move is valid.

    Parameters:
    current_location: The current coordinate of the knight.
    destination: The destination coordinate.

    Returns:
    bool: True if the move is valid, False otherwise.
    """
    if not is_valid_coordinate(current_location) or not is_valid_coordinate(destination):
        return False

    current_col = current_location[0].lower()
    current_row = int(current_location[1])
    dest_col = destination[0].lower()
    dest_row = int(destination[1])
    col_diff = abs(ord(current_col) - ord(dest_col))
    row_diff = abs(current_row - dest_row)

    return (col_diff == 2 and row_diff == 1) or (col_diff == 1 and row_diff == 2)

def is_move_valid(piece, current_location, destination):
    """
    Check if a requested chess piece's move is valid.

    Parameters:
    piece: The chess piece
    current_location: The current coordinate of the piece.
    destination: The destination coordinate.

    Returns:
    bool:True if the move is valid, False otherwise.
    """
    piece = piece.lower()

    if piece == 'king':
        return is_king_move_valid(current_location, destination)
    elif piece == 'queen':
        return is_queen_move_valid(current_location, destination)
    elif piece == 'bishop':
        return is_bishop_move_valid(current_location, destination)
    elif piece == 'rook':
        return is_rook_move_valid(current_location, destination)
    elif piece == 'knight':
        return is_knight_move_valid(current_location, destination)
    else:
        return False

# Testing
print(is_move_valid('Queen', 'a7', 'a1'))  
print(is_move_valid('queen', '7A', 'A1'))  
print(is_move_valid('king', 'A7', 'C8'))  
print(is_move_valid('knight', 'A7', 'C8'))  
print(is_move_valid('knight', 'AA', 'C8'))  
print(is_move_valid('knight', 'A7', 'C9'))  
print(is_move_valid('hammer', 'A7', 'A1'))  