# Functions for running an encryption or decryption algorithm

ENCRYPT = 'e'
DECRYPT = 'd'

# Write your functions after this comment.  Do not change the statements above
# this comment.  Do not use import, open, input or print statements in the 
# code that you submit.  Do not use break or continue statements.

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def clean_message(message):
    """(str) -> str
    
    Return string new_message that contains only capitalized letters from 
    string message in the order the letters appear. This function only keeps 
    characters that appear in the 26 letter English alphabet.
    
    >>>clean_message('aBc12 3 @ ')
    'ABC'
    >>>clean_message('')
    ''
    """
    
    new_message = ''
    
    for ch in message:
        if ch.isalpha():
            new_message += ch.upper()
    
    return new_message


def encrypt_letter(plain_letter, key):
    """(str, int) -> str 
    
    Precondition: str plain_letter must be str of a capital English letter.

    Return a string that is the ciphertext letter, which is the result of 
    applying int key to string plain_letter. This function only works with 
    English.
    
    >>>encrypt_letter('A', 15)
    'P'
    >>>encrypt_letter('J', 100)
    'F'
    """
    
    return ALPHABET[(ALPHABET.index(plain_letter) + key) % 26]
    
    # ALPHABET is str that is created for locating the index of each 
    # plain_letter in the English alphabet.


def decrypt_letter(cipher_letter, key):
    """(str, int) -> str
    
    Precondition: str cipher_letter must be str of a capital English letter.
    
    Return the string that is the plaintext letter, which is the result of 
    applying int key to string cipher_letter. This function only works with 
    English.
    
    >>>decrypt_letter('P', 15)
    'A'
    >>>decrypt_letter('F', 100)
    'J'
    """
    
    return ALPHABET[(ALPHABET.index(cipher_letter) - key) % 26]


def swap_cards(deck, index):
    """(list of int, int) -> NoneType
    
    Precondition: - len(deck) <= index < len(deck)
    
    Swap the int at position index with the int at position (int + 1) in list 
    of int deck. Treat deck as circular; thus, deck[-1] swaps with deck[0].
    
    >>>deck = [1, 2, 3, 4, 5, 6]
    >>>swap_cards(deck, 3)
    >>>deck
    [1, 2, 3, 5, 4, 6]
    >>>deck = [5, 2, 4, 6, 3, 1]
    >>>swap_cards(deck, -1)
    >>>deck
    [1, 2, 4, 6, 3, 5]
    """
    
    deck_value_at_index = deck[index]
    value_of_next = deck[(index + 1) % len(deck)]
    
    deck[index] = value_of_next
    deck[(index + 1) % len(deck)] = deck_value_at_index


def get_small_joker_value(deck):
    """ (list of int) -> int
    
    Precondition: list of int deck must be a valid deck.
    
    Return the second highest int (the small joker) from the given list of int 
    deck.
    
    >>>get_small_joker_value([1, 2, 3, 4, 5, 6])
    5
    >>>get_small_joker_value([4, 9, 5, 2, 3, 6, 1, 7, 8])
    8
    """
    
    return max(deck) - 1


def get_big_joker_value(deck):
    """ (list of int) -> int
    
    Precondition: list of int deck must be a valid deck.
    
    Return the highest int (the big joker) from the given list of int deck.
    
    >>>get_big_joker_value([1, 2, 3, 4])
    4
    >>>get_big_joker_value([3, 5, 6, 2, 4, 1])
    6
    """
     
    return max(deck)


def move_small_joker(deck):
    """(list of int) -> NoneType
    
    Mutate list of int deck, so that the second highest int (the small joker)
    is swapped with the int that follows it. Treat deck as circular; thus, 
    deck[-1] swaps with deck[0].
    
    >>>deck = [1, 4, 3, 2]
    >>>move_small_joker(deck)
    >>>deck
    [1, 4, 2, 3]
    >>>deck = [1, 4, 2, 3]
    >>>move_small_joker(deck)
    >>>deck
    [3, 4, 2, 1]
    """
    
    swap_cards(deck, deck.index(get_small_joker_value(deck)))


def move_big_joker(deck):
    """(list of int) -> NoneType
    
    Mutate list of int deck, so that the highest int (the big joker) is 
    swapped with the int that follows it twice. Treat deck as circular; thus, 
    deck[-1] swaps with deck[0].
    
    >>>deck = [1, 4, 3, 2]
    >>>move_big_joker(deck)
    >>>deck
    [1, 3, 2, 4]
    >>>deck = [1, 2, 3, 4]
    >>>move_big_joker(deck)
    >>>deck
    [2, 4, 3, 1]
    """
    
    for i in range(2):
        swap_cards(deck, deck.index(get_big_joker_value(deck)))


def triple_cut(deck):
    """(list of int) -> NoneType
    
    Precondition: len(deck) >= 2
    
    Mutate list of int deck, so that every element before the first joker 
    swaps with every element after the second joker. The first joker is one of
    the two highest ints in the deck, which is closest to the beginning. The 
    second joker is one of the two highest ints in the deck, which is closest
    to the bottom.
    
    >>>deck = [1, 2, 5, 6, 3, 4]
    >>>triple_cut(deck)
    >>>deck
    [3, 4, 5, 6, 1, 2]
    >>>deck = [5, 1, 2, 3, 4, 6]
    >>>triple_cut(deck)
    >>>deck
    [5, 1, 2, 3, 4, 6]
    """

    small_range = deck[0:min(deck.index(get_small_joker_value(deck)), 
                      deck.index(get_big_joker_value(deck)))]
    
    # Small_range is the range of int's from index 0 to the joker with the
    # smallest index in the of list of int deck. 
    
    big_range = deck[max(deck.index(get_small_joker_value(deck)), 
                      deck.index(get_big_joker_value(deck))) + 1:]
    
    # Likewise, but from index -1 of list of int deck.
    
    for num in small_range:
        deck.remove(num)
    
    for num_1 in big_range:
        deck.remove(num_1)
        
    deck.extend(small_range)
    
    i = 0
    
    for num_2 in big_range:
        deck.insert(i, num_2)
        i = i + 1
        

