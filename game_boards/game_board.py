from __future__ import annotations
from abc import abstractmethod
from typing import List, Tuple
import game_boards.game_board_validation
import game_boards.game_board_check_mills


class GameBoard:
    def __init__(self,
                 rectangles_num,
                 allow_diagonal_movement: bool,
                 allow_center_position: bool,
                 initial_board: List[List] = None):
        self.rectangles_num = rectangles_num
        self.allow_diagonal_movement = allow_diagonal_movement
        self.allow_center_position = allow_center_position
        if initial_board:
            self.validate_initial_board(initial_board)
            self.board = initial_board
        else:
            self.board = [
                [None for _ in range(8)] if rectangle > 0 else [None]
                for rectangle in range(rectangles_num + 1)]

    def get_pawn_value(self, pawn_position):
        self.validate_pawn_position(pawn_position)
        rect, position = pawn_position
        return self.board[rect][position]

    def __eq__(self: GameBoard, __o: GameBoard) -> bool:
        conditions = [type(self).__name__ == type(__o).__name__,
                      self.board == __o.board]

        return False not in conditions

    @abstractmethod
    def check_if_pawn_in_mill(self, pawn_position: Tuple[int]):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def validate_pawn_position(self, pawn_position):
        game_boards.game_board_validation.validate_pawn_position(self, pawn_position)

    def validate_initial_board(self, initial_board):
        game_boards.game_board_validation.validate_initial_board(self, initial_board)

    def check_center_mills(self, pawn_position: Tuple[int]):
        return game_boards.game_board_check_mills.check_center_mills(self, pawn_position)

    def check_same_rect_mills(self, pawn_position: Tuple[int]):
        return game_boards.game_board_check_mills.check_same_rect_mills(self, pawn_position)

    def check_simple_diff_rect_mills(self, pawn_position: Tuple[int]):
        return game_boards.game_board_check_mills.check_simple_diff_rect_mills(self, pawn_position)

    def check_all_diff_rect_mills(self, pawn_position: Tuple[int]):
        return game_boards.game_board_check_mills.check_all_diff_rect_mills(self, pawn_position)
