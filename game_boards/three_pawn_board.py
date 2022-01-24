from typing import Tuple
from game_boards.game_board import GameBoard
from player import Player


class ThreePawnBoard(GameBoard):
    def __init__(self, initial_board=None):
        super().__init__(1, True, True, initial_board)

    def check_if_pawn_in_mill(self, pawn_position: Tuple[int]):
        self.validate_pawn_position(pawn_position)
        rect, position = pawn_position
        if self.board[rect][position] is None:
            return False
        if self.check_center_mills(pawn_position):
            return True
        if self.check_same_rect_mills(pawn_position):
            return True
        return False

    def get_possible_moves_for_pawn_specific(self, pawn_position, player: Player):
        rect, pos = pawn_position
        if rect == 0:
            return self.get_all_empty_pawn_positions()
        else:
            possible_moves = [
                (rect, (pos+1) % 8),
                (rect, (pos-1) % 8),
                (0, 0)
            ]
            for move in possible_moves:
                if self.get_pawn_value(move) is not None:
                    possible_moves.remove(move)
            return possible_moves
