#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.

class Player:
    """ represents a player for connect four """
    
    # 2-1
    def __init__(self, checker):
        """ constructs a new player """
        assert(checker == 'X' or checker == 'O')
        if checker in "XO":
            self.checker = checker
            self.num_moves = 0
        else:
            print('Your checker must be either "X" or "O" (case sensitive).')

    # 2-2
    def __repr__(self):
        """  returns a string representing a Player object """ 
        return str(self)

    # 2-3
    def opponent_checker(self):
        """ returns a one-character string representing the checker of the Player 
        object’s opponent """
        if self.checker == 'X':
            return 'O'
        if self.checker == 'O':
            return 'X'
        
    # 2-4
    def next_move(self, board):
        """ accepts a Board object b as a parameter and returns the column where the 
        player wants to make the next move """
        self.num_moves += 1
        while True:
            colstr = input('Enter a column: ')
            if colstr in "0123456":
                colnum = int(colstr)
                if board.can_add_to(colnum):
                    return colnum
            print('Try again!')