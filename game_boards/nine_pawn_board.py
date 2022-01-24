from typing import Tuple
from game_boards.game_board import GameBoard
from player import Player


class NinePawnBoard(GameBoard):
    def __init__(self, initial_board=None):
        super().__init__(3, False, False, initial_board)

    def check_if_pawn_in_mill(self, pawn_position: Tuple[int]):
        self.validate_pawn_position(pawn_position)
        rect, position = pawn_position
        if self.board[rect][position] is None:
            return False
        if self.check_same_rect_mills(pawn_position):
            return True
        if self.check_simple_diff_rect_mills(pawn_position):
            return True
        return False

    def get_possible_moves_for_pawn_specific(self, pawn_position, player: Player):
        rect, pos = pawn_position
        possible_moves = [
            (rect, (pos-1) % 8)
            (rect, (pos+1) % 8)
        ]
        if pos in {1, 3, 5, 7}:
            if rect > 1:
                possible_moves.append((rect-1, pos))
            if rect < 3:
                possible_moves.append((rect+1, pos))
        for move in possible_moves:
            if self.get_pawn_value(move) is not None:
                possible_moves.remove(move)
        return possible_moves
