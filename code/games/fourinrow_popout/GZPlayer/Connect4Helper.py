from optparse import Option
from typing import List, Optional

from GZPlayer.types import Moves
from copy import deepcopy

class Connect4Helper():
    AVAILABLE_SPACE = 0
    MIDDLE_COLUMN = 3
    def __init__(self, board: List[List[int]], move: Moves, column: int):
        self.board = board
        self.move = move
        self.column = column

    
    def _get_board_dimensions(self):
        return len(self.board[0]), len(self.board)
    

    def is_move_valid(self, move: Moves, column: int, player_code: int):
        w, h = self._get_board_dimensions()

        # print(move, column)
        # print(self.board)
        if column < 0 or column >= w:
            return False

        if move == Moves.POPOUT:
            # print(self.board[h-1][column] == player_code)
            return self.board[h-1][column] == player_code

        elif move == Moves.PLACE:
            # print(self.board[0], self.board[0][column] == 0)
            return self.board[0][column] == 0

    
    def _get_right_diagonal_4(self, row_idx, col_idx):
        return [
            self.board[row_idx][col_idx],
            self.board[row_idx+1][col_idx+1],
            self.board[row_idx+2][col_idx+2],
            self.board[row_idx+3][col_idx+3]
        ]

    
    def _get_left_diagonal_4(self, row_idx, col_idx):
        return [
            self.board[row_idx][col_idx],
            self.board[row_idx+1][col_idx-1],
            self.board[row_idx+2][col_idx-2],
            self.board[row_idx+3][col_idx-3]
        ]
    

    def _get_bottom_vertical_4(self, row_idx, col_idx):
        return [
            self.board[row_idx][col_idx],
            self.board[row_idx+1][col_idx],
            self.board[row_idx+2][col_idx],
            self.board[row_idx+3][col_idx]
        ]
    

    def _get_right_horizontal_4(self, row_idx, col_idx):
        return list(self.board[row_idx][col_idx:col_idx+4])
    

    def is_final_board(self, board: List[List[int]], player_code: int):
        BIG_SCORE = 1000
        for row_idx, row in enumerate(board):
            for col_idx, col in enumerate(row):
                # VERTICAL CHECKING
                if row_idx < 3:
                    next_bottom_4 = self._get_bottom_vertical_4(row_idx, col_idx)
                    if next_bottom_4 == [player_code]*4:
                        return BIG_SCORE
                    elif Connect4Helper.AVAILABLE_SPACE not in next_bottom_4 and len(set(next_bottom_4)) == 1:
                        return -BIG_SCORE
                
                # HORIZONTAL CHECKING
                if col_idx < 4:
                    next_inline_4 = self._get_right_horizontal_4(row_idx, col_idx)
                    if next_inline_4 == [player_code]*4: 
                        return BIG_SCORE
                    elif Connect4Helper.AVAILABLE_SPACE not in next_inline_4 and len(set(next_inline_4)) == 1: 
                        return -BIG_SCORE
                
                # CHECK RIGHT DIAGONAL
                if col_idx < 4 and row_idx < 3:
                    next_right_diagonal_4 = self._get_right_diagonal_4(row_idx, col_idx)
                    if next_right_diagonal_4 == [player_code]*4: 
                        return BIG_SCORE
                    elif Connect4Helper.AVAILABLE_SPACE not in next_right_diagonal_4 and len(set(next_right_diagonal_4)) == 1: 
                        return -BIG_SCORE

                # CHECK LEFT DIAGONAL
                if col_idx >= 3 and row_idx < 3:
                    next_left_diagonal_4 = self._get_left_diagonal_4(row_idx, col_idx)
                    if next_left_diagonal_4 == [player_code]*4: 
                        return BIG_SCORE
                    elif Connect4Helper.AVAILABLE_SPACE not in next_left_diagonal_4 and len(set(next_left_diagonal_4)) == 1:
                        return -BIG_SCORE

        return False


    def generate_move_board(self, move: Moves, column: int, player_code: int, in_place: Optional[bool] = True):
        w, h = self._get_board_dimensions()
        if column < 0 or column+1 > w:
            return False

        new_board = deepcopy(self.board)
        if move == Moves.POPOUT:
            for row_idx, row_value in enumerate(self.board):
                if row_idx == h-1:
                    continue
                new_board[row_idx+1][column] = row_value[column]
                new_board[row_idx][column] = 0

        elif move == Moves.PLACE:
            for row_idx, row_value in enumerate(self.board):
                if row_value[column] != 0:
                    new_board[row_idx-1][column] = player_code
                    break
                elif row_idx+1 == h:
                    new_board[row_idx][column] = player_code
                    break
                elif row_value[column] == 0:
                    continue
        
        if (in_place): self.board = new_board
        return new_board

    def get_affected_coordinates(self, player_code: int):
        if self.move == Moves.PLACE:
            for row_idx, row in enumerate(self.board):
                if row[self.column] == player_code:
                    return row_idx, self.column
        else:
            return 0, self.column

    
    def successors(self, player_code: int):
        w, _ = self._get_board_dimensions()
        successors = []
        for col in range(0, w):
            if self.is_move_valid(Moves.PLACE, col, player_code):
                board = self.generate_move_board(
                    move=Moves.PLACE,
                    column=col,
                    player_code=player_code,
                    in_place=False
                )
                successors.append(Connect4Helper(
                    board=board,
                    move=Moves.PLACE,
                    column=col
                ))
                
            if self.is_move_valid(Moves.POPOUT, col, player_code):
                board = self.generate_move_board(
                    move=Moves.POPOUT,
                    column=col,
                    player_code=player_code,
                    in_place=False
                )
                successors.append(Connect4Helper(
                    board=board,
                    move=Moves.POPOUT,
                    column=col
                ))

        return successors