def insert_top_to_bottom(deck):
    """(list of in) -> NoneType
    
    Precondition: len(deck) >= 2
    
    int bottom_value is equal to the last element in the list of int 
    deck. Then, take a group of int from the front deck containing 
    bottom_value elements. Insert this group before bottom_value in deck. 
    If bottom_value is the highest int in deck, then group of int will have 
    one less element than the value of bottom_value.
    
    >>>deck = [1, 4, 5, 6, 3, 2]
    >>>insert_top_to_bottom(deck)
    >>>deck
    [5, 6, 3, 1, 4, 2]
    >>>deck = [1, 2, 3, 4, 5, 6]
    >>>insert_top_to_bottom(deck)
    >>>deck
    [1, 2, 3, 4, 5, 6]
    """
    
    bottom_value = deck[-1]
    
    if bottom_value == get_big_joker_value(deck):
        bottom_value = get_small_joker_value(deck)
    
    for num in deck[0:bottom_value]:
        deck.insert(-1, num)
        deck.remove(num)
        
        
def get_card_at_top_index(deck):
    """(list of int) -> int
    
    Precondition: list of int deck must return True with 
                  function is_valid_deck().
    
    Return the int at the position of the value of the first int in list of 
    int deck. If the value of the first int in deck is the highest int, then 
    take the value as the second highest int. 
    
    >>>get_card_at_top_index([1, 2, 5, 6, 3, 4])
    2
    >>>get_card_at_top_index([6, 2, 5, 4, 3, 1])
    1
    """
    
    stream_index = deck[0]
    
    if deck[0] == get_big_joker_value(deck):
        stream_index = get_small_joker_value(deck)
    
    return deck[stream_index]


def get_next_keystream_value(deck):
    """(list of int) -> int
    
    Precondition: list of int deck must return True with 
                  function is_valid_deck().
                  
    Return int that is the next valid keystream value.
        
    >>>get_next_keystream_value([1, 2, 3, 4, 5, 6])
    3
    >>>get_next_keystream_value([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, \
    9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26])
    11
    """ 
    
    i = 0
    
    while get_card_at_top_index(deck) == get_small_joker_value(deck)\
          or get_card_at_top_index(deck) == get_big_joker_value(deck)\
          or i < 1:
        move_small_joker(deck)
        move_big_joker(deck)
        triple_cut(deck)
        insert_top_to_bottom(deck)
        i = i + 1
        
    # List of int deck has been shuffled at least once by the appropriate 
    # algorithm, and the top card won't be a joker.
        
    return get_card_at_top_index(deck)


def process_messages(deck, messages, mode):
    """(list of int, list of str, str) -> list of str
    
    Precondition: list of str messages has been returned from function 
                  clean_message.
    
    Return a list of encrypted or decrypted messages, in the same order as
    they appear in the given lists of str messages. List of int deck might be 
    mutated during a function call.
    
    >>>deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, \
    19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    >>>process_messages(deck, ["HELLO"], ENCRYPT)
    ['PUWTU']
    >>>deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, \
    19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    >>>process_messages(deck, ['PUWTU', ''], DECRYPT)
    ['HELLO', '']
    """
    
    returned_messages = []
    
    if mode == ENCRYPT:
        for index in range(len(messages)):
            string = ""
            for ch in messages[index]:
                string += encrypt_letter(ch, get_next_keystream_value(deck))
            returned_messages.append(string)
    
    elif mode == DECRYPT:
        for index in range(len(messages)):
            string = ""
            for ch in messages[index]:
                string += decrypt_letter(ch, get_next_keystream_value(deck))
            returned_messages.append(string)
            
    return returned_messages
    
    # Variable string accumulates all the letters in a line, so that every 
    # element in returned_messages is a string that contains all letters of 
    # the corresponding line.


def read_messages(msg_file):
    """(file open for reading) -> list of str
    
    Read and return a list of str containing all lines from file msg_file in 
    the order in which they appear in the file. Strip the newline from each 
    line. 
    """
    
    returned_lines = []
    
    for line in msg_file:
        returned_lines.append(clean_message(line))
        
    return returned_lines


def is_valid_deck(deck):
    """(list of int) -> bool
    
    Return True if and only if list of int deck is a valid deck of cards.
    A valid deck consists every int from 1 up to len(deck).
    
    >>>is_valid_deck([1, 2, 3, 4])
    True
    >>>is_valid_deck([8, 8, 8, "@", "hello"])
    False
    >>>is_valid_deck([1, 2])
    False
    """
    
    if len(deck) < 3:
        return False

    for number in range(1, len(deck)+1):
        if number not in deck:
            return False
    
    return True


def read_deck(deck_file):
    """(file open for reading) -> list of int
    
    Read and return the numbers that are in the file deck_file, in the order
    in which they appear in the file.
    """

    returned_numbers = []
    
    file = deck_file.read()
    string_list = file.split()
    
    for ch in string_list:
        returned_numbers.append(int(ch))
    
    return returned_numbers