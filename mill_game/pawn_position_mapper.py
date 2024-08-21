from typing import Tuple
from mill_game.game_board import GameBoard


def get_position_tuple_from_alphabet(pos: str, board: GameBoard) -> Tuple[int]:
    conv_dict = get_conversion_dict_from_rectangles_num(board.rectangles_num)
    return conv_dict[pos]


def get_alphabet_from_position_tuple(pos: Tuple[int], board: GameBoard) -> str:
    conv_dict = get_conversion_dict_from_rectangles_num(board.rectangles_num)
    for alphabet, tuple in conv_dict.items():
        if tuple == pos:
            return alphabet
    return None


def get_conversion_dict_from_rectangles_num(rectangles_num) -> dict:
    if rectangles_num == 3:
        conversion_dict = {
            "a1": (3, 0),
            "a4": (3, 7),
            "a7": (3, 6),
            "b2": (2, 0),
            "b4": (2, 7),
            "b6": (2, 6),
            "c3": (1, 0),
            "c4": (1, 7),
            "c5": (1, 6),
            "d1": (3, 1),
            "d2": (2, 1),
            "d3": (1, 1),
            "d4": (0, 0),
            "d5": (1, 5),
            "d6": (2, 5),
            "d7": (3, 5),
            "e3": (1, 2),
            "e4": (1, 3),
            "e5": (1, 4),
            "f2": (2, 2),
            "f4": (2, 3),
            "f6": (2, 4),
            "g1": (3, 2),
            "g4": (3, 3),
            "g7": (3, 4),
        }
    elif rectangles_num == 2:
        conversion_dict = {
            "a1": (2, 0),
            "a3": (2, 7),
            "a5": (2, 6),
            "b2": (1, 0),
            "b3": (1, 7),
            "b4": (1, 6),
            "c1": (2, 1),
            "c2": (1, 1),
            "c3": (0, 0),
            "c4": (1, 5),
            "c5": (2, 5),
            "d2": (1, 2),
            "d3": (1, 3),
            "d4": (1, 4),
            "e1": (2, 2),
            "e3": (2, 3),
            "e5": (2, 4)
        }
    elif rectangles_num == 1:
        conversion_dict = {
            "a1": (1, 0),
            "a2": (1, 7),
            "a3": (1, 6),
            "b1": (1, 1),
            "b2": (0, 0),
            "b3": (1, 5),
            "c1": (1, 2),
            "c2": (1, 3),
            "c3": (1, 4)
        }
    return conversion_dict
