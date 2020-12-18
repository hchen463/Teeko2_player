import random
import copy


class Teeko2Player:
    """ An object representation for an AI game player for the game Teeko2.
    """
    board = [[' ' for j in range(5)] for i in range(5)]
    pieces = ['b', 'r']
    d_limit = 3



    def __init__(self):
        """ Initializes a Teeko2Player object by randomly selecting red or black as its
        piece color.
        """
        self.my_piece = random.choice(self.pieces)
        self.opp = self.pieces[0] if self.my_piece == self.pieces[1] else self.pieces[1]

    def make_move(self, state):
        """ Selects a (row, col) space for the next move. You may assume that whenever
        this function is called, it is this player's turn to move.

        Args:
            state (list of lists): should be the current state of the game as saved in
                this Teeko2Player object. Note that this is NOT assumed to be a copy of
                the game state and should NOT be modified within this method (use
                place_piece() instead). Any modifications (e.g. to generate successors)
                should be done on a deep copy of the state.

                In the "drop phase", the state will contain less than 8 elements which
                are not ' ' (a single space character).

        Return:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.

        Note that without drop phase behavior, the AI will just keep placing new markers
            and will eventually take over the board. This is not a valid strategy and
            will earn you no points.
        """
        drop_phase = True   # TODO: detect drop phase
        num = 0
        # Count the number of that are not ' ' in the board.
        for i in range(5):
            for j in range(5):
                if(state[i][j] != ' '):
                    num = num + 1
        if num == 8:
            drop_phase = False

        
        if not drop_phase:
            # TODO: choose a piece to move and remove it from the board
            # Use minimax algorithm to find the largest value and the corresponding successor.
            # Set the initial alpha to be -2, beta to be 2.
            # In the Max_Value function we also return the corresponding successor
            # so that we don't need to compare all the successor again.
            val, next_state = self.Max_Value(state, 0, -2, 2)
            # Compare the current state and the successor, the difference is
            # either the location to place or the source of the location.
            move = [None]*2
            for i in range(5):
                for j in range(5):
                    if state[i][j] != next_state[i][j]:
                        if state[i][j] != ' ':
                            move[1] = (i,j)
                        else:
                            move[0] = (i,j)
            return move
            
            
            # (You may move this condition anywhere, just be sure to handle it)
            #
            # Until this part is implemented and the move list is updated
            # accordingly, the AI will not follow the rules after the drop phase!
            


        # TODO: implement a minimax algorithm to play better
        # Use minimax algorithm to find the largest value and the corresponding successor.
        move = []
        val, next_state = self.Max_Value(state, 0, -2, 2)
        # Compare the current state and the successor, the difference is
        # the location to place a piece.
        for row in range(5):
            for col in range(5):
                if state[row][col] != next_state[row][col]:
                    move.append((row,col))
                    break
        # ensure the destination (row,col) tuple is at the beginning of the move list
        return move




    def succ(self, piece, state):
        drop_phase = True   # TODO: detect drop phase
        num = 0
        for i in range(5):
            for j in range(5):
                if state[i][j] != ' ':
                    num = num + 1
        if num >= 8:
            drop_phase = False
            
        successor = []
        if drop_phase:
            for i in range(5):
                for j in range(5):
                    if state[i][j] == ' ':
                        succ = copy.deepcopy(state)
                        succ[i][j] = piece
                        successor.append(succ)
        else:
            for i in range(5):
                for j in range(5):
                    if state[i][j] == piece:
                        if i+1 != 5 and j+1 != 5:
                            if state[i+1][j+1] == ' ':
                                succ = copy.deepcopy(state)
                                succ[i][j] = ' '
                                succ[i+1][j+1] = piece
                                successor.append(succ)
                        if i+1 != 5 and j-1 != -1:
                            if state[i+1][j-1] == ' ':
                                succ = copy.deepcopy(state)
                                succ[i][j] = ' '
                                succ[i+1][j-1] = piece
                                successor.append(succ)
                        if i+1 != 5:
                            if state[i+1][j] == ' ':
                                succ = copy.deepcopy(state)
                                succ[i][j] = ' '
                                succ[i+1][j] = piece
                                successor.append(succ)
                        if i-1 != -1 and j+1 != 5:
                            if state[i-1][j+1] == ' ':
                                succ = copy.deepcopy(state)
                                succ[i][j] = ' '
                                succ[i-1][j+1] = piece
                                successor.append(succ)
                        if i-1 != -1 and j-1 != -1:
                            if state[i-1][j-1] == ' ':
                                succ = copy.deepcopy(state)
                                succ[i][j] = ' '
                                succ[i-1][j-1] = piece
                                successor.append(succ)
                        if i-1 != -1:
                            if state[i-1][j] == ' ':
                                succ = copy.deepcopy(state)
                                succ[i][j] = ' '
                                succ[i-1][j] = piece
                                successor.append(succ)
                        if j+1 != 5:
                            if state[i][j+1] == ' ':
                                succ = copy.deepcopy(state)
                                succ[i][j] = ' '
                                succ[i][j+1] = piece
                                successor.append(succ)
                        if j-1 != 0:
                            if state[i][j-1] == ' ':
                                succ = copy.deepcopy(state)
                                succ[i][j] = ' '
                                succ[i][j-1] = piece
                                successor.append(succ)
        return successor
            
        







    def opponent_move(self, move):
        """ Validates the opponent's next move against the internal board representation.
        You don't need to touch this code.

        Args:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.
        """
        # validate input
        if len(move) > 1:
            source_row = move[1][0]
            source_col = move[1][1]
            if source_row != None and self.board[source_row][source_col] != self.opp:
                raise Exception("You don't have a piece there!")
        if self.board[move[0][0]][move[0][1]] != ' ':
            raise Exception("Illegal move detected")
        # make move
        self.place_piece(move, self.opp)

    def place_piece(self, move, piece):
        """ Modifies the board representation using the specified move and piece

        Args:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.

                This argument is assumed to have been validated before this method
                is called.
            piece (str): the piece ('b' or 'r') to place on the board
        """
        if len(move) > 1:
            self.board[move[1][0]][move[1][1]] = ' '
        self.board[move[0][0]][move[0][1]] = piece

    def print_board(self):
        """ Formatted printing for the board """
        for row in range(len(self.board)):
            line = str(row)+": "
            for cell in self.board[row]:
                line += cell + " "
            print(line)
        print("   A B C D E")







    def game_value(self, state):
        """ Checks the current board status for a win condition

        Args:
        state (list of lists): either the current state of the game as saved in
            this Teeko2Player object, or a generated successor state.

        Returns:
            int: 1 if this Teeko2Player wins, -1 if the opponent wins, 0 if no winner

        TODO: complete checks for diagonal and diamond wins
        """
        # check horizontal wins
        for row in state:
            for i in range(2):
                if row[i] != ' ' and row[i] == row[i+1] == row[i+2] == row[i+3]:
                    return 1 if row[i]==self.my_piece else -1

        # check vertical wins
        for col in range(5):
            for i in range(2):
                if state[i][col] != ' ' and state[i][col] == state[i+1][col] == state[i+2][col] == state[i+3][col]:
                    return 1 if state[i][col]==self.my_piece else -1
                
        # TODO: check \ diagonal wins
        for row in range(2):
            for col in range(2):
                if state[row][col] != ' ' and state[row][col] == state[row+1][col+1] \
                    == state[row+2][col+2] == state[row+3][col+3]:
                        return 1 if state[row][col]==self.my_piece else -1
                    
        # TODO: check / diagonal wins
        for row in range(3,5):
            for col in range(2):
                if state[row][col] != ' ' and state[row][col] == state[row-1][col+1] \
                    == state[row-2][col+2] == state[row-3][col+3]:
                        return 1 if state[row][col]==self.my_piece else -1
        
        # TODO: check diamond wins
        for row in range(3):
            for col in range(1,4):
                if state[row][col] != ' ' and state[row][col] == state[row+1][col-1]\
                    == state[row+2][col] == state[row+1][col+1]:
                        return 1 if state[row][col]==self.my_piece else -1

        return 0 # no winner yet
    
    
    def heuristic_game_value(self, state):
        '''
        For three consecutives pieces like rr, we assign value 3 to corresponding player.
        For two consecutives pieces like rrr, we assign value 2 to corresponding player.
        For the case like rr, we assign value 2.5 to corresponding player.
                          r
        For the case like rrr, we assign value 3.5 to the corresponding player.
                           r
        For case with no consecutive piece, we assign value 1.
        Then we have my_value and oppo_value. The game value is computed as
        (my_value/(oppo_value + my_value) - 0.5) * 2.
        
        '''
        oppo_value = 1
        my_value = 1
        my_index = []
        oppo_index = []
        for row in range(5):
            for col in range(5):
                if state[row][col] == self.my_piece:
                    my_index.append([row,col])
                elif state[row][col] == self.opp:
                    oppo_index.append([row,col])
        my_index.sort()
        oppo_index.sort()
        for pos in my_index:
            if [pos[0]+1,pos[1]] in my_index:
                if [pos[0]+2,pos[1]] in my_index:
                    if [pos[0],pos[1]+1] in my_index or [pos[0], pos[1]-1] in my_index \
                        or [pos[0]+1,pos[1]+1] in my_index or [pos[0]+1, pos[1]-1] in my_index\
                            or [pos[0]+2,pos[1]+1] in my_index or [pos[0]+2, pos[1]-1] in my_index:
                        my_value = 3.5
                    else:
                        my_value = 3
                    break
                elif [pos[0]+1,pos[1]+1] in my_index or [pos[0]+1,pos[1]-1] in my_index \
                    or [pos[0]-1, pos[1]] in my_index or [pos[0]+1, pos[1]] in my_index:
                    my_value = 2.5
                else:
                    my_value = 2
                
            
            if [pos[0],pos[1]+1] in my_index:
                if [pos[0],pos[1]+2] in my_index:
                    if [pos[0]+1,pos[1]] in my_index or [pos[0]-1, pos[1]] in my_index \
                        or [pos[0]+1,pos[1]+1] in my_index or [pos[0]-1, pos[1]+1] in my_index\
                            or [pos[0]+1,pos[1]+2] in my_index or [pos[0]-1, pos[1]+2] in my_index:
                        my_value = 3.5
                    else:
                        my_value = 3
                    break
                elif [pos[0]+1,pos[1]+1] in my_index or [pos[0]-1,pos[1]+1] in my_index:
                    my_value = 2.5
                else:
                    my_value = 2
            
            if [pos[0]+1,pos[1]+1] in my_index:
                if [pos[0]+2,pos[1]+2] in my_index \
                    or [pos[0]+1,pos[1]-1] in my_index \
                        or [pos[0]+2,pos[1]] in my_index:
                    my_value = 3
                    break
                else:
                    my_value = 2
            
            if [pos[0]+1,pos[1]-1] in my_index:
                if [pos[0]+2,pos[1]-2] in my_index \
                    or [pos[0]+1,pos[1]+1] in my_index \
                        or [pos[0]+2,pos[1]] in my_index:
                    my_value = 3
                    break
                else:
                    my_value = 2
                
            if [pos[0]+2,pos[1]] in my_index:
                if [pos[0]+1,pos[1]-1] in my_index \
                    or [pos[0]+1,pos[1]+1] in my_index:
                    my_value = 3
                    break
                else:
                    my_value = 2
        
        for pos in oppo_index:
            if [pos[0]+1,pos[1]] in oppo_index:
                if [pos[0]+2,pos[1]] in oppo_index:
                    if [pos[0],pos[1]+1] in oppo_index or [pos[0], pos[1]-1] in oppo_index \
                        or [pos[0]+1,pos[1]+1] in oppo_index or [pos[0]+1, pos[1]-1] in oppo_index\
                            or [pos[0]+2,pos[1]+1] in oppo_index or [pos[0]+2, pos[1]-1] in oppo_index:
                        my_value = 3.5
                    else:
                        my_value = 3
                    break
                elif [pos[0]+1,pos[1]+1] in oppo_index or [pos[0]+1,pos[1]-1] in oppo_index\
                    or [pos[0]-1, pos[1]] in oppo_index or [pos[0]+1, pos[1]] in oppo_index:
                    oppo_value = 2.5
                else:
                    oppo_value = 2
                
            
            if [pos[0],pos[1]+1] in oppo_index:
                if [pos[0],pos[1]+2] in oppo_index:
                    if [pos[0]+1,pos[1]] in oppo_index or [pos[0]-1, pos[1]] in oppo_index \
                        or [pos[0]+1,pos[1]+1] in oppo_index or [pos[0]-1, pos[1]+1] in oppo_index\
                            or [pos[0]+1,pos[1]+2] in oppo_index or [pos[0]-1, pos[1]+2] in oppo_index:
                        my_value = 3.5
                    else:
                        my_value = 3
                    break
                elif [pos[0]+1,pos[1]+1] in oppo_index or [pos[0]-1,pos[1]+1] in oppo_index:
                    oppo_value = 2.5
                else:
                    oppo_value = 2
            
            if [pos[0]+1,pos[1]+1] in oppo_index:
                if [pos[0]+2,pos[1]+2] in oppo_index \
                    or [pos[0]+1,pos[1]-1] in oppo_index \
                        or [pos[0]+2,pos[1]] in oppo_index:
                    oppo_value = 3
                    break
                else:
                    oppo_value = 2
            
            if [pos[0]+1,pos[1]-1] in oppo_index:
                if [pos[0]+2,pos[1]-2] in oppo_index \
                    or [pos[0]+1,pos[1]+1] in oppo_index \
                        or [pos[0]+2,pos[1]] in oppo_index:
                    oppo_value = 3
                    break
                else:
                    oppo_value = 2
                
            if [pos[0]+2,pos[1]] in oppo_index:
                if [pos[0]+1,pos[1]-1] in oppo_index \
                    or [pos[0]+1,pos[1]+1] in oppo_index:
                    oppo_value = 3
                    break
                else:
                    oppo_value = 2
        
        if oppo_value == my_value:
            return 0
        
        return (my_value/(oppo_value + my_value) - 0.5) * 2
        
    
    
    
    
    
    def Max_Value(self, state, depth, alpha, beta):
        '''
        Apply alpha beta pruning to compute the value of the Max player.
        Here we return both the max value and the corresponding successor.
        The reason is we want to know what is the next move in the make move function.
        
        '''
        
        # When one of the player win or reach the depth limit, 
        # return the corresponding value and terminate.
        value = self.game_value(state)
        if value != 0:
            return value, copy.deepcopy(state)
        if depth == self.d_limit:
            return self.heuristic_game_value(state), copy.deepcopy(state)
        # Apply alpha beta pruning.
        a = alpha
        b = beta
        next_state = None
        successor = self.succ(self.my_piece, state)
        for suc in successor:
            # Apply min_value to all successors with a and b inherited from alpha beta
            val = self.Min_Value(suc, depth+1, a, b)
            # Update the value of alpha and the sucecessor if we find a larger value
            if val > a:
                a = val
                next_state = copy.deepcopy(suc) 
            # Prune the rest if a>b
            if a > b:
                break   
        # Return the max value and the corresponding successor.
        return a, next_state
    
    
    
    
    
    def Min_Value(self, state, depth, alpha, beta):
        '''
        Apply alpha beta pruning to compute the value of the Max player.
        Here do not return the successor since we don't use the min value
        in the make move function.
        
        '''
        # When one of the player win or reach the depth limit, 
        # return the corresponding value and terminate.
        value = self.game_value(state)
        if value != 0:
            return value
        if depth == self.d_limit:
            return self.heuristic_game_value(state)
        # Apply alpha beta pruning.
        a = alpha
        b = beta
        successor = self.succ(self.opp, state)
        # Apply max_value to all successors with a and b inherited from alpha beta
        for suc in successor:
            val, sta = self.Max_Value(suc, depth+1, a, b)
            # Update b if we find a smaller value
            if val < b:
                b = val
            # Prune the rest if a>b
            if a > b:
                break  
        return b
        
        
        
        
        
        
        


    










