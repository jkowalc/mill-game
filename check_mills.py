from typing import Tuple

from game_board import GameBoard


def check_center_mills(board: GameBoard, pawn_position: Tuple[int]):
    rect, position = pawn_position
    if rect == 1:
        if (board.board[1][position] == board.board[0][0] and
                board.board[0][0] == board.board[1][(position+4) % 8]):
            return True
    else:
        for pos in range(8):
            if (board.board[1][pos] == board.board[0][0] and
                    board.board[0][0] == board.board[1][(pos+4) % 8]):
                return True
    return False


def check_same_rect_mills(board: GameBoard, pawn_position: Tuple[int]):
    rect, position = pawn_position
    for first_pos in [0, 2, 4, 6]:
        second_pos = (first_pos+1) % 8
        third_pos = (first_pos+2) % 8
        if (position in {first_pos, second_pos, third_pos} and
                board.board[rect][first_pos] == board.board[rect][second_pos] and
                board.board[rect][second_pos] == board.board[rect][third_pos]):
            return True
    return False


def check_simple_diff_rect_mills(board: GameBoard, pawn_position: Tuple[int]):
    rect, position = pawn_position
    if position in {1, 3, 5, 7}:
        if (board.board[1][position] == board.board[2][position] and
                board.board[2][position] == board.board[3][position]):
            return True
    return False


def check_all_diff_rect_mills(board: GameBoard, pawn_position: Tuple[int]):
    rect, position = pawn_position
    if (board.board[1][position] == board.board[2][position] and
            board.board[2][position] == board.board[3][position]):
        return True
    return False
