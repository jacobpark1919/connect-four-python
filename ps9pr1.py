#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#
# Computer Science 111
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """
    ### add your constructor here ###

    # 1-1
    def __init__(self, height, width):
        """ contruscts a new board object """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    # 1-2
    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''
        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'
        s += (2*self.width + 1) * '-'
        s += '\n'
        for num in range(self.width):
            s += ' '+str(num % 10)
        return s

    # 1-3
    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)

        ### put the rest of the method here ###
        row = 0
        while self.slots[row][col] == ' ': 
            row += 1
            if row == self.height-1:
                break
        if self.slots[row][col] != ' ':
            row += -1
        self.slots[row][col] = checker
        
            ### add your reset method here ###
    # 1-4  
    def reset(self):
        """ resets the board """ 
        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col] = ' '
    # 1-5
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    # add your remaining methods here
    
    # 1-6
    def can_add_to(self, col):
        """ returns true if it is possible to place a checker in desired column, 
        and returns false if it is not possible to place a checker in desired column. """
        if col < 0:
            return False
        elif col > self.width - 1:
            return False
        elif self.slots[0][col] != ' ':
            return False
        else:
            return True
    
    # 1-7
    def is_full(self):
        """ returns True if the board is full, and returns False if the board 
        is not full """
        for col in range(self.height):
            for row in range(self.width):
                if self.slots[col][row] == ' ':
                    return False
                else:
                    return True
                
    # 1-8
    def remove_checker(self, col):
        """ removes top checker from the desired column. If the column is empty,
        then this method does nothing """
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                return

    # 1-9
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker. """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                    self.slots[row][col + 1] == checker and \
                    self.slots[row][col + 2] == checker and \
                    self.slots[row][col + 3] == checker:
                        return True
        # if we make it here, there were no horizontal wins
        return False

    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker """
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True
        return False
    
    def is_up_diagonal_win(self, checker):
        """ Checks for a diagonal-up win for the specified checker """
        for row in range(3,self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True
        return False

    def is_down_diagonal_win(self, checker):
        """ Checks for a diagonal-down win for the specified checker """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True
        return False
    
    def is_win_for(self, checker):
        """ returns True if there is a connect four and False if there is not a 
        connect four """ 
        assert(checker == 'X' or checker == 'O')
        if self.is_down_diagonal_win(checker) == True:
            return True
        elif self.is_up_diagonal_win(checker) == True:
            return True
        elif self.is_vertical_win(checker) == True:
            return True
        elif self.is_horizontal_win(checker) == True:
            return True
        else:
            return False        
        
    
        