from typing import Tuple
from game_boards.game_board import GameBoard


class ThreePawnBoard(GameBoard):
    def __init__(self, initial_board):
        super().__init__(1, True, True, initial_board)

    def get_mills_containing_pawn(self, pawn_position: Tuple[int]):
        self.validate_pawn_position(pawn_position)
        rect, position = pawn_position
        if self.board[rect][position] is None:
            return []
        mills = []
        mills.extend(self.check_center_mills(pawn_position))
        mills.extend(self.check_same_rect_mills(pawn_position))
        return mills
