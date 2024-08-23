from mill_game.check_mills import check_same_rect_mills, check_simple_diff_rect_mills
from mill_game.game_board import GameBoard
from mill_game.pawn_position_mapper import (get_position_tuple_from_alphabet,
                                            get_conversion_dict_from_rectangles_num)
from mill_game.validation import validate_pawn_position


class NinePawnBoard(GameBoard):
    def __init__(self, initial_board_repr=None):
        super().__init__(3, False, False, initial_board_repr)

    def check_if_pawn_in_mill(self, pawn_position: tuple[int, int]):
        validate_pawn_position(self, pawn_position)
        rect, position = pawn_position
        if self.board_repr[rect][position] is None:
            return False
        if check_same_rect_mills(self, pawn_position):
            return True
        if check_simple_diff_rect_mills(self, pawn_position):
            return True
        return False

    def get_possible_moves_for_pawn(self, pawn_position):
        rect, pos = pawn_position
        possible_moves = [
            (rect, (pos - 1) % 8),
            (rect, (pos + 1) % 8)
        ]
        if pos in {1, 3, 5, 7}:
            if rect > 1:
                possible_moves.append((rect - 1, pos))
            if rect < 3:
                possible_moves.append((rect + 1, pos))
        possible_moves_copy = possible_moves.copy()
        for move in possible_moves:
            if self.get_pawn_value(move) is not None:
                possible_moves_copy.remove(move)
        return possible_moves_copy

    def __str__(self):
        board_str = "\n    A   B   C   D   E   F   G\n"
        conv_dict = get_conversion_dict_from_rectangles_num(3)
        positions = {}
        for key in conv_dict.keys():
            rect, pos = get_position_tuple_from_alphabet(key, self)
            if self.board_repr[rect][pos] is None:
                positions[key] = " "
            else:
                positions[key] = str(self.board_repr[rect][pos])
        board_str += f"1   {positions['a1']}-----------{positions['d1']}-----------{positions['g1']}\n"
        board_str += "    |           |           |\n"
        board_str += f"2   |   {positions['b2']}-------{positions['d2']}-------{positions['f2']}   |\n"
        board_str += "    |   |       |       |   |\n"
        board_str += f"3   |   |   {positions['c3']}---{positions['d3']}---{positions['e3']}   |   |\n"
        board_str += "    |   |   |       |   |   |\n"
        board_str += f"4   {positions['a4']}---{positions['b4']}---{positions['c4']}       {positions['e4']}---{positions['f4']}---{positions['g4']}\n"
        board_str += "    |   |   |       |   |   |\n"
        board_str += f"5   |   |   {positions['c5']}---{positions['d5']}---{positions['e5']}   |   |\n"
        board_str += "    |   |       |       |   |\n"
        board_str += f"6   |   {positions['b6']}-------{positions['d6']}-------{positions['f6']}   |\n"
        board_str += "    |           |           |\n"
        board_str += f"7   {positions['a7']}-----------{positions['d7']}-----------{positions['g7']}\n"
        return board_str
