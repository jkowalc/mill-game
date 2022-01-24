from typing import List, Tuple
from game_boards.game_board import GameBoard


class TwelvePawnBoard(GameBoard):
    def __init__(self, initial_board=None):
        super().__init__(3, True, False, initial_board)

    def get_mills_containing_pawn(self, pawn_position: Tuple[int]) -> List:
        self.validate_pawn_position(pawn_position)
        rect, position = pawn_position
        if self.board[rect][position] is None:
            return []
        mills = []
        mills.extend(self.check_same_rect_mills(pawn_position))
        mills.extend(self.check_all_diff_rect_mills(pawn_position))
        return mills
