from typing import Tuple
from game_boards.game_board import GameBoard
from player import Player


class SixPawnBoard(GameBoard):
    def __init__(self, initial_board=None):
        super().__init__(2, False, False, initial_board)

    def check_if_pawn_in_mill(self, pawn_position: Tuple[int]):
        self.validate_pawn_position(pawn_position)
        rect, position = pawn_position
        if self.board[rect][position] is None:
            return False
        return self.check_same_rect_mills(pawn_position)

    def get_possible_moves_for_pawn(self, pawn_position):
        rect, pos = pawn_position
        possible_moves = [
            (rect, (pos+1) % 8),
            (rect, (pos-1) % 8)
        ]
        if pos in {1, 3, 5, 7}:
            if rect == 1:
                possible_moves.append((2, pos))
            else:
                possible_moves.append((1, pos))
        for move in possible_moves:
            if self.get_pawn_value(move) is not None:
                possible_moves.remove(move)
        return possible_moves

    def __str__(self):
        return super().__str__()