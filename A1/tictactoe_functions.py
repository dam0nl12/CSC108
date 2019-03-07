import math

EMPTY = '-'

def is_between(value, min_value, max_value):
    """ (number, number, number) -> bool

    Precondition: min_value <= max_value

    Return True if and only if value is between min_value and max_value,
    or equal to one or both of them.

    >>> is_between(1.0, 0.0, 2)
    True
    >>> is_between(0, 1, 2)
    False
    """
   
    # Students are to complete the body of this function, and then put their
    # solutions for the other required functions below this function.
    
    return min_value <= value <= max_value


def game_board_full(game_board):
    """ (str) -> bool
    
    Return True if and only if there are not any EMPTY characters in 
    game_board. game_board should refer to a valid variable.
    
    >>> game_board_full('XOXO')
    True
    >>> game_board_full('XXXOOO---')
    False
    """
    
    return not EMPTY in game_board


def get_board_size(game_board):
    """ (str) -> int
    
    Return the length of each side of game_board. game_board should refer to 
    a valid variable, and must have a length of perfect square.
    
    >>> get_board_size('XOXO')
    2
    >>> get_board_size('XXXOOOXXX')
    3
    """
    
    return int(math.sqrt(len(game_board)))

    # The type of return of math.sqrt is float; thus, in order to get 
    # function's return as an int, int(...) must be added into the line.


def make_empty_board(size_of_game_board):
    """ (int) -> str
    
    Precondition: 1 <= size_of_game_board <= 9
    
    Return the game_board, with size given by size_of_game_board, that filled 
    with the EMPTY character. 
    
    >>> make_empty_board(1)
    "-"
    >>> make_empty_board(3)
    "---------"
    """
    
    return EMPTY * size_of_game_board ** 2


def get_position(row_index, col_index, game_board_size):
    """ (int, int, int) -> int
    
    Return the str_index of the cell in the game_board whose size is given 
    by game_board_size, corresponding to row_index and col_index. row_index, 
    col_inde and game_board_size should refer to valid variables. 
    
    >>> get_position(1, 1, 4)
    0
    >>> get_position(2, 2, 3)
    4
    """
    
    return (row_index - 1) * game_board_size + col_index - 1


def make_move(player_symbol, row_index, col_index, game_board):
    """ (str, int, int, str) -> str
    
    Return game_board that results when the player_symbol is placed at the 
    chosen cell, which corresponding to row_index and col_index.
    
    >>> make_move('X', 1, 1, '---------')
    'X--------'
    >>> make_move('O', 2, 1, '----')
    '--O-'
    """
    
    changed_cell = (row_index - 1) * get_board_size(game_board) + col_index - 1
    
    return game_board[:changed_cell] + player_symbol + game_board[
        changed_cell + 1:] 
    
    # The key is to replace EMPTY character on the chosen cell by player's 
    # symbol, while keep same characters in front of and behind of the changed 
    # cell.


def extract_line(game_board, direction, index):
    """ (str, str, int) -> str
    
    Return the characters that make up the specificed row, column or diagonal, 
    depdning on direction and index, in the game_board. index of a row or a 
    column should be a valid variable.
    
    >>> extract_line('XOXO', "down", 1)
    'XX'
    >>> extract_line('OXOXOX-XO', 'down_diagonal', '')
    'OOO'

    """
    
    board_size = get_board_size(game_board)
    
    if direction == 'across':
        return game_board[(index - 1) * board_size:index * board_size]
    elif direction == 'down':
        return game_board[index - 1:len(game_board):board_size]
    elif direction == 'down_diagonal':
        return game_board[0:len(game_board):board_size + 1]
    else:
        return game_board[len(game_board) - board_size:0:-(board_size - 1)]
    
    # Since there are only 4 kinds of directions, and 'across,''down,' 
    # 'down_diagonal' have already been listed above, we can simply write 
    # 'else:' to represent the forth condiiton, instead of writing 
    # "elif direction == "down_diagonal':".