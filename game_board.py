from __future__ import annotations
from typing import List, Tuple

from exceptions import InvalidPawnPositionError


class GameBoard:
    def __init__(self,
                 rectangles_num,
                 allow_diagonal_movement: bool,
                 allow_center_position: bool,
                 initial_board: List[List]):
        self.rectangles_num = rectangles_num
        self.allow_diagonal_movement = allow_diagonal_movement
        self.allow_center_position = allow_center_position
        if initial_board:
            self.board = initial_board
        else:
            self.board = [
                [None for _ in range(8)] if rectangle > 0 else [None]
                for rectangle in range(rectangles_num + 1)]

    def validate_pawn_position(self, pawn_position):
        rect, position = pawn_position
        if not (0 <= position <= 7):
            return False
        if not (1 <= rect <= self.rectangles_num):
            if rect == 0 and self.allow_center_position:
                return True
            else:
                return False
        return True

    def check_if_pawn_in_mill(self, pawn_position: Tuple[int]):
        if not self.validate_pawn_position(pawn_position):
            raise InvalidPawnPositionError
        rect, position = pawn_position
        if self.board[rect][position] is None:
            return None

        # 3 pawns special case
        if self.allow_center_position:
            if rect == 1:
                first_value = self.board[1][position]
                second_value = self.board[0][0]
                third_value = self.board[1][position+4]
                if first_value == second_value == third_value:
                    return [(1, position), (0, 0), (1, position+4)]
            else:
                for pos in range(8):
                    first_value = self.board[1][pos]
                    second_value = self.board[0][0]
                    third_value = self.board[1][pos+4]
                    if first_value == second_value == third_value:
                        return [(1, pos), (0, 0), (1, pos+4)]

        # In the same rectangle (check sides)
        for first_pos in [0, 2, 4, 6]:
            first_value = self.board[rect][first_pos]
            second_value = self.board[rect][first_pos+1]
            third_pos = (first_pos+2) % 8
            third_value = self.board[rect][third_pos]
            if (position in {first_pos, first_pos+1, third_pos} and
                    first_value == second_value == third_value):
                return [(rect, first_pos),
                        (rect, first_pos+1),
                        (rect, third_pos)]

        # In a different rectangle (check diagonals and other mills)
        first_rect = 1
        if self.rectangles_num == 3:
            if position in {1, 3, 5, 7} or self.allow_diagonal_movement:
                first_value = self.board[first_rect][position]
                second_value = self.board[first_rect+1][position]
                third_value = self.board[first_rect+2][position]
                if first_rect == second_value == third_value:
                    return [(first_rect, position),
                            (first_rect+1, position)
                            (first_rect+2, position)]
        return None

    def __eq__(self: GameBoard, __o: GameBoard) -> bool:
        conditions = [self.rectangles_num == __o.rectangles_num,
                      self.allow_center_position == __o.allow_center_position,
                      self.allow_diagonal_movement == __o.allow_diagonal_movement,
                      self.board == __o.board]
        return False not in conditions
