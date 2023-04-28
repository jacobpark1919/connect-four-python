#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game 
#   

from ps9pr1 import Board
from ps9pr2 import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b

# 1-1
def process_move(p, b):
    """ the function will perform all of the steps involved in processing a single
    move by player p on board b """
    print(str(p) + "'s turn")
    col = p.next_move(b)
    b.add_checker(p.checker, col)
    print()
    print(b)
    if b.is_win_for(p.checker) == True:
        print(p, 'wins in', p.num_moves, 'moves.')
        print('Congratulations!')
        return True
    elif b.is_full() == True:
        print("It's a tie!")
        return True
    else:
        return False

# 1-2
class RandomPlayer(Player):
    """ can be used for an unintelligent computer player that chooses at random
    from the available columns """
    def next_move(self, board):
        """ chooses at random  from the columns in the board b that are not yet full, 
        and returns the index of that randomly selected column """
        self.num_moves += 1
        avail_cols = []
        for col in range(board.width):
            if board.can_add_to(col) == True:
                avail_cols += [col]
        return random.choice(avail_cols)
    
    