from typing import Tuple
from game_boards.game_board import GameBoard
from pawn_position_mapper import (get_position_tuple_from_alphabet,
                                  get_conversion_dict_from_rectangles_num)


class ThreePawnBoard(GameBoard):
    def __init__(self, initial_board=None):
        super().__init__(1, True, True, initial_board)

    def check_if_pawn_in_mill(self, pawn_position: Tuple[int]):
        self.validate_pawn_position(pawn_position)
        rect, position = pawn_position
        if self.board[rect][position] is None:
            return False
        if self.check_center_mills(pawn_position):
            return True
        if self.check_same_rect_mills(pawn_position):
            return True
        return False

    def get_possible_moves_for_pawn(self, pawn_position):
        rect, pos = pawn_position
        if rect == 0:
            return self.get_all_empty_pawn_positions()
        else:
            possible_moves = [
                (rect, (pos+1) % 8),
                (rect, (pos-1) % 8),
                (0, 0)
            ]
            for move in possible_moves:
                if self.get_pawn_value(move) is not None:
                    possible_moves.remove(move)
            return possible_moves

    def __str__(self):
        board_str = "A B C"
        conv_dict = get_conversion_dict_from_rectangles_num(1)
        positions = {}
        for key in conv_dict.keys():
            rect, pos = get_position_tuple_from_alphabet(key, self.board)
            if self.board[rect][pos] is None:
                positions[key] = " "
            else:
                positions[key] = str(self.board[rect][pos])
        board_str += f"1 {positions['a1']} - {positions['b1']} - {positions['c1']}"
        board_str += f"2 {positions['a2']} - {positions['b2']} - {positions['c2']}"
        board_str += f"3 {positions['a3']} - {positions['b3']} - {positions['c3']}"
        return board_str