############################################################################
#
# THE FOLLOWING CODE IS FOR SAMPLE GAMEPLAY ONLY
#
############################################################################

ai = Teeko2Player()
piece_count = 0
turn = 0

# drop phase
while piece_count < 8:

    # get the player or AI's move
    if ai.my_piece == ai.pieces[turn]:
        ai.print_board()
        move = ai.make_move(ai.board)
        ai.place_piece(move, ai.my_piece)
        print(ai.my_piece+" moved at "+chr(move[0][1]+ord("A"))+str(move[0][0]))
    else:
        move_made = False
        ai.print_board()
        print(ai.opp+"'s turn")
        while not move_made:
            player_move = input("Move (e.g. B3): ")
            while player_move[0] not in "ABCDE" or player_move[1] not in "01234":
                player_move = input("Move (e.g. B3): ")
            try:
                ai.opponent_move([(int(player_move[1]), ord(player_move[0])-ord("A"))])
                move_made = True
            except Exception as e:
                print(e)

    # update the game variables
    piece_count += 1
    turn += 1
    turn %= 2

# move phase - can't have a winner until all 8 pieces are on the board
while ai.game_value(ai.board) == 0:

    # get the player or AI's move
    if ai.my_piece == ai.pieces[turn]:
        ai.print_board()
        move = ai.make_move(ai.board)
        ai.place_piece(move, ai.my_piece)
        print(ai.my_piece+" moved from "+chr(move[1][1]+ord("A"))+str(move[1][0]))
        print("  to "+chr(move[0][1]+ord("A"))+str(move[0][0]))
    else:
        move_made = False
        ai.print_board()
        print(ai.opp+"'s turn")
        while not move_made:
            move_from = input("Move from (e.g. B3): ")
            while move_from[0] not in "ABCDE" or move_from[1] not in "01234":
                move_from = input("Move from (e.g. B3): ")
            move_to = input("Move to (e.g. B3): ")
            while move_to[0] not in "ABCDE" or move_to[1] not in "01234":
                move_to = input("Move to (e.g. B3): ")
            try:
                ai.opponent_move([(int(move_to[1]), ord(move_to[0])-ord("A")),
                                 (int(move_from[1]), ord(move_from[0])-ord("A"))])
                move_made = True
            except Exception as e:
                print(e)

    # update the game variables
    turn += 1
    turn %= 2

ai.print_board()
if ai.game_value(ai.board) == 1:
    print("AI wins! Game over.")
else:
    print("You win! Game over.")
