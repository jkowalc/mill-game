from typing import List, Tuple
from game_boards.game_board import GameBoard
from player import Player
import pawn_position_mapper

class TwelvePawnBoard(GameBoard):
    def __init__(self, initial_board=None):
        super().__init__(3, True, False, initial_board)

    def check_if_pawn_in_mill(self, pawn_position: Tuple[int]) -> List:
        self.validate_pawn_position(pawn_position)
        rect, position = pawn_position
        if self.board[rect][position] is None:
            return False
        if self.check_same_rect_mills(pawn_position):
            return True
        if self.check_all_diff_rect_mills(pawn_position):
            return True
        return False

    def get_possible_moves_for_pawn(self, pawn_position):
        rect, pos = pawn_position
        possible_moves = [
            (rect, (pos+1) % 8),
            (rect, (pos-1) % 8)
        ]
        if rect > 1:
            possible_moves.append((rect-1, pos))
        if rect < 3:
            possible_moves.append((rect+1, pos))
        for move in possible_moves:
            if self.get_pawn_value(move) is not None:
                possible_moves.remove(move)
        return possible_moves

    def __str__(self):
        board_str = "A B C D E F G\n"
        conv_dict = pawn_position_mapper.get_conversion_dict_from_rectangles_num(2)
        positions = {}
        for key in conv_dict.keys():
            rect, pos = pawn_position_mapper.get_position_tuple_from_alphabet(key)
            if self.board[rect][pos] is None:
                positions[key] = " "
            else:
                positions[key] = str(self.board[rect][pos])
        board_str += f"1 {positions['a1']} - {positions['d1']} - {positions['g1']}\n"
        board_str += f"2    {positions['b2']} - {positions['d2']} - {positions['f2']}\n"
        board_str += f"3 {positions['c3']} - {positions['d3']}  - {positions['e3']}"
        board_str += f"4    {positions['a4']} - {positions['b4']}  {positions['c4']}  {positions['e4']} - {positions['f4']} - {positions['g4']}\n"
        board_str += f"5 {positions['c5']} - {positions['d5']} - {positions['e5']}\n"
        board_str += f"6    {positions['b6']} - {positions['d6']} - {positions['f6']}\n"
        board_str += f"7 {positions['a7']} - {positions['d7']} - {positions['g7']}\n"
        return board_str