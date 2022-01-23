from __future__ import annotations
from typing import Tuple


class GameBoard:
    def __init__(self,
                 rectangles_num,
                 allow_diagonal_movement: bool,
                 allow_center_position: bool):
        self.rectangles_num = rectangles_num
        self.allow_diagonal_movement = allow_diagonal_movement
        self.allow_center_position = allow_center_position

    def validate_pawn_position(self, pawn_position):
        pass

    def check_if_pawn_in_mill(self, pawn_position: Tuple[int]):
        pass

    def __eq__(self, __o: GameBoard) -> bool:
        pass
