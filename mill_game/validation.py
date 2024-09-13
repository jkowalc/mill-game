from __future__ import annotations
from mill_game.exceptions import InvalidInitialBoardError, InvalidPawnPositionError
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from mill_game.game_board import GameBoard
    from mill_game.player import PlayerSymbol


def validate_pawn_position(board: GameBoard, pawn_position: tuple[int, int]):
    rect, position = pawn_position
    if not (0 <= position <= 7):
        raise InvalidPawnPositionError("Pawn position must between 0 and 7")
    rect_num = board.rectangles_num
    if board.allow_center_position:
        if not (0 <= rect <= rect_num):
            raise InvalidPawnPositionError(f"Pawn rectangle must be between 0 and {rect_num}")
    else:
        if not (1 <= rect <= rect_num):
            raise InvalidPawnPositionError(f"Pawn rectangle must be between 1 and {rect_num}")


def validate_initial_board(rect_num: int, initial_board_repr: list[list[PlayerSymbol | None]]):
    if not len(initial_board_repr) == rect_num + 1:
        raise InvalidInitialBoardError("Number of rectangles in board must be the same as declared")
    for i, rect in enumerate(initial_board_repr):
        if i == 0 and len(rect) != 1:
            raise InvalidInitialBoardError("Rectangle zero must contain one position")
        elif i > 0 and len(rect) != 8:
            raise InvalidInitialBoardError("Rectangles bigger than zero must contain 8 positions")
