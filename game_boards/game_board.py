from __future__ import annotations
from abc import abstractmethod
from typing import List, Tuple
from exceptions import InvalidInitialBoardError, InvalidPawnPositionError


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

    def validate_pawn_position(self, pawn_position):
        rect, position = pawn_position
        if not (0 <= position <= 7):
            msg = "Pawn position must between 0 and 7"
            raise InvalidPawnPositionError(msg)
        rect_num = self.rectangles_num
        if self.allow_center_position:
            if not (0 <= rect <= rect_num):
                msg = f"Pawn rectangle must be between 0 and {rect_num}"
                raise InvalidPawnPositionError(msg)
        else:
            if not (1 <= rect <= rect_num):
                msg = f"Pawn rectangle must be between 1 and {rect_num}"
                raise InvalidPawnPositionError(msg)

    def get_pawn_value(self, pawn_position):
        self.validate_pawn_position(pawn_position)
        rect, position = pawn_position
        return self.board[rect][position]

    def validate_initial_board(self, initial_board):
        if not len(initial_board) == self.rectangles_num + 1:
            msg = "Number of rectangles in board must be the same as declared"
            raise InvalidInitialBoardError(msg)
        for i, rect in enumerate(initial_board):
            if i == 0 and len(rect) != 1:
                msg = "Rectangle zero must contain one position"
                raise InvalidInitialBoardError(msg)
            elif i > 0 and len(rect) != 8:
                msg = "Rectangles bigger than zero must contain 8 positions"
                raise InvalidInitialBoardError(msg)

    def check_center_mills(self, pawn_position: Tuple[int]):
        rect, position = pawn_position
        mills = []
        if rect == 1:
            if (self.board[1][position] == self.board[0][0] and
                    self.board[0][0] == self.board[1][position+4]):
                mills.append(((1, position), (0, 0), (1, position+4)))
        else:
            for pos in range(8):
                if (self.board[1][pos] == self.board[0][0] and
                        self.board[0][0] == self.board[1][pos+4]):
                    mills.append(((1, pos), (0, 0), (1, pos+4)))
        return mills

    def check_same_rect_mills(self, pawn_position: Tuple[int]):
        rect, position = pawn_position
        mills = []
        for first_pos in [0, 2, 4, 6]:
            second_pos = first_pos+1
            third_pos = (first_pos+2) % 8
            if (position in {first_pos, second_pos, third_pos} and
                    self.board[rect][first_pos] == self.board[rect][second_pos] and
                    self.board[rect][second_pos] == self.board[rect][third_pos]):
                mills.append(((rect, first_pos),
                              (rect, second_pos),
                              (rect, third_pos)))
        return mills

    def check_simple_diff_rect_mills(self, pawn_position: Tuple[int]):
        rect, position = pawn_position
        mills = []
        if position in {1, 3, 5, 7}:
            if (self.board[1][position] == self.board[2][position] and
                    self.board[2][position] == self.board[3][position]):
                mills.append(((1, position),
                              (2, position),
                              (3, position)))
        return mills

    def check_all_diff_rect_mills(self, pawn_position: Tuple[int]):
        rect, position = pawn_position
        mills = []
        if (self.board[1][position] == self.board[2][position] and
                self.board[2][position] == self.board[3][position]):
            mills.append(((1, position),
                          (2, position),
                          (3, position)))
        return mills

    @abstractmethod
    def get_mills_containing_pawn(self, pawn_position: Tuple[int]):
        pass

    def __eq__(self: GameBoard, __o: GameBoard) -> bool:
        conditions = [type(self).__name__ == type(__o).__name__,
                      self.board == __o.board]
        return False not in conditions

    @abstractmethod
    def __str__(self):
        pass












