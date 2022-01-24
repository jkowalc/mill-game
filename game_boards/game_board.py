from __future__ import annotations
from abc import abstractmethod
from re import S
from typing import List, Tuple
from game_boards.game_board_check_mills import (check_all_diff_rect_mills,
                                                check_center_mills,
                                                check_simple_diff_rect_mills,
                                                check_same_rect_mills)
from game_boards import game_board_validation


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

    def place_pawn(self, pawn_position, player):
        self.validate_pawn_position(pawn_position)
        rect, pos = pawn_position
        self.board[rect][pos] = player

    def take_out_pawn(self, pawn_position):
        self.validate_pawn_position(pawn_position)
        rect, pos = pawn_position
        self.board[rect][pos] = None

    def execute_move(self, move):
        source, dest = move
        self.board[dest[0]][dest[1]] = self.board[source[0]][source[1]]
        self.board[source[0]][source[1]] = None

    def __eq__(self: GameBoard, __o: GameBoard) -> bool:
        conditions = [type(self).__name__ == type(__o).__name__,
                      self.board == __o.board]

        return False not in conditions

    def get_all_empty_pawn_positions(self):
        empty_pawn_positions = []
        for rect, rect_list in enumerate(self.board):
            for pos, pos_value in enumerate(rect_list):
                if pos_value is None:
                    if rect == 0 and self.allow_center_position or rect > 0:
                        empty_pawn_positions.append((rect, pos))
        return empty_pawn_positions

    @abstractmethod
    def check_if_pawn_in_mill(self, pawn_position: Tuple[int]):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def get_possible_moves_for_pawn(self, pawn_position):
        pass

    def validate_pawn_position(self, pawn_position):
        game_board_validation.validate_pawn_position(
            self, pawn_position)

    def validate_initial_board(self, initial_board):
        game_board_validation.validate_initial_board(
            self, initial_board)

    def check_center_mills(self, pawn_position: Tuple[int]):
        return check_center_mills(self, pawn_position)

    def check_same_rect_mills(self, pawn_position: Tuple[int]):
        return check_same_rect_mills(self, pawn_position)

    def check_simple_diff_rect_mills(self, pawn_position: Tuple[int]):
        return check_simple_diff_rect_mills(self, pawn_position)

    def check_all_diff_rect_mills(self, pawn_position: Tuple[int]):
        return check_all_diff_rect_mills(self, pawn_position)
