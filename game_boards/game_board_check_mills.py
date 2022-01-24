from typing import Tuple


def check_center_mills(self, pawn_position: Tuple[int]):
    rect, position = pawn_position
    if rect == 1:
        if (self.board[1][position] == self.board[0][0] and
                self.board[0][0] == self.board[1][position+4]):
            return True
    else:
        for pos in range(8):
            if (self.board[1][pos] == self.board[0][0] and
                    self.board[0][0] == self.board[1][pos+4]):
                return True
    return False


def check_same_rect_mills(self, pawn_position: Tuple[int]):
    rect, position = pawn_position
    for first_pos in [0, 2, 4, 6]:
        second_pos = first_pos+1
        third_pos = (first_pos+2) % 8
        if (position in {first_pos, second_pos, third_pos} and
                self.board[rect][first_pos] == self.board[rect][second_pos] and
                self.board[rect][second_pos] == self.board[rect][third_pos]):
            return True
    return False


def check_simple_diff_rect_mills(self, pawn_position: Tuple[int]):
    rect, position = pawn_position
    if position in {1, 3, 5, 7}:
        if (self.board[1][position] == self.board[2][position] and
                self.board[2][position] == self.board[3][position]):
            return True
    return False


def check_all_diff_rect_mills(self, pawn_position: Tuple[int]):
    rect, position = pawn_position
    if (self.board[1][position] == self.board[2][position] and
            self.board[2][position] == self.board[3][position]):
        return True
    return False
