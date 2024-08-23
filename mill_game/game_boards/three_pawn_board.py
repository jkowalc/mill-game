from mill_game.game_board import GameBoard
from mill_game.pawn_position_mapper import (get_position_tuple_from_alphabet,
                                            get_conversion_dict_from_rectangles_num)
from mill_game.check_mills import check_center_mills, check_same_rect_mills
from mill_game.validation import validate_pawn_position


class ThreePawnBoard(GameBoard):
    def __init__(self, initial_board_repr=None):
        super().__init__(1, True, True, initial_board_repr)

    def check_if_pawn_in_mill(self, pawn_position: tuple[int, int]):
        validate_pawn_position(self, pawn_position)
        rect, position = pawn_position
        if self.board_repr[rect][position] is None:
            return False
        if check_center_mills(self, pawn_position):
            return True
        if pawn_position != (0, 0):
            if check_same_rect_mills(self, pawn_position):
                return True
        return False

    def get_possible_moves_for_pawn(self, pawn_position: tuple[int, int]):
        rect, pos = pawn_position
        if rect == 0:
            return self.get_all_empty_pawn_positions()
        else:
            possible_moves = [
                (rect, (pos + 1) % 8),
                (rect, (pos - 1) % 8),
                (0, 0)
            ]
            possible_moves_copy = possible_moves.copy()
            for move in possible_moves:
                if self.get_pawn_value(move) is not None:
                    possible_moves_copy.remove(move)
            return possible_moves_copy

    def __str__(self):
        board_str = "\n    A   B   C\n\n"
        conv_dict = get_conversion_dict_from_rectangles_num(1)
        positions = {}
        for key in conv_dict.keys():
            rect, pos = get_position_tuple_from_alphabet(key, self)
            if self.board_repr[rect][pos] is None:
                positions[key] = " "
            else:
                positions[key] = str(self.board_repr[rect][pos])
        board_str += f"1   {positions['a1']}---{positions['b1']}---{positions['c1']}\n"
        board_str += "    | \\ | / |\n"
        board_str += f"2   {positions['a2']}---{positions['b2']}---{positions['c2']}\n"
        board_str += "    | / | \\ |\n"
        board_str += f"3   {positions['a3']}---{positions['b3']}---{positions['c3']}\n"
        return board_str
