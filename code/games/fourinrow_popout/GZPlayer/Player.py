import math
from typing import List, Optional
from GZPlayer.lib.Player import Player
from GZPlayer.Connect4Helper import Connect4Helper
from GZPlayer.types import Moves
import time

class GZPlayer(Player):
    def __init__(self, max_depth: Optional[int] = 4):
        self.MAX_DEPTH = max_depth

    def name(self):
        return 'GZ Player'


    def move(self, player_code, board):
        start = time.time()
        self.player_code = player_code

        self.opp_code = 2
        if player_code == 2:
            self.opp_code = 1

        connect4 = Connect4Helper(board=board, move=Moves.INIT, column=-1)

        score, move = self.minmax(
            state=connect4,
            current_depth=self.MAX_DEPTH,
        )
        # if score > best_score:
        #     best_score = score
        #     best_move = successor

        #print(score, move.move, move.column)
        
        #print("ELAPSED AI: ", time.time() - start)
        return move.move.value, move.column

    

    def minmax(self, state: Connect4Helper, current_depth: int):
        is_final = state.is_final_board(player_code=self.player_code, board=state.board)
        if is_final:
            return is_final, None

        if current_depth == 0:
            return self.evaluate_board(
                connect4=state
            ), None

        best_move = None
        if current_depth % 2 == 0:
            max_score = -math.inf
            for successor in state.successors(player_code=self.player_code):
                curr_score, _ = self.minmax(
                    state=successor,
                    current_depth=current_depth-1,
                )
                if curr_score > max_score:
                    max_score = curr_score
                    best_move = successor

            return max_score, best_move

        else:
            min_score = math.inf
            for successor in state.successors(player_code=self.opp_code):
                curr_score, _ = self.minmax(
                    state=successor,
                    current_depth=current_depth-1,
                )
                if curr_score < min_score:
                    min_score = curr_score
                    best_move = successor
                    
            return min_score, best_move
                

    def _evaluate_4_section(self, next_4: List[int]):
        empty_spaces_count = next_4.count(Connect4Helper.AVAILABLE_SPACE)
        section_score = 0

        player_piece_count = next_4.count(self.player_code)
        enemy_piece_count  = next_4.count(self.opp_code)

        
        if player_piece_count == 2 and enemy_piece_count == 0:
            section_score += 20

        if player_piece_count == 3 and enemy_piece_count == 0:
            section_score += 50
        
        if player_piece_count == 4:
            section_score += 100

        if player_piece_count >= enemy_piece_count:
            section_score += 5

        if enemy_piece_count == 3 and empty_spaces_count == 1:
            section_score -= 50
        

        return section_score
    

    def _evaluate_coordinate(self, row_idx: int, col_idx: int, connect4: Connect4Helper):
        coord_score = 0

        # VERTICAL CHECKING
        if row_idx < 3:
            next_bottom_4 = connect4._get_bottom_vertical_4(row_idx, col_idx)
            coord_score += self._evaluate_4_section(
                next_4=next_bottom_4,
            )

        # HORIZONTAL CHECKING
        if col_idx < 4:
            next_inline_4 = connect4._get_right_horizontal_4(row_idx, col_idx)
            coord_score += self._evaluate_4_section(
                next_4=next_inline_4,
            )

        # CHECK RIGHT DIAGONAL
        if col_idx < 4 and row_idx < 3:
            next_right_diagonal_4 = connect4._get_right_diagonal_4(row_idx, col_idx)
            coord_score += self._evaluate_4_section(
                next_4=next_right_diagonal_4,
            )

        # CHECK LEFT DIAGONAL
        if col_idx >= 3 and row_idx < 3:
            next_left_diagonal_4 = connect4._get_left_diagonal_4(row_idx, col_idx)
            coord_score += self._evaluate_4_section(
                next_4=next_left_diagonal_4,
            )

        return coord_score          


    def evaluate_board(self, connect4: Connect4Helper):
        is_final_board = connect4.is_final_board(
            board=connect4.board,
            player_code=self.player_code
        )

        if is_final_board:
            return is_final_board
        
        score = 0

        middle_rows = [r[Connect4Helper.MIDDLE_COLUMN] for r in connect4.board]
        score += middle_rows.count(self.player_code) * 5
        score -= middle_rows.count(self.opp_code) * 5

        for row_idx, row in enumerate(connect4.board):
            for col_idx, col in enumerate(row):
                score += self._evaluate_coordinate(
                    row_idx=row_idx,
                    col_idx=col_idx,
                    connect4=connect4
                )

        return score
