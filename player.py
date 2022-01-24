from __future__ import annotations
from exceptions import WrongPawnNumberError
import interface


class Player:
    def __init__(self, name, symbol, board, pawns_num=9, pawns_on_board=None):
        self.name = name
        self.symbol = symbol
        if pawns_num not in {3, 6, 9, 12}:
            raise WrongPawnNumberError
        self.pawns_num = pawns_num
        self.pawns_on_board = pawns_on_board
        self.board = board

    def can_jump(self) -> bool:
        return self.pawns_num == 3

    def has_placed_all_pawns(self) -> bool:
        return len(self.pawns_on_board) == self.pawns_num

    def select_move(self, moves: dict):
        return interface.get_player_move(moves, self, self.board)

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Player):
            return self.name == __o.name
        else:
            return False

    def __str__(self):
        return self.symbol


class ComputerPlayer(Player):
    def __init__(self, symbol, pawns_num=9, pawns_on_board=None):
        name = "Computer"
        super().__init__(name, symbol, pawns_num, pawns_on_board)

    def select_move(self, moves: dict):
        pass


class SmartComputerPlayer(ComputerPlayer):
    def select_move(self, moves: dict):
        pass
