from __future__ import annotations
from exceptions import InvalidInitialBoardError, InvalidPawnPositionError


def validate_pawn_position(board, pawn_position):
    rect, position = pawn_position
    if not (0 <= position <= 7):
        msg = "Pawn position must between 0 and 7"
        raise InvalidPawnPositionError(msg)
    rect_num = board.rectangles_num
    if board.allow_center_position:
        if not (0 <= rect <= rect_num):
            msg = f"Pawn rectangle must be between 0 and {rect_num}"
            raise InvalidPawnPositionError(msg)
    else:
        if not (1 <= rect <= rect_num):
            msg = f"Pawn rectangle must be between 1 and {rect_num}"
            raise InvalidPawnPositionError(msg)


def validate_initial_board(rect_num, initial_board):
    if not len(initial_board) == rect_num + 1:
        msg = "Number of rectangles in board must be the same as declared"
        raise InvalidInitialBoardError(msg)
    for i, rect in enumerate(initial_board):
        if i == 0 and len(rect) != 1:
            msg = "Rectangle zero must contain one position"
            raise InvalidInitialBoardError(msg)
        elif i > 0 and len(rect) != 8:
            msg = "Rectangles bigger than zero must contain 8 positions"
            raise InvalidInitialBoardError(msg)
