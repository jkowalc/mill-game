from typing import Tuple
from game_boards.game_board import GameBoard
from pawn_position_mapper import (get_position_tuple_from_alphabet,
                                  get_conversion_dict_from_rectangles_num)


class SixPawnBoard(GameBoard):
    def __init__(self, initial_board=None):
        super().__init__(2, False, False, initial_board)

    def check_if_pawn_in_mill(self, pawn_position: Tuple[int]):
        self.validate_pawn_position(pawn_position)
        rect, position = pawn_position
        if self.board[rect][position] is None:
            return False
        return self.check_same_rect_mills(pawn_position)

    def get_possible_moves_for_pawn(self, pawn_position):
        rect, pos = pawn_position
        possible_moves = [
            (rect, (pos+1) % 8),
            (rect, (pos-1) % 8)
        ]
        if pos in {1, 3, 5, 7}:
            if rect == 1:
                possible_moves.append((2, pos))
            else:
                possible_moves.append((1, pos))
        possible_moves_copy = possible_moves.copy()
        for move in possible_moves:
            if self.get_pawn_value(move) is not None:
                possible_moves_copy.remove(move)
        return possible_moves_copy

    def __str__(self):
        board_str = "\n    A   B   C   D   E\n"
        conv_dict = get_conversion_dict_from_rectangles_num(2)
        positions = {}
        for key in conv_dict.keys():
            rect, pos = get_position_tuple_from_alphabet(key, self)
            if self.board[rect][pos] is None:
                positions[key] = " "
            else:
                positions[key] = str(self.board[rect][pos])
        board_str += f"1   {positions['a1']}-------{positions['c1']}-------{positions['e1']}\n"
        board_str += f"    |       |       |\n"
        board_str += f"2   |   {positions['b2']}---{positions['c2']}---{positions['d2']}   |\n"
        board_str += f"    |   |       |   |\n"
        board_str += f"3   {positions['a3']}---{positions['b3']}       {positions['d3']}---{positions['e3']}\n"
        board_str += f"    |   |       |   |\n"
        board_str += f"4   |   {positions['b4']}---{positions['c4']}---{positions['d4']}   |\n"
        board_str += f"    |       |       |\n"
        board_str += f"5   {positions['a5']}-------{positions['c5']}--------{positions['e5']}\n"
        return board_str
