from __future__ import annotations
from abc import abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from mill_game.player import Player
from mill_game.validation import validate_initial_board, validate_pawn_position


class GameBoard:
    def __init__(self,
                 rectangles_num: int,
                 allow_diagonal_movement: bool,
                 allow_center_position: bool,
                 initial_board_repr: list[list[Player | None]] = None):
        self.rectangles_num = rectangles_num
        self.allow_diagonal_movement = allow_diagonal_movement
        self.allow_center_position = allow_center_position
        if initial_board_repr:
            validate_initial_board(self.rectangles_num, initial_board_repr)
            self.board_repr: list[list[Player | None]] = initial_board_repr
        else:
            self.board_repr: list[list[Player | None]] = [
                [None for _ in range(8)] if rectangle > 0 else [None]
                for rectangle in range(rectangles_num + 1)]

    def get_pawn_value(self, pawn_position: tuple[int, int]) -> Player | None:
        validate_pawn_position(self, pawn_position)
        rect, position = pawn_position
        return self.board_repr[rect][position]

    def place_pawn(self, pawn_position: tuple[int, int], player: Player):
        validate_pawn_position(self, pawn_position)
        rect, pos = pawn_position
        self.board_repr[rect][pos] = player

    def take_out_pawn(self, pawn_position: tuple[int, int]):
        validate_pawn_position(self, pawn_position)
        rect, pos = pawn_position
        self.board_repr[rect][pos] = None

    def execute_move(self, move: tuple[tuple[int, int], tuple[int, int]]):
        source, dest = move
        self.board_repr[dest[0]][dest[1]] = self.board_repr[source[0]][source[1]]
        self.board_repr[source[0]][source[1]] = None

    def __eq__(self: GameBoard, __o: GameBoard) -> bool:
        return all([
            type(self).__name__ == type(__o).__name__,
            self.board_repr == __o.board_repr
        ])

    def get_all_empty_pawn_positions(self) -> list[tuple[int, int]]:
        empty_pawn_positions = []
        for rect, rect_list in enumerate(self.board_repr):
            for pos, pos_value in enumerate(rect_list):
                if pos_value is None:
                    if rect == 0 and self.allow_center_position or rect > 0:
                        empty_pawn_positions.append((rect, pos))
        return empty_pawn_positions

    @abstractmethod
    def check_if_pawn_in_mill(self, pawn_position: tuple[int, int]):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def get_possible_moves_for_pawn(self, pawn_position):
        pass
